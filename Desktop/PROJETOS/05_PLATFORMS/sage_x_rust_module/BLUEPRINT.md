# Blueprint: Integração WARP_RULES com SAGE-X Rust Module

## 1. Diagrama de Arquitetura do Sistema

```
+--------------------------------------+       +--------------------------------------+
|           Sistema Python             |       |            Sistema Rust              |
|                                      |       |                                      |
|  +--------------------------------+  |       |  +--------------------------------+  |
|  |         WARP_RULES             |  |       |  |      sage_x_rust_module        |  |
|  |                                |  |       |  |                                |  |
|  |  +------------------------+    |  |       |  |  +------------------------+    |  |
|  |  |     warp_rules.json    |    |  |       |  |  |    warp_rules_client   |    |  |
|  |  +------------------------+    |  |       |  |  |                        |    |  |
|  |                                |  |       |  |  |    +---------------+   |    |  |
|  |  +------------------------+    |  |       |  |  |    |    models     |   |    |  |
|  |  | warp_rules_importer.py |    |  |       |  |  |    +---------------+   |    |  |
|  |  +------------------------+    |  |       |  |  |                        |    |  |
|  |                                |  |       |  |  |    +---------------+   |    |  |
|  |  +------------------------+    |  |       |  |  |    |     sync      |   |    |  |
|  |  |   apply_warp_rules.py  |    |  |       |  |  |    +---------------+   |    |  |
|  |  +------------------------+    |  |       |  |  |                        |    |  |
|  |                                |  |       |  |  |    +---------------+   |    |  |
|  |  +------------------------+    |  |       |  |  |    |    engine     |   |    |  |
|  |  |   warp_rules_api.py    |<---|--+-------|--+--|--->+---------------+   |    |  |
|  |  +------------------------+    |  |       |  |  |                        |    |  |
|  |                                |  |       |  |  +------------------------+    |  |
|  +--------------------------------+  |       |  |                                |  |
|                                      |       |  |  +------------------------+    |  |
|                                      |       |  |  |        main.rs        |    |  |
|                                      |       |  |  +------------------------+    |  |
|                                      |       |  |                                |  |
+--------------------------------------+       +--+------------------+-------------+  |
                                                  |                  |                |
                                                  |                  |                |
                                                  v                  v                |
                                       +------------------+  +----------------+       |
                                       |   EON-Framework  |  |  Outros Sistemas|      |
                                       +------------------+  +----------------+       |
```

O diagrama representa a arquitetura completa do sistema integrado. À esquerda, temos o Sistema Python com o WARP_RULES, responsável pelo gerenciamento, definição e disponibilização das regras via API. À direita, temos o Sistema Rust com o sage_x_rust_module, que consome as regras, aplica-as no contexto do agente, e utiliza o comportamento ajustado para interagir com o EON-Framework e outros sistemas.

A comunicação entre os sistemas ocorre através da API REST definida em warp_rules_api.py e consumida pelo cliente Rust. Essa integração permite que as regras definidas no lado Python influenciem o comportamento do agente Rust sem necessidade de recompilação.

## 2. Estrutura Analítica do Projeto (EAP)

```
Integração WARP_RULES ↔ SAGE-X
│
├── 1. Sistema Python (WARP_RULES)
│   ├── 1.1. Armazenamento de Regras
│   │   └── 1.1.1. warp_rules.json
│   │
│   ├── 1.2. Gerenciamento de Regras
│   │   ├── 1.2.1. warp_rules_importer.py
│   │   └── 1.2.2. apply_warp_rules.py
│   │
│   └── 1.3. API de Regras
│       ├── 1.3.1. Endpoints RESTful
│       │   ├── 1.3.1.1. GET /api/rules/v1/rules
│       │   ├── 1.3.1.2. GET /api/rules/v1/rules/{rule_id}
│       │   ├── 1.3.1.3. GET /api/rules/v1/rules/stream
│       │   └── 1.3.1.4. POST /api/rules/v1/results
│       │
│       ├── 1.3.2. Autenticação e Segurança
│       │   ├── 1.3.2.1. JWT Authentication
│       │   └── 1.3.2.2. ETag para Versionamento
│       │
│       └── 1.3.3. Event Streaming
│           └── 1.3.3.1. Server-Sent Events (SSE)
│
├── 2. Sistema Rust (sage_x_rust_module)
│   ├── 2.1. Biblioteca Cliente (warp_rules_client)
│   │   ├── 2.1.1. Modelos de Dados (models.rs)
│   │   │   ├── 2.1.1.1. Estruturas de Regras
│   │   │   ├── 2.1.1.2. Estruturas de Autenticação
│   │   │   └── 2.1.1.3. Estruturas de Resultado
│   │   │
│   │   ├── 2.1.2. Comunicação HTTP (sync.rs)
│   │   │   ├── 2.1.2.1. Cliente RESTful
│   │   │   ├── 2.1.2.2. Autenticação JWT
│   │   │   ├── 2.1.2.3. Cache de Regras
│   │   │   └── 2.1.2.4. Stream de Eventos
│   │   │
│   │   ├── 2.1.3. Motor de Regras (engine.rs)
│   │   │   ├── 2.1.3.1. Parser de Regras
│   │   │   ├── 2.1.3.2. Avaliador de Condições
│   │   │   ├── 2.1.3.3. Executor de Ações
│   │   │   └── 2.1.3.4. Registro de Resultados
│   │   │
│   │   └── 2.1.4. Interface Pública (lib.rs)
│   │       ├── 2.1.4.1. Inicialização Assíncrona
│   │       ├── 2.1.4.2. Busca de Regras
│   │       ├── 2.1.4.3. Aplicação de Regras
│   │       └── 2.1.4.4. Monitoramento de Atualizações
│   │
│   └── 2.2. Aplicação de Exemplo (main.rs)
│       ├── 2.2.1. Configuração do Cliente
│       ├── 2.2.2. Busca e Aplicação de Regras
│       ├── 2.2.3. Integração com EON-Framework
│       └── 2.2.4. Envio de Resultados
│
└── 3. Integração e Testes
    ├── 3.1. Autenticação entre Sistemas
    ├── 3.2. Cache e Sincronização
    ├── 3.3. Event-Sourcing
    └── 3.4. Resiliência e Fallbacks
```

## 3. Features Implementadas

### 3.1. Sistema Python (WARP_RULES)

#### 3.1.1. Armazenamento e Gerenciamento de Regras
- **Formato JSON**: Armazenamento de regras em formato JSON, facilitando a edição manual e serialização.
- **Scripts de Importação**: Ferramentas para importar regras de diferentes fontes e formatos.
- **Aplicação Local**: Capacidade de testar regras localmente antes de disponibilizá-las.

#### 3.1.2. API RESTful
- **Endpoints Versão 1**: API RESTful com endpoints específicos para integração com Rust.
- **Versionamento**: Suporte a ETag para cache e versionamento de recursos.
- **Streaming de Eventos**: Server-Sent Events para notificações em tempo real de alterações.
- **Resultados**: Endpoint para receber feedback sobre aplicação de regras.

#### 3.1.3. Segurança
- **Autenticação JWT**: Tokens JWT para autenticação segura entre sistemas.
- **CORS**: Configuração de CORS para integração web.
- **Validação**: Validação de entrada utilizando Pydantic.

### 3.2. Sistema Rust (sage_x_rust_module)

#### 3.2.1. Cliente de API
- **Comunicação HTTP Assíncrona**: Cliente HTTP assíncrono usando reqwest e tokio.
- **Autenticação**: Autenticação automática e renovação de tokens.
- **Cache**: Cache local de regras para resiliência e desempenho.
- **Streaming**: Suporte a Server-Sent Events para atualizações em tempo real.

#### 3.2.2. Motor de Regras
- **Parser de Regras**: Análise de regras em formato de texto.
- **Avaliador de Condições**: Avaliação de condições para aplicação de regras.
- **Executor de Ações**: Aplicação de diferentes tipos de ações ao contexto do agente.
- **Registro**: Registro detalhado dos resultados de aplicação de regras.

#### 3.2.3. Biblioteca Client
- **API Simples**: Interface pública simples e intuitiva.
- **Configuração Flexível**: Opções de configuração para diferentes cenários.
- **Monitoramento em Background**: Atualização automática de regras em background.
- **Builder Pattern**: Métodos encadeados para construção do cliente.

#### 3.2.4. Integração EON-Framework
- **Contexto do Agente**: As regras modificam o contexto do agente.
- **Comportamento Adaptativo**: O comportamento do agente se adapta com base nas regras.
- **Feedback Bidirecional**: Envio de resultados de volta para WARP_RULES.

## 4. Modos de Uso Recomendados

### 4.1. Implementação de Novos Agentes

Para integrar novos agentes ao sistema, siga estas etapas:

1. **Configuração do Cliente**:
   ```rust
   let config = ClientConfig {
       api_url: "http://localhost:8001".to_string(),
       credentials: Some(Credentials {
           client_id: "seu_agente_id".to_string(),
           client_secret: "seu_segredo".to_string(),
       }),
       use_sse: true,  // Recomendado para ambientes de produção
       ..Default::default()
   };
   
   let mut client = WarpRulesClient::new(config);
   client.init().await?;
   ```

2. **Criação e Atualização do Contexto**:
   ```rust
   // Crie um contexto para seu agente
   let mut context = AgentContext::default();
   context.agent_id = "seu_agente_id".to_string();
   context.agent_name = "Nome do Agente".to_string();
   
   // Defina o estado inicial
   context.state.insert("capabilities".to_string(), json!(["nlp", "vision"]));
   context.state.insert("version".to_string(), json!("1.0.0"));
   
   // Busque e aplique regras
   let rules = client.fetch_rules().await?;
   let results = client.apply_rules(&mut context).await?;
   
   // Envie os resultados de volta
   client.send_results(&context).await?;
   ```

3. **Monitoramento de Regras**:
   ```rust
   // Inicie o monitoramento em background
   client.start_monitor()?;
   
   // Seu código principal aqui...
   
   // Pare o monitoramento quando terminar
   client.stop_monitor();
   ```

### 4.2. Definição de Regras

As regras devem seguir um formato específico para serem corretamente interpretadas pelo motor:

```json
{
  "id": "frameworks_preferidos",
  "name": "Frameworks de Desenvolvimento Preferidos",
  "description": "rule: O agente deve preferir FastAPI para APIs assíncronas e microserviços IA.\n\n• Define framework_web como FastAPI\n• Sugere utilizar documentação OpenAPI\n• Restringe uso de frameworks síncronos\n• Preferência por asynchronous_apis: true",
  "active": true
}
```

O motor de regras interpreta diferentes diretivas:
- `Define/Set/Configura`: Define um valor no contexto
- `Sugere/Recomenda`: Sugere um comportamento (não altera o contexto)
- `Restringe/Evita`: Define uma restrição (não altera o contexto)
- `Preferência por`: Define uma preferência no contexto com prefixo "pref_"

### 4.3. Monitoramento e Depuração

Para monitoramento e depuração, utilize:

1. **Logs**:
   ```rust
   // Configure o logger
   let mut builder = Builder::new();
   builder.filter_level(LevelFilter::Debug);  // Mais detalhado para depuração
   builder.init();
   ```

2. **Verificação de Resultados**:
   ```rust
   // Após aplicar regras
   for result in &results {
       if result.applied {
           println!("Regra aplicada: {}", result.rule_id);
           if let Some(outcome) = &result.outcome {
               println!("Resultado: {}", outcome);
           }
       } else {
           println!("Regra

