"""Tests for Universal Ethics Engine."""

import pytest

try:
    from seve_framework.universal.ethics import (
        UniversalEthicsEngine,
        DomainEthicsEngine,
        EthicalRule,
        EthicalAssessment,
        EthicalPrinciple,
        EthicalComplianceLevel,
    )
except ImportError:
    import sys
    from pathlib import Path
    src_path = Path(__file__).parent.parent / "src"
    sys.path.insert(0, str(src_path))
    from seve_framework.universal.ethics import (
        UniversalEthicsEngine,
        DomainEthicsEngine,
        EthicalRule,
        EthicalAssessment,
        EthicalPrinciple,
        EthicalComplianceLevel,
    )


class TestEthicalRule:
    """Tests for EthicalRule."""

    def test_ethical_rule_creation(self):
        """Test creating an EthicalRule."""
        rule = EthicalRule(
            principle=EthicalPrinciple.PRIVACY,
            rule_id="test_rule",
            description="Test rule description",
            compliance_level=EthicalComplianceLevel.CRITICAL
        )
        
        assert rule.principle == EthicalPrinciple.PRIVACY
        assert rule.rule_id == "test_rule"
        assert rule.compliance_level == EthicalComplianceLevel.CRITICAL
        assert rule.domain_specific is False


class TestUniversalEthicsEngine:
    """Tests for UniversalEthicsEngine."""

    def test_engine_initialization(self):
        """Test engine initialization."""
        engine = UniversalEthicsEngine()
        
        assert len(engine.universal_rules) > 0
        assert engine.domain_engines == {}
        assert engine.compliance_history == []

    def test_universal_rules_loaded(self):
        """Test that universal rules are loaded."""
        engine = UniversalEthicsEngine()
        
        rule_ids = [rule.rule_id for rule in engine.universal_rules]
        
        assert "privacy_data_protection" in rule_ids
        assert "transparency_decisions" in rule_ids
        assert "fairness_bias_prevention" in rule_ids
        assert "accountability_decisions" in rule_ids
        assert "autonomy_user_control" in rule_ids

    @pytest.mark.asyncio
    async def test_assess_universal_compliance_basic(self):
        """Test basic universal compliance assessment."""
        engine = UniversalEthicsEngine()
        data = {"test": "data"}
        context = {"timestamp": 1234567890}
        
        result = await engine.assess_universal_compliance(data, context)
        
        assert "overall_compliance_score" in result
        assert "assessments" in result
        assert "critical_violations" in result
        assert "recommendations" in result
        assert "risk_level" in result
        assert isinstance(result["overall_compliance_score"], float)
        assert 0.0 <= result["overall_compliance_score"] <= 1.0

    @pytest.mark.asyncio
    async def test_assess_universal_compliance_privacy_violation(self):
        """Test privacy violation detection."""
        engine = UniversalEthicsEngine()
        data = {
            "personal_data": {"name": "John", "email": "john@example.com"},
            "encrypted": False  # Privacy violation
        }
        context = {"timestamp": 1234567890}
        
        result = await engine.assess_universal_compliance(data, context)
        
        assert result["overall_compliance_score"] < 1.0
        assert len(result["critical_violations"]) > 0 or len(result["recommendations"]) > 0

    @pytest.mark.asyncio
    async def test_assess_universal_compliance_with_domain(self):
        """Test compliance assessment with domain."""
        engine = UniversalEthicsEngine()
        data = {"test": "data"}
        context = {"timestamp": 1234567890, "domain": "healthcare"}
        
        # Should work even without domain engine registered
        result = await engine.assess_universal_compliance(data, context, domain="healthcare")
        
        assert "domain" in result
        assert result["domain"] == "healthcare"

    @pytest.mark.asyncio
    async def test_assess_universal_compliance_fairness(self):
        """Test fairness assessment."""
        engine = UniversalEthicsEngine()
        
        # Low diversity data
        data = {
            "demographics": {
                "gender": "male",
                "age": "30-40",
                "location": "urban"
            }
        }
        context = {"timestamp": 1234567890}
        
        result = await engine.assess_universal_compliance(data, context)
        
        # Should detect lack of diversity
        assessments = result["assessments"]
        fairness_assessments = [
            a for a in assessments 
            if isinstance(a, dict) and "fairness" in str(a.get("rule_id", "")).lower()
        ]
        assert len(fairness_assessments) > 0

    @pytest.mark.asyncio
    async def test_assess_universal_compliance_transparency(self):
        """Test transparency assessment."""
        engine = UniversalEthicsEngine()
        data = {"decision": "approved"}
        context = {
            "timestamp": 1234567890,
            "explanation_provided": False  # Transparency violation
        }
        
        result = await engine.assess_universal_compliance(data, context)
        
        # Should have recommendations for transparency
        assert len(result["recommendations"]) > 0

    def test_calculate_overall_score(self):
        """Test overall score calculation."""
        engine = UniversalEthicsEngine()
        
        # Empty assessments
        score = engine._calculate_overall_score([])
        assert score == 1.0
        
        # Single assessment
        assessment = EthicalAssessment(
            rule_id="test_rule",
            compliance_score=0.8,
            violations=[],
            recommendations=[]
        )
        score = engine._calculate_overall_score([assessment])
        assert 0.0 <= score <= 1.0

    def test_get_compliance_weight(self):
        """Test getting compliance weights."""
        engine = UniversalEthicsEngine()
        
        assert engine._get_compliance_weight(EthicalComplianceLevel.CRITICAL) == 1.0
        assert engine._get_compliance_weight(EthicalComplianceLevel.HIGH) == 0.8
        assert engine._get_compliance_weight(EthicalComplianceLevel.MEDIUM) == 0.6
        assert engine._get_compliance_weight(EthicalComplianceLevel.LOW) == 0.4
        assert engine._get_compliance_weight(EthicalComplianceLevel.OPTIONAL) == 0.2

    def test_identify_critical_violations(self):
        """Test identifying critical violations."""
        engine = UniversalEthicsEngine()
        
        assessments = [
            EthicalAssessment(
                rule_id="rule1",
                compliance_score=0.5,
                violations=["violation1"],
                risk_level="critical"
            ),
            EthicalAssessment(
                rule_id="rule2",
                compliance_score=0.9,
                violations=[],
                risk_level="low"
            )
        ]
        
        violations = engine._identify_critical_violations(assessments)
        assert "violation1" in violations

    def test_determine_risk_level(self):
        """Test determining risk level."""
        engine = UniversalEthicsEngine()
        
        # Critical violations
        risk = engine._determine_risk_level(0.9, ["critical_violation"])
        assert risk == "critical"
        
        # Low score
        risk = engine._determine_risk_level(0.4, [])
        assert risk == "high"
        
        # Medium score
        risk = engine._determine_risk_level(0.6, [])
        assert risk == "medium"
        
        # High score
        risk = engine._determine_risk_level(0.8, [])
        assert risk == "low"

    def test_get_compliance_metrics(self):
        """Test getting compliance metrics."""
        engine = UniversalEthicsEngine()
        
        # No history
        metrics = engine.get_compliance_metrics()
        assert "no_data" in metrics
        
        # Add some history
        assessment = EthicalAssessment(
            rule_id="test_rule",
            compliance_score=0.8,
            violations=[],
            recommendations=[],
            risk_level="low"
        )
        engine.compliance_history.append(assessment)
        
        metrics = engine.get_compliance_metrics()
        assert metrics["total_assessments"] == 1
        assert "average_score" in metrics
        assert "domains_covered" in metrics
        assert "universal_rules" in metrics

    def test_register_domain_engine(self):
        """Test registering domain engine."""
        engine = UniversalEthicsEngine()
        
        class MockDomainEngine(DomainEthicsEngine):
            def assess_ethical_compliance(self, data, context):
                return []
            def get_domain_rules(self):
                return []
            def apply_ethical_constraints(self, decision, context):
                return decision
        
        domain_engine = MockDomainEngine()
        engine.register_domain_engine("healthcare", domain_engine)
        
        assert "healthcare" in engine.domain_engines
        assert engine.domain_engines["healthcare"] == domain_engine


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

