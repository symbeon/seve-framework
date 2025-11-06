# API Reference: Domain Adapters

**Módulo**: `seve_framework.universal.adapters`  
**Relacionado**: `seve_framework.universal.core.DomainAdapterRegistry`

---

## Visão Geral

Os Domain Adapters permitem adaptar o comportamento do SEVE para diferentes nichos (Healthcare, Education, Business, Smart City, Gaming, Retail, Finance, Manufacturing). Fornecem:

- Adaptação de contexto (`adapt_to_context`)
- Extração de features específicas do domínio (`extract_domain_features`)
- Aplicação de regras do domínio (`apply_domain_rules`)

Os adaptadores são utilizados pelo `SEVEUniversalCore` durante `process_universal_context`.

---

## Registro de Adaptadores

### `DomainAdapterRegistry`

```python
from seve_framework.universal import DomainAdapterRegistry, DomainType
from seve_framework.universal.adapters import HealthcareAdapter

registry = DomainAdapterRegistry()
registry.register_adapter(DomainType.HEALTHCARE, HealthcareAdapter())

adapter = registry.get_adapter(DomainType.HEALTHCARE)
```

Métodos:
- `register_adapter(domain: DomainType, adapter: DomainAdapter) -> None`
- `register_custom_adapter(name: str, adapter: DomainAdapter) -> None`
- `get_adapter(domain: DomainType) -> Optional[DomainAdapter]`
- `get_custom_adapter(name: str) -> Optional[DomainAdapter]`
- `list_available_domains() -> List[DomainType]`
- `get_adapter_info(domain: DomainType) -> Dict[str, Any]`

---

## Interface do Adaptador

### `DomainAdapter` (ABC)

Assinatura típica:
```python
class DomainAdapter(ABC):
    def adapt_to_context(self, context: UniversalContext) -> UniversalContext: ...
    def extract_domain_features(self, data: Dict[str, Any]) -> Dict[str, Any]: ...
    def apply_domain_rules(self, decision: Dict[str, Any]) -> Dict[str, Any]: ...
```

---

## Adaptadores Disponíveis

### HealthcareAdapter
- Metadados: `medical_privacy=True`, `hipaa_compliance=True`, `patient_safety=True`
- Features: `patient_id`, `medical_history`, `vital_signs`, `diagnosis`, `treatment`
- Regras: segurança do paciente, proteção de privacidade

### EducationAdapter
- Metadados: `learning_objectives=True`, `student_privacy=True`, `educational_standards=True`
- Features: `learning_style`, `academic_level`, `subject_matter`, `learning_progress`
- Regras: adequação pedagógica, privacidade de estudantes

### BusinessAdapter
- Metadados: conformidade corporativa e governança
- Features: `customer_segments`, `kpis`, `operations`
- Regras: compliance, risco operacional

### SmartCityAdapter
- Metadados: dados urbanos e padrões de sustentabilidade
- Features: `traffic`, `energy`, `sensors`
- Regras: segurança pública, privacidade urbana

### GamingAdapter
- Metadados: experiência do jogador e fairness
- Features: `session_stats`, `player_profile`
- Regras: anticheat, balanceamento

### RetailAdapter
- Metadados: `customer_privacy=True`, `esg_compliance=True`, `inventory_management=True`
- Features: `customer_profile`, `product_catalog`, `purchase_history`, `inventory`, `esg_scores`
- Regras: práticas ESG, proteção de dados do cliente

### FinanceAdapter
- Metadados: conformidade regulatória (KYC/AML)
- Features: `accounts`, `transactions`, `risk_scores`
- Regras: prevenção à fraude, risco financeiro

### ManufacturingAdapter
- Metadados: segurança industrial
- Features: `production_line`, `quality_metrics`, `maintenance`
- Regras: segurança, qualidade, downtime

---

## Exemplo Completo

```python
from seve_framework.universal import (
    SEVEUniversalCore, DomainConfig, DomainType, UniversalContext
)
from seve_framework.universal.adapters import HealthcareAdapter

# 1) Configurar domínio
config = DomainConfig(domain_type=DomainType.HEALTHCARE, domain_name="Medical Assistant")
core = SEVEUniversalCore(config)

# 2) Registrar adaptador
core.domain_adapter_registry.register_adapter(DomainType.HEALTHCARE, HealthcareAdapter())

# 3) Criar contexto
context = UniversalContext(
    domain=DomainType.HEALTHCARE,
    user_profile={"patient_id": "P123"},
    environmental_data={"hospital": "General"},
    cultural_context="brazil",
    temporal_context={"timestamp": 1234567890},
    metadata={}
)

# 4) Processar
data = {"patient_id": "P123", "vitals": {"heart_rate": 72}}
result = await core.process_universal_context(context, data)

print(result["domain_features"])   # features extraídas
print(result["domain_result"])     # resultado de regras do domínio
```

---

## Boas Práticas
- Sempre definir metadados de compliance (ex.: HIPAA, ESG) no `adapt_to_context`
- Reduzir dados sensíveis no `extract_domain_features` (privacy by design)
- Isolar efeitos colaterais e validar entradas em `apply_domain_rules`

---

## Referências
- `docs/MODULE_CLASSIFICATION_BY_NICHE.md`
- `docs/TECHNICAL_VALIDATION_ALIGNMENT.md`
- `docs/adr/ADR-008-universal-integration.md`
