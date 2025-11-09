use std::path::Path;
use std::time::Duration;

use async_trait::async_trait;
use chrono::Utc;
use eventsource_stream::Eventsource;
use futures::{Stream, StreamExt};
use log::{debug, error, info, warn};
use reqwest::{Client, RequestBuilder, StatusCode};
use serde::Deserialize;
use tokio::fs;
use tokio::io::AsyncWriteExt;
use tokio::time::sleep;

use crate::models::{
    AgentContext, ClientConfig, Credentials, ResultsPayload, Rule, RulesCache, RulesList, Token,
    WarpRulesError, WarpRulesResult,
};

/// Cliente para sincronização com a API WARP_RULES
pub struct WarpRulesClient {
    /// Configuração do cliente
    config: ClientConfig,
    
    /// Cliente HTTP reqwest
    http_client: Client,
    
    /// Token de autenticação atual
    token: Option<Token>,
    
    /// ETag da última resposta de regras
    last_etag: Option<String>,
    
    /// Versão atual das regras em cache
    current_version: Option<String>,
}

impl WarpRulesClient {
    /// Cria um novo cliente com a configuração fornecida
    pub fn new(config: ClientConfig) -> Self {
        let http_client = Client::builder()
            .timeout(Duration::from_secs(30))
            .build()
            .expect("Falha ao criar cliente HTTP");
            
        Self {
            config,
            http_client,
            token: None,
            last_etag: None,
            current_version: None,
        }
    }
    
    /// Autentica o cliente para obter um token JWT
    pub async fn authenticate(&mut self) -> WarpRulesResult<Token> {
        // Verifica se já temos um token válido
        if let Some(token) = &self.token {
            if token.is_valid() {
                debug!("Usando token de autenticação existente");
                return Ok(token.clone());
            }
        }
        
        // Obtém as credenciais
        let credentials = match &self.config.credentials {
            Some(creds) => creds,
            None => return Err(WarpRulesError::Authentication(
                "Credenciais não configuradas".to_string()
            )),
        };
        
        debug!("Obtendo novo token de autenticação");
        
        // Prepara o formulário para autenticação OAuth2
        let params = [
            ("grant_type", "password"),
            ("username", &credentials.client_id),
            ("password", &credentials.client_secret),
        ];
        
        // Faz a requisição de autenticação
        let response = self.http_client
            .post(format!("{}/api/rules/v1/token", self.config.api_url))
            .form(&params)
            .send()
            .await?;
            
        // Verifica o status da resposta
        if !response.status().is_success() {
            let status = response.status();
            let error_text = response.text().await.unwrap_or_default();
            return Err(WarpRulesError::Authentication(
                format!("Falha na autenticação. Status: {}, Erro: {}", status, error_text)
            ));
        }
        
        // Deserializa o token
        let mut token: Token = response.json().await?;
        
        // Define a data/hora de emissão
        token.issued_at = Some(Utc::now());
        
        // Armazena o token
        self.token = Some(token.clone());
        
        Ok(token)
    }
    
    /// Adiciona o token de autenticação a uma requisição
    async fn authenticate_request(&mut self, request: RequestBuilder) -> WarpRulesResult<RequestBuilder> {
        // Autentica se necessário
        let token = self.authenticate().await?;
        
        // Retorna a requisição com o cabeçalho de autorização
        Ok(request.header(
            "Authorization", 
            format!("{} {}", token.token_type, token.access_token)
        ))
    }
    
    /// Busca as regras da API WARP_RULES
    pub async fn fetch_rules(&mut self) -> WarpRulesResult<RulesList> {
        debug!("Buscando regras da API");
        
        // Prepara a requisição
        let mut request = self.http_client
            .get(format!("{}/api/rules/v1/rules", self.config.api_url));
            
        // Adiciona o ETag se disponível para cache
        if let Some(etag) = &self.last_etag {
            request = request.header("If-None-Match", etag);
        }
        
        // Autentica a requisição
        let request = self.authenticate_request(request).await?;
        
        // Envia a requisição
        let response = request.send().await?;
        
        // Verifica se o conteúdo não foi modificado (304)
        if response.status() == StatusCode::NOT_MODIFIED {
            debug!("Regras não modificadas, usando cache");
            
            // Tenta carregar do cache local
            if let Some(cache_path) = &self.config.cache_path {
                return self.load_rules_from_cache(cache_path).await;
            }
            
            return Err(WarpRulesError::Cache(
                "Cache solicitado mas não disponível localmente".to_string()
            ));
        }
        
        // Verifica se a resposta foi bem-sucedida
        if !response.status().is_success() {
            let status = response.status();
            let error_text = response.text().await.unwrap_or_default();
            return Err(WarpRulesError::Connection(
                format!("Falha ao buscar regras. Status: {}, Erro: {}", status, error_text)
            ));
        }
        
        // Obtém o ETag da resposta
        if let Some(etag) = response.headers().get("ETag") {
            if let Ok(etag_str) = etag.to_str() {
                self.last_etag = Some(etag_str.to_string());
            }
        }
        
        // Deserializa a resposta
        let rules_list: RulesList = response.json().await?;
        
        // Atualiza a versão atual
        self.current_version = Some(rules_list.version.clone());
        
        // Salva no cache local se configurado
        if let Some(cache_path) = &self.config.cache_path {
            self.save_rules_to_cache(&rules_list, cache_path).await?;
        }
        
        Ok(rules_list)
    }
    
    /// Salva as regras no cache local
    async fn save_rules_to_cache(&self, rules: &RulesList, cache_path: &Path) -> WarpRulesResult<()> {
        debug!("Salvando regras no cache local: {:?}", cache_path);
        
        // Cria o diretório pai se não existir
        if let Some(parent) = cache_path.parent() {
            fs::create_dir_all(parent).await?;
        }
        
        // Prepara o objeto de cache
        let cache = RulesCache {
            rules: rules.rules.clone(),
            version: rules.version.clone(),
            timestamp: Utc::now(),
        };
        
        // Serializa o cache
        let cache_json = serde_json::to_string(&cache)?;
        
        // Salva no arquivo
        let mut file = fs::File::create(cache_path).await?;
        file.write_all(cache_json.as_bytes()).await?;
        
        Ok(())
    }
    
    /// Carrega regras do cache local
    async fn load_rules_from_cache(&self, cache_path: &Path) -> WarpRulesResult<RulesList> {
        debug!("Carregando regras do cache local: {:?}", cache_path);
        
        // Verifica se o arquivo existe
        if !cache_path.exists() {
            return Err(WarpRulesError::Cache(
                format!("Arquivo de cache não encontrado: {:?}", cache_path)
            ));
        }
        
        // Lê o conteúdo do arquivo
        let cache_content = fs::read_to_string(cache_path).await?;
        
        // Deserializa o cache
        let cache: RulesCache = serde_json::from_str(&cache_content)?;
        
        // Converte para RulesList
        let rules_list = RulesList {
            rules: cache.rules,
            count: cache.rules.len(),
            version: cache.version,
        };
        
        Ok(rules_list)
    }
    
    /// Cria um stream de eventos SSE para receber atualizações em tempo real
    pub async fn watch_rules(&mut self) -> WarpRulesResult<impl Stream<Item = WarpRulesResult<RulesList>>> {
        debug!("Iniciando stream de eventos SSE para atualizações de regras");
        
        // Obtém um token de autenticação
        let token = self.authenticate().await?;
        
        // URL do endpoint SSE
        let sse_url = format!("{}/api/rules/v1/rules/stream", self.config.api_url);
        
        // Cabeçalho de autorização
        let auth_header = format!("{} {}", token.token_type, token.access_token);
        
        // Prepara o cliente para SSE
        let client = self.http_client.clone();
        let req = client.get(&sse_url).header("Authorization", auth_header);
        
        // Tipo de evento esperado
        #[derive(Debug, Deserialize)]
        struct SseEvent {
            rules: Vec<Rule>,
            count: usize,
            version: String,
        }
        
        // Cria o stream de eventos
        let event_stream = req.send()
            .await
            .map_err(WarpRulesError::from)?
            .bytes_stream()
            .eventsource()
            .map(|event_result| {
                match event_result {
                    Ok(event) => {
                        // Processa o evento SSE
                        match serde_json::from_str::<SseEvent>(&event.data) {
                            Ok(sse_event) => {
                                // Converte para RulesList
                                Ok(RulesList {
                                    rules: sse_event.rules,
                                    count: sse_event.count,
                                    version: sse_event.version,
                                })
                            },
                            Err(e) => Err(WarpRulesError::Serialization(e)),
                        }
                    },
                    Err(e) => Err(WarpRulesError::Connection(
                        format!("Erro no stream de eventos: {:?}", e)
                    )),
                }
            });
            
        Ok(event_stream)
    }
    
    /// Envia resultados de aplicação de regras para a API
    pub async fn send_results(&mut self, results: ResultsPayload) -> WarpRulesResult<()> {
        debug!("Enviando {} resultados de aplicação de regras", results.results.len());
        
        // Prepara a requisição
        let request = self.http_client
            .post(format!("{}/api/rules/v1/results", self.config.api_url))
            .json(&results);
            
        // Autentica a requisição
        let request = self.authenticate_request(request).await?;
        
        // Envia a requisição
        let response = request.send().await?;
        
        // Verifica se a resposta foi bem-sucedida
        if !response.status().is_success() {
            let status = response.status();
            let error_text = response.text().await.unwrap_or_default();
            return Err(WarpRulesError::Connection(
                format!("Falha ao enviar resultados. Status: {}, Erro: {}", status, error_text)
            ));
        }
        
        Ok(())
    }
}

/// Interface para sincronização de regras
#[async_trait]
pub trait RulesSync {
    /// Busca regras da fonte de regras
    async fn fetch_rules(&mut self) -> WarpRulesResult<Vec<Rule>>;
    
    /// Envia resultados de aplicação de regras
    async fn send_results(&mut self, results: ResultsPayload) -> WarpRulesResult<()>;
}

#[async_trait]
impl RulesSync for WarpRulesClient {
    async fn fetch_rules(&mut self) -> WarpRulesResult<Vec<Rule>> {
        let rules_list = self.fetch_rules().await?;
        Ok(rules_list.rules)
    }
    
    async fn send_results(&mut self, results: ResultsPayload) -> WarpRulesResult<()> {
        self.send_results(results).await
    }
}

