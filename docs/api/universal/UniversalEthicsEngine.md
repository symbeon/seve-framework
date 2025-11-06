# API Reference: UniversalEthicsEngine

**Módulo**: `seve_framework.universal.ethics`  
**Classe Principal**: `UniversalEthicsEngine`

---

## Visão Geral

O `UniversalEthicsEngine` é o motor de ética multi-domínio do SEVE Framework. Ele avalia conformidade com princípios éticos universais (Privacidade, Transparência, Justiça, Responsabilidade, Autonomia) e agrega regras específicas por domínio (Healthcare, Education, etc.). Produz avaliações, recomendações e nível de risco consolidado.

- Integração nativa com `SEVEEthicsModule` (GuardFlow) no modo HYBRID/UNIVERSAL
- Retorna score global de compliance, violações críticas e recomendações
- Extensível via `DomainEthicsEngine` para regras de domínio

---

## Classe Principal

### `UniversalEthicsEngine`

```python
from seve_framework.universal.ethics import UniversalEthicsEngine

engine = UniversalEthicsEngine()
```

#### Métodos Principais

##### `async assess_universal_compliance(data: Dict[str, Any], context: Dict[str, Any], domain: Optional[str] = None) -> Dict[str, Any]`

Avalia compliance ético universal (e opcionalmente por domínio) para um determinado input.

Parâmetros:

- `data`: dados/processo/decisão a ser avaliado
- `context`: contexto de execução (timestamp, explicabilidade, consentimento, etc.)
- `domain`: domínio específico (ex.: "healthcare")

Retorno (exemplo):

```python
{
  "overall_compliance_score": 0.82,
  "assessments": [
    {"rule_id": "privacy_data_protection", "compliance_score": 0.9, ...},
    {"rule_id": "transparency_decisions", "compliance_score": 0.7, ...},
  ],
  "critical_violations": ["missing_encryption"],
  "recommendations": ["Habilitar criptografia at rest"],
  "risk_level": "medium",
  "domain": "healthcare"
}
```

##### `register_domain_engine(domain: str, engine: DomainEthicsEngine) -> None`

Registra um motor de ética específico de domínio.

##### `get_compliance_metrics() -> Dict[str, Any]`

Retorna métricas agregadas (histórico, média de scores, domínios cobertos, etc.).

---

## Classes de Suporte

### `DomainEthicsEngine`

Interface para motores de ética por domínio.

```python
from seve_framework.universal.ethics import DomainEthicsEngine

class HealthcareEthics(DomainEthicsEngine):
    def assess_ethical_compliance(self, data, context):
        return []
    def get_domain_rules(self):
        return []
    def apply_ethical_constraints(self, decision, context):
        return decision
```

### `EthicalRule`

Regra ética com princípio, severidade e descrição.

### `EthicalAssessment`

Resultado de avaliação de uma regra com score, violações e recomendações.

### Enums

- `EthicalPrinciple`: PRIVACY, TRANSPARENCY, FAIRNESS, ACCOUNTABILITY, AUTONOMY
- `EthicalComplianceLevel`: OPTIONAL, LOW, MEDIUM, HIGH, CRITICAL

---

## Exemplos

### Avaliação básica

```python
engine = UniversalEthicsEngine()

result = await engine.assess_universal_compliance(
    data={"personal_data": {"email": "user@example.com"}, "encrypted": False},
    context={"timestamp": 1234567890}
)

print(result["overall_compliance_score"])  # 0.0..1.0
print(result["critical_violations"])      # ["missing_encryption"]
print(result["recommendations"])          # ["Habilitar criptografia at rest"]
```

### Avaliação com domínio

```python
result = await engine.assess_universal_compliance(
    data={"patient_id": "P123"},
    context={"timestamp": 1234567890},
    domain="healthcare"
)
```

---

## Integração com GuardFlow (SEVEEthicsModule)

No modo HYBRID/UNIVERSAL, `SEVEEthicsModule` utiliza o `UniversalEthicsEngine` para obter contexto amplo (score e recomendações) e sempre executa as políticas críticas do GuardFlow. O resultado final combina as duas avaliações, mantendo a segurança e conformidade.

Pontos-chave:

- Universal fornece visão global e recomendações de mitigação
- GuardFlow aplica políticas obrigatórias e auditoria
- Fallback seguro: caso Universal falhe, GuardFlow continua ativo

---

## Métricas & Risco

- `overall_compliance_score`: ponderado por severidade (CRITICAL > HIGH > ...)
- `risk_level`:
  - `critical` se houver violações críticas
  - `high` se score < 0.5
  - `medium` se 0.5 ≤ score < 0.75
  - `low` se score ≥ 0.75

---

## Notas de Performance

- Avaliação universal: ~5-10ms (dependendo do volume de regras)
- Métricas agregadas mantidas em memória

---

## Referências

- ADR-008: Integração dos Módulos Universais
- WHY_I_CREATED_SEVE (princípio "Watch, not judge")
- BEST_PRACTICES (Seção de ética)
