"""Universal ethics engine migrated from the legacy implementation."""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class EthicalPrinciple(Enum):
    """Universal ethical principles."""

    AUTONOMY = "autonomy"
    BENEFICENCE = "beneficence"
    NON_MALEFICENCE = "non_maleficence"
    JUSTICE = "justice"
    TRANSPARENCY = "transparency"
    ACCOUNTABILITY = "accountability"
    PRIVACY = "privacy"
    FAIRNESS = "fairness"


class EthicalComplianceLevel(Enum):
    """Ethical compliance levels."""

    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    OPTIONAL = "optional"


@dataclass
class EthicalRule:
    """Specific ethical rule definition."""

    principle: EthicalPrinciple
    rule_id: str
    description: str
    compliance_level: EthicalComplianceLevel
    domain_specific: bool = False
    cultural_context: Optional[str] = None
    enforcement_mechanism: str = "automatic"
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class EthicalAssessment:
    """Result of ethical assessment."""

    rule_id: str
    compliance_score: float
    violations: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    risk_level: str = "low"
    metadata: Dict[str, Any] = field(default_factory=dict)


class DomainEthicsEngine(ABC):
    """Domain-specific ethics engine interface."""

    @abstractmethod
    def assess_ethical_compliance(
        self,
        data: Any,
        context: Dict[str, Any],
    ) -> List[EthicalAssessment]:
        """Assess ethical compliance for a domain."""

    @abstractmethod
    def get_domain_rules(self) -> List[EthicalRule]:
        """Return domain-specific ethical rules."""

    @abstractmethod
    def apply_ethical_constraints(
        self,
        decision: Any,
        context: Dict[str, Any],
    ) -> Any:
        """Apply ethical constraints to a decision."""


class UniversalEthicsEngine:
    """
    Universal ethics engine for SEVE Framework.

    Manages ethical compliance across all domains,
    applying universal and domain-specific principles.
    """

    def __init__(self) -> None:
        self.universal_rules = self._load_universal_rules()
        self.domain_engines: Dict[str, DomainEthicsEngine] = {}
        self.compliance_history: List[EthicalAssessment] = []
        self._initialize_domain_engines()

    def _load_universal_rules(self) -> List[EthicalRule]:
        """Load universal ethical rules."""
        return [
            EthicalRule(
                principle=EthicalPrinciple.PRIVACY,
                rule_id="privacy_data_protection",
                description="Proteção de dados pessoais",
                compliance_level=EthicalComplianceLevel.CRITICAL,
                enforcement_mechanism="automatic",
            ),
            EthicalRule(
                principle=EthicalPrinciple.TRANSPARENCY,
                rule_id="transparency_decisions",
                description="Transparência em decisões automatizadas",
                compliance_level=EthicalComplianceLevel.HIGH,
                enforcement_mechanism="automatic",
            ),
            EthicalRule(
                principle=EthicalPrinciple.FAIRNESS,
                rule_id="fairness_bias_prevention",
                description="Prevenção de viés e discriminação",
                compliance_level=EthicalComplianceLevel.CRITICAL,
                enforcement_mechanism="automatic",
            ),
            EthicalRule(
                principle=EthicalPrinciple.ACCOUNTABILITY,
                rule_id="accountability_decisions",
                description="Responsabilização por decisões",
                compliance_level=EthicalComplianceLevel.HIGH,
                enforcement_mechanism="automatic",
            ),
            EthicalRule(
                principle=EthicalPrinciple.AUTONOMY,
                rule_id="autonomy_user_control",
                description="Controle do usuário sobre dados",
                compliance_level=EthicalComplianceLevel.HIGH,
                enforcement_mechanism="automatic",
            ),
        ]

    def _initialize_domain_engines(self) -> None:
        """Initialize domain-specific ethics engines."""
        # Placeholder for domain-specific engine initialization
        pass

    def register_domain_engine(self, domain: str, engine: DomainEthicsEngine) -> None:
        """Register domain-specific ethics engine."""
        self.domain_engines[domain] = engine
        logger.info("Motor de ética registrado para domínio: %s", domain)

    async def assess_universal_compliance(
        self,
        data: Any,
        context: Dict[str, Any],
        domain: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Assess universal ethical compliance.

        Args:
            data: Data to assess
            context: Assessment context
            domain: Specific domain (optional)

        Returns:
            Ethical assessment result
        """
        assessments: List[EthicalAssessment] = []

        # Assess universal rules
        universal_assessments = await self._assess_universal_rules(data, context)
        assessments.extend(universal_assessments)

        # Assess domain-specific rules
        if domain and domain in self.domain_engines:
            domain_assessments = await self._assess_domain_rules(data, context, domain)
            assessments.extend(domain_assessments)

        # Calculate overall compliance score
        overall_score = self._calculate_overall_score(assessments)

        # Identify critical violations
        critical_violations = self._identify_critical_violations(assessments)

        # Generate recommendations
        recommendations = self._generate_recommendations(assessments)

        result = {
            "overall_compliance_score": overall_score,
            "assessments": [a.__dict__ for a in assessments],
            "critical_violations": critical_violations,
            "recommendations": recommendations,
            "risk_level": self._determine_risk_level(overall_score, critical_violations),
            "domain": domain,
            "timestamp": context.get("timestamp"),
        }

        # Store history
        self.compliance_history.extend(assessments)

        return result

    async def _assess_universal_rules(
        self,
        data: Any,
        context: Dict[str, Any],
    ) -> List[EthicalAssessment]:
        """Assess universal rules."""
        assessments = []

        for rule in self.universal_rules:
            assessment = await self._evaluate_rule(rule, data, context)
            assessments.append(assessment)

        return assessments

    async def _assess_domain_rules(
        self,
        data: Any,
        context: Dict[str, Any],
        domain: str,
    ) -> List[EthicalAssessment]:
        """Assess domain-specific rules."""
        engine = self.domain_engines[domain]
        return engine.assess_ethical_compliance(data, context)

    async def _evaluate_rule(
        self,
        rule: EthicalRule,
        data: Any,
        context: Dict[str, Any],
    ) -> EthicalAssessment:
        """Evaluate a specific rule."""
        score = 0.8
        violations: List[str] = []
        recommendations: List[str] = []

        # Principle-specific logic
        if rule.principle == EthicalPrinciple.PRIVACY:
            score, violations, recommendations = self._assess_privacy(data, context)
        elif rule.principle == EthicalPrinciple.FAIRNESS:
            score, violations, recommendations = self._assess_fairness(data, context)
        elif rule.principle == EthicalPrinciple.TRANSPARENCY:
            score, violations, recommendations = self._assess_transparency(data, context)

        return EthicalAssessment(
            rule_id=rule.rule_id,
            compliance_score=score,
            violations=violations,
            recommendations=recommendations,
            risk_level=self._determine_rule_risk_level(score, rule.compliance_level),
        )

    def _assess_privacy(
        self,
        data: Any,
        context: Dict[str, Any],
    ) -> tuple[float, List[str], List[str]]:
        """Assess privacy compliance."""
        score = 0.9
        violations: List[str] = []
        recommendations: List[str] = []

        # Check if personal data is protected
        if isinstance(data, dict) and "personal_data" in data:
            if not data.get("encrypted", False):
                violations.append("Dados pessoais não criptografados")
                score -= 0.3

        if violations:
            recommendations.append("Implementar criptografia de dados pessoais")

        return max(0.0, score), violations, recommendations

    def _assess_fairness(
        self,
        data: Any,
        context: Dict[str, Any],
    ) -> tuple[float, List[str], List[str]]:
        """Assess fairness compliance."""
        score = 0.85
        violations: List[str] = []
        recommendations: List[str] = []

        # Check bias in data
        if isinstance(data, dict) and "demographics" in data:
            demographics = data["demographics"]
            if len(set(demographics.values())) < 2:
                violations.append("Falta de diversidade demográfica")
                score -= 0.2

        if violations:
            recommendations.append("Garantir diversidade nos dados de treinamento")

        return max(0.0, score), violations, recommendations

    def _assess_transparency(
        self,
        data: Any,
        context: Dict[str, Any],
    ) -> tuple[float, List[str], List[str]]:
        """Assess transparency compliance."""
        score = 0.8
        violations: List[str] = []
        recommendations: List[str] = []

        # Check if decisions are explainable
        if not context.get("explanation_provided", False):
            violations.append("Decisão sem explicação")
            score -= 0.3

        if violations:
            recommendations.append("Fornecer explicações para decisões automatizadas")

        return max(0.0, score), violations, recommendations

    def _calculate_overall_score(
        self,
        assessments: List[EthicalAssessment],
    ) -> float:
        """Calculate overall compliance score."""
        if not assessments:
            return 1.0

        weighted_scores = []
        for assessment in assessments:
            rule = next(
                (r for r in self.universal_rules if r.rule_id == assessment.rule_id),
                None,
            )
            if rule:
                weight = self._get_compliance_weight(rule.compliance_level)
                weighted_scores.append(assessment.compliance_score * weight)

        return (
            sum(weighted_scores) / len(weighted_scores) if weighted_scores else 0.0
        )

    def _get_compliance_weight(
        self,
        level: EthicalComplianceLevel,
    ) -> float:
        """Return weight based on compliance level."""
        weights = {
            EthicalComplianceLevel.CRITICAL: 1.0,
            EthicalComplianceLevel.HIGH: 0.8,
            EthicalComplianceLevel.MEDIUM: 0.6,
            EthicalComplianceLevel.LOW: 0.4,
            EthicalComplianceLevel.OPTIONAL: 0.2,
        }
        return weights.get(level, 0.5)

    def _identify_critical_violations(
        self,
        assessments: List[EthicalAssessment],
    ) -> List[str]:
        """Identify critical violations."""
        critical_violations = []

        for assessment in assessments:
            if assessment.risk_level == "critical" and assessment.violations:
                critical_violations.extend(assessment.violations)

        return critical_violations

    def _generate_recommendations(
        self,
        assessments: List[EthicalAssessment],
    ) -> List[str]:
        """Generate recommendations based on assessments."""
        recommendations = []

        for assessment in assessments:
            recommendations.extend(assessment.recommendations)

        # Remove duplicates
        return list(set(recommendations))

    def _determine_risk_level(
        self,
        overall_score: float,
        critical_violations: List[str],
    ) -> str:
        """Determine overall risk level."""
        if critical_violations:
            return "critical"
        elif overall_score < 0.5:
            return "high"
        elif overall_score < 0.7:
            return "medium"
        else:
            return "low"

    def _determine_rule_risk_level(
        self,
        score: float,
        compliance_level: EthicalComplianceLevel,
    ) -> str:
        """Determine risk level for a specific rule."""
        if compliance_level == EthicalComplianceLevel.CRITICAL and score < 0.8:
            return "critical"
        elif compliance_level == EthicalComplianceLevel.HIGH and score < 0.7:
            return "high"
        elif score < 0.6:
            return "medium"
        else:
            return "low"

    def get_compliance_metrics(self) -> Dict[str, Any]:
        """Return compliance metrics."""
        if not self.compliance_history:
            return {"no_data": True}

        recent_assessments = self.compliance_history[-100:]

        return {
            "total_assessments": len(self.compliance_history),
            "recent_assessments": len(recent_assessments),
            "average_score": (
                sum(a.compliance_score for a in recent_assessments)
                / len(recent_assessments)
                if recent_assessments
                else 0.0
            ),
            "critical_violations": sum(
                1 for a in recent_assessments if a.risk_level == "critical"
            ),
            "domains_covered": len(self.domain_engines),
            "universal_rules": len(self.universal_rules),
        }

