use std::env;
use std::collections::HashMap;
use std::error::Error;
use std::time::Duration;

use reqwest::Client;
use serde::{Serialize, Deserialize};
use serde_json::{json, Value};
use tokio;
use dotenv::dotenv;
use chrono::Utc;
use log::{info, warn, error, LevelFilter};
use env_logger::Builder;

// Importação da nossa biblioteca de cliente WARP_RULES
use warp_rules_client::{
    WarpRulesClient, AgentContext, ClientConfig, Credentials, WarpRulesResult
};

#[derive(Serialize, Deserialize, Debug)]
struct RequestPayload {
    agent: String,
    task: String,
    payload: Value,
}

/// Configura o logger para exibir informações úteis
fn setup_logger() {
    let mut builder = Builder::new();
    builder.filter_level(LevelFilter::Info);
    builder.init();
}

/// Carrega configurações do ambiente
fn load_config() -> HashMap<String, String> {
    let mut config = HashMap::new();
    
    // Tenta carregar do arquivo .env
    let _ = dotenv();
    
    // Define valores padrão
    config.insert("WARP_API_URL".to_string(), 
                  env::var("WARP_API_URL").unwrap_or_else(|_| "http://localhost:8001".to_string()));
    
    config.insert("EON_API_URL".to_string(), 
                  env::var("EON_API_URL").unwrap_or_else(|_| "http://localhost:8000/api/task".to_string()));
    
    config.insert("AGENT_ID".to_string(), 
                  env::var("AGENT_ID").unwrap_or_else(|_| "sage_x_rust_agent".to_string()));
    
    config.insert("CLIENT_ID".to_string(), 
                  env::var("CLIENT_ID").unwrap_or_else(|_| "sage_x_client".to_string()));
    
    config.insert("CLIENT_SECRET".to_string(), 
                  env::var("CLIENT_SECRET").unwrap_or_else(|_| "client_secret".to_string()));
    
    config
}

/// Inicializa e configura o cliente WARP_RULES
async fn init_warp_rules_client(config: &HashMap<String, String>) -> WarpRulesResult<WarpRulesClient> {
    let api_url = config.get("WARP_API_URL").unwrap();
    let client_id = config.get("CLIENT_ID").unwrap();
    let client_secret = config.get("CLIENT_SECRET").unwrap();
    
    // Cria a configuração do cliente
    let client_config = ClientConfig {
        api_url: api_url.to_string(),
        credentials: Some(Credentials {
            client_id: client_id.to_string(),
            client_secret: client_secret.to_string(),
        }),
        use_sse: true,
        refresh_interval: Some(300), // 5 minutos como fallback
        ..Default::default()
    };
    
    // Inicializa o cliente
    let mut client = WarpRulesClient::new(client_config);
    client.init().await?;
    
    Ok(client)
}

/// Cria e inicializa um contexto de agente
fn create_agent_context(config: &HashMap<String, String>) -> AgentContext {
    let agent_id = config.get("AGENT_ID").unwrap();
    
    let mut context = AgentContext::default();
    context.agent_id = agent_id.to_string();
    context.agent_name = "SAGE-X Rust Module".to_string();
    context.last_updated = Utc::now();
    
    // Define alguns estados iniciais
    context.state.insert("framework".to_string(), json!("EON-Framework"));
    context.state.insert("runtime".to_string(), json!("Rust/Tokio"));
    context.state.insert("initialized".to_string(), json!(true));
    
    context
}

/// Constrói uma mensagem para o EON-Framework baseada no contexto do agente
fn build_message(context: &AgentContext) -> RequestPayload {
    // Define valores padrão
    let mut agent_name = "rust_agent".to_string();
    let mut task = "teste_conexao".to_string();
    let mut message = "Rust conectado ao EON-Framework!".to_string();
    
    // Verifica se o contexto do agente contém valores personalizados definidos pelas regras
    if let Some(name) = context.state.get("agent_name") {
        if let Some(name_str) = name.as_str() {
            agent_name = name_str.to_string();
        }
    }
    
    if let Some(task_val) = context.state.get("current_task") {
        if let Some(task_str) = task_val.as_str() {
            task = task_str.to_string();
        }
    }
    
    if let Some(msg) = context.state.get("message") {
        if let Some(msg_str) = msg.as_str() {
            message = msg_str.to_string();
        }
    }
    
    // Constrói mensagens adicionais baseadas nas preferências definidas nas regras
    let mut additional_info = Vec::new();
    
    for (key, value) in &context.state {
        if key.starts_with("pref_") {
            additional_info.push(format!("{}={}", 
                key.trim_start_matches("pref_"), 
                value.to_string().trim_matches('"')
            ));
        }
    }
    
    // Constrói o payload final
    let payload = if additional_info.is_empty() {
        json!({
            "msg": message,
            "timestamp": Utc::now().to_rfc3339()
        })
    } else {
        json!({
            "msg": message,
            "preferences": additional_info.join(", "),
            "timestamp": Utc::now().to_rfc3339(),
            "rule_guided": true
        })
    };
    
    RequestPayload {
        agent: agent_name,
        task,
        payload,
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    // Configura o logger
    setup_logger();
    
    // Carrega configurações
    let config = load_config();
    info!("Iniciando SAGE-X Rust Module com integração WARP_RULES");
    
    // Inicializa o cliente WARP_RULES
    let mut warp_client = match init_warp_rules_client(&config).await {
        Ok(client) => {
            info!("Cliente WARP_RULES inicializado com sucesso");
            client
        },
        Err(e) => {
            warn!("Não foi possível inicializar o cliente WARP_RULES: {}. Continuando sem regras.", e);
            WarpRulesClient::new(ClientConfig::default())
        }
    };
    
    // Busca regras e inicia monitoramento em background
    let rules = match warp_client.fetch_rules().await {
        Ok(rules) => {
            info!("Carregadas {} regras do servidor WARP_RULES", rules.len());
            
            // Inicia o monitoramento em background
            if let Err(e) = warp_client.start_monitor() {
                warn!("Não foi possível iniciar o monitoramento de regras: {}", e);
            } else {
                info!("Monitoramento de regras em background iniciado");
            }
            
            rules
        },
        Err(e) => {
            warn!("Não foi possível carregar regras: {}", e);
            Vec::new()
        }
    };
    
    // Cria e inicializa o contexto do agente
    let mut context = create_agent_context(&config);
    
    // Aplica as regras ao contexto do agente
    if !rules.is_empty() {
        match warp_client.apply_rules(&mut context).await {
            Ok(results) => {
                info!("Aplicadas {} regras ao contexto do agente", results.len());
                
                // Registra quais regras foram aplicadas
                for result in &results {
                    if result.applied {
                        info!("Regra aplicada: {}", result.rule_id);
                    }
                }
                
                // Envia os resultados de volta para a API WARP_RULES
                if let Err(e) = warp_client.send_results(&context).await {
                    warn!("Não foi possível enviar resultados: {}", e);
                } else {
                    info!("Resultados de aplicação de regras enviados com sucesso");
                }
            },
            Err(e) => {
                warn!("Não foi possível aplicar regras: {}", e);
            }
        }
    }
    
    // Cria uma mensagem para o EON-Framework baseada no contexto do agente
    let payload = build_message(&context);
    info!("Enviando mensagem ao EON-Framework: {:?}", payload);
    
    // Envia para o EON-Framework
    let eon_url = config.get("EON_API_URL").unwrap();
    let client = Client::new();
    
    match client.post(eon_url)
        .json(&payload)
        .timeout(Duration::from_secs(10))
        .send()
        .await
    {
        Ok(resp) => {
            if resp.status().is_success() {
                let text = resp.text().await?;
                info!("Resposta do EON-Framework: {}", text);
            } else {
                let status = resp.status();
                let text = resp.text().await.unwrap_or_default();
                warn!("Erro na resposta do EON-Framework. Status: {}, Erro: {}", status, text);
            }
        },
        Err(e) => {
            error!("Erro ao conectar ao EON-Framework: {}", e);
        }
    }
    
    // Para o monitoramento de regras em background
    warp_client.stop_monitor();
    info!("SAGE-X Rust Module finalizado com sucesso");
    
    Ok(())
}
