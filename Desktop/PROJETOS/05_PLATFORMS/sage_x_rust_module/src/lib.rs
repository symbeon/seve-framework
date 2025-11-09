//! # WarpRulesClient
//!
//! Cliente Rust para integração com a API WARP_RULES, permitindo buscar,
//! monitorar e aplicar regras em um contexto de agente.
//!
//! ## Exemplo básico
//! ```rust
//! use warp_rules_client::{WarpRulesClient, AgentContext, ClientConfig, Credentials};
//!
//! #[tokio::main]
//! async fn main() -> Result<(), Box<dyn std::error::Error>> {
//!     // Configuração do cliente
//!     let config = ClientConfig {
//!         api_url: "http://localhost:8001".to_string(),
//!         credentials: Some(Credentials {
//!             client_id: "sage_x_agent".to_string(),
//!             client_secret: "agent_secret".to_string(),
//!         }),
//!         ..Default::default()
//!     };
//!
//!     // Inicializa o cliente
//!     let mut client = WarpRulesClient::new(config);
//!
//!     // Busca as regras
//!     let rules = client.fetch_rules().await?;
//!     println!("Carregadas {} regras", rules.len());
//!
//!     // Cria um contexto do agente
//!     let mut context = AgentContext::default();
//!     context.agent_id = "sage_x_001".to_string();
//!     context.agent_name = "SAGE-X Agent".to_string();
//!
//!     // Aplica as regras
//!     let results = client.apply_rules(&mut context).await?;
//!     println!("Aplicadas {} regras", results.len());
//!
//!     // Envia os resultados
//!     client.send_results(&context).await?;
//!
//!     Ok(())
//! }
//! ```

// Módulos internos
mod engine;
mod models;
mod sync;

// Re-exportações públicas
pub use crate::models::{
    AgentContext, ClientConfig, Credentials, ResultsPayload, Rule, RuleResult,
    WarpRulesError, WarpRulesResult,
};

use std::path::PathBuf;
use std::sync::{Arc, Mutex};
use std::time::Duration;

use chrono::Utc;
use futures::StreamExt;
use log::{debug, error, info, warn};
use tokio::task::JoinHandle;
use tokio::time::sleep;

use crate::engine::RulesEngine;
use crate::models::RulesList;
use crate::sync::{RulesSync, WarpRulesClient as SyncClient};

/// Cliente principal para a API WARP_RULES
pub struct WarpRulesClient {
    /// Cliente para comunicação com a API
    sync_client: SyncClient,
    
    /// Motor de regras para aplicação
    rules_engine: Arc<Mutex<RulesEngine>>,
    
    /// Configuração do cliente
    config: ClientConfig,
    
    /// Handle para a tarefa de monitoramento em background
    monitor_task: Option<JoinHandle<()>>,
    
    /// Última vez que as regras foram buscadas
    last_fetch: Option<chrono::DateTime<Utc>>,
}

impl WarpRulesClient {
    /// Cria um novo cliente com a configuração fornecida
    pub fn new(config: ClientConfig) -> Self {
        let sync_client = SyncClient::new(config.clone());
        let rules_engine = Arc::new(Mutex::new(RulesEngine::new()));
        
        Self {
            sync_client,
            rules_engine,
            config,
            monitor_task: None,
            last_fetch: None,
        }
    }
    
    /// Inicializa o cliente com autenticação e busca inicial de regras
    pub async fn init(&mut self) -> WarpRulesResult<()> {
        info!("Inicializando cliente WARP_RULES");
        
        // Autentica o cliente
        self.sync_client.authenticate().await?;
        
        // Busca regras iniciais
        let rules = self.fetch_rules().await?;
        
        // Carrega as regras no engine
        if let Ok(mut engine) = self.rules_engine.lock() {
            engine.load_rules(rules);
        } else {
            return Err(WarpRulesError::Unknown("Falha ao obter lock no motor de regras".to_string()));
        }
        
        info!("Cliente inicializado com sucesso");
        Ok(())
    }
    
    /// Busca as regras da API
    pub async fn fetch_rules(&mut self) -> WarpRulesResult<Vec<Rule>> {
        info!("Buscando regras da API WARP_RULES");
        
        // Busca as regras via cliente de sincronização
        let rules_list = self.sync_client.fetch_rules().await?;
        self.last_fetch = Some(Utc::now());
        
        info!("Carregadas {} regras", rules_list.rules.len());
        Ok(rules_list.rules)
    }
    
    /// Aplica as regras carregadas ao contexto do agente
    pub async fn apply_rules(&mut self, context: &mut AgentContext) -> WarpRulesResult<Vec<RuleResult>> {
        info!("Aplicando regras ao contexto do agente");
        
        // Tenta obter o lock no motor de regras
        let engine = match self.rules_engine.lock() {
            Ok(engine) => engine,
            Err(_) => {
                return Err(WarpRulesError::RuleProcessing(
                    "Falha ao obter lock no motor de regras".to_string()
                ));
            }
        };
        
        // Aplica todas as regras
        let results = engine.apply_rules(context)?;
        
        info!("Aplicadas {} regras", results.len());
        Ok(results)
    }
    
    /// Envia os resultados da aplicação de regras para a API
    pub async fn send_results(&mut self, context: &AgentContext) -> WarpRulesResult<()> {
        // Tenta obter o lock no motor de regras
        let engine = match self.rules_engine.lock() {
            Ok(engine) => engine,
            Err(_) => {
                return Err(WarpRulesError::RuleProcessing(
                    "Falha ao obter lock no motor de regras".to_string()
                ));
            }
        };
        
        // Constrói o payload de resultados
        let payload = engine.build_results_payload(context);
        
        // Envia via cliente de sincronização
        self.sync_client.send_results(payload).await
    }
    
    /// Inicia um monitoramento contínuo de regras em background
    pub fn start_monitor(&mut self) -> WarpRulesResult<()> {
        // Verifica se já existe um monitor em execução
        if self.monitor_task.is_some() {
            return Ok(());
        }
        
        info!("Iniciando monitoramento de regras em background");
        
        // Clone dos dados necessários para a tarefa async
        let config = self.config.clone();
        let rules_engine = self.rules_engine.clone();
        
        // Se SSE estiver habilitado, usamos streaming de eventos
        if config.use_sse {
            // Clone para uso na task
            let sync_client_for_task = SyncClient::new(config.clone());
            
            // Spawn da tarefa de monitoramento SSE
            let task = tokio::spawn(async move {
                let mut client = sync_client_for_task;
                
                // Loop de tentativas
                loop {
                    // Tenta iniciar o stream de eventos
                    match client.watch_rules().await {
                        Ok(mut stream) => {
                            info!("Stream SSE conectado, monitorando atualizações");
                            
                            // Processa eventos do stream
                            while let Some(result) = stream.next().await {
                                match result {
                                    Ok(rules_list) => {
                                        info!("Recebida atualização de regras via SSE: {} regras", rules_list.rules.len());
                                        
                                        // Atualiza o motor de regras
                                        if let Ok(mut engine) = rules_engine.lock() {
                                            engine.load_rules(rules_list.rules);
                                        } else {
                                            error!("Falha ao obter lock no motor de regras");
                                        }
                                    },
                                    Err(e) => {
                                        error!("Erro ao processar evento SSE: {}", e);
                                        break;
                                    }
                                }
                            }
                            
                            // Se chegamos aqui, o stream foi encerrado
                            warn!("Stream SSE encerrado, reconectando em 5 segundos");
                        },
                        Err(e) => {
                            error!("Erro ao iniciar stream SSE: {}", e);
                        }
                    }
                    
                    // Aguarda antes de tentar reconectar
                    sleep(Duration::from_secs(5)).await;
                }
            });
            
            self.monitor_task = Some(task);
        } else if let Some(interval) = config.refresh_interval {
            // Se SSE não estiver habilitado, usamos polling
            // Clone para uso na task
            let mut sync_client_for_task = SyncClient::new(config.clone());
            
            // Spawn da tarefa de monitoramento por polling
            let task = tokio::spawn(async move {
                loop {
                    // Busca regras na API
                    match sync_client_for_task.fetch_rules().await {
                        Ok(rules_list) => {
                            debug!("Polling: atualização de regras: {} regras", rules_list.rules.len());
                            
                            // Atualiza o motor de regras
                            if let Ok(mut engine) = rules_engine.lock() {
                                engine.load_rules(rules_list.rules);
                            } else {
                                error!("Falha ao obter lock no motor de regras");
                            }
                        },
                        Err(e) => {
                            error!("Polling: erro ao buscar regras: {}", e);
                        }
                    }
                    
                    // Aguarda o intervalo configurado
                    sleep(Duration::from_secs(interval)).await;
                }
            });
            
            self.monitor_task = Some(task);
        } else {
            warn!("Monitoramento não iniciado: SSE desabilitado e intervalo de refresh não configurado");
        }
        
        Ok(())
    }
    
    /// Para o monitoramento de regras em background
    pub fn stop_monitor(&mut self) {
        if let Some(handle) = self.monitor_task.take() {
            info!("Parando monitoramento de regras em background");
            handle.abort();
        }
    }
    
    /// Define um caminho de cache para as regras
    pub fn with_cache_path(mut self, path: impl Into<PathBuf>) -> Self {
        self.config.cache_path = Some(path.into());
        self
    }
    
    /// Define credenciais para o cliente
    pub fn with_credentials(mut self, client_id: &str, client_secret: &str) -> Self {
        self.config.credentials = Some(Credentials {
            client_id: client_id.to_string(),
            client_secret: client_secret.to_string(),
        });
        self
    }
    
    /// Define se deve usar Server-Sent Events para monitoramento
    pub fn with_sse(mut self, use_sse: bool) -> Self {
        self.config.use_sse = use_sse;
        self
    }
    
    /// Define o intervalo de atualização quando SSE não está disponível
    pub fn with_refresh_interval(mut self, seconds: u64) -> Self {
        self.config.refresh_interval = Some(seconds);
        self
    }
}

impl Drop for WarpRulesClient {
    fn drop(&mut self) {
        self.stop_monitor();
    }
}

