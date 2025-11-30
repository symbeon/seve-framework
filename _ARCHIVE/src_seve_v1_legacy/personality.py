"""
SEVE-Personality: Personalização e Adaptação

Componente responsável por:
- Perfis de personalidade adaptativos
- Comportamento contextual
- Aprendizado de preferências
- Adaptação dinâmica
- Personalização de experiência
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum


class PersonalityType(Enum):
    """Tipos de personalidade"""
    ANALYTICAL = "analytical"
    EMPATHETIC = "empathetic"
    EFFICIENT = "efficient"
    SUPPORTIVE = "supportive"
    INNOVATIVE = "innovative"
    CONSERVATIVE = "conservative"


class AdaptationLevel(Enum):
    """Níveis de adaptação"""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    STATIC = "static"


@dataclass
class PersonalityProfile:
    """Perfil de personalidade"""
    personality_type: PersonalityType
    adaptation_level: AdaptationLevel
    preferences: Dict[str, Any]
    learning_rate: float
    confidence: float


@dataclass
class AdaptiveResponse:
    """Resposta adaptativa"""
    message: str
    tone: str
    personality_type: PersonalityType
    adaptation_applied: List[str]
    learning_data: Dict[str, Any]


class SEVEPersonality:
    """
    Sistema de personalização e adaptação
    
    Adapta o comportamento do sistema baseado no perfil
    do usuário e contexto da interação.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Inicializa o SEVE-Personality
        
        Args:
            config: Configurações de personalização
        """
        self.config = config or {}
        self.profile_manager = PersonalityProfileManager()
        self.adaptation_engine = AdaptationEngine()
        self.learning_system = PersonalityLearningSystem()
        self.preference_analyzer = PreferenceAnalyzer()
    
    def create_personality_profile(
        self,
        user_id: str,
        initial_data: Dict[str, Any]
    ) -> PersonalityProfile:
        """
        Cria perfil de personalidade para usuário
        
        Args:
            user_id: ID do usuário
            initial_data: Dados iniciais do usuário
            
        Returns:
            Perfil de personalidade criado
        """
        # Analisar preferências iniciais
        preferences = self.preference_analyzer.analyze_preferences(initial_data)
        
        # Determinar tipo de personalidade
        personality_type = self._determine_personality_type(preferences)
        
        # Criar perfil
        profile = PersonalityProfile(
            personality_type=personality_type,
            adaptation_level=AdaptationLevel.MEDIUM,
            preferences=preferences,
            learning_rate=0.1,
            confidence=0.7
        )
        
        # Salvar perfil
        self.profile_manager.save_profile(user_id, profile)
        
        return profile
    
    def adapt_response(
        self,
        user_id: str,
        base_response: str,
        context: Dict[str, Any]
    ) -> AdaptiveResponse:
        """
        Adapta resposta baseada no perfil do usuário
        
        Args:
            user_id: ID do usuário
            base_response: Resposta base
            context: Contexto da interação
            
        Returns:
            Resposta adaptada
        """
        # Recuperar perfil
        profile = self.profile_manager.get_profile(user_id)
        if not profile:
            profile = self.create_personality_profile(user_id, {})
        
        # Adaptar resposta
        adapted_response = self.adaptation_engine.adapt_response(
            base_response, profile, context
        )
        
        # Aplicar aprendizado
        learning_data = self.learning_system.update_profile(
            user_id, context, adapted_response
        )
        
        return AdaptiveResponse(
            message=adapted_response["message"],
            tone=adapted_response["tone"],
            personality_type=profile.personality_type,
            adaptation_applied=adapted_response["adaptations"],
            learning_data=learning_data
        )
    
    def _determine_personality_type(
        self,
        preferences: Dict[str, Any]
    ) -> PersonalityType:
        """Determina tipo de personalidade baseado em preferências"""
        # Placeholder para algoritmo de determinação
        if preferences.get("detailed_info", False):
            return PersonalityType.ANALYTICAL
        elif preferences.get("emotional_support", False):
            return PersonalityType.EMPATHETIC
        elif preferences.get("speed", False):
            return PersonalityType.EFFICIENT
        else:
            return PersonalityType.SUPPORTIVE
    
    def get_personality_metrics(self, user_id: str) -> Dict[str, Any]:
        """Retorna métricas de personalização"""
        profile = self.profile_manager.get_profile(user_id)
        if not profile:
            return {}
        
        return {
            "personality_type": profile.personality_type.value,
            "adaptation_level": profile.adaptation_level.value,
            "learning_rate": profile.learning_rate,
            "confidence": profile.confidence,
            "preferences_count": len(profile.preferences)
        }


class PersonalityProfileManager:
    """Gerenciador de perfis de personalidade"""
    
    def __init__(self):
        self.profiles: Dict[str, PersonalityProfile] = {}
    
    def save_profile(self, user_id: str, profile: PersonalityProfile) -> None:
        """Salva perfil de personalidade"""
        self.profiles[user_id] = profile
    
    def get_profile(self, user_id: str) -> Optional[PersonalityProfile]:
        """Recupera perfil de personalidade"""
        return self.profiles.get(user_id)
    
    def update_profile(self, user_id: str, updates: Dict[str, Any]) -> None:
        """Atualiza perfil de personalidade"""
        if user_id in self.profiles:
            profile = self.profiles[user_id]
            # Aplicar atualizações
            for key, value in updates.items():
                if hasattr(profile, key):
                    setattr(profile, key, value)


class AdaptationEngine:
    """Motor de adaptação"""
    
    def adapt_response(
        self,
        base_response: str,
        profile: PersonalityProfile,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Adapta resposta baseada no perfil"""
        
        if profile.personality_type == PersonalityType.ANALYTICAL:
            return {
                "message": f"[ANÁLISE] {base_response}",
                "tone": "analytical",
                "adaptations": ["detailed_info", "metrics"]
            }
        elif profile.personality_type == PersonalityType.EMPATHETIC:
            return {
                "message": f"💙 {base_response}",
                "tone": "empathetic",
                "adaptations": ["emotional_support", "encouragement"]
            }
        elif profile.personality_type == PersonalityType.EFFICIENT:
            return {
                "message": f"⚡ {base_response}",
                "tone": "efficient",
                "adaptations": ["quick_actions", "shortcuts"]
            }
        else:
            return {
                "message": base_response,
                "tone": "supportive",
                "adaptations": ["step_by_step"]
            }


class PersonalityLearningSystem:
    """Sistema de aprendizado de personalidade"""
    
    def update_profile(
        self,
        user_id: str,
        context: Dict[str, Any],
        response: AdaptiveResponse
    ) -> Dict[str, Any]:
        """Atualiza perfil baseado em interação"""
        # Placeholder para aprendizado real
        return {
            "interaction_count": 1,
            "preferences_learned": [],
            "adaptation_success": 0.8
        }


class PreferenceAnalyzer:
    """Analisador de preferências"""
    
    def analyze_preferences(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analisa preferências do usuário"""
        preferences = {}
        
        # Análise de comportamento
        if data.get("click_speed", 0) > 1.5:
            preferences["speed"] = True
        
        if data.get("error_count", 0) > 2:
            preferences["detailed_info"] = True
        
        if data.get("help_requests", 0) > 0:
            preferences["emotional_support"] = True
        
        return preferences
