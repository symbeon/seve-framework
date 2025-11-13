"""
SEVE Ethics Module - GuardFlow Ethical Validation
Symbiotic Ethical Vision Engine

This module implements the SEVE-Ethics component, providing
real-time ethical validation and decision oversight through
the GuardFlow system.
"""

import asyncio
import logging
import time
import json
from typing import Dict, List, Any, Optional, Union, Tuple
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime

from .config import SEVEConfig, EthicsLevel

# Import Universal Ethics Engine if available
try:
    from .universal.ethics import UniversalEthicsEngine
    UNIVERSAL_ETHICS_AVAILABLE = True
except ImportError:
    UNIVERSAL_ETHICS_AVAILABLE = False
    UniversalEthicsEngine = None

logger = logging.getLogger(__name__)

class EthicalPrinciple(Enum):
    """Core ethical principles"""
    PRIVACY = "privacy"
    FAIRNESS = "fairness"
    TRANSPARENCY = "transparency"
    ACCOUNTABILITY = "accountability"
    HUMAN_AUTONOMY = "human_autonomy"
    SAFETY = "safety"
    SUSTAINABILITY = "sustainability"
    NON_DISCRIMINATION = "non_discrimination"
    BENEFICENCE = "beneficence"
    NON_MALEFICENCE = "non_maleficence"

class ComplianceLevel(Enum):
    """Levels of ethical compliance"""
    CRITICAL = "critical"      # Must comply, no exceptions
    HIGH = "high"             # Strong recommendation, minor exceptions with justification
    MEDIUM = "medium"         # Recommended, flexible
    LOW = "low"              # Optional, good practice

class ValidationResult(Enum):
    """Results of ethical validation"""
    APPROVED = "approved"
    BLOCKED = "blocked"
    REQUIRES_REVIEW = "requires_review"
    MODIFIED = "modified"

@dataclass
class EthicalRule:
    """Represents an ethical rule"""
    name: str
    principle: EthicalPrinciple
    description: str
    compliance_level: ComplianceLevel
    conditions: Dict[str, Any] = field(default_factory=dict)
    mitigation_actions: List[str] = field(default_factory=list)
    weight: float = 1.0

@dataclass
class EthicalAssessment:
    """Result of ethical assessment"""
    rule_name: str
    principle: EthicalPrinciple
    result: ValidationResult
    confidence: float
    reason: str
    suggested_mitigation: Optional[str] = None
    timestamp: float = field(default_factory=time.time)
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class GuardFlowResult:
    """Result of GuardFlow validation"""
    overall_result: ValidationResult
    assessments: List[EthicalAssessment]
    processing_time_ms: float = 0.0
    confidence_score: float = 0.0
    mitigation_applied: List[str] = field(default_factory=list)
    audit_trail: List[Dict[str, Any]] = field(default_factory=list)

class SEVEEthicsModule:
    """
    SEVE Ethics Module
    
    Implements the GuardFlow system for real-time ethical validation
    of all decisions and actions in the SEVE Framework.
    """
    
    def __init__(self, config: SEVEConfig):
        self.config = config
        self.is_initialized = False
        
        # Ethics configuration
        self.ethics_level = config.ethics_level
        self.guardflow_enabled = config.guardflow_enabled
        self.audit_logging_enabled = config.audit_logging_enabled
        
        # Ethical rules and policies
        self.ethical_rules: List[EthicalRule] = []
        self.policy_weights: Dict[EthicalPrinciple, float] = {}
        
        # Audit trail
        self.audit_trail: List[Dict[str, Any]] = []
        
        # Decision history for learning
        self.decision_history: List[Dict[str, Any]] = []
        
        # Universal Ethics Engine (optional integration)
        self.universal_ethics_engine: Optional[Any] = None
        if UNIVERSAL_ETHICS_AVAILABLE and config.mode.value in ["universal", "hybrid"]:
            try:
                self.universal_ethics_engine = UniversalEthicsEngine()
                logger.info("Universal Ethics Engine integrated with GuardFlow")
            except Exception as e:
                logger.warning(f"Could not initialize Universal Ethics Engine: {e}")
        
        logger.info(f"SEVE Ethics Module initialized with level: {self.ethics_level.value}")
    
    async def initialize(self) -> None:
        """Initialize ethics module and load rules"""
        try:
            # Load ethical rules
            await self._load_ethical_rules()
            
            # Initialize policy weights
            await self._initialize_policy_weights()
            
            # Load audit configuration
            await self._load_audit_config()
            
            self.is_initialized = True
            logger.info("SEVE Ethics Module fully initialized")
            
        except Exception as e:
            logger.error(f"Error initializing SEVE Ethics Module: {e}")
            raise
    
    async def _load_ethical_rules(self) -> None:
        """Load ethical rules based on configuration"""
        # Base ethical rules
        base_rules = [
            EthicalRule(
                name="Privacy_FacialRecognition_Consent",
                principle=EthicalPrinciple.PRIVACY,
                description="Facial recognition data should not be stored without explicit consent",
                compliance_level=ComplianceLevel.CRITICAL,
                conditions={
                    "data_type": "facial_recognition",
                    "action": "store",
                    "consent_given": False
                },
                mitigation_actions=["anonymize_data", "block_storage", "request_consent"]
            ),
            EthicalRule(
                name="Fairness_BiasDetection",
                principle=EthicalPrinciple.FAIRNESS,
                description="Detect and mitigate algorithmic bias in decision-making",
                compliance_level=ComplianceLevel.HIGH,
                conditions={"has_bias_risk": True},
                mitigation_actions=["adjust_algorithm", "human_review", "bias_correction"]
            ),
            EthicalRule(
                name="Safety_HazardDetection_Alert",
                principle=EthicalPrinciple.SAFETY,
                description="Critical safety hazards must trigger immediate alerts",
                compliance_level=ComplianceLevel.CRITICAL,
                conditions={"hazard_detected": True, "severity": "critical"},
                mitigation_actions=["trigger_alarm", "notify_authorities", "emergency_stop"]
            ),
            EthicalRule(
                name="Transparency_DecisionExplanation",
                principle=EthicalPrinciple.TRANSPARENCY,
                description="All decisions must be explainable and auditable",
                compliance_level=ComplianceLevel.MEDIUM,
                conditions={"decision_made": True},
                mitigation_actions=["generate_explanation", "log_decision", "audit_trail"]
            ),
            EthicalRule(
                name="NonDiscrimination_ProtectedAttributes",
                principle=EthicalPrinciple.NON_DISCRIMINATION,
                description="Decisions must not discriminate based on protected attributes",
                compliance_level=ComplianceLevel.CRITICAL,
                conditions={"uses_protected_attributes": True},
                mitigation_actions=["remove_protected_attributes", "fairness_testing", "human_review"]
            ),
            EthicalRule(
                name="HumanAutonomy_OverrideCapability",
                principle=EthicalPrinciple.HUMAN_AUTONOMY,
                description="Humans must be able to override AI decisions",
                compliance_level=ComplianceLevel.HIGH,
                conditions={"ai_decision": True},
                mitigation_actions=["enable_override", "human_confirmation", "manual_control"]
            )
        ]
        
        # Add rules based on ethics level
        if self.ethics_level == EthicsLevel.BASIC:
            self.ethical_rules = [rule for rule in base_rules if rule.compliance_level == ComplianceLevel.CRITICAL]
        elif self.ethics_level == EthicsLevel.STANDARD:
            self.ethical_rules = [rule for rule in base_rules if rule.compliance_level in [ComplianceLevel.CRITICAL, ComplianceLevel.HIGH]]
        elif self.ethics_level == EthicsLevel.STRICT:
            self.ethical_rules = [rule for rule in base_rules if rule.compliance_level in [ComplianceLevel.CRITICAL, ComplianceLevel.HIGH, ComplianceLevel.MEDIUM]]
        else:  # MAXIMUM
            self.ethical_rules = base_rules
        
        logger.info(f"Loaded {len(self.ethical_rules)} ethical rules for level {self.ethics_level.value}")
    
    async def _initialize_policy_weights(self) -> None:
        """Initialize policy weights based on ethics level"""
        # Base weights
        base_weights = {
            EthicalPrinciple.PRIVACY: 1.0,
            EthicalPrinciple.SAFETY: 1.0,
            EthicalPrinciple.FAIRNESS: 0.9,
            EthicalPrinciple.NON_DISCRIMINATION: 1.0,
            EthicalPrinciple.HUMAN_AUTONOMY: 0.8,
            EthicalPrinciple.TRANSPARENCY: 0.7,
            EthicalPrinciple.ACCOUNTABILITY: 0.7,
            EthicalPrinciple.SUSTAINABILITY: 0.6,
            EthicalPrinciple.BENEFICENCE: 0.8,
            EthicalPrinciple.NON_MALEFICENCE: 0.9
        }
        
        # Adjust weights based on ethics level
        if self.ethics_level == EthicsLevel.BASIC:
            # Focus on critical principles
            self.policy_weights = {k: v if k in [EthicalPrinciple.PRIVACY, EthicalPrinciple.SAFETY, EthicalPrinciple.NON_DISCRIMINATION] else v * 0.5 for k, v in base_weights.items()}
        elif self.ethics_level == EthicsLevel.STANDARD:
            # Standard weights
            self.policy_weights = base_weights
        elif self.ethics_level == EthicsLevel.STRICT:
            # Increased weights for all principles
            self.policy_weights = {k: v * 1.2 for k, v in base_weights.items()}
        else:  # MAXIMUM
            # Maximum weights
            self.policy_weights = {k: v * 1.5 for k, v in base_weights.items()}
        
        logger.info(f"Policy weights initialized for ethics level {self.ethics_level.value}")
    
    async def _load_audit_config(self) -> None:
        """Load audit configuration"""
        # Audit configuration based on ethics level
        if self.ethics_level in [EthicsLevel.STRICT, EthicsLevel.MAXIMUM]:
            self.audit_logging_enabled = True
        else:
            self.audit_logging_enabled = self.config.audit_logging_enabled
        
        logger.info(f"Audit logging: {'enabled' if self.audit_logging_enabled else 'disabled'}")
    
    async def validate_decision(
        self,
        decision_data: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None,
        use_universal: Optional[bool] = None
    ) -> List[EthicalAssessment]:
        """
        Validate a decision against ethical rules
        
        Args:
            decision_data: Data about the decision to validate
            context: Additional context information
            use_universal: Force use of Universal Ethics Engine (None = auto-detect)
            
        Returns:
            List of ethical assessments
        """
        if not self.is_initialized:
            await self.initialize()
        
        # Determine if we should use Universal Ethics Engine
        should_use_universal = (
            use_universal is not None and use_universal
        ) or (
            use_universal is None
            and self.universal_ethics_engine is not None
            and self.config.mode.value in ["universal", "hybrid"]
        )
        
        assessments = []
        
        # Use Universal Ethics Engine if available and requested
        if should_use_universal and self.universal_ethics_engine:
            try:
                # Get domain from context if available
                domain = None
                if context:
                    domain = context.get("domain") or context.get("domain_type")
                
                # Assess using Universal Ethics Engine
                universal_result = await self.universal_ethics_engine.assess_universal_compliance(
                    decision_data,
                    context or {},
                    domain=domain
                )
                
                # Convert Universal assessments to GuardFlow format
                for universal_assessment_dict in universal_result.get("assessments", []):
                    # Map Universal assessment to GuardFlow format
                    guardflow_assessment = EthicalAssessment(
                        rule_name=universal_assessment_dict.get("rule_id", "universal_rule"),
                        principle=EthicalPrinciple.PRIVACY,  # Default, will be mapped if needed
                        result=ValidationResult.APPROVED if universal_assessment_dict.get("compliance_score", 0) > 0.8 else ValidationResult.REQUIRES_REVIEW,
                        confidence=universal_assessment_dict.get("compliance_score", 0.5),
                        reason=f"Universal assessment: {universal_assessment_dict.get('rule_id', 'unknown')}",
                        suggested_mitigation=universal_result.get("recommendations", [""])[0] if universal_result.get("recommendations") else None,
                        metadata={
                            "source": "universal_ethics_engine",
                            "universal_data": universal_assessment_dict
                        }
                    )
                    assessments.append(guardflow_assessment)
                
                logger.debug(f"Universal Ethics Engine assessed: {len(assessments)} assessments")
            except Exception as e:
                logger.error(f"Error in Universal Ethics Engine assessment: {e}")
                # Fall through to GuardFlow
        
        # Always run GuardFlow for critical policy enforcement
        guardflow_assessments = []
        for rule in self.ethical_rules:
            try:
                assessment = await self._evaluate_rule(rule, decision_data, context)
                guardflow_assessments.append(assessment)
            except Exception as e:
                logger.error(f"Error evaluating rule {rule.name}: {e}")
                continue
        
        # Combine assessments: Universal provides broader context, GuardFlow enforces policies
        # GuardFlow assessments take priority for critical violations
        all_assessments = assessments + guardflow_assessments
        
        # Log audit trail if enabled
        if self.audit_logging_enabled:
            await self._log_audit_trail(decision_data, all_assessments, context)
        
        return all_assessments
    
    async def _evaluate_rule(
        self,
        rule: EthicalRule,
        decision_data: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> EthicalAssessment:
        """Evaluate a single ethical rule"""
        # Check if rule conditions are met
        conditions_met = await self._check_conditions(rule.conditions, decision_data, context)
        
        if not conditions_met:
            # Rule doesn't apply
            return EthicalAssessment(
                rule_name=rule.name,
                principle=rule.principle,
                result=ValidationResult.APPROVED,
                confidence=1.0,
                reason="Rule conditions not met - no violation"
            )
        
        # Rule applies - evaluate compliance
        is_compliant = await self._check_compliance(rule, decision_data, context)
        
        if is_compliant:
            result = ValidationResult.APPROVED
            reason = f"Compliant with {rule.name}"
            suggested_mitigation = None
        else:
            if rule.compliance_level == ComplianceLevel.CRITICAL:
                result = ValidationResult.BLOCKED
                reason = f"Critical violation of {rule.name}: {rule.description}"
            elif rule.compliance_level == ComplianceLevel.HIGH:
                result = ValidationResult.REQUIRES_REVIEW
                reason = f"High priority violation of {rule.name}: {rule.description}"
            else:
                result = ValidationResult.MODIFIED
                reason = f"Moderate violation of {rule.name}: {rule.description}"
            
            suggested_mitigation = rule.mitigation_actions[0] if rule.mitigation_actions else None
        
        return EthicalAssessment(
            rule_name=rule.name,
            principle=rule.principle,
            result=result,
            confidence=rule.weight,
            reason=reason,
            suggested_mitigation=suggested_mitigation,
            metadata={
                "compliance_level": rule.compliance_level.value,
                "rule_weight": rule.weight
            }
        )
    
    async def _check_conditions(
        self,
        conditions: Dict[str, Any],
        decision_data: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> bool:
        """Check if rule conditions are met"""
        for key, expected_value in conditions.items():
            # Check in decision data
            if key in decision_data:
                actual_value = decision_data[key]
                if not self._compare_values(actual_value, expected_value):
                    return False
            
            # Check in context
            elif context and key in context:
                actual_value = context[key]
                if not self._compare_values(actual_value, expected_value):
                    return False
            
            # Check nested conditions
            elif "." in key:
                nested_value = self._get_nested_value(decision_data, key)
                if nested_value is None or not self._compare_values(nested_value, expected_value):
                    return False
            
            else:
                # Condition not found
                return False
        
        return True
    
    def _compare_values(self, actual: Any, expected: Any) -> bool:
        """Compare actual and expected values"""
        if isinstance(expected, bool):
            return bool(actual) == expected
        elif isinstance(expected, str):
            return str(actual).lower() == expected.lower()
        elif isinstance(expected, (int, float)):
            return float(actual) == float(expected)
        elif isinstance(expected, list):
            return actual in expected
        else:
            return actual == expected
    
    def _get_nested_value(self, data: Dict[str, Any], key: str) -> Any:
        """Get nested value from dictionary"""
        keys = key.split(".")
        current = data
        
        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return None
        
        return current
    
    async def _check_compliance(
        self,
        rule: EthicalRule,
        decision_data: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> bool:
        """Check compliance with a specific rule"""
        # This is a simplified implementation
        # In a real system, this would use more sophisticated compliance checking
        
        if rule.name == "Privacy_FacialRecognition_Consent":
            return decision_data.get("consent_given", False)
        
        elif rule.name == "Fairness_BiasDetection":
            return not decision_data.get("has_bias_risk", False)
        
        elif rule.name == "Safety_HazardDetection_Alert":
            return not (decision_data.get("hazard_detected", False) and 
                       decision_data.get("severity") == "critical")
        
        elif rule.name == "Transparency_DecisionExplanation":
            return decision_data.get("explanation_provided", True)
        
        elif rule.name == "NonDiscrimination_ProtectedAttributes":
            return not decision_data.get("uses_protected_attributes", False)
        
        elif rule.name == "HumanAutonomy_OverrideCapability":
            return decision_data.get("override_enabled", True)
        
        # Default to compliant
        return True
    
    async def _log_audit_trail(
        self,
        decision_data: Dict[str, Any],
        assessments: List[EthicalAssessment],
        context: Optional[Dict[str, Any]] = None
    ) -> None:
        """Log audit trail entry"""
        audit_entry = {
            "timestamp": datetime.now().isoformat(),
            "decision_data": decision_data,
            "assessments": [
                {
                    "rule_name": a.rule_name,
                    "principle": a.principle.value,
                    "result": a.result.value,
                    "confidence": a.confidence,
                    "reason": a.reason
                }
                for a in assessments
            ],
            "context": context or {},
            "overall_result": self._determine_overall_result(assessments)
        }
        
        self.audit_trail.append(audit_entry)
        
        # Keep only last 1000 entries to prevent memory issues
        if len(self.audit_trail) > 1000:
            self.audit_trail = self.audit_trail[-1000:]
    
    def _determine_overall_result(self, assessments: List[EthicalAssessment]) -> str:
        """Determine overall validation result"""
        if not assessments:
            return ValidationResult.APPROVED.value
        
        # Check for any blocked decisions
        for assessment in assessments:
            if assessment.result == ValidationResult.BLOCKED:
                return ValidationResult.BLOCKED.value
        
        # Check for any requiring review
        for assessment in assessments:
            if assessment.result == ValidationResult.REQUIRES_REVIEW:
                return ValidationResult.REQUIRES_REVIEW.value
        
        # Check for any modifications
        for assessment in assessments:
            if assessment.result == ValidationResult.MODIFIED:
                return ValidationResult.MODIFIED.value
        
        return ValidationResult.APPROVED.value
    
    async def apply_mitigation(
        self,
        decision_data: Dict[str, Any],
        assessments: List[EthicalAssessment]
    ) -> Dict[str, Any]:
        """Apply mitigation actions based on assessments"""
        modified_data = decision_data.copy()
        mitigation_applied = []
        
        for assessment in assessments:
            if assessment.result in [ValidationResult.BLOCKED, ValidationResult.REQUIRES_REVIEW, ValidationResult.MODIFIED]:
                if assessment.suggested_mitigation:
                    mitigation_result = await self._apply_specific_mitigation(
                        modified_data, assessment.suggested_mitigation
                    )
                    if mitigation_result:
                        mitigation_applied.append(assessment.suggested_mitigation)
        
        modified_data["mitigation_applied"] = mitigation_applied
        return modified_data
    
    async def _apply_specific_mitigation(
        self,
        data: Dict[str, Any],
        mitigation: str
    ) -> bool:
        """Apply a specific mitigation action"""
        if mitigation == "anonymize_data":
            data["anonymized"] = True
            if "facial_recognition_data" in data:
                data["facial_recognition_data"] = "ANONYMIZED"
            return True
        
        elif mitigation == "block_storage":
            data["action"] = "blocked_storage"
            return True
        
        elif mitigation == "request_consent":
            data["consent_required"] = True
            return True
        
        elif mitigation == "adjust_algorithm":
            data["algorithm_adjusted"] = True
            return True
        
        elif mitigation == "human_review":
            data["human_review_required"] = True
            return True
        
        elif mitigation == "trigger_alarm":
            data["alarm_triggered"] = True
            return True
        
        elif mitigation == "notify_authorities":
            data["authorities_notified"] = True
            return True
        
        elif mitigation == "generate_explanation":
            data["explanation_provided"] = True
            return True
        
        elif mitigation == "log_decision":
            data["decision_logged"] = True
            return True
        
        elif mitigation == "remove_protected_attributes":
            data["protected_attributes_removed"] = True
            return True
        
        elif mitigation == "enable_override":
            data["override_enabled"] = True
            return True
        
        return False
    
    def get_audit_trail(self) -> List[Dict[str, Any]]:
        """Get audit trail"""
        return self.audit_trail.copy()
    
    def get_status(self) -> Dict[str, Any]:
        """Get current status of the ethics module"""
        return {
            "initialized": self.is_initialized,
            "ethics_level": self.ethics_level.value,
            "guardflow_enabled": self.guardflow_enabled,
            "audit_logging_enabled": self.audit_logging_enabled,
            "ethical_rules_count": len(self.ethical_rules),
            "audit_trail_entries": len(self.audit_trail),
            "policy_weights": {k.value: v for k, v in self.policy_weights.items()},
            "universal_ethics_engine": {
                "available": self.universal_ethics_engine is not None,
                "enabled": self.universal_ethics_engine is not None and self.config.mode.value in ["universal", "hybrid"],
                "metrics": self.universal_ethics_engine.get_compliance_metrics() if self.universal_ethics_engine else {}
            }
        }

# Demo function
async def run_ethics_demo():
    """Run SEVE Ethics Module demonstration"""
    print("⚖️ SEVE Ethics Module Demo")
    print("=" * 40)
    
    # Create configuration
    config = SEVEConfig(
        ethics_level=EthicsLevel.STRICT,
        guardflow_enabled=True,
        audit_logging_enabled=True
    )
    
    # Create ethics module
    ethics = SEVEEthicsModule(config)
    await ethics.initialize()
    
    print(f"✅ Ethics module initialized")
    print(f"⚖️ Ethics level: {config.ethics_level.value}")
    print(f"🛡️ GuardFlow enabled: {config.guardflow_enabled}")
    print(f"📋 Audit logging: {config.audit_logging_enabled}")
    print(f"📜 Ethical rules loaded: {len(ethics.ethical_rules)}")
    print()
    
    # Demo decision data
    demo_decisions = [
        {
            "name": "Safe Decision",
            "data": {
                "consent_given": True,
                "has_bias_risk": False,
                "hazard_detected": False,
                "explanation_provided": True,
                "uses_protected_attributes": False,
                "override_enabled": True
            }
        },
        {
            "name": "Privacy Violation",
            "data": {
                "data_type": "facial_recognition",
                "action": "store",
                "consent_given": False,
                "has_bias_risk": False,
                "hazard_detected": False
            }
        },
        {
            "name": "Safety Hazard",
            "data": {
                "consent_given": True,
                "has_bias_risk": False,
                "hazard_detected": True,
                "severity": "critical",
                "explanation_provided": True
            }
        }
    ]
    
    for demo in demo_decisions:
        print(f"🔄 Testing: {demo['name']}")
        assessments = await ethics.validate_decision(demo['data'])
        
        print(f"📊 Assessments: {len(assessments)}")
        for assessment in assessments:
            print(f"  {assessment.rule_name}: {assessment.result.value} - {assessment.reason}")
        
        # Apply mitigation if needed
        modified_data = await ethics.apply_mitigation(demo['data'], assessments)
        if modified_data.get("mitigation_applied"):
            print(f"🔧 Mitigation applied: {modified_data['mitigation_applied']}")
        
        print()
    
    print(f"📋 Audit trail entries: {len(ethics.get_audit_trail())}")
    print()
    print("🌍 SEVE Ethics ready for ethical AI validation!")

if __name__ == "__main__":
    asyncio.run(run_ethics_demo())
