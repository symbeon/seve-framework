"""Domain adapters migrated from the legacy SEVE-Universal implementation."""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

from .core import DomainAdapter, DomainType, UniversalContext

logger = logging.getLogger(__name__)


class HealthcareAdapter(DomainAdapter):
    def adapt_to_context(self, context: UniversalContext) -> UniversalContext:
        context.metadata.update(
            {
                "medical_privacy": True,
                "hipaa_compliance": True,
                "patient_safety": True,
                "clinical_context": True,
            }
        )
        return context

    def extract_domain_features(self, data: Any) -> Dict[str, Any]:
        return {
            "medical_data": data,
            "patient_id": data.get("patient_id") if isinstance(data, dict) else None,
            "medical_history": data.get("history", []) if isinstance(data, dict) else [],
            "vital_signs": data.get("vitals", {}) if isinstance(data, dict) else {},
            "diagnosis": data.get("diagnosis") if isinstance(data, dict) else None,
            "treatment_plan": data.get("treatment") if isinstance(data, dict) else None,
        }

    def apply_domain_rules(self, decision: Any) -> Any:
        return {
            "medical_decision": decision,
            "safety_check": True,
            "privacy_protected": True,
        }


class EducationAdapter(DomainAdapter):
    def adapt_to_context(self, context: UniversalContext) -> UniversalContext:
        context.metadata.update(
            {
                "learning_objectives": True,
                "student_privacy": True,
                "educational_standards": True,
                "pedagogical_context": True,
            }
        )
        return context

    def extract_domain_features(self, data: Any) -> Dict[str, Any]:
        return {
            "student_data": data,
            "learning_style": data.get("learning_style") if isinstance(data, dict) else None,
            "academic_level": data.get("level") if isinstance(data, dict) else None,
            "subject_matter": data.get("subject") if isinstance(data, dict) else None,
            "learning_progress": data.get("progress", {}) if isinstance(data, dict) else {},
            "assessment_results": data.get("assessments", []) if isinstance(data, dict) else [],
        }

    def apply_domain_rules(self, decision: Any) -> Any:
        return {
            "educational_decision": decision,
            "pedagogical_appropriate": True,
            "student_centered": True,
        }


class BusinessAdapter(DomainAdapter):
    def adapt_to_context(self, context: UniversalContext) -> UniversalContext:
        context.metadata.update(
            {
                "business_objectives": True,
                "corporate_compliance": True,
                "performance_metrics": True,
                "organizational_context": True,
            }
        )
        return context

    def extract_domain_features(self, data: Any) -> Dict[str, Any]:
        return {
            "business_data": data,
            "employee_profile": data.get("employee") if isinstance(data, dict) else None,
            "department": data.get("department") if isinstance(data, dict) else None,
            "role": data.get("role") if isinstance(data, dict) else None,
            "performance_metrics": data.get("metrics", {}) if isinstance(data, dict) else {},
            "organizational_goals": data.get("goals", []) if isinstance(data, dict) else [],
        }

    def apply_domain_rules(self, decision: Any) -> Any:
        return {
            "business_decision": decision,
            "aligned_with_goals": True,
            "performance_optimized": True,
        }


class SmartCityAdapter(DomainAdapter):
    def adapt_to_context(self, context: UniversalContext) -> UniversalContext:
        context.metadata.update(
            {
                "urban_planning": True,
                "citizen_privacy": True,
                "sustainability": True,
                "civic_context": True,
            }
        )
        return context

    def extract_domain_features(self, data: Any) -> Dict[str, Any]:
        return {
            "city_data": data,
            "citizen_profile": data.get("citizen") if isinstance(data, dict) else None,
            "location": data.get("location") if isinstance(data, dict) else None,
            "urban_services": data.get("services", []) if isinstance(data, dict) else [],
            "environmental_data": data.get("environment", {}) if isinstance(data, dict) else {},
            "traffic_patterns": data.get("traffic", {}) if isinstance(data, dict) else {},
        }

    def apply_domain_rules(self, decision: Any) -> Any:
        return {
            "urban_decision": decision,
            "sustainable": True,
            "citizen_centered": True,
        }


class GamingAdapter(DomainAdapter):
    def adapt_to_context(self, context: UniversalContext) -> UniversalContext:
        context.metadata.update(
            {
                "game_mechanics": True,
                "player_privacy": True,
                "entertainment_value": True,
                "immersive_context": True,
            }
        )
        return context

    def extract_domain_features(self, data: Any) -> Dict[str, Any]:
        return {
            "game_data": data,
            "player_profile": data.get("player") if isinstance(data, dict) else None,
            "game_state": data.get("state") if isinstance(data, dict) else None,
            "player_behavior": data.get("behavior", {}) if isinstance(data, dict) else {},
            "game_progress": data.get("progress", {}) if isinstance(data, dict) else {},
            "social_interactions": data.get("social", []) if isinstance(data, dict) else [],
        }

    def apply_domain_rules(self, decision: Any) -> Any:
        return {
            "game_decision": decision,
            "engaging": True,
            "balanced": True,
        }


class RetailAdapter(DomainAdapter):
    def adapt_to_context(self, context: UniversalContext) -> UniversalContext:
        context.metadata.update(
            {
                "customer_privacy": True,
                "purchase_behavior": True,
                "inventory_management": True,
                "retail_context": True,
                "esg_compliance": True,
            }
        )
        return context

    def extract_domain_features(self, data: Any) -> Dict[str, Any]:
        return {
            "retail_data": data,
            "customer_profile": data.get("customer") if isinstance(data, dict) else None,
            "product_catalog": data.get("products", []) if isinstance(data, dict) else [],
            "purchase_history": data.get("history", []) if isinstance(data, dict) else [],
            "inventory_status": data.get("inventory", {}) if isinstance(data, dict) else {},
            "esg_scores": data.get("esg", {}) if isinstance(data, dict) else {},
            "transaction_context": data.get("transaction", {}) if isinstance(data, dict) else {},
        }

    def apply_domain_rules(self, decision: Any) -> Any:
        return {
            "retail_decision": decision,
            "customer_centered": True,
            "esg_compliant": True,
            "inventory_optimized": True,
        }


class FinanceAdapter(DomainAdapter):
    def adapt_to_context(self, context: UniversalContext) -> UniversalContext:
        context.metadata.update(
            {
                "financial_privacy": True,
                "regulatory_compliance": True,
                "risk_management": True,
                "financial_context": True,
            }
        )
        return context

    def extract_domain_features(self, data: Any) -> Dict[str, Any]:
        return {
            "financial_data": data,
            "client_profile": data.get("client") if isinstance(data, dict) else None,
            "transaction_history": data.get("transactions", []) if isinstance(data, dict) else [],
            "risk_assessment": data.get("risk", {}) if isinstance(data, dict) else {},
            "compliance_status": data.get("compliance", {}) if isinstance(data, dict) else {},
            "financial_goals": data.get("goals", []) if isinstance(data, dict) else [],
        }

    def apply_domain_rules(self, decision: Any) -> Any:
        return {
            "financial_decision": decision,
            "risk_assessed": True,
            "compliant": True,
            "client_protected": True,
        }


class ManufacturingAdapter(DomainAdapter):
    def adapt_to_context(self, context: UniversalContext) -> UniversalContext:
        context.metadata.update(
            {
                "industrial_safety": True,
                "quality_control": True,
                "sustainability": True,
                "manufacturing_context": True,
            }
        )
        return context

    def extract_domain_features(self, data: Any) -> Dict[str, Any]:
        return {
            "manufacturing_data": data,
            "production_line": data.get("production") if isinstance(data, dict) else None,
            "quality_metrics": data.get("quality", {}) if isinstance(data, dict) else {},
            "safety_standards": data.get("safety", {}) if isinstance(data, dict) else {},
            "environmental_impact": data.get("environment", {}) if isinstance(data, dict) else {},
            "efficiency_metrics": data.get("efficiency", {}) if isinstance(data, dict) else {},
        }

    def apply_domain_rules(self, decision: Any) -> Any:
        return {
            "manufacturing_decision": decision,
            "quality_assured": True,
            "safety_compliant": True,
            "sustainable": True,
        }


class UniversalAdapterRegistry:
    """Helper registry that instantiates built-in adapters."""

    def __init__(self) -> None:
        self._adapters = {
            DomainType.HEALTHCARE: HealthcareAdapter(),
            DomainType.EDUCATION: EducationAdapter(),
            DomainType.BUSINESS: BusinessAdapter(),
            DomainType.SMART_CITY: SmartCityAdapter(),
            DomainType.GAMING: GamingAdapter(),
            DomainType.RETAIL: RetailAdapter(),
            DomainType.FINANCE: FinanceAdapter(),
            DomainType.MANUFACTURING: ManufacturingAdapter(),
        }
        self._custom_adapters: Dict[str, DomainAdapter] = {}

    def get_adapter(self, domain: DomainType) -> Optional[DomainAdapter]:
        return self._adapters.get(domain)

    def register_custom_adapter(self, name: str, adapter: DomainAdapter) -> None:
        self._custom_adapters[name] = adapter
        logger.info("Adaptador customizado registrado: %s", name)

    def get_custom_adapter(self, name: str) -> Optional[DomainAdapter]:
        return self._custom_adapters.get(name)

    def list_available_domains(self) -> List[DomainType]:
        return list(self._adapters.keys())

    def get_adapter_info(self, domain: DomainType) -> Dict[str, Any]:
        adapter = self._adapters.get(domain)
        if not adapter:
            return {}
        return {
            "domain": domain.value,
            "adapter_class": adapter.__class__.__name__,
            "capabilities": _get_adapter_capabilities(adapter),
        }


def _get_adapter_capabilities(adapter: DomainAdapter) -> List[str]:
    if isinstance(adapter, HealthcareAdapter):
        return ["medical_privacy", "hipaa_compliance", "patient_safety"]
    if isinstance(adapter, EducationAdapter):
        return ["learning_adaptation", "student_privacy", "pedagogical_support"]
    if isinstance(adapter, BusinessAdapter):
        return ["business_optimization", "corporate_compliance", "performance_metrics"]
    if isinstance(adapter, SmartCityAdapter):
        return ["urban_planning", "citizen_privacy", "sustainability"]
    if isinstance(adapter, GamingAdapter):
        return ["game_mechanics", "player_privacy", "entertainment_value"]
    if isinstance(adapter, RetailAdapter):
        return [
            "customer_privacy",
            "purchase_behavior",
            "esg_compliance",
            "inventory_management",
        ]
    if isinstance(adapter, FinanceAdapter):
        return ["financial_privacy", "regulatory_compliance", "risk_management"]
    if isinstance(adapter, ManufacturingAdapter):
        return ["industrial_safety", "quality_control", "sustainability", "efficiency_optimization"]
    return []

