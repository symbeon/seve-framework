"""
Testes de sanidade para SEVE Universal

Verifica se o framework universal pode se adaptar a diferentes domínios
mantendo suas capacidades universais.
"""

import pytest
import asyncio
from typing import Dict, Any

from seve_universal import (
    SEVEUniversalCore, DomainConfig, UniversalContext, DomainType, AdaptationLevel
)
from seve_universal.adapters import (
    UniversalAdapterRegistry, HealthcareAdapter, EducationAdapter, 
    BusinessAdapter, SmartCityAdapter, GamingAdapter
)


class TestSEVEUniversalCore:
    """Testes para o núcleo universal"""
    
    def test_core_initialization(self):
        """Testa inicialização do núcleo universal"""
        config = DomainConfig(
            domain_type=DomainType.HEALTHCARE,
            domain_name="Test Domain",
            cultural_context="global"
        )
        
        core = SEVEUniversalCore(config)
        assert core is not None
        assert core.config.domain_type == DomainType.HEALTHCARE
    
    def test_domain_config_creation(self):
        """Testa criação de configuração de domínio"""
        config = DomainConfig(
            domain_type=DomainType.EDUCATION,
            domain_name="Education AI",
            cultural_context="brazil",
            adaptation_level=AdaptationLevel.ADVANCED,
            ethical_rules=["student_privacy"],
            personalization_rules=["learning_style"],
            empathy_rules=["student_support"]
        )
        
        assert config.domain_type == DomainType.EDUCATION
        assert config.cultural_context == "brazil"
        assert config.adaptation_level == AdaptationLevel.ADVANCED
        assert "student_privacy" in config.ethical_rules
    
    def test_universal_context_creation(self):
        """Testa criação de contexto universal"""
        context = UniversalContext(
            domain=DomainType.BUSINESS,
            user_profile={"role": "manager", "department": "engineering"},
            environmental_data={"company": "TechCorp"},
            cultural_context="global",
            temporal_context={"time": "morning"},
            metadata={"test": True}
        )
        
        assert context.domain == DomainType.BUSINESS
        assert context.user_profile["role"] == "manager"
        assert context.cultural_context == "global"


class TestDomainAdapters:
    """Testes para adaptadores de domínio"""
    
    def test_healthcare_adapter(self):
        """Testa adaptador de saúde"""
        adapter = HealthcareAdapter()
        
        context = UniversalContext(
            domain=DomainType.HEALTHCARE,
            user_profile={"patient_id": "P001"},
            environmental_data={},
            cultural_context="global",
            temporal_context={},
            metadata={}
        )
        
        adapted_context = adapter.adapt_to_context(context)
        assert adapted_context.metadata["medical_privacy"] is True
        assert adapted_context.metadata["hipaa_compliance"] is True
    
    def test_education_adapter(self):
        """Testa adaptador educacional"""
        adapter = EducationAdapter()
        
        context = UniversalContext(
            domain=DomainType.EDUCATION,
            user_profile={"student_id": "S001"},
            environmental_data={},
            cultural_context="global",
            temporal_context={},
            metadata={}
        )
        
        adapted_context = adapter.adapt_to_context(context)
        assert adapted_context.metadata["learning_objectives"] is True
        assert adapted_context.metadata["student_privacy"] is True
    
    def test_business_adapter(self):
        """Testa adaptador empresarial"""
        adapter = BusinessAdapter()
        
        context = UniversalContext(
            domain=DomainType.BUSINESS,
            user_profile={"employee_id": "E001"},
            environmental_data={},
            cultural_context="global",
            temporal_context={},
            metadata={}
        )
        
        adapted_context = adapter.adapt_to_context(context)
        assert adapted_context.metadata["business_objectives"] is True
        assert adapted_context.metadata["corporate_compliance"] is True
    
    def test_smart_city_adapter(self):
        """Testa adaptador de cidade inteligente"""
        adapter = SmartCityAdapter()
        
        context = UniversalContext(
            domain=DomainType.SMART_CITY,
            user_profile={"citizen_id": "C001"},
            environmental_data={},
            cultural_context="global",
            temporal_context={},
            metadata={}
        )
        
        adapted_context = adapter.adapt_to_context(context)
        assert adapted_context.metadata["urban_planning"] is True
        assert adapted_context.metadata["citizen_privacy"] is True
    
    def test_gaming_adapter(self):
        """Testa adaptador de jogos"""
        adapter = GamingAdapter()
        
        context = UniversalContext(
            domain=DomainType.GAMING,
            user_profile={"player_id": "G001"},
            environmental_data={},
            cultural_context="global",
            temporal_context={},
            metadata={}
        )
        
        adapted_context = adapter.adapt_to_context(context)
        assert adapted_context.metadata["game_mechanics"] is True
        assert adapted_context.metadata["player_privacy"] is True


class TestUniversalAdapterRegistry:
    """Testes para registro de adaptadores"""
    
    def test_registry_initialization(self):
        """Testa inicialização do registro"""
        registry = UniversalAdapterRegistry()
        assert registry is not None
        assert len(registry.list_available_domains()) > 0
    
    def test_get_adapter(self):
        """Testa recuperação de adaptador"""
        registry = UniversalAdapterRegistry()
        
        healthcare_adapter = registry.get_adapter(DomainType.HEALTHCARE)
        assert healthcare_adapter is not None
        assert isinstance(healthcare_adapter, HealthcareAdapter)
        
        education_adapter = registry.get_adapter(DomainType.EDUCATION)
        assert education_adapter is not None
        assert isinstance(education_adapter, EducationAdapter)
    
    def test_custom_adapter_registration(self):
        """Testa registro de adaptador customizado"""
        registry = UniversalAdapterRegistry()
        
        from seve_universal.core import DomainAdapter
        
        class CustomAdapter(DomainAdapter):
            def adapt_to_context(self, context):
                return context
            
            def extract_domain_features(self, data):
                return {"custom": data}
            
            def apply_domain_rules(self, decision):
                return {"custom_decision": decision}
        
        registry.register_custom_adapter("custom", CustomAdapter())
        custom_adapter = registry.get_custom_adapter("custom")
        
        assert custom_adapter is not None
        assert isinstance(custom_adapter, CustomAdapter)


class TestDomainSwitching:
    """Testes para mudança de domínio"""
    
    def test_domain_switching(self):
        """Testa mudança de domínio"""
        # Configuração inicial para saúde
        config = DomainConfig(
            domain_type=DomainType.HEALTHCARE,
            domain_name="Test",
            cultural_context="global"
        )
        
        core = SEVEUniversalCore(config)
        assert core.config.domain_type == DomainType.HEALTHCARE
        
        # Mudar para educação
        education_config = DomainConfig(
            domain_type=DomainType.EDUCATION,
            domain_name="Test",
            cultural_context="global"
        )
        
        core.switch_domain(education_config)
        assert core.config.domain_type == DomainType.EDUCATION
        
        # Mudar para negócios
        business_config = DomainConfig(
            domain_type=DomainType.BUSINESS,
            domain_name="Test",
            cultural_context="global"
        )
        
        core.switch_domain(business_config)
        assert core.config.domain_type == DomainType.BUSINESS


class TestUniversalProcessing:
    """Testes para processamento universal"""
    
    @pytest.mark.asyncio
    async def test_healthcare_processing(self):
        """Testa processamento para domínio de saúde"""
        config = DomainConfig(
            domain_type=DomainType.HEALTHCARE,
            domain_name="Healthcare AI",
            cultural_context="global"
        )
        
        core = SEVEUniversalCore(config)
        
        context = UniversalContext(
            domain=DomainType.HEALTHCARE,
            user_profile={"patient_id": "P001"},
            environmental_data={},
            cultural_context="global",
            temporal_context={},
            metadata={}
        )
        
        medical_data = {
            "patient_id": "P001",
            "vitals": {"blood_pressure": "120/80"},
            "symptoms": ["headache"]
        }
        
        result = await core.process_universal_context(context, medical_data)
        
        assert result is not None
        assert "domain_result" in result
        assert "learning_result" in result
        assert "adapted_context" in result
    
    @pytest.mark.asyncio
    async def test_education_processing(self):
        """Testa processamento para domínio educacional"""
        config = DomainConfig(
            domain_type=DomainType.EDUCATION,
            domain_name="Education AI",
            cultural_context="global"
        )
        
        core = SEVEUniversalCore(config)
        
        context = UniversalContext(
            domain=DomainType.EDUCATION,
            user_profile={"student_id": "S001"},
            environmental_data={},
            cultural_context="global",
            temporal_context={},
            metadata={}
        )
        
        education_data = {
            "student_id": "S001",
            "subject": "mathematics",
            "progress": {"completed": 0.5}
        }
        
        result = await core.process_universal_context(context, education_data)
        
        assert result is not None
        assert "domain_result" in result
        assert "learning_result" in result
        assert "adapted_context" in result


class TestIntegration:
    """Testes de integração"""
    
    def test_all_domains_importable(self):
        """Testa se todos os domínios podem ser importados"""
        from seve_universal import (
            SEVEUniversalCore, DomainConfig, UniversalContext, DomainType, AdaptationLevel
        )
        
        # Todos os imports devem funcionar sem erro
        assert SEVEUniversalCore is not None
        assert DomainConfig is not None
        assert UniversalContext is not None
        assert DomainType is not None
        assert AdaptationLevel is not None
    
    def test_all_adapters_importable(self):
        """Testa se todos os adaptadores podem ser importados"""
        from seve_universal.adapters import (
            UniversalAdapterRegistry, HealthcareAdapter, EducationAdapter,
            BusinessAdapter, SmartCityAdapter, GamingAdapter
        )
        
        # Todos os imports devem funcionar sem erro
        assert UniversalAdapterRegistry is not None
        assert HealthcareAdapter is not None
        assert EducationAdapter is not None
        assert BusinessAdapter is not None
        assert SmartCityAdapter is not None
        assert GamingAdapter is not None
    
    def test_domain_types_complete(self):
        """Testa se todos os tipos de domínio estão disponíveis"""
        expected_domains = [
            DomainType.HEALTHCARE,
            DomainType.EDUCATION,
            DomainType.BUSINESS,
            DomainType.SMART_CITY,
            DomainType.GAMING,
            DomainType.RETAIL,
            DomainType.FINANCE,
            DomainType.MANUFACTURING,
            DomainType.CUSTOM
        ]
        
        for domain in expected_domains:
            assert domain is not None
            assert domain.value is not None


if __name__ == "__main__":
    # Executar testes
    pytest.main([__file__, "-v"])
