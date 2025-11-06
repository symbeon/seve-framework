"""Universal empathy engine migrated from the legacy implementation."""

from __future__ import annotations

import json
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class EmpathyType(Enum):
    COGNITIVE = "cognitive"
    EMOTIONAL = "emotional"
    COMPASSIONATE = "compassionate"
    CULTURAL = "cultural"
    CONTEXTUAL = "contextual"


class EmotionalState(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    STRESSED = "stressed"
    EXCITED = "excited"
    CONCERNED = "concerned"
    CONFUSED = "confused"
    SATISFIED = "satisfied"


@dataclass
class EmpathyContext:
    user_state: EmotionalState
    domain_context: str
    cultural_context: str
    urgency_level: str = "normal"
    communication_style: str = "professional"
    sensitivity_level: str = "medium"
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class EmpathyResponse:
    empathy_type: EmpathyType
    emotional_tone: str
    message: str
    supportive_actions: List[str] = field(default_factory=list)
    cultural_adaptations: Dict[str, Any] = field(default_factory=dict)
    confidence_score: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)


class DomainEmpathyEngine(ABC):
    @abstractmethod
    def generate_domain_empathy(
        self,
        context: EmpathyContext,
        situation: Dict[str, Any],
    ) -> EmpathyResponse:
        """Generate empathy specific to a domain."""

    @abstractmethod
    def detect_emotional_cues(self, data: Any) -> List[EmotionalState]:
        """Detect emotional cues."""

    @abstractmethod
    def adapt_to_domain_culture(
        self,
        response: EmpathyResponse,
        cultural_context: str,
    ) -> EmpathyResponse:
        """Apply domain specific cultural adaptations."""


class UniversalEmpathyEngine:
    """Generates contextualised empathy responses for any domain."""

    def __init__(self) -> None:
        self.domain_engines: Dict[str, DomainEmpathyEngine] = {}
        self.empathy_templates = self._load_empathy_templates()
        self.cultural_patterns = self._load_cultural_patterns()
        self.response_history: List[EmpathyResponse] = []
        self._initialize_domain_engines()

    def _load_empathy_templates(self) -> Dict[str, Dict[str, Any]]:
        return {
            "acknowledgment": {
                "positive": "Entendo sua satisfação com {context}. É ótimo ver que {positive_aspect}.",
                "negative": "Reconheço que {situation} pode ser {challenging_aspect}. Sua preocupação é compreensível.",
                "neutral": "Agradeço por compartilhar {context} comigo. Vou analisar {situation} cuidadosamente.",
                "stressed": "Vejo que você está enfrentando {stress_source}. Isso pode ser realmente {challenging_aspect}.",
                "confused": "Entendo que {situation} pode parecer confuso. Vamos esclarecer {confusion_point} juntos.",
            },
            "support": {
                "positive": "Estou aqui para continuar apoiando {positive_journey}.",
                "negative": "Estou aqui para ajudar você a {solution_approach}.",
                "neutral": "Estou disponível para {support_type} conforme necessário.",
                "stressed": "Vamos trabalhar juntos para {stress_relief}.",
                "confused": "Vou explicar {clarification_point} de forma mais clara.",
            },
            "action": {
                "positive": [
                    "Celebrar o sucesso",
                    "Manter o momentum",
                    "Compartilhar aprendizados",
                ],
                "negative": [
                    "Identificar soluções",
                    "Buscar alternativas",
                    "Oferecer suporte",
                ],
                "neutral": [
                    "Monitorar progresso",
                    "Coletar feedback",
                    "Ajustar abordagem",
                ],
                "stressed": [
                    "Reduzir pressão",
                    "Priorizar tarefas",
                    "Oferecer recursos",
                ],
                "confused": [
                    "Simplificar explicações",
                    "Fornecer exemplos",
                    "Clarificar dúvidas",
                ],
            },
        }

    def _load_cultural_patterns(self) -> Dict[str, Dict[str, Any]]:
        return {
            "brazil": {
                "communication_style": "warm_and_personal",
                "formality_level": "medium",
                "emotional_expression": "open",
                "greeting_patterns": ["Olá", "Oi", "Bom dia/tarde/noite"],
                "support_patterns": [
                    "Estou aqui para ajudar",
                    "Vamos resolver isso juntos",
                ],
                "cultural_sensitivity": [
                    "family_importance",
                    "personal_relationships",
                    "optimism",
                ],
            },
            "usa": {
                "communication_style": "direct_and_efficient",
                "formality_level": "low",
                "emotional_expression": "moderate",
                "greeting_patterns": ["Hello", "Hi", "Good morning/afternoon/evening"],
                "support_patterns": ["I'm here to help", "Let's work through this"],
                "cultural_sensitivity": [
                    "individual_achievement",
                    "time_efficiency",
                    "problem_solving",
                ],
            },
            "japan": {
                "communication_style": "polite_and_respectful",
                "formality_level": "high",
                "emotional_expression": "subtle",
                "greeting_patterns": ["Konnichiwa", "Ohayou gozaimasu", "Konbanwa"],
                "support_patterns": ["O-tetsudai shimasu", "Issho ni ganbarimashou"],
                "cultural_sensitivity": ["harmony", "respect", "group_cooperation"],
            },
            "global": {
                "communication_style": "professional_and_inclusive",
                "formality_level": "medium",
                "emotional_expression": "balanced",
                "greeting_patterns": ["Hello", "Greetings", "Good day"],
                "support_patterns": ["I'm here to assist", "Let's work together"],
                "cultural_sensitivity": ["inclusivity", "respect", "understanding"],
            },
        }

    def _initialize_domain_engines(self) -> None:
        # Placeholder for future, we only ship the universal engine for now.
        if not self.domain_engines:
            logger.debug("Motores de empatia de domínio não definidos, usando universal.")

    def register_domain_engine(self, domain: str, engine: DomainEmpathyEngine) -> None:
        self.domain_engines[domain] = engine
        logger.info("Motor de empatia registrado para domínio: %s", domain)

    async def generate_universal_empathy(
        self,
        context: EmpathyContext,
        situation: Dict[str, Any],
        domain: Optional[str] = None,
    ) -> EmpathyResponse:
        emotional_cues = await self._detect_emotional_cues(situation)
        empathy_type = self._determine_empathy_type(context, emotional_cues)
        base_response = await self._generate_base_response(context, situation, empathy_type)

        if domain and domain in self.domain_engines:
            domain_response = self.domain_engines[domain].generate_domain_empathy(
                context, situation
            )
            base_response = self._merge_responses(base_response, domain_response)

        cultural_response = await self._adapt_culturally(
            base_response, context.cultural_context
        )
        cultural_response.confidence_score = self._calculate_confidence_score(
            cultural_response, context, situation
        )
        self.response_history.append(cultural_response)
        return cultural_response

    async def _detect_emotional_cues(self, situation: Dict[str, Any]) -> List[EmotionalState]:
        cues: List[EmotionalState] = []
        text = situation.get("text", "").lower()
        if any(word in text for word in ["feliz", "satisfeito", "ótimo", "excelente"]):
            cues.append(EmotionalState.POSITIVE)
        if any(word in text for word in ["preocupado", "triste", "frustrado", "difícil"]):
            cues.append(EmotionalState.NEGATIVE)
        if any(word in text for word in ["estressado", "pressão", "urgente", "correndo"]):
            cues.append(EmotionalState.STRESSED)
        if any(word in text for word in ["confuso", "não entendo", "claro", "explicar"]):
            cues.append(EmotionalState.CONFUSED)

        if "metrics" in situation:
            metrics = situation["metrics"]
            if metrics.get("satisfaction_score", 0) > 0.8:
                cues.append(EmotionalState.POSITIVE)
            if metrics.get("error_rate", 0) > 0.1:
                cues.append(EmotionalState.CONCERNED)

        if situation.get("urgency") == "high":
            cues.append(EmotionalState.STRESSED)

        return cues or [EmotionalState.NEUTRAL]

    def _determine_empathy_type(
        self,
        context: EmpathyContext,
        emotional_cues: List[EmotionalState],
    ) -> EmpathyType:
        if context.sensitivity_level == "high":
            return EmpathyType.COMPASSIONATE
        if context.cultural_context != "global":
            return EmpathyType.CULTURAL
        if emotional_cues:
            return EmpathyType.EMOTIONAL
        return EmpathyType.CONTEXTUAL

    async def _generate_base_response(
        self,
        context: EmpathyContext,
        situation: Dict[str, Any],
        empathy_type: EmpathyType,
    ) -> EmpathyResponse:
        emotional_tone = self._determine_emotional_tone(context.user_state)
        message = await self._generate_message(context, situation, emotional_tone)
        supportive_actions = await self._generate_supportive_actions(
            context, situation, emotional_tone
        )
        return EmpathyResponse(
            empathy_type=empathy_type,
            emotional_tone=emotional_tone,
            message=message,
            supportive_actions=supportive_actions,
            metadata={"context_analyzed": True},
        )

    def _determine_emotional_tone(self, user_state: EmotionalState) -> str:
        mapping = {
            EmotionalState.POSITIVE: "encouraging",
            EmotionalState.NEGATIVE: "supportive",
            EmotionalState.NEUTRAL: "professional",
            EmotionalState.STRESSED: "calming",
            EmotionalState.EXCITED: "enthusiastic",
            EmotionalState.CONCERNED: "reassuring",
            EmotionalState.CONFUSED: "clarifying",
            EmotionalState.SATISFIED: "appreciative",
        }
        return mapping.get(user_state, "professional")

    async def _generate_message(
        self,
        context: EmpathyContext,
        situation: Dict[str, Any],
        emotional_tone: str,
    ) -> str:
        template_key = self._get_template_key(emotional_tone)
        template = self.empathy_templates["acknowledgment"].get(template_key, "")
        message = template.format(
            context=situation.get("context", "a situação"),
            situation=situation.get("situation", "isso"),
            positive_aspect=situation.get(
                "positive_aspect", "as coisas estão funcionando bem"
            ),
            challenging_aspect=situation.get("challenging_aspect", "desafiador"),
            stress_source=situation.get("stress_source", "pressões"),
            confusion_point=situation.get("confusion_point", "os pontos confusos"),
        )
        support_template = self.empathy_templates["support"].get(template_key, "")
        if support_template:
            support_message = support_template.format(
                positive_journey=situation.get("positive_journey", "seu progresso"),
                solution_approach=situation.get("solution_approach", "resolver isso"),
                support_type=situation.get("support_type", "ajudar"),
                stress_relief=situation.get("stress_relief", "reduzir o estresse"),
                clarification_point=situation.get("clarification_point", "os pontos importantes"),
            )
            message = f"{message} {support_message}".strip()
        return message

    def _get_template_key(self, emotional_tone: str) -> str:
        mapping = {
            "encouraging": "positive",
            "supportive": "negative",
            "professional": "neutral",
            "calming": "stressed",
            "enthusiastic": "positive",
            "reassuring": "negative",
            "clarifying": "confused",
            "appreciative": "positive",
        }
        return mapping.get(emotional_tone, "neutral")

    async def _generate_supportive_actions(
        self,
        context: EmpathyContext,
        situation: Dict[str, Any],
        emotional_tone: str,
    ) -> List[str]:
        template_key = self._get_template_key(emotional_tone)
        actions = self.empathy_templates["action"].get(template_key, [])
        adapted_actions: List[str] = []
        for action in actions:
            domain = context.domain_context
            if domain == "healthcare":
                adapted_actions.append(f"[Saúde] {action}")
            elif domain == "education":
                adapted_actions.append(f"[Educação] {action}")
            elif domain == "business":
                adapted_actions.append(f"[Negócios] {action}")
            else:
                adapted_actions.append(action)
        return adapted_actions

    def _merge_responses(
        self, base: EmpathyResponse, domain_response: EmpathyResponse
    ) -> EmpathyResponse:
        merged_actions = list({*base.supportive_actions, *domain_response.supportive_actions})
        return EmpathyResponse(
            empathy_type=domain_response.empathy_type,
            emotional_tone=domain_response.emotional_tone or base.emotional_tone,
            message=f"{base.message} {domain_response.message}".strip(),
            supportive_actions=merged_actions,
            cultural_adaptations={**base.cultural_adaptations, **domain_response.cultural_adaptations},
            metadata={**base.metadata, **domain_response.metadata},
        )

    async def _adapt_culturally(
        self, response: EmpathyResponse, cultural_context: str
    ) -> EmpathyResponse:
        cultural_data = self.cultural_patterns.get(cultural_context.lower())
        if not cultural_data:
            return response
        response.cultural_adaptations.update(cultural_data)
        greeting = cultural_data.get("greeting_patterns", ["Olá"])[0]
        response.message = f"{greeting}! {response.message}".strip()
        return response

    def _calculate_confidence_score(
        self,
        response: EmpathyResponse,
        context: EmpathyContext,
        situation: Dict[str, Any],
    ) -> float:
        score = 0.7
        if response.cultural_adaptations:
            score += 0.1
        if context.sensitivity_level == "high":
            score += 0.1
        if situation.get("metrics", {}).get("satisfaction_score", 0) > 0.8:
            score += 0.05
        return min(score, 1.0)

    def export_history(self) -> str:
        serialised = [
            {
                "empathy_type": resp.empathy_type.value,
                "emotional_tone": resp.emotional_tone,
                "message": resp.message,
                "supportive_actions": resp.supportive_actions,
                "confidence_score": resp.confidence_score,
            }
            for resp in self.response_history
        ]
        return json.dumps(serialised, ensure_ascii=False, indent=2)

