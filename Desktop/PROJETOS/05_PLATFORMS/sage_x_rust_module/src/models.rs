use std::collections::HashMap;
use std::path::PathBuf;
use std::fmt;

use serde::{Serialize, Deserialize};
use chrono::{DateTime, Utc};
use thiserror::Error;

/// Erro específico do cliente warp_rules_client
#[derive(Error, Debug)]
pub enum WarpRulesError {
    #[error("Erro de autenticação: {0}")]
    Authentication(String),
    
    #[error("Erro de conexão: {0}")]
    Connection(String),
    
    #[error("Erro ao processar regra: {0}")]
    RuleProcessing(String),
    
    #[error("Erro de cache: {0}")]
    Cache(String),
    
    #[error("Erro de requisição HTTP: {0}")]
    Http(#[from] reqwest::Error),
    
    #[error("Erro de serialização/deserialização: {0}")]
    Serialization(#[from] serde_json::Error),
    
    #[error("Erro de I/O: {0}")]
    Io(#[from] std::io::Error),
    
    #[error("Erro desconhecido: {0}")]
    Unknown(String),
}

/// Tipo de resultado utilizado pelo cliente
pub type WarpRulesResult<T> = Result<T, WarpRulesError>;

/// Configuração do cliente warp_rules_client
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ClientConfig {
    /// URL base da API WARP_RULES
    pub api_url: String,
    
    /// Credenciais para autenticação
    pub credentials: Option<Credentials>,
    
    /// Caminho para armazenar o cache local de regras
    pub cache_path: Option<PathBuf>,
    
    /// Intervalo em segundos para atualização automática das regras
    pub refresh_interval: Option<u64>,
    
    /// Se deve utilizar SSE (Server-Sent Events) para atualizações em tempo real
    pub use_sse: bool,
}

impl Default for ClientConfig {
    fn default() -> Self {
        Self {
            api_url: "http://localhost:8001".to_string(),
            credentials: None,
            cache_path: None,
            refresh_interval: Some(300), // 5 minutos por padrão
            use_sse: true,
        }
    }
}

/// Credenciais para autenticação na API
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Credentials {
    pub client_id: String,
    pub client_secret: String,
}

/// Token de autenticação recebido da API
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Token {
    pub access_token: String,
    pub token_type: String,
    pub expires_in: i64,
    
    #[serde(skip)]
    pub issued_at: Option<DateTime<Utc>>,
}

impl Token {
    /// Verifica se o token ainda é válido
    pub fn is_valid(&self) -> bool {
        if let Some(issued_at) = self.issued_at {
            let expiry = issued_at + chrono::Duration::seconds(self.expires_in);
            // Considera válido se o token não expira nos próximos 60 segundos
            return expiry > Utc::now() + chrono::Duration::seconds(60);
        }
        false
    }
}

/// Regra recebida da API (formato V1)
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub struct Rule {
    pub id: String,
    pub name: String,
    pub content: String,
    pub active: bool,
    pub version: String,
}

impl fmt::Display for Rule {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "Regra '{}' ({}): {}", self.name, self.id, self.content)
    }
}

/// Lista de regras recebida da API
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RulesList {
    pub rules: Vec<Rule>,
    pub count: usize,
    pub version: String,
}

/// Contexto do agente para aplicação de regras
#[derive(Debug, Clone, Default)]
pub struct AgentContext {
    /// Identificador do agente
    pub agent_id: String,
    
    /// Nome do agente
    pub agent_name: String,
    
    /// Estado atual do agente
    pub state: HashMap<String, serde_json::Value>,
    
    /// Carimbo de data/hora da última atualização
    pub last_updated: DateTime<Utc>,
}

/// Resultado da aplicação de uma regra
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RuleResult {
    /// Identificador da regra
    pub rule_id: String,
    
    /// Se a regra foi aplicada com sucesso
    pub applied: bool,
    
    /// Resultado ou efeito da aplicação da regra
    pub outcome: Option<serde_json::Value>,
    
    /// Carimbo de data/hora da aplicação da regra
    #[serde(with = "chrono::serde::ts_seconds")]
    pub timestamp: DateTime<Utc>,
    
    /// Identificador do agente que aplicou a regra
    pub agent_id: String,
}

/// Payload para enviar resultados de aplicação de regras à API
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ResultsPayload {
    /// Lista de resultados de aplicação de regras
    pub results: Vec<RuleResult>,
    
    /// Informações adicionais sobre o agente
    pub agent_info: serde_json::Value,
}

/// Informações armazenadas no cache local de regras
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RulesCache {
    pub rules: Vec<Rule>,
    pub version: String,
    #[serde(with = "chrono::serde::ts_seconds")]
    pub timestamp: DateTime<Utc>,
}

