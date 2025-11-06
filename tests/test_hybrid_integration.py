"""Integration tests for HYBRID mode and Universal components."""

import pytest

try:
    from seve_framework.config import SEVEConfig, SEVEMode, PrivacyLevel, EthicsLevel
    from seve_framework.core import SEVEHybridFramework
    from seve_framework.universal import (
        DomainConfig,
        DomainType,
        UniversalContext,
        SEVEUniversalCore,
    )
except ImportError:
    import sys
    from pathlib import Path
    src_path = Path(__file__).parent.parent / "src"
    sys.path.insert(0, str(src_path))
    from seve_framework.config import SEVEConfig, SEVEMode, PrivacyLevel, EthicsLevel
    from seve_framework.core import SEVEHybridFramework
    from seve_framework.universal import (
        DomainConfig,
        DomainType,
        UniversalContext,
        SEVEUniversalCore,
    )


class TestHybridModeIntegration:
    """Tests for HYBRID mode integration."""

    @pytest.mark.asyncio
    async def test_hybrid_framework_initialization(self):
        """Test initializing hybrid framework."""
        config = SEVEConfig(
            mode=SEVEMode.HYBRID,
            privacy_level=PrivacyLevel.HIGH,
            ethics_level=EthicsLevel.STANDARD
        )
        
        framework = SEVEHybridFramework(config)
        
        assert framework.config.mode == SEVEMode.HYBRID
        assert framework.v3_core is not None
        # Universal core should be available in HYBRID mode
        # (may be None if imports fail, but structure should exist)

    def test_hybrid_framework_capabilities(self):
        """Test getting hybrid framework capabilities."""
        config = SEVEConfig(
            mode=SEVEMode.HYBRID,
            privacy_level=PrivacyLevel.HIGH,
            ethics_level=EthicsLevel.STANDARD
        )
        
        framework = SEVEHybridFramework(config)
        capabilities = framework.get_capabilities()
        
        assert capabilities["version"] == "1.0.0"
        assert capabilities["mode"] == "hybrid"
        assert capabilities["v3_core_available"] is True
        assert "universal_core_available" in capabilities
        assert "modules" in capabilities
        assert capabilities["modules"]["vision"] is True

    def test_universal_core_standalone(self):
        """Test Universal Core works standalone."""
        domain_config = DomainConfig(
            domain_type=DomainType.HEALTHCARE,
            domain_name="Healthcare System"
        )
        
        core = SEVEUniversalCore(domain_config)
        
        assert core.config.domain_type == DomainType.HEALTHCARE
        assert core.domain_adapter_registry is not None
        assert core.learning_module is not None

    @pytest.mark.asyncio
    async def test_universal_ethics_in_guardflow(self):
        """Test Universal Ethics Engine integration with GuardFlow."""
        from seve_framework.ethics import SEVEEthicsModule
        
        config = SEVEConfig(
            mode=SEVEMode.HYBRID,
            ethics_level=EthicsLevel.STRICT,
            guardflow_enabled=True
        )
        
        ethics_module = SEVEEthicsModule(config)
        
        # Check if Universal Ethics Engine is available
        assert hasattr(ethics_module, "universal_ethics_engine")
        
        # Initialize module
        await ethics_module.initialize()
        
        # Check status includes universal ethics info
        status = ethics_module.get_status()
        assert "universal_ethics_engine" in status
        assert "available" in status["universal_ethics_engine"]
        
        # Test validation (should use both engines if available)
        decision_data = {
            "test": "data",
            "personal_data": {"encrypted": True}
        }
        context = {"domain": "healthcare"}
        
        assessments = await ethics_module.validate_decision(decision_data, context)
        
        assert isinstance(assessments, list)
        assert len(assessments) > 0

    @pytest.mark.asyncio
    async def test_domain_switching(self):
        """Test switching between domains."""
        domain_config1 = DomainConfig(
            domain_type=DomainType.EDUCATION,
            domain_name="Education System"
        )
        
        core = SEVEUniversalCore(domain_config1)
        assert core.config.domain_type == DomainType.EDUCATION
        
        domain_config2 = DomainConfig(
            domain_type=DomainType.BUSINESS,
            domain_name="Business System"
        )
        
        core.switch_domain(domain_config2)
        assert core.config.domain_type == DomainType.BUSINESS

    @pytest.mark.asyncio
    async def test_universal_context_processing(self):
        """Test processing universal context."""
        from seve_framework.universal.adapters import HealthcareAdapter
        
        domain_config = DomainConfig(
            domain_type=DomainType.HEALTHCARE,
            domain_name="Healthcare System"
        )
        
        core = SEVEUniversalCore(domain_config)
        
        # Register adapter
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
        
        data = {
            "patient_id": "P123",
            "vitals": {"heart_rate": 72}
        }
        
        result = await core.process_universal_context(context, data)
        
        assert "domain_result" in result
        assert "learning_result" in result
        assert "adapted_context" in result
        assert "domain_features" in result
        
        # Check that healthcare features were extracted
        assert "medical_data" in result["domain_features"]


class TestBackwardCompatibility:
    """Tests to ensure backward compatibility with v3.0 mode."""

    def test_v3_mode_still_works(self):
        """Test that v3.0 mode still works independently."""
        config = SEVEConfig(
            mode=SEVEMode.V3,
            privacy_level=PrivacyLevel.HIGH,
            ethics_level=EthicsLevel.STANDARD
        )
        
        framework = SEVEHybridFramework(config)
        
        assert framework.config.mode == SEVEMode.V3
        assert framework.v3_core is not None
        # Universal core should not be initialized in V3 mode
        # (this is expected behavior)

    @pytest.mark.asyncio
    async def test_guardflow_works_independently(self):
        """Test that GuardFlow works without Universal Ethics Engine."""
        from seve_framework.ethics import SEVEEthicsModule
        
        config = SEVEConfig(
            mode=SEVEMode.V3,  # V3 mode, not HYBRID
            ethics_level=EthicsLevel.STRICT,
            guardflow_enabled=True
        )
        
        ethics_module = SEVEEthicsModule(config)
        await ethics_module.initialize()
        
        # GuardFlow should work independently
        decision_data = {"test": "data"}
        assessments = await ethics_module.validate_decision(
            decision_data,
            use_universal=False  # Force GuardFlow only
        )
        
        assert isinstance(assessments, list)
        assert len(assessments) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

