# Guia do Modo Universal / HYBRID

Este guia explica como ativar e usar os recursos do `SEVEUniversalCore`, adaptadores de domínio, Empathy e Universal Ethics dentro do SEVE Framework nos modos UNIVERSAL e HYBRID.

---

## 1. Conceitos

- **UNIVERSAL**: Usa apenas o núcleo universal para adaptação multi-domínio (sem pipeline v3 dedicado de visão).
- **HYBRID**: Combina o pipeline v3 (visão, sense) com o núcleo universal para enriquecer contexto, empatia e ética.

---

## 2. Configuração Rápida

```python
from seve_framework import SEVEHybridFramework
from seve_framework.config import SEVEConfig, SEVEMode, PrivacyLevel, EthicsLevel

config = SEVEConfig(
    mode=SEVEMode.HYBRID,            # ou SEVEMode.UNIVERSAL
    privacy_level=PrivacyLevel.HIGH,
    ethics_level=EthicsLevel.STRICT
)

framework = SEVEHybridFramework(config)
await framework.initialize()
print(framework.get_capabilities())
```

---

## 3. Uso do Universal Core

```python
from seve_framework.universal import (
    SEVEUniversalCore, DomainConfig, DomainType, UniversalContext, AdaptationLevel
)

config = DomainConfig(
    domain_type=DomainType.HEALTHCARE,
    domain_name="Medical Assistant",
    cultural_context="brazil",
    adaptation_level=AdaptationLevel.ADVANCED
)

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

## 4. Adaptadores de Domínio

```python
from seve_framework.universal import DomainType
from seve_framework.universal.adapters import HealthcareAdapter

core.domain_adapter_registry.register_adapter(DomainType.HEALTHCARE, HealthcareAdapter())
```

- Consulte a API completa em: `docs/api/universal/DomainAdapters.md`

---

## 5. Empatia Computacional

```python
from seve_framework.universal import UniversalEmpathyEngine, EmpathyContext, EmotionalState

empathy = UniversalEmpathyEngine()
context = EmpathyContext(
    user_state=EmotionalState.STRESSED,
    domain_context="healthcare",
    cultural_context="brazil",
    sensitivity_level="high"
)

response = await empathy.generate_universal_empathy(context, {"text": "preocupado com exame"})
print(response.message)
```

- API: `docs/api/universal/UniversalEmpathyEngine.md`

---

## 6. Ética Universal + GuardFlow (HYBRID)

```python
from seve_framework.ethics import SEVEEthicsModule
from seve_framework.config import SEVEConfig, SEVEMode, EthicsLevel

ethics_cfg = SEVEConfig(mode=SEVEMode.HYBRID, ethics_level=EthicsLevel.STRICT)
ethics = SEVEEthicsModule(ethics_cfg)
await ethics.initialize()

assessments = await ethics.validate_decision(
    {"personal_data": {"email": "user@example.com"}, "encrypted": False},
    context={"domain": "healthcare"}
)

for a in assessments:
    print(a)
```

- API: `docs/api/universal/UniversalEthicsEngine.md`

---

## 7. Boas Práticas

- Use HYBRID quando precisar de visão/sensores + contexto universal
- Sempre registrar adaptadores do domínio antes de processar contexto
- Em Healthcare/Finance, priorize `ethics_level=STRICT`
- Mantenha logs de auditoria habilitados ao validar decisões

---

## 8. Solução de Problemas

- ImportError (cv2/torch): use testes com mocks (veja `tests/conftest.py`)
- Sem adaptador: registre adaptadores com `DomainAdapterRegistry`
- Score baixo de compliance: aplique recomendações sugeridas pelo UniversalEthicsEngine

---

## 9. Referências

- `docs/api/universal/SEVEUniversalCore.md`
- `docs/api/universal/UniversalEmpathyEngine.md`
- `docs/api/universal/UniversalEthicsEngine.md`
- `docs/api/universal/DomainAdapters.md`
