# API Reference - SEVE Framework

**SEVE Framework v1.0.0**  
**Última Atualização**: 2025-01-29

---

## 📋 **Índice**

- [Python API](#python-api)
  - [Core Framework](#core-framework)
  - [Módulos](#módulos)
  - [Configuração](#configuração)
- [REST API](#rest-api)
  - [Endpoints](#endpoints)
  - [Autenticação](#autenticação)
  - [Modelos de Dados](#modelos-de-dados)
- [Smart Contracts](#smart-contracts)
  - [SEVEToken](#sevetoken)
  - [SEVEProtocol](#seveprotocol)
  - [SEVEDAO](#sevedao)

---

## Python API

### Core Framework

#### `SEVEHybridFramework`

Classe principal do framework, combina capacidades Universal e v3.0.

**Localização**: `seve_framework.core.SEVEHybridFramework`

**Inicialização:**
```python
from seve_framework import SEVEHybridFramework, SEVEConfig

config = SEVEConfig()
framework = SEVEHybridFramework(config)
await framework.initialize()
```

**Métodos Principais:**

##### `async initialize() -> None`
Inicializa todos os módulos do framework.

**Retorno**: `None`

**Exceções**:
- `RuntimeError`: Se inicialização falhar

**Exemplo:**
```python
await framework.initialize()
```

---

##### `async process_context(data: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcessingResult`
Processa dados multimodais com validação ética integrada.

**Parâmetros**:
- `data` (Dict[str, Any]): Dados de entrada (visual, sensor, etc.)
- `context` (Optional[Dict[str, Any]]): Contexto adicional (localização, consentimento, etc.)

**Retorno**: `ProcessingResult`

**Campos de `ProcessingResult`**:
- `status` (ProcessingStatus): Status da operação
- `data` (Dict[str, Any]): Dados processados
- `metadata` (Dict[str, Any]): Metadados do processamento
- `processing_time_ms` (float): Tempo de processamento em milissegundos
- `ethics_assessments` (List[Dict]): Avaliações éticas
- `errors` (List[str]): Erros encontrados

**Exemplo:**
```python
data = {
    "visual": {"image_path": "image.jpg"},
    "sensor": {"temperature": 23.5}
}
context = {"location": "downtown", "consent_given": True}

result = await framework.process_context(data, context)

if result.status == ProcessingStatus.COMPLETED:
    print(f"Processado em {result.processing_time_ms}ms")
```

---

##### `def get_capabilities() -> Dict[str, Any]`
Retorna capacidades e configuração do framework.

**Retorno**: `Dict[str, Any]` com:
- `version` (str): Versão do framework
- `universal_available` (bool): Se componentes Universal estão disponíveis
- `modes` (List[str]): Modos disponíveis
- `privacy_levels` (List[str]): Níveis de privacidade
- `ethics_levels` (List[str]): Níveis de ética
- `modules` (List[str]): Módulos disponíveis

**Exemplo:**
```python
capabilities = framework.get_capabilities()
print(f"Versão: {capabilities['version']}")
print(f"Módulos: {capabilities['modules']}")
```

---

##### `def get_status() -> Dict[str, Any]`
Retorna status atual do framework.

**Retorno**: `Dict[str, Any]` com:
- `initialized` (bool): Se está inicializado
- `processing_count` (int): Número de processamentos realizados
- `modules_status` (Dict): Status de cada módulo

**Exemplo:**
```python
status = framework.get_status()
if status['initialized']:
    print(f"Processamentos: {status['processing_count']}")
```

---

#### `SEVECoreV3`

Core v3.0 específico para visão computacional.

**Localização**: `seve_framework.core.SEVECoreV3`

**Métodos Principais:**

##### `async process_context(input_data: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcessingResult`
Processa contexto focado em visão computacional.

**Similar a `SEVEHybridFramework.process_context()`, mas otimizado para v3.0.**

---

#### `SEVEUniversalCore` 🔴 **ATUALIZADO**

Core Universal para adaptação multi-domínio (integrado no framework).

**Localização**: `seve_framework.universal.core.SEVEUniversalCore`

**📚 Documentação Completa**: [SEVEUniversalCore API Reference](./universal/SEVEUniversalCore.md)

**Métodos Principais:**

##### `async process_universal_context(context: UniversalContext, data: Dict[str, Any]) -> Dict[str, Any]`
Processa contexto Universal com adaptação de domínio.

**Parâmetros**:
- `context` (UniversalContext): Contexto Universal
- `data` (Dict[str, Any]): Dados a processar

**Retorno**: `Dict[str, Any]` com resultados adaptados ao domínio

**Exemplo:**
```python
from seve_framework.universal import SEVEUniversalCore, DomainConfig, DomainType, UniversalContext

config = DomainConfig(domain_type=DomainType.HEALTHCARE, domain_name="Healthcare System")
core = SEVEUniversalCore(config)

context = UniversalContext(
    domain=DomainType.HEALTHCARE,
    user_profile={"patient_id": "P123"},
    environmental_data={"hospital": "General"},
    cultural_context="brazil",
    temporal_context={"timestamp": 1234567890},
    metadata={}
)

result = await core.process_universal_context(context, {"patient_id": "P123", "vitals": {"heart_rate": 72}})
```

---

## Componentes Universais 🔴 **NOVO**

Componentes para adaptação multi-domínio e empatia computacional.

### SEVE Universal Core

- **[SEVEUniversalCore](./universal/SEVEUniversalCore.md)** 🔴 **NOVO**
  - Núcleo adaptativo universal
  - Gerenciamento de domínios e adaptadores
  - Processamento contextual multi-domínio

### Universal Empathy Engine

- **[UniversalEmpathyEngine](./universal/UniversalEmpathyEngine.md)** 🔴 **NOVO**
  - Motor de empatia computacional
  - Detecção de pistas emocionais
  - Adaptação cultural de respostas

### Universal Ethics Engine

- **[UniversalEthicsEngine](./universal/UniversalEthicsEngine.md)** 🔴 **NOVO**
  - Motor de ética multi-domínio
  - Avaliação de compliance global
  - Princípios éticos universais

### Domain Adapters

- **[Domain Adapters](./universal/DomainAdapters.md)** 🔴 **NOVO**
  - 8 adaptadores prontos (Healthcare, Education, Business, Smart City, Gaming, Retail, Finance, Manufacturing)
  - Registro e gerenciamento de adaptadores
  - Interface para adaptadores customizados

---

## Módulos

### SEVE-Vision

#### `SEVEVisionModule`

Módulo de visão computacional ética.

**Localização**: `seve_framework.vision.SEVEVisionModule`

**Métodos Principais:**

##### `async initialize() -> None`
Inicializa modelos de visão.

##### `async process_visual_input(image_data: Union[bytes, str, np.ndarray]) -> VisionProcessingResult`
Processa imagem/vídeo com anonimização automática.

**Parâmetros**:
- `image_data`: Imagem como bytes, path ou array numpy

**Retorno**: `VisionProcessingResult` com:
- `detected_objects` (List[str]): Objetos detectados
- `faces_detected` (int): Número de faces detectadas
- `anonymization_applied` (bool): Se anonimização foi aplicada
- `processing_time_ms` (float): Tempo de processamento

**Exemplo:**
```python
from seve_framework.vision import SEVEVisionModule

vision = SEVEVisionModule(config)
await vision.initialize()

result = await vision.process_visual_input("image.jpg")
print(f"Objetos: {result.detected_objects}")
```

---

### SEVE-Sense

#### `SEVESenseModule`

Módulo de processamento multimodal de sensores.

**Localização**: `seve_framework.sense.SEVESenseModule`

**Métodos Principais:**

##### `async process_multimodal_input(sensor_data: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> SenseProcessingResult`
Processa dados de múltiplos sensores.

**Parâmetros**:
- `sensor_data`: Dados de sensores (temperatura, movimento, etc.)
- `context`: Contexto adicional

**Retorno**: `SenseProcessingResult`

**Exemplo:**
```python
from seve_framework.sense import SEVESenseModule

sense = SEVESenseModule(config)
await sense.initialize()

sensor_data = {
    "temperature": 23.5,
    "motion": True,
    "proximity": 2.1
}
result = await sense.process_multimodal_input(sensor_data)
```

---

### SEVE-Ethics

#### `SEVEEthicsModule`

Módulo de validação ética (GuardFlow).

**Localização**: `seve_framework.ethics.SEVEEthicsModule`

**Métodos Principais:**

##### `async validate_decision(decision_data: Dict[str, Any]) -> EthicsValidationResult`
Valida decisão contra regras éticas.

**Parâmetros**:
- `decision_data`: Dados da decisão a validar

**Retorno**: `EthicsValidationResult` com:
- `result` (ValidationResult): BLOCKED, WARNING, APPROVED
- `rule_name` (str): Nome da regra aplicada
- `reason` (str): Razão do resultado
- `suggested_mitigation` (Optional[str]): Sugestão de mitigação

**Exemplo:**
```python
from seve_framework.ethics import SEVEEthicsModule

ethics = SEVEEthicsModule(config)
await ethics.initialize()

decision = {
    "action": "store_personal_data",
    "data_type": "facial_recognition",
    "consent": False
}

validation = await ethics.validate_decision(decision)
if validation.result == ValidationResult.BLOCKED:
    print(f"Bloqueado: {validation.reason}")
```

---

### SEVE-Link

#### `SEVELinkModule`

Módulo de conectividade e integração.

**Localização**: `seve_framework.link.SEVELinkModule`

**Métodos Principais:**

##### `async connect_external_system(system_type: str, config: Dict[str, Any]) -> str`
Conecta com sistema externo (ERP, IoT, etc.).

**Parâmetros**:
- `system_type`: Tipo de sistema ("erp", "iot", etc.)
- `config`: Configuração de conexão

**Retorno**: `str` - ID da conexão

##### `async sync_transaction(transaction_data: Dict[str, Any], connection_id: str) -> SyncResult`
Sincroniza transação com sistema externo.

**Parâmetros**:
- `transaction_data`: Dados da transação
- `connection_id`: ID da conexão

**Retorno**: `SyncResult`

---

## Configuração

### `SEVEConfig`

Classe de configuração do framework.

**Localização**: `seve_framework.config.SEVEConfig`

**Parâmetros de Inicialização:**
- `mode` (SEVEMode): Modo de operação (HYBRID, VISION_SPECIFIC, UNIVERSAL)
- `privacy_level` (PrivacyLevel): Nível de privacidade (MINIMUM, MODERATE, HIGH, MAXIMUM)
- `ethics_level` (EthicsLevel): Nível de ética (MINIMUM, MODERATE, STRICT, MAXIMUM)
- `debug` (bool): Modo debug

**Exemplo:**
```python
from seve_framework.config import SEVEConfig, SEVEMode, PrivacyLevel, EthicsLevel

config = SEVEConfig(
    mode=SEVEMode.HYBRID,
    privacy_level=PrivacyLevel.HIGH,
    ethics_level=EthicsLevel.STRICT,
    debug=True
)
```

---

## REST API

### Base URL

```
http://localhost:8000
```

### Endpoints

#### `GET /health`

Health check do servidor.

**Resposta:**
```json
{
  "status": "healthy",
  "framework_initialized": true,
  "timestamp": "2025-01-29T10:00:00Z"
}
```

---

#### `POST /api/v1/process`

Processa dados com SEVE Framework.

**Request Body:**
```json
{
  "sensor_data": {
    "temperature": 23.5,
    "motion": true
  },
  "context": {
    "location": "downtown",
    "consent_given": true
  },
  "privacy_level": "high"
}
```

**Resposta:**
```json
{
  "status": "completed",
  "processing_time_ms": 123.45,
  "result": {
    "processed_data": {...}
  },
  "ethics_validation": {
    "passed": true,
    "assessments": [...]
  }
}
```

**Códigos de Status:**
- `200`: Sucesso
- `400`: Requisição inválida
- `500`: Erro interno

---

#### `POST /api/v1/process-image`

Processa imagem com SEVE-Vision.

**Request**: `multipart/form-data`
- `file`: Arquivo de imagem (jpg, png, etc.)

**Resposta:**
```json
{
  "status": "success",
  "detected_objects": ["person", "car"],
  "faces_detected": 2,
  "anonymization_applied": true,
  "privacy_protected": true
}
```

---

#### `GET /api/v1/capabilities`

Retorna capacidades do framework.

**Resposta:**
```json
{
  "version": "1.0.0",
  "universal_available": false,
  "modes": ["hybrid", "vision_specific"],
  "modules": ["SEVEVisionModule", "SEVESenseModule", ...]
}
```

---

#### `POST /webhook/erp/{event_type}`

Webhook para eventos de ERP.

**Path Parameters:**
- `event_type`: Tipo de evento (order_created, payment_received, etc.)

**Request Body:**
```json
{
  "event_id": "evt_123",
  "data": {...}
}
```

---

## Smart Contracts

Veja documentação detalhada em:
- [SEVEToken API](./smart-contracts/SEVEToken.md)
- [SEVEProtocol API](./smart-contracts/SEVEProtocol.md)
- [SEVEDAO API](./smart-contracts/SEVEDAO.md)

---

## 📞 **Suporte**

- **Documentação**: [Índice Completo](../INDEX.md)
- **FAQ**: [FAQ.md](../FAQ.md)
- **GitHub Issues**: [Reportar problema](https://github.com/symbeon/seve-framework/issues)

---

**Mantido por**: Equipe EON - Symbeon Tech

