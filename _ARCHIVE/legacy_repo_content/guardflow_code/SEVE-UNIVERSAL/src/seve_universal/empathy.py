"""
SEVE Universal Empathy - Motor de Empatia Universal

Componente responsável por gerar respostas empáticas contextualizadas
em todos os domínios de aplicação.
"""

from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
import logging
from abc import ABC, abstractmethod
import json

logger = logging.getLogger(__name__)


class EmpathyType(Enum):
    """Tipos de empatia"""
    COGNITIVE = "cognitive"        # Compreensão intelectual
    EMOTIONAL = "emotional"        # Compartilhamento emocional
    COMPASSIONATE = "compassionate" # Preocupação e cuidado
    CULTURAL = "cultural"          # Sensibilidade cultural
    CONTEXTUAL = "contextual"      # Adaptação ao contexto


class EmotionalState(Enum):
    """Estados emocionais"""
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
    """Contexto para geração de empatia"""
    user_state: EmotionalState
    domain_context: str
    cultural_context: str
    urgency_level: str = "normal"
    communication_style: str = "professional"
    sensitivity_level: str = "medium"
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class EmpathyResponse:
    """Resposta empática"""
    empathy_type: EmpathyType
    emotional_tone: str
    message: str
    supportive_actions: List[str] = field(default_factory=list)
    cultural_adaptations: Dict[str, Any] = field(default_factory=dict)
    confidence_score: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)


class DomainEmpathyEngine(ABC):
    """Motor de empatia específico por domínio"""
    
    @abstractmethod
    def generate_domain_empathy(
        self, 
        context: EmpathyContext, 
        situation: Dict[str, Any]
    ) -> EmpathyResponse:
        """Gera resposta empática específica do domínio"""
        pass
    
    @abstractmethod
    def detect_emotional_cues(
        self, 
        data: Any
    ) -> List[EmotionalState]:
        """Detecta pistas emocionais nos dados"""
        pass
    
    @abstractmethod
    def adapt_to_domain_culture(
        self, 
        response: EmpathyResponse, 
        cultural_context: str
    ) -> EmpathyResponse:
        """Adapta resposta à cultura do domínio"""
        pass


class UniversalEmpathyEngine:
    """
    Motor de empatia universal do SEVE
    
    Gera respostas empáticas contextualizadas para qualquer domínio,
    adaptando-se a diferentes culturas e contextos emocionais.
    """
    
    def __init__(self):
        self.domain_engines: Dict[str, DomainEmpathyEngine] = {}
        self.empathy_templates = self._load_empathy_templates()
        self.cultural_patterns = self._load_cultural_patterns()
        self.response_history: List[EmpathyResponse] = []
        self._initialize_domain_engines()
    
    def _load_empathy_templates(self) -> Dict[str, Dict[str, Any]]:
        """Carrega templates de empatia"""
        return {
            "acknowledgment": {
                "positive": "Entendo sua satisfação com {context}. É ótimo ver que {positive_aspect}.",
                "negative": "Reconheço que {situation} pode ser {challenging_aspect}. Sua preocupação é compreensível.",
                "neutral": "Agradeço por compartilhar {context} comigo. Vou analisar {situation} cuidadosamente.",
                "stressed": "Vejo que você está enfrentando {stress_source}. Isso pode ser realmente {challenging_aspect}.",
                "confused": "Entendo que {situation} pode parecer confuso. Vamos esclarecer {confusion_point} juntos."
            },
            "support": {
                "positive": "Estou aqui para continuar apoiando {positive_journey}.",
                "negative": "Estou aqui para ajudar você a {solution_approach}.",
                "neutral": "Estou disponível para {support_type} conforme necessário.",
                "stressed": "Vamos trabalhar juntos para {stress_relief}.",
                "confused": "Vou explicar {clarification_point} de forma mais clara."
            },
            "action": {
                "positive": ["Celebrar o sucesso", "Manter o momentum", "Compartilhar aprendizados"],
                "negative": ["Identificar soluções", "Buscar alternativas", "Oferecer suporte"],
                "neutral": ["Monitorar progresso", "Coletar feedback", "Ajustar abordagem"],
                "stressed": ["Reduzir pressão", "Priorizar tarefas", "Oferecer recursos"],
                "confused": ["Simplificar explicações", "Fornecer exemplos", "Clarificar dúvidas"]
            }
        }
    
    def _load_cultural_patterns(self) -> Dict[str, Dict[str, Any]]:
        """Carrega padrões culturais"""
        return {
            "brazil": {
                "communication_style": "warm_and_personal",
                "formality_level": "medium",
                "emotional_expression": "open",
                "greeting_patterns": ["Olá", "Oi", "Bom dia/tarde/noite"],
                "support_patterns": ["Estou aqui para ajudar", "Vamos resolver isso juntos"],
                "cultural_sensitivity": ["family_importance", "personal_relationships", "optimism"]
            },
            "usa": {
                "communication_style": "direct_and_efficient",
                "formality_level": "low",
                "emotional_expression": "moderate",
                "greeting_patterns": ["Hello", "Hi", "Good morning/afternoon/evening"],
                "support_patterns": ["I'm here to help", "Let's work through this"],
                "cultural_sensitivity": ["individual_achievement", "time_efficiency", "problem_solving"]
            },
            "japan": {
                "communication_style": "polite_and_respectful",
                "formality_level": "high",
                "emotional_expression": "subtle",
                "greeting_patterns": ["Konnichiwa", "Ohayou gozaimasu", "Konbanwa"],
                "support_patterns": ["O-tetsudai shimasu", "Issho ni ganbarimashou"],
                "cultural_sensitivity": ["harmony", "respect", "group_cooperation"]
            },
            "global": {
                "communication_style": "professional_and_inclusive",
                "formality_level": "medium",
                "emotional_expression": "balanced",
                "greeting_patterns": ["Hello", "Greetings", "Good day"],
                "support_patterns": ["I'm here to assist", "Let's work together"],
                "cultural_sensitivity": ["inclusivity", "respect", "understanding"]
            }
        }
    
    def _initialize_domain_engines(self) -> None:
        """Inicializa motores de empatia por domínio"""
        # Placeholder para inicialização de motores específicos
        pass
    
    def register_domain_engine(
        self, 
        domain: str, 
        engine: DomainEmpathyEngine
    ) -> None:
        """Registra motor de empatia para domínio"""
        self.domain_engines[domain] = engine
        logger.info(f"Motor de empatia registrado para domínio: {domain}")
    
    async def generate_universal_empathy(
        self,
        context: EmpathyContext,
        situation: Dict[str, Any],
        domain: Optional[str] = None
    ) -> EmpathyResponse:
        """
        Gera resposta empática universal
        
        Args:
            context: Contexto empático
            situation: Situação específica
            domain: Domínio específico (opcional)
            
        Returns:
            Resposta empática contextualizada
        """
        # Detectar pistas emocionais
        emotional_cues = await self._detect_emotional_cues(situation)
        
        # Determinar tipo de empatia apropriado
        empathy_type = self._determine_empathy_type(context, emotional_cues)
        
        # Gerar resposta base
        base_response = await self._generate_base_response(
            context, situation, empathy_type
        )
        
        # Adaptar para domínio específico
        if domain and domain in self.domain_engines:
            domain_response = self.domain_engines[domain].generate_domain_empathy(
                context, situation
            )
            base_response = self._merge_responses(base_response, domain_response)
        
        # Adaptar culturalmente
        cultural_response = await self._adapt_culturally(
            base_response, context.cultural_context
        )
        
        # Calcular score de confiança
        confidence_score = self._calculate_confidence_score(
            cultural_response, context, situation
        )
        
        cultural_response.confidence_score = confidence_score
        
        # Armazenar histórico
        self.response_history.append(cultural_response)
        
        return cultural_response
    
    async def _detect_emotional_cues(self, situation: Dict[str, Any]) -> List[EmotionalState]:
        """Detecta pistas emocionais na situação"""
        cues = []
        
        # Análise de texto
        if "text" in situation:
            text = situation["text"].lower()
            if any(word in text for word in ["feliz", "satisfeito", "ótimo", "excelente"]):
                cues.append(EmotionalState.POSITIVE)
            elif any(word in text for word in ["preocupado", "triste", "frustrado", "difícil"]):
                cues.append(EmotionalState.NEGATIVE)
            elif any(word in text for word in ["estressado", "pressão", "urgente", "correndo"]):
                cues.append(EmotionalState.STRESSED)
            elif any(word in text for word in ["confuso", "não entendo", "claro", "explicar"]):
                cues.append(EmotionalState.CONFUSED)
        
        # Análise de métricas
        if "metrics" in situation:
            metrics = situation["metrics"]
            if metrics.get("satisfaction_score", 0) > 0.8:
                cues.append(EmotionalState.POSITIVE)
            elif metrics.get("error_rate", 0) > 0.1:
                cues.append(EmotionalState.CONCERNED)
        
        # Análise de contexto
        if "urgency" in situation:
            if situation["urgency"] == "high":
                cues.append(EmotionalState.STRESSED)
        
        return cues if cues else [EmotionalState.NEUTRAL]
    
    def _determine_empathy_type(
        self, 
        context: EmpathyContext, 
        emotional_cues: List[EmotionalState]
    ) -> EmpathyType:
        """Determina tipo de empatia apropriado"""
        if context.sensitivity_level == "high":
            return EmpathyType.COMPASSIONATE
        elif context.cultural_context != "global":
            return EmpathyType.CULTURAL
        elif emotional_cues:
            return EmpathyType.EMOTIONAL
        else:
            return EmpathyType.CONTEXTUAL
    
    async def _generate_base_response(
        self,
        context: EmpathyContext,
        situation: Dict[str, Any],
        empathy_type: EmpathyType
    ) -> EmpathyResponse:
        """Gera resposta base empática"""
        
        # Determinar tom emocional
        emotional_tone = self._determine_emotional_tone(context.user_state)
        
        # Gerar mensagem
        message = await self._generate_message(
            context, situation, emotional_tone, empathy_type
        )
        
        # Gerar ações de suporte
        supportive_actions = await self._generate_supportive_actions(
            context, situation, emotional_tone
        )
        
        return EmpathyResponse(
            empathy_type=empathy_type,
            emotional_tone=emotional_tone,
            message=message,
            supportive_actions=supportive_actions,
            metadata={
                "generated_at": situation.get("timestamp"),
                "context_analyzed": True
            }
        )
    
    def _determine_emotional_tone(self, user_state: EmotionalState) -> str:
        """Determina tom emocional apropriado"""
        tone_mapping = {
            EmotionalState.POSITIVE: "encouraging",
            EmotionalState.NEGATIVE: "supportive",
            EmotionalState.NEUTRAL: "professional",
            EmotionalState.STRESSED: "calming",
            EmotionalState.EXCITED: "enthusiastic",
            EmotionalState.CONCERNED: "reassuring",
            EmotionalState.CONFUSED: "clarifying",
            EmotionalState.SATISFIED: "appreciative"
        }
        return tone_mapping.get(user_state, "professional")
    
    async def _generate_message(
        self,
        context: EmpathyContext,
        situation: Dict[str, Any],
        emotional_tone: str,
        empathy_type: EmpathyType
    ) -> str:
        """Gera mensagem empática"""
        
        # Obter template apropriado
        template_key = self._get_template_key(emotional_tone)
        template = self.empathy_templates["acknowledgment"].get(template_key, "")
        
        # Substituir placeholders
        message = template.format(
            context=situation.get("context", "a situação"),
            situation=situation.get("situation", "isso"),
            positive_aspect=situation.get("positive_aspect", "as coisas estão funcionando bem"),
            challenging_aspect=situation.get("challenging_aspect", "desafiador"),
            stress_source=situation.get("stress_source", "pressões"),
            confusion_point=situation.get("confusion_point", "os pontos confusos")
        )
        
        # Adicionar suporte
        support_template = self.empathy_templates["support"].get(template_key, "")
        if support_template:
            support_message = support_template.format(
                positive_journey=situation.get("positive_journey", "seu progresso"),
                solution_approach=situation.get("solution_approach", "resolver isso"),
                support_type=situation.get("support_type", "ajudar"),
                stress_relief=situation.get("stress_relief", "reduzir o estresse"),
                clarification_point=situation.get("clarification_point", "os pontos importantes")
            )
            message += f" {support_message}"
        
        return message
    
    def _get_template_key(self, emotional_tone: str) -> str:
        """Mapeia tom emocional para chave de template"""
        mapping = {
            "encouraging": "positive",
            "supportive": "negative",
            "professional": "neutral",
            "calming": "stressed",
            "enthusiastic": "positive",
            "reassuring": "negative",
            "clarifying": "confused",
            "appreciative": "positive"
        }
        return mapping.get(emotional_tone, "neutral")
    
    async def _generate_supportive_actions(
        self,
        context: EmpathyContext,
        situation: Dict[str, Any],
        emotional_tone: str
    ) -> List[str]:
        """Gera ações de suporte"""
        template_key = self._get_template_key(emotional_tone)
        actions = self.empathy_templates["action"].get(template_key, [])
        
        # Adaptar ações ao contexto
        adapted_actions = []
        for action in actions:
            if context.domain_context == "healthcare":
                adapted_actions.append(f"[Saúde] {action}")
            elif context.domain_context == "education":
                adapted_actions.append(f"[Educação] {action}")
            elif context.domain_context == "business":
                adapted_actions.append(f"[Negócios] {action}")
            else:
                adapted_actions.append(action)
        
        return adapted_actions
    
    def _merge_responses(
        self, 
        base_response: EmpathyResponse, 
        domain_response: EmpathyResponse
    ) -> EmpathyResponse:
        """Mescla respostas base e específicas do domínio"""
        # Combinar mensagens
        combined_message = f"{base_response.message} {domain_response.message}"
        
        # Combinar ações de suporte
        combined_actions = base_response.supportive_actions + domain_response.supportive_actions
        
        # Usar adaptações culturais do domínio se disponíveis
        cultural_adaptations = domain_response.cultural_adaptations or base_response.cultural_adaptations
        
        return EmpathyResponse(
            empathy_type=domain_response.empathy_type,
            emotional_tone=base_response.emotional_tone,
            message=combined_message,
            supportive_actions=combined_actions,
            cultural_adaptations=cultural_adaptations,
            metadata={
                **base_response.metadata,
                **domain_response.metadata,
                "merged": True
            }
        )
    
    async def _adapt_culturally(
        self, 
        response: EmpathyResponse, 
        cultural_context: str
    ) -> EmpathyResponse:
        """Adapta resposta culturalmente"""
        cultural_pattern = self.cultural_patterns.get(cultural_context, self.cultural_patterns["global"])
        
        # Adaptar estilo de comunicação
        if cultural_pattern["communication_style"] == "warm_and_personal":
            response.message = self._add_warmth(response.message)
        elif cultural_pattern["communication_style"] == "direct_and_efficient":
            response.message = self._make_direct(response.message)
        elif cultural_pattern["communication_style"] == "polite_and_respectful":
            response.message = self._add_politeness(response.message)
        
        # Adicionar adaptações culturais
        response.cultural_adaptations = {
            "communication_style": cultural_pattern["communication_style"],
            "formality_level": cultural_pattern["formality_level"],
            "cultural_sensitivity": cultural_pattern["cultural_sensitivity"]
        }
        
        return response
    
    def _add_warmth(self, message: str) -> str:
        """Adiciona calor à mensagem"""
        warm_prefixes = ["Querido(a)", "Caro(a)", "Amigo(a)"]
        return f"{warm_prefixes[0]}, {message.lower()}"
    
    def _make_direct(self, message: str) -> str:
        """Torna mensagem mais direta"""
        return message.replace("pode ser", "é").replace("parece", "é")
    
    def _add_politeness(self, message: str) -> str:
        """Adiciona polidez à mensagem"""
        return f"Com todo o respeito, {message.lower()}"
    
    def _calculate_confidence_score(
        self,
        response: EmpathyResponse,
        context: EmpathyContext,
        situation: Dict[str, Any]
    ) -> float:
        """Calcula score de confiança da resposta"""
        score = 0.5  # Score base
        
        # Ajustar baseado no contexto
        if context.sensitivity_level == "high":
            score += 0.2
        if context.cultural_context in self.cultural_patterns:
            score += 0.1
        if response.supportive_actions:
            score += 0.1
        if response.cultural_adaptations:
            score += 0.1
        
        return min(1.0, score)
    
    def get_empathy_metrics(self) -> Dict[str, Any]:
        """Retorna métricas de empatia"""
        if not self.response_history:
            return {"no_data": True}
        
        recent_responses = self.response_history[-50:]  # Últimas 50
        
        return {
            "total_responses": len(self.response_history),
            "recent_responses": len(recent_responses),
            "average_confidence": sum(r.confidence_score for r in recent_responses) / len(recent_responses),
            "empathy_types_used": list(set(r.empathy_type.value for r in recent_responses)),
            "domains_covered": len(self.domain_engines),
            "cultural_contexts": list(set(r.cultural_adaptations.get("communication_style", "unknown") for r in recent_responses))
        }
