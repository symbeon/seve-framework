"""Tests for Universal Empathy Engine."""

import pytest

try:
    from seve_framework.universal.empathy import (
        UniversalEmpathyEngine,
        EmpathyContext,
        EmpathyResponse,
        EmpathyType,
        EmotionalState,
    )
except ImportError:
    import sys
    from pathlib import Path
    src_path = Path(__file__).parent.parent / "src"
    sys.path.insert(0, str(src_path))
    from seve_framework.universal.empathy import (
        UniversalEmpathyEngine,
        EmpathyContext,
        EmpathyResponse,
        EmpathyType,
        EmotionalState,
    )


class TestEmpathyContext:
    """Tests for EmpathyContext."""

    def test_empathy_context_creation(self):
        """Test creating an EmpathyContext."""
        context = EmpathyContext(
            user_state=EmotionalState.POSITIVE,
            domain_context="healthcare",
            cultural_context="brazil"
        )
        
        assert context.user_state == EmotionalState.POSITIVE
        assert context.domain_context == "healthcare"
        assert context.cultural_context == "brazil"
        assert context.urgency_level == "normal"
        assert context.communication_style == "professional"

    def test_empathy_context_custom(self):
        """Test creating EmpathyContext with custom values."""
        context = EmpathyContext(
            user_state=EmotionalState.STRESSED,
            domain_context="education",
            cultural_context="usa",
            urgency_level="high",
            sensitivity_level="high"
        )
        
        assert context.urgency_level == "high"
        assert context.sensitivity_level == "high"


class TestUniversalEmpathyEngine:
    """Tests for UniversalEmpathyEngine."""

    def test_engine_initialization(self):
        """Test engine initialization."""
        engine = UniversalEmpathyEngine()
        
        assert engine.domain_engines == {}
        assert len(engine.empathy_templates) > 0
        assert len(engine.cultural_patterns) > 0
        assert engine.response_history == []

    def test_templates_loaded(self):
        """Test that templates are loaded."""
        engine = UniversalEmpathyEngine()
        
        assert "acknowledgment" in engine.empathy_templates
        assert "support" in engine.empathy_templates
        assert "action" in engine.empathy_templates
        
        # Check that templates have expected emotional states
        assert "positive" in engine.empathy_templates["acknowledgment"]
        assert "negative" in engine.empathy_templates["acknowledgment"]

    def test_cultural_patterns_loaded(self):
        """Test that cultural patterns are loaded."""
        engine = UniversalEmpathyEngine()
        
        assert "brazil" in engine.cultural_patterns
        assert "usa" in engine.cultural_patterns
        assert "japan" in engine.cultural_patterns
        assert "global" in engine.cultural_patterns
        
        # Check structure
        brazil_pattern = engine.cultural_patterns["brazil"]
        assert "communication_style" in brazil_pattern
        assert "greeting_patterns" in brazil_pattern

    @pytest.mark.asyncio
    async def test_generate_universal_empathy_positive(self):
        """Test generating empathy for positive state."""
        engine = UniversalEmpathyEngine()
        context = EmpathyContext(
            user_state=EmotionalState.POSITIVE,
            domain_context="business",
            cultural_context="global"
        )
        situation = {
            "text": "feliz com os resultados",
            "context": "projeto",
            "positive_aspect": "tudo funcionando bem"
        }
        
        response = await engine.generate_universal_empathy(context, situation)
        
        assert isinstance(response, EmpathyResponse)
        assert response.empathy_type in [EmpathyType.EMOTIONAL, EmpathyType.CONTEXTUAL]
        assert len(response.message) > 0
        assert response.confidence_score > 0.0
        assert len(response.supportive_actions) > 0

    @pytest.mark.asyncio
    async def test_generate_universal_empathy_stressed(self):
        """Test generating empathy for stressed state."""
        engine = UniversalEmpathyEngine()
        context = EmpathyContext(
            user_state=EmotionalState.STRESSED,
            domain_context="education",
            cultural_context="brazil",
            sensitivity_level="high"
        )
        situation = {
            "text": "estressado com a pressão",
            "situation": "deadline",
            "stress_source": "múltiplas tarefas"
        }
        
        response = await engine.generate_universal_empathy(context, situation)
        
        assert isinstance(response, EmpathyResponse)
        assert response.empathy_type == EmpathyType.COMPASSIONATE  # High sensitivity
        assert "estressado" in response.message.lower() or "pressão" in response.message.lower()
        assert len(response.supportive_actions) > 0

    @pytest.mark.asyncio
    async def test_generate_universal_empathy_cultural_adaptation(self):
        """Test cultural adaptation of empathy."""
        engine = UniversalEmpathyEngine()
        context = EmpathyContext(
            user_state=EmotionalState.NEUTRAL,
            domain_context="healthcare",
            cultural_context="brazil"
        )
        situation = {
            "text": "preciso de ajuda",
            "context": "consulta médica"
        }
        
        response = await engine.generate_universal_empathy(context, situation)
        
        assert isinstance(response, EmpathyResponse)
        assert len(response.cultural_adaptations) > 0
        # Brazilian greeting should be in message
        brazil_greetings = ["olá", "oi", "bom dia", "bom tarde", "bom noite"]
        message_lower = response.message.lower()
        assert any(greeting in message_lower for greeting in brazil_greetings)

    @pytest.mark.asyncio
    async def test_detect_emotional_cues_from_text(self):
        """Test detecting emotional cues from text."""
        engine = UniversalEmpathyEngine()
        
        # Positive cues
        situation_positive = {"text": "feliz com os resultados excelentes"}
        cues = await engine._detect_emotional_cues(situation_positive)
        assert EmotionalState.POSITIVE in cues
        
        # Negative cues
        situation_negative = {"text": "preocupado e triste com a situação difícil"}
        cues = await engine._detect_emotional_cues(situation_negative)
        assert EmotionalState.NEGATIVE in cues
        
        # Stressed cues
        situation_stressed = {"text": "estressado com pressão urgente"}
        cues = await engine._detect_emotional_cues(situation_stressed)
        assert EmotionalState.STRESSED in cues
        
        # Confused cues
        situation_confused = {"text": "confuso, não entendo, preciso que explique"}
        cues = await engine._detect_emotional_cues(situation_confused)
        assert EmotionalState.CONFUSED in cues

    @pytest.mark.asyncio
    async def test_detect_emotional_cues_from_metrics(self):
        """Test detecting emotional cues from metrics."""
        engine = UniversalEmpathyEngine()
        
        # High satisfaction
        situation = {
            "metrics": {"satisfaction_score": 0.9}
        }
        cues = await engine._detect_emotional_cues(situation)
        assert EmotionalState.POSITIVE in cues
        
        # High error rate
        situation = {
            "metrics": {"error_rate": 0.15}
        }
        cues = await engine._detect_emotional_cues(situation)
        assert EmotionalState.CONCERNED in cues

    def test_determine_empathy_type(self):
        """Test determining empathy type."""
        engine = UniversalEmpathyEngine()
        
        # High sensitivity -> Compassionate
        context = EmpathyContext(
            user_state=EmotionalState.POSITIVE,
            domain_context="healthcare",
            cultural_context="global",
            sensitivity_level="high"
        )
        empathy_type = engine._determine_empathy_type(context, [])
        assert empathy_type == EmpathyType.COMPASSIONATE
        
        # Cultural context -> Cultural
        context = EmpathyContext(
            user_state=EmotionalState.NEUTRAL,
            domain_context="business",
            cultural_context="japan"
        )
        empathy_type = engine._determine_empathy_type(context, [])
        assert empathy_type == EmpathyType.CULTURAL
        
        # With emotional cues -> Emotional
        context = EmpathyContext(
            user_state=EmotionalState.POSITIVE,
            domain_context="retail",
            cultural_context="global"
        )
        empathy_type = engine._determine_empathy_type(context, [EmotionalState.POSITIVE])
        assert empathy_type == EmpathyType.EMOTIONAL

    def test_determine_emotional_tone(self):
        """Test determining emotional tone."""
        engine = UniversalEmpathyEngine()
        
        tone = engine._determine_emotional_tone(EmotionalState.POSITIVE)
        assert tone == "encouraging"
        
        tone = engine._determine_emotional_tone(EmotionalState.STRESSED)
        assert tone == "calming"
        
        tone = engine._determine_emotional_tone(EmotionalState.CONFUSED)
        assert tone == "clarifying"

    def test_export_history(self):
        """Test exporting response history."""
        engine = UniversalEmpathyEngine()
        
        # Generate some responses
        context = EmpathyContext(
            user_state=EmotionalState.POSITIVE,
            domain_context="test",
            cultural_context="global"
        )
        
        # Add mock response
        from seve_framework.universal.empathy import EmpathyResponse
        mock_response = EmpathyResponse(
            empathy_type=EmpathyType.EMOTIONAL,
            emotional_tone="encouraging",
            message="Test message",
            supportive_actions=["action1"],
            confidence_score=0.85
        )
        engine.response_history.append(mock_response)
        
        exported = engine.export_history()
        assert isinstance(exported, str)
        assert "Test message" in exported
        assert "action1" in exported


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

