# API Reference: UniversalEmpathyEngine

**Módulo**: `seve_framework.universal.empathy`  
**Classe Principal**: `UniversalEmpathyEngine`

---

## Visão Geral

O `UniversalEmpathyEngine` é o motor de empatia computacional do SEVE Framework, responsável por gerar respostas empáticas contextualizadas para qualquer domínio de aplicação.

Implementa detecção de pistas emocionais, geração de mensagens empáticas culturalmente adaptadas, e suporte contextual baseado no estado emocional do usuário e no domínio de aplicação.

**Princípio Fundamental**: "Watch, not judge" - Observar e apoiar emocionalmente, sem julgar.

---

## Classe Principal

### `UniversalEmpathyEngine`

```python
from seve_framework.universal import UniversalEmpathyEngine, EmpathyContext, EmotionalState

engine = UniversalEmpathyEngine()

context = EmpathyContext(
    user_state=EmotionalState.STRESSED,
    domain_context="healthcare",
    cultural_context="brazil",
    sensitivity_level="high"
)

situation = {
    "text": "estou preocupado com os resultados do exame",
    "situation": "resultados médicos",
    "stress_source": "incerteza diagnóstica"
}

response = await engine.generate_universal_empathy(context, situation)
print(response.message)
```

---

## Métodos Principais

### `generate_universal_empathy(context, situation, domain=None) -> EmpathyResponse`

Gera resposta empática universal adaptada ao contexto.

**Parâmetros**:
- `context` (EmpathyContext): Contexto empático com estado do usuário e configurações
- `situation` (Dict[str, Any]): Situação específica com dados e pistas emocionais
- `domain` (Optional[str]): Domínio específico para adaptação (opcional)

**Retorna**: `EmpathyResponse`

**Exemplo**:
```python
context = EmpathyContext(
    user_state=EmotionalState.CONFUSED,
    domain_context="education",
    cultural_context="usa",
    urgency_level="normal",
    sensitivity_level="medium"
)

situation = {
    "text": "I don't understand this concept",
    "context": "mathematics lesson",
    "confusion_point": "algebraic equations"
}

response = await engine.generate_universal_empathy(context, situation, domain="education")

# Response contém:
# - message: Mensagem empática adaptada
# - supportive_actions: Ações de suporte sugeridas
# - cultural_adaptations: Adaptações culturais aplicadas
# - confidence_score: Score de confiança da resposta
```

### `register_domain_engine(domain: str, engine: DomainEmpathyEngine) -> None`

Registra motor de empatia específico para um domínio.

**Parâmetros**:
- `domain` (str): Nome do domínio
- `engine` (DomainEmpathyEngine): Motor de empatia do domínio

**Exemplo**:
```python
from seve_framework.universal.empathy import DomainEmpathyEngine

class HealthcareEmpathyEngine(DomainEmpathyEngine):
    def generate_domain_empathy(self, context, situation):
        # Implementação específica para healthcare
        pass
    # ... outros métodos obrigatórios

engine.register_domain_engine("healthcare", HealthcareEmpathyEngine())
```

### `export_history() -> str`

Exporta histórico de respostas empáticas em JSON.

**Retorna**: String JSON com histórico

**Exemplo**:
```python
history_json = engine.export_history()
print(history_json)
```

---

## Classes de Suporte

### `EmpathyContext`

Contexto para geração de empatia.

```python
from seve_framework.universal import EmpathyContext, EmotionalState

context = EmpathyContext(
    user_state=EmotionalState.POSITIVE,
    domain_context="retail",
    cultural_context="brazil",
    urgency_level="normal",
    communication_style="professional",
    sensitivity_level="medium",
    metadata={"session_id": "sess_123"}
)
```

**Campos**:
- `user_state` (EmotionalState): Estado emocional do usuário (requerido)
- `domain_context` (str): Contexto do domínio (requerido)
- `cultural_context` (str): Contexto cultural (requerido)
- `urgency_level` (str): Nível de urgência (padrão: "normal")
- `communication_style` (str): Estilo de comunicação (padrão: "professional")
- `sensitivity_level` (str): Nível de sensibilidade (padrão: "medium")
- `metadata` (Dict[str, Any]): Metadados adicionais

### `EmpathyResponse`

Resposta empática gerada.

```python
from seve_framework.universal import EmpathyResponse, EmpathyType

response = EmpathyResponse(
    empathy_type=EmpathyType.COMPASSIONATE,
    emotional_tone="supportive",
    message="Entendo sua preocupação...",
    supportive_actions=["Oferecer esclarecimentos", "Buscar recursos"],
    cultural_adaptations={"greeting": "Olá!"},
    confidence_score=0.85
)
```

**Campos**:
- `empathy_type` (EmpathyType): Tipo de empatia aplicada
- `emotional_tone` (str): Tom emocional da resposta
- `message` (str): Mensagem empática gerada
- `supportive_actions` (List[str]): Ações de suporte sugeridas
- `cultural_adaptations` (Dict[str, Any]): Adaptações culturais aplicadas
- `confidence_score` (float): Score de confiança (0.0 a 1.0)
- `metadata` (Dict[str, Any]): Metadados da resposta

### `EmpathyType` (Enum)

Tipos de empatia disponíveis.

```python
from seve_framework.universal import EmpathyType

EmpathyType.COGNITIVE       # Compreensão intelectual
EmpathyType.EMOTIONAL       # Compartilhamento emocional
EmpathyType.COMPASSIONATE  # Preocupação e cuidado
EmpathyType.CULTURAL       # Sensibilidade cultural
EmpathyType.CONTEXTUAL     # Adaptação ao contexto
```

### `EmotionalState` (Enum)

Estados emocionais suportados.

```python
from seve_framework.universal import EmotionalState

EmotionalState.POSITIVE    # Positivo
EmotionalState.NEGATIVE   # Negativo
EmotionalState.NEUTRAL    # Neutro
EmotionalState.STRESSED   # Estressado
EmotionalState.EXCITED    # Animado
EmotionalState.CONCERNED  # Preocupado
EmotionalState.CONFUSED    # Confuso
EmotionalState.SATISFIED  # Satisfeito
```

---

## Funcionalidades

### Detecção de Pistas Emocionais

O engine detecta automaticamente pistas emocionais de:

1. **Texto**: Análise de palavras-chave emocionais
   - Positivo: "feliz", "satisfeito", "ótimo", "excelente"
   - Negativo: "preocupado", "triste", "frustrado", "difícil"
   - Estressado: "estressado", "pressão", "urgente"
   - Confuso: "confuso", "não entendo", "explicar"

2. **Métricas**: Análise de métricas numéricas
   - Alta satisfação (score > 0.8) → POSITIVE
   - Alta taxa de erro (rate > 0.1) → CONCERNED

3. **Contexto**: Análise de contexto
   - Alta urgência → STRESSED

### Adaptação Cultural

O engine adapta mensagens para diferentes culturas:

**Brasil**:
- Estilo: "warm_and_personal"
- Formulidade: "medium"
- Saudações: "Olá", "Oi", "Bom dia/tarde/noite"

**USA**:
- Estilo: "direct_and_efficient"
- Formulidade: "low"
- Saudações: "Hello", "Hi", "Good morning/afternoon/evening"

**Japão**:
- Estilo: "polite_and_respectful"
- Formulidade: "high"
- Saudações: "Konnichiwa", "Ohayou gozaimasu", "Konbanwa"

**Global** (padrão):
- Estilo: "professional_and_inclusive"
- Formulidade: "medium"

### Templates de Empatia

O engine usa templates pré-configurados para diferentes estados:

- **Acknowledgment**: Reconhecimento da situação
- **Support**: Mensagens de suporte
- **Action**: Ações de suporte sugeridas

---

## Exemplos de Uso

### Exemplo 1: Suporte ao Cliente (Retail)

```python
from seve_framework.universal import (
    UniversalEmpathyEngine,
    EmpathyContext,
    EmotionalState
)

engine = UniversalEmpathyEngine()

# Cliente frustrado com produto
context = EmpathyContext(
    user_state=EmotionalState.NEGATIVE,
    domain_context="retail",
    cultural_context="brazil",
    sensitivity_level="high"
)

situation = {
    "text": "frustrado com produto quebrado",
    "situation": "produto defeituoso",
    "challenging_aspect": "preciso de troca urgente",
    "solution_approach": "resolver a situação rapidamente"
}

response = await engine.generate_universal_empathy(context, situation)

print(response.message)
# "Reconheço que produto defeituoso pode ser frustrante. Sua preocupação é compreensível. 
#  Estou aqui para ajudar você a resolver a situação rapidamente."

print(response.supportive_actions)
# ["Identificar soluções", "Buscar alternativas", "Oferecer suporte"]
```

### Exemplo 2: Suporte Educacional

```python
# Estudante confuso
context = EmpathyContext(
    user_state=EmotionalState.CONFUSED,
    domain_context="education",
    cultural_context="usa",
    sensitivity_level="medium"
)

situation = {
    "text": "I'm confused, I don't understand this concept",
    "context": "mathematics lesson",
    "confusion_point": "algebraic equations",
    "clarification_point": "step-by-step explanation"
}

response = await engine.generate_universal_empathy(context, situation)

print(response.message)
# Adaptado para cultura americana com tom clarificante

print(response.cultural_adaptations)
# {"communication_style": "direct_and_efficient", ...}
```

### Exemplo 3: Suporte em Healthcare

```python
# Paciente preocupado
context = EmpathyContext(
    user_state=EmotionalState.CONCERNED,
    domain_context="healthcare",
    cultural_context="brazil",
    sensitivity_level="high"  # Alta sensibilidade em saúde
)

situation = {
    "text": "preocupado com os resultados do exame",
    "situation": "exame médico",
    "challenging_aspect": "incerteza sobre diagnóstico",
    "stress_source": "espera de resultados"
}

response = await engine.generate_universal_empathy(context, situation)

# Tipo de empatia será COMPASSIONATE (alta sensibilidade)
assert response.empathy_type == EmpathyType.COMPASSIONATE

# Mensagem incluirá adaptações culturais brasileiras
assert "Olá" in response.message or "Oi" in response.message
```

---

## Integração com SEVE Framework

O `UniversalEmpathyEngine` pode ser usado standalone ou integrado ao pipeline do SEVE.

### Uso Standalone

```python
engine = UniversalEmpathyEngine()
response = await engine.generate_universal_empathy(context, situation)
```

### Integração no Pipeline (Futuro)

```python
# No processamento do SEVEHybridFramework
# (integração será adicionada em versão futura)
```

---

## Configuração de Templates

Os templates podem ser personalizados estendendo a classe:

```python
class CustomEmpathyEngine(UniversalEmpathyEngine):
    def _load_empathy_templates(self):
        templates = super()._load_empathy_templates()
        # Personalizar templates
        templates["acknowledgment"]["positive"] = "Custom positive message: {context}"
        return templates
```

---

## Métricas e Histórico

### Exportar Histórico

```python
# Gerar algumas respostas
# ...

# Exportar histórico em JSON
history = engine.export_history()
print(history)
```

### Acessar Histórico Diretamente

```python
# Histórico completo
history = engine.response_history

# Última resposta
last_response = engine.response_history[-1] if engine.response_history else None
```

---

## Notas de Performance

- **Geração de resposta**: ~5-10ms por resposta
- **Detecção emocional**: ~2-3ms
- **Adaptação cultural**: ~1-2ms
- **Memória**: ~2-3 MB para templates e padrões

---

## Referências

- [Guia do Motor de Empatia](../universal/EMPATHY_ENGINE_GUIDE.md)
- [Documentação de Adaptadores](./DomainAdapters.md)
- [ADR-003: Não Usar Reconhecimento Facial](../adr/ADR-003-no-facial-recognition.md)

