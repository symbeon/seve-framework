# API Reference: SEVEUniversalCore

**Módulo**: `seve_framework.universal.core`  
**Classe Principal**: `SEVEUniversalCore`

---

## Visão Geral

O `SEVEUniversalCore` é o núcleo adaptativo universal do SEVE Framework, responsável por gerenciar adaptação contextual e orquestração de componentes para qualquer domínio de aplicação.

Permite que o SEVE opere em múltiplos nichos (Healthcare, Education, Business, Smart City, Gaming, Retail, Finance, Manufacturing) através de adaptadores de domínio que ajustam comportamento, regras e contexto conforme necessário.

---

## Classe Principal

### `SEVEUniversalCore`

```python
from seve_framework.universal import SEVEUniversalCore, DomainConfig, DomainType

# Criar configuração de domínio
config = DomainConfig(
    domain_type=DomainType.HEALTHCARE,
    domain_name="Healthcare System",
    cultural_context="brazil",
    adaptation_level=AdaptationLevel.ADVANCED
)

# Inicializar core universal
core = SEVEUniversalCore(config)
```

#### Métodos Principais

##### `process_universal_context(context, data) -> Dict[str, Any]`

Processa um contexto universal e retorna resultado adaptado ao domínio.

**Parâmetros**:
- `context` (UniversalContext): Contexto universal com informações de domínio, usuário e ambiente
- `data` (Any): Dados para processamento

**Retorna**:
```python
{
    "domain_result": Dict[str, Any],      # Resultado processado pelo adaptador
    "learning_result": Dict[str, Any],    # Resultado do aprendizado trans-domínio
    "adapted_context": UniversalContext,  # Contexto adaptado para o domínio
    "domain_features": Dict[str, Any]     # Características extraídas do domínio
}
```

**Exemplo**:
```python
from seve_framework.universal import UniversalContext, DomainType

context = UniversalContext(
    domain=DomainType.HEALTHCARE,
    user_profile={"patient_id": "P123"},
    environmental_data={"hospital": "General"},
    cultural_context="brazil",
    temporal_context={"timestamp": 1234567890},
    metadata={}
)

data = {"patient_id": "P123", "vitals": {"heart_rate": 72}}
result = await core.process_universal_context(context, data)
```

##### `switch_domain(new_config: DomainConfig) -> None`

Muda dinamicamente para um novo domínio em runtime.

**Parâmetros**:
- `new_config` (DomainConfig): Nova configuração de domínio

**Exemplo**:
```python
# Mudar de Healthcare para Education
new_config = DomainConfig(
    domain_type=DomainType.EDUCATION,
    domain_name="Education Platform"
)
core.switch_domain(new_config)
```

##### `get_domain_metrics() -> Dict[str, Any]`

Retorna métricas do domínio atual.

**Retorna**:
```python
{
    "domain": str,                    # Nome do domínio atual
    "adaptation_level": str,          # Nível de adaptação
    "cultural_context": str,          # Contexto cultural
    "registered_adapters": int,       # Número de adaptadores registrados
    "custom_adapters": int           # Número de adaptadores customizados
}
```

---

## Classes de Suporte

### `DomainConfig`

Configuração de domínio para o SEVE Universal.

```python
from seve_framework.universal import DomainConfig, DomainType, AdaptationLevel

config = DomainConfig(
    domain_type=DomainType.HEALTHCARE,
    domain_name="Healthcare System",
    cultural_context="brazil",
    adaptation_level=AdaptationLevel.ADVANCED,
    ethical_rules=["privacy", "fairness", "transparency"],
    personalization_rules=["adaptive_learning"],
    empathy_rules=["contextual_empathy"],
    custom_adapters=["custom_adapter_1"]
)
```

**Campos**:
- `domain_type` (DomainType): Tipo do domínio (requerido)
- `domain_name` (str): Nome do domínio (requerido)
- `cultural_context` (str): Contexto cultural (padrão: "global")
- `adaptation_level` (AdaptationLevel): Nível de adaptação (padrão: INTERMEDIATE)
- `ethical_rules` (List[str]): Regras éticas específicas do domínio
- `personalization_rules` (List[str]): Regras de personalização
- `empathy_rules` (List[str]): Regras de empatia
- `custom_adapters` (List[str]): Adaptadores customizados

### `UniversalContext`

Contexto universal transportado entre domínios.

```python
from seve_framework.universal import UniversalContext, DomainType

context = UniversalContext(
    domain=DomainType.HEALTHCARE,
    user_profile={"patient_id": "P123", "age": 45},
    environmental_data={"hospital": "General", "department": "Cardiology"},
    cultural_context="brazil",
    temporal_context={"timestamp": 1234567890, "timezone": "UTC-3"},
    metadata={"session_id": "sess_123", "request_id": "req_456"}
)
```

**Campos**:
- `domain` (DomainType): Domínio atual (requerido)
- `user_profile` (Dict[str, Any]): Perfil do usuário (requerido)
- `environmental_data` (Dict[str, Any]): Dados do ambiente (requerido)
- `cultural_context` (str): Contexto cultural (requerido)
- `temporal_context` (Dict[str, Any]): Contexto temporal (requerido)
- `metadata` (Dict[str, Any]): Metadados adicionais (requerido)

### `DomainType` (Enum)

Tipos de domínios suportados.

```python
from seve_framework.universal import DomainType

DomainType.HEALTHCARE      # Healthcare
DomainType.EDUCATION       # Education
DomainType.BUSINESS        # Business
DomainType.SMART_CITY      # Smart City
DomainType.GAMING          # Gaming
DomainType.RETAIL          # Retail
DomainType.FINANCE         # Finance
DomainType.MANUFACTURING   # Manufacturing
DomainType.CUSTOM          # Custom domain
```

### `AdaptationLevel` (Enum)

Níveis de adaptação disponíveis.

```python
from seve_framework.universal import AdaptationLevel

AdaptationLevel.BASIC         # Adaptação básica
AdaptationLevel.INTERMEDIATE  # Adaptação intermediária (padrão)
AdaptationLevel.ADVANCED      # Adaptação avançada
AdaptationLevel.EXPERT        # Adaptação especializada
```

### `DomainAdapterRegistry`

Registro de adaptadores de domínio.

```python
from seve_framework.universal import DomainAdapterRegistry, DomainType
from seve_framework.universal.adapters import HealthcareAdapter

registry = DomainAdapterRegistry()

# Registrar adaptador
adapter = HealthcareAdapter()
registry.register_adapter(DomainType.HEALTHCARE, adapter)

# Recuperar adaptador
adapter = registry.get_adapter(DomainType.HEALTHCARE)
```

**Métodos**:
- `register_adapter(domain: DomainType, adapter: DomainAdapter) -> None`
- `register_custom_adapter(name: str, adapter: DomainAdapter) -> None`
- `get_adapter(domain: DomainType) -> Optional[DomainAdapter]`
- `get_custom_adapter(name: str) -> Optional[DomainAdapter]`

---

## Componentes Relacionados

### `UniversalLearningModule`

Módulo de aprendizado trans-domínio.

```python
core = SEVEUniversalCore(config)
learning_module = core.learning_module

result = await learning_module.update_knowledge(
    result_data,
    context
)
```

### `UniversalContextManager`

Gerenciador de histórico de contextos.

```python
core = SEVEUniversalCore(config)
context_manager = core.context_manager

# Armazenar contexto
context_manager.store_context(context)

# Analisar padrões
patterns = context_manager.analyze_patterns()
```

---

## Exemplos de Uso

### Exemplo 1: Processamento Healthcare

```python
from seve_framework.universal import (
    SEVEUniversalCore,
    DomainConfig,
    DomainType,
    UniversalContext,
    AdaptationLevel
)

# Configurar para Healthcare
config = DomainConfig(
    domain_type=DomainType.HEALTHCARE,
    domain_name="Medical Assistant",
    cultural_context="brazil",
    adaptation_level=AdaptationLevel.ADVANCED,
    ethical_rules=["hipaa_compliance", "medical_privacy"]
)

core = SEVEUniversalCore(config)

# Criar contexto médico
context = UniversalContext(
    domain=DomainType.HEALTHCARE,
    user_profile={"patient_id": "P123", "age": 45, "gender": "M"},
    environmental_data={"hospital": "General", "department": "Cardiology"},
    cultural_context="brazil",
    temporal_context={"timestamp": 1234567890},
    metadata={"consultation_id": "cons_123"}
)

# Processar dados médicos
medical_data = {
    "patient_id": "P123",
    "vitals": {"heart_rate": 72, "blood_pressure": "120/80"},
    "symptoms": ["chest_pain", "shortness_of_breath"],
    "history": ["hypertension"]
}

result = await core.process_universal_context(context, medical_data)

# Resultado incluirá:
# - domain_features: Características médicas extraídas
# - domain_result: Resultado com regras médicas aplicadas
# - adapted_context: Contexto adaptado com metadados HIPAA
```

### Exemplo 2: Mudança Dinâmica de Domínio

```python
# Iniciar em Healthcare
config_health = DomainConfig(
    domain_type=DomainType.HEALTHCARE,
    domain_name="Healthcare"
)
core = SEVEUniversalCore(config_health)

# Processar algo em Healthcare
# ...

# Mudar para Education
config_edu = DomainConfig(
    domain_type=DomainType.EDUCATION,
    domain_name="Education Platform",
    cultural_context="usa"
)
core.switch_domain(config_edu)

# Agora processa em contexto educacional
context_edu = UniversalContext(
    domain=DomainType.EDUCATION,
    user_profile={"student_id": "S456"},
    environmental_data={"school": "Tech High"},
    cultural_context="usa",
    temporal_context={"timestamp": 1234567890},
    metadata={}
)

edu_data = {"student_id": "S456", "learning_style": "visual"}
result = await core.process_universal_context(context_edu, edu_data)
```

### Exemplo 3: Obter Métricas

```python
core = SEVEUniversalCore(config)
metrics = core.get_domain_metrics()

print(f"Domínio atual: {metrics['domain']}")
print(f"Nível de adaptação: {metrics['adaptation_level']}")
print(f"Adaptadores registrados: {metrics['registered_adapters']}")
```

---

## Integração com SEVEHybridFramework

O `SEVEUniversalCore` é usado automaticamente pelo `SEVEHybridFramework` quando em modo HYBRID ou UNIVERSAL.

```python
from seve_framework import SEVEHybridFramework, SEVEConfig, SEVEMode

config = SEVEConfig(
    mode=SEVEMode.HYBRID,  # Usa ambos v3.0 e Universal
    privacy_level=PrivacyLevel.HIGH,
    ethics_level=EthicsLevel.STRICT
)

framework = SEVEHybridFramework(config)
await framework.initialize()

# O framework automaticamente usa SEVEUniversalCore quando apropriado
capabilities = framework.get_capabilities()
if capabilities["universal_core_available"]:
    print("Universal Core disponível e ativo!")
```

---

## Notas de Performance

- **Inicialização**: ~20ms overhead comparado ao modo v3.0 puro
- **Processamento**: ~5-8ms overhead por contexto processado
- **Mudança de domínio**: ~10ms para reconfigurar

---

## Referências

- [Documentação de Adaptadores](./DomainAdapters.md)
- [Guia de Uso Universal](../universal/UNIVERSAL_MODE_GUIDE.md)
- [ADR-008: Integração dos Módulos Universais](../adr/ADR-008-universal-integration.md)

