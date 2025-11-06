"""Tests for Universal Core module."""

import pytest

# Try importing from installed package first, then fallback to direct path
try:
    from seve_framework.universal.core import (
        SEVEUniversalCore,
        DomainConfig,
        DomainType,
        UniversalContext,
        AdaptationLevel,
        DomainAdapterRegistry,
    )
except ImportError:
    # Fallback for development/testing without installation
    import sys
    from pathlib import Path
    src_path = Path(__file__).parent.parent / "src"
    sys.path.insert(0, str(src_path))
    from seve_framework.universal.core import (
        SEVEUniversalCore,
        DomainConfig,
        DomainType,
        UniversalContext,
        AdaptationLevel,
        DomainAdapterRegistry,
    )


class TestDomainConfig:
    """Tests for DomainConfig."""

    def test_domain_config_creation(self):
        """Test creating a DomainConfig."""
        config = DomainConfig(
            domain_type=DomainType.HEALTHCARE,
            domain_name="Healthcare System"
        )
        assert config.domain_type == DomainType.HEALTHCARE
        assert config.domain_name == "Healthcare System"
        assert config.cultural_context == "global"
        assert config.adaptation_level == AdaptationLevel.INTERMEDIATE

    def test_domain_config_with_custom_values(self):
        """Test DomainConfig with custom values."""
        config = DomainConfig(
            domain_type=DomainType.EDUCATION,
            domain_name="Education Platform",
            cultural_context="brazil",
            adaptation_level=AdaptationLevel.ADVANCED,
            ethical_rules=["privacy", "fairness"]
        )
        assert config.cultural_context == "brazil"
        assert config.adaptation_level == AdaptationLevel.ADVANCED
        assert len(config.ethical_rules) == 2


class TestUniversalContext:
    """Tests for UniversalContext."""

    def test_universal_context_creation(self):
        """Test creating a UniversalContext."""
        context = UniversalContext(
            domain=DomainType.BUSINESS,
            user_profile={"user_id": "123"},
            environmental_data={"location": "office"},
            cultural_context="global",
            temporal_context={"timestamp": 1234567890},
            metadata={"test": True}
        )
        assert context.domain == DomainType.BUSINESS
        assert context.user_profile["user_id"] == "123"
        assert context.metadata["test"] is True


class TestDomainAdapterRegistry:
    """Tests for DomainAdapterRegistry."""

    def test_registry_creation(self):
        """Test creating a registry."""
        registry = DomainAdapterRegistry()
        assert len(registry._adapters) == 0
        assert len(registry._custom_adapters) == 0

    def test_register_adapter(self):
        """Test registering an adapter."""
        from seve_framework.universal.adapters import HealthcareAdapter
        
        registry = DomainAdapterRegistry()
        adapter = HealthcareAdapter()
        registry.register_adapter(DomainType.HEALTHCARE, adapter)
        
        assert DomainType.HEALTHCARE in registry._adapters
        assert registry.get_adapter(DomainType.HEALTHCARE) == adapter

    def test_get_nonexistent_adapter(self):
        """Test getting non-existent adapter."""
        registry = DomainAdapterRegistry()
        adapter = registry.get_adapter(DomainType.GAMING)
        assert adapter is None


class TestSEVEUniversalCore:
    """Tests for SEVEUniversalCore."""

    def test_core_initialization(self):
        """Test core initialization."""
        config = DomainConfig(
            domain_type=DomainType.RETAIL,
            domain_name="Retail System"
        )
        core = SEVEUniversalCore(config)
        
        assert core.config == config
        assert core.domain_adapter_registry is not None
        assert core.learning_module is not None
        assert core.context_manager is not None

    def test_get_domain_metrics(self):
        """Test getting domain metrics."""
        config = DomainConfig(
            domain_type=DomainType.FINANCE,
            domain_name="Finance System"
        )
        core = SEVEUniversalCore(config)
        metrics = core.get_domain_metrics()
        
        assert metrics["domain"] == "finance"
        assert metrics["adaptation_level"] == "intermediate"
        assert "registered_adapters" in metrics
        assert "custom_adapters" in metrics

    @pytest.mark.asyncio
    async def test_process_universal_context(self):
        """Test processing universal context."""
        config = DomainConfig(
            domain_type=DomainType.HEALTHCARE,
            domain_name="Healthcare System"
        )
        core = SEVEUniversalCore(config)
        
        # Register adapter
        from seve_framework.universal.adapters import HealthcareAdapter
        core.domain_adapter_registry.register_adapter(
            DomainType.HEALTHCARE,
            HealthcareAdapter()
        )
        
        context = UniversalContext(
            domain=DomainType.HEALTHCARE,
            user_profile={"patient_id": "P123"},
            environmental_data={"hospital": "General"},
            cultural_context="global",
            temporal_context={"timestamp": 1234567890},
            metadata={}
        )
        
        data = {"patient_id": "P123", "vitals": {"heart_rate": 72}}
        result = await core.process_universal_context(context, data)
        
        assert "domain_result" in result
        assert "learning_result" in result
        assert "adapted_context" in result
        assert "domain_features" in result

    def test_switch_domain(self):
        """Test switching domain."""
        config1 = DomainConfig(
            domain_type=DomainType.EDUCATION,
            domain_name="Education System"
        )
        core = SEVEUniversalCore(config1)
        
        config2 = DomainConfig(
            domain_type=DomainType.BUSINESS,
            domain_name="Business System"
        )
        core.switch_domain(config2)
        
        assert core.config.domain_type == DomainType.BUSINESS
        assert core.config.domain_name == "Business System"


class TestUniversalLearningModule:
    """Tests for UniversalLearningModule."""

    @pytest.mark.asyncio
    async def test_update_knowledge(self):
        """Test updating knowledge."""
        from seve_framework.universal.core import UniversalLearningModule, UniversalContext
        
        module = UniversalLearningModule()
        context = UniversalContext(
            domain=DomainType.RETAIL,
            user_profile={},
            environmental_data={},
            cultural_context="global",
            temporal_context={},
            metadata={}
        )
        
        result = await module.update_knowledge({"test": "data"}, context)
        
        assert result["knowledge_updated"] is True
        assert "transfer_learning" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

