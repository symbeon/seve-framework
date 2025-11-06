"""Tests for Universal Domain Adapters."""

import pytest

try:
    from seve_framework.universal.core import DomainType, UniversalContext
    from seve_framework.universal.adapters import (
        HealthcareAdapter,
        EducationAdapter,
        BusinessAdapter,
        SmartCityAdapter,
        GamingAdapter,
        RetailAdapter,
        FinanceAdapter,
        ManufacturingAdapter,
        UniversalAdapterRegistry,
    )
except ImportError:
    import sys
    from pathlib import Path
    src_path = Path(__file__).parent.parent / "src"
    sys.path.insert(0, str(src_path))
    from seve_framework.universal.core import DomainType, UniversalContext
    from seve_framework.universal.adapters import (
        HealthcareAdapter,
        EducationAdapter,
        BusinessAdapter,
        SmartCityAdapter,
        GamingAdapter,
        RetailAdapter,
        FinanceAdapter,
        ManufacturingAdapter,
        UniversalAdapterRegistry,
    )


class TestHealthcareAdapter:
    """Tests for HealthcareAdapter."""

    def test_adapt_to_context(self):
        """Test adapting context for healthcare."""
        adapter = HealthcareAdapter()
        context = UniversalContext(
            domain=DomainType.HEALTHCARE,
            user_profile={},
            environmental_data={},
            cultural_context="global",
            temporal_context={},
            metadata={}
        )
        
        adapted = adapter.adapt_to_context(context)
        
        assert adapted.metadata["medical_privacy"] is True
        assert adapted.metadata["hipaa_compliance"] is True
        assert adapted.metadata["patient_safety"] is True

    def test_extract_domain_features(self):
        """Test extracting healthcare features."""
        adapter = HealthcareAdapter()
        data = {
            "patient_id": "P123",
            "history": ["condition1", "condition2"],
            "vitals": {"heart_rate": 72, "blood_pressure": "120/80"},
            "diagnosis": "Healthy",
            "treatment": "Monitoring"
        }
        
        features = adapter.extract_domain_features(data)
        
        assert features["patient_id"] == "P123"
        assert len(features["medical_history"]) == 2
        assert features["vital_signs"]["heart_rate"] == 72
        assert features["diagnosis"] == "Healthy"

    def test_apply_domain_rules(self):
        """Test applying healthcare rules."""
        adapter = HealthcareAdapter()
        decision = {"action": "prescribe", "medication": "aspirin"}
        
        result = adapter.apply_domain_rules(decision)
        
        assert result["medical_decision"] == decision
        assert result["safety_check"] is True
        assert result["privacy_protected"] is True


class TestEducationAdapter:
    """Tests for EducationAdapter."""

    def test_adapt_to_context(self):
        """Test adapting context for education."""
        adapter = EducationAdapter()
        context = UniversalContext(
            domain=DomainType.EDUCATION,
            user_profile={},
            environmental_data={},
            cultural_context="global",
            temporal_context={},
            metadata={}
        )
        
        adapted = adapter.adapt_to_context(context)
        
        assert adapted.metadata["learning_objectives"] is True
        assert adapted.metadata["student_privacy"] is True
        assert adapted.metadata["educational_standards"] is True

    def test_extract_domain_features(self):
        """Test extracting education features."""
        adapter = EducationAdapter()
        data = {
            "learning_style": "visual",
            "level": "high_school",
            "subject": "mathematics",
            "progress": {"completed": 75, "total": 100},
            "assessments": [{"score": 85, "date": "2025-01-15"}]
        }
        
        features = adapter.extract_domain_features(data)
        
        assert features["learning_style"] == "visual"
        assert features["academic_level"] == "high_school"
        assert features["subject_matter"] == "mathematics"
        assert features["learning_progress"]["completed"] == 75


class TestRetailAdapter:
    """Tests for RetailAdapter."""

    def test_adapt_to_context(self):
        """Test adapting context for retail."""
        adapter = RetailAdapter()
        context = UniversalContext(
            domain=DomainType.RETAIL,
            user_profile={},
            environmental_data={},
            cultural_context="global",
            temporal_context={},
            metadata={}
        )
        
        adapted = adapter.adapt_to_context(context)
        
        assert adapted.metadata["customer_privacy"] is True
        assert adapted.metadata["esg_compliance"] is True
        assert adapted.metadata["inventory_management"] is True

    def test_extract_domain_features(self):
        """Test extracting retail features."""
        adapter = RetailAdapter()
        data = {
            "customer": {"id": "C123", "name": "John"},
            "products": [{"id": "P1", "name": "Product 1"}],
            "history": [{"id": "O1", "date": "2025-01-15"}],
            "inventory": {"P1": 50},
            "esg": {"environmental_score": 85, "social_score": 90}
        }
        
        features = adapter.extract_domain_features(data)
        
        assert features["customer_profile"]["id"] == "C123"
        assert len(features["product_catalog"]) == 1
        assert features["esg_scores"]["environmental_score"] == 85


class TestUniversalAdapterRegistry:
    """Tests for UniversalAdapterRegistry."""

    def test_registry_initialization(self):
        """Test registry initialization."""
        registry = UniversalAdapterRegistry()
        
        assert registry.get_adapter(DomainType.HEALTHCARE) is not None
        assert registry.get_adapter(DomainType.EDUCATION) is not None
        assert registry.get_adapter(DomainType.RETAIL) is not None

    def test_list_available_domains(self):
        """Test listing available domains."""
        registry = UniversalAdapterRegistry()
        domains = registry.list_available_domains()
        
        assert DomainType.HEALTHCARE in domains
        assert DomainType.EDUCATION in domains
        assert DomainType.BUSINESS in domains
        assert DomainType.SMART_CITY in domains
        assert DomainType.GAMING in domains
        assert DomainType.RETAIL in domains
        assert DomainType.FINANCE in domains
        assert DomainType.MANUFACTURING in domains
        assert len(domains) == 8

    def test_get_adapter_info(self):
        """Test getting adapter information."""
        registry = UniversalAdapterRegistry()
        info = registry.get_adapter_info(DomainType.HEALTHCARE)
        
        assert info["domain"] == "healthcare"
        assert "adapter_class" in info
        assert "capabilities" in info
        assert len(info["capabilities"]) > 0

    def test_register_custom_adapter(self):
        """Test registering custom adapter."""
        from seve_framework.universal.core import DomainAdapter
        
        class CustomAdapter(DomainAdapter):
            def adapt_to_context(self, context):
                return context
            def extract_domain_features(self, data):
                return {"custom": data}
            def apply_domain_rules(self, decision):
                return decision
        
        registry = UniversalAdapterRegistry()
        custom = CustomAdapter()
        registry.register_custom_adapter("custom_domain", custom)
        
        retrieved = registry.get_custom_adapter("custom_domain")
        assert retrieved == custom


class TestAllAdapters:
    """Test all adapters have consistent interface."""

    @pytest.mark.parametrize("adapter_class,domain_type", [
        (HealthcareAdapter, DomainType.HEALTHCARE),
        (EducationAdapter, DomainType.EDUCATION),
        (BusinessAdapter, DomainType.BUSINESS),
        (SmartCityAdapter, DomainType.SMART_CITY),
        (GamingAdapter, DomainType.GAMING),
        (RetailAdapter, DomainType.RETAIL),
        (FinanceAdapter, DomainType.FINANCE),
        (ManufacturingAdapter, DomainType.MANUFACTURING),
    ])
    def test_adapter_interface(self, adapter_class, domain_type):
        """Test that all adapters implement required interface."""
        adapter = adapter_class()
        context = UniversalContext(
            domain=domain_type,
            user_profile={},
            environmental_data={},
            cultural_context="global",
            temporal_context={},
            metadata={}
        )
        
        # Test adapt_to_context
        adapted = adapter.adapt_to_context(context)
        assert isinstance(adapted, UniversalContext)
        assert len(adapted.metadata) > 0
        
        # Test extract_domain_features
        features = adapter.extract_domain_features({"test": "data"})
        assert isinstance(features, dict)
        
        # Test apply_domain_rules
        result = adapter.apply_domain_rules({"test": "decision"})
        assert isinstance(result, dict)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

