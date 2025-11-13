"""Universal adaptive core for the SEVE Framework.

This module was migrated from the legacy SEVE-Universal implementation and
provides domain adaptation, transfer learning and context management features
that can operate across different industries.
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class DomainType(Enum):
    """Supported domain types."""

    HEALTHCARE = "healthcare"
    EDUCATION = "education"
    BUSINESS = "business"
    SMART_CITY = "smart_city"
    GAMING = "gaming"
    RETAIL = "retail"
    FINANCE = "finance"
    MANUFACTURING = "manufacturing"
    CUSTOM = "custom"


class AdaptationLevel(Enum):
    """Levels of adaptation."""

    BASIC = "basic"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"


@dataclass
class DomainConfig:
    """Domain configuration descriptor."""

    domain_type: DomainType
    domain_name: str
    cultural_context: str = "global"
    adaptation_level: AdaptationLevel = AdaptationLevel.INTERMEDIATE
    ethical_rules: List[str] = field(default_factory=list)
    personalization_rules: List[str] = field(default_factory=list)
    empathy_rules: List[str] = field(default_factory=list)
    custom_adapters: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class UniversalContext:
    """Runtime context transported across domains."""

    domain: DomainType
    user_profile: Dict[str, Any]
    environmental_data: Dict[str, Any]
    cultural_context: str
    temporal_context: Dict[str, Any]
    metadata: Dict[str, Any]


class DomainAdapter(ABC):
    """Base contract for domain adapters."""

    @abstractmethod
    def adapt_to_context(self, context: UniversalContext) -> UniversalContext:
        """Adapt context for a specific domain."""

    @abstractmethod
    def extract_domain_features(self, data: Any) -> Dict[str, Any]:
        """Extract domain specific features from data."""

    @abstractmethod
    def apply_domain_rules(self, decision: Any) -> Any:
        """Apply domain specific rules to a decision."""


class DomainAdapterRegistry:
    """Registry of available domain adapters."""

    def __init__(self) -> None:
        self._adapters: Dict[DomainType, DomainAdapter] = {}
        self._custom_adapters: Dict[str, DomainAdapter] = {}

    def register_adapter(self, domain: DomainType, adapter: DomainAdapter) -> None:
        self._adapters[domain] = adapter
        logger.info("Adaptador registrado para domínio: %s", domain.value)

    def register_custom_adapter(self, name: str, adapter: DomainAdapter) -> None:
        self._custom_adapters[name] = adapter
        logger.info("Adaptador customizado registrado: %s", name)

    def get_adapter(self, domain: DomainType) -> Optional[DomainAdapter]:
        return self._adapters.get(domain)

    def get_custom_adapter(self, name: str) -> Optional[DomainAdapter]:
        return self._custom_adapters.get(name)


class SEVEUniversalCore:
    """Universal orchestration engine for adaptive scenarios."""

    def __init__(self, config: DomainConfig):
        self.config = config
        self.domain_adapter_registry = DomainAdapterRegistry()
        self.knowledge_graph: Dict[str, Any] = {}
        self.learning_module = UniversalLearningModule()
        self.context_manager = UniversalContextManager()
        self._initialize_components()

    def _initialize_components(self) -> None:
        self._load_default_adapters()
        self._load_custom_adapters()
        self._initialize_domain_modules()
        register_default_adapters(self.domain_adapter_registry)

    def _load_default_adapters(self) -> None:
        # Adapters are registered explicitly via UniversalAdapterRegistry helper
        pass

    def _load_custom_adapters(self) -> None:
        for adapter_name in self.config.custom_adapters:
            _ = adapter_name  # Placeholder for loading logic

    def _initialize_domain_modules(self) -> None:
        # Placeholder for domain specific initialization hooks
        pass

    async def process_universal_context(
        self,
        context: UniversalContext,
        data: Any,
    ) -> Dict[str, Any]:
        adapter = self.domain_adapter_registry.get_adapter(context.domain)
        adapted_context = adapter.adapt_to_context(context) if adapter else context
        domain_features = (
            adapter.extract_domain_features(data) if adapter else {"raw_data": data}
        )
        domain_result = (
            adapter.apply_domain_rules(domain_features) if adapter else domain_features
        )
        learning_result = await self.learning_module.update_knowledge(
            domain_result, adapted_context
        )
        return {
            "domain_result": domain_result,
            "learning_result": learning_result,
            "adapted_context": adapted_context,
            "domain_features": domain_features,
        }

    def switch_domain(self, new_config: DomainConfig) -> None:
        self.config = new_config
        self._initialize_components()
        logger.info("Domínio alterado para: %s", new_config.domain_type.value)

    def get_domain_metrics(self) -> Dict[str, Any]:
        return {
            "domain": self.config.domain_type.value,
            "adaptation_level": self.config.adaptation_level.value,
            "cultural_context": self.config.cultural_context,
            "registered_adapters": len(self.domain_adapter_registry._adapters),
            "custom_adapters": len(self.domain_adapter_registry._custom_adapters),
        }


class UniversalLearningModule:
    """Transfer learning across domains."""

    def __init__(self) -> None:
        self.knowledge_base: Dict[str, Any] = {}
        self.transfer_learning = TransferLearningEngine()

    async def update_knowledge(
        self,
        result: Dict[str, Any],
        context: UniversalContext,
    ) -> Dict[str, Any]:
        transfer = await self.transfer_learning.apply_transfer(result, context)
        return {"knowledge_updated": True, "transfer_learning": transfer}


class TransferLearningEngine:
    """Cross-domain transfer logic placeholder."""

    async def apply_transfer(
        self,
        result: Dict[str, Any],
        context: UniversalContext,
    ) -> Dict[str, Any]:
        _ = (result, context)
        return {"transfer_applied": True}


class UniversalContextManager:
    """Stores and analyses historical contexts."""

    def __init__(self) -> None:
        self.context_history: List[UniversalContext] = []
        self.context_patterns: Dict[str, Any] = {}

    def store_context(self, context: UniversalContext) -> None:
        self.context_history.append(context)

    def analyze_patterns(self) -> Dict[str, Any]:
        return {"patterns_detected": True}


# Helper for dynamic adapter registration
def register_default_adapters(registry: DomainAdapterRegistry) -> None:
    """Populate the registry with built-in adapters if available."""

    try:
        from .adapters import UniversalAdapterRegistry as _LegacyRegistry

        legacy_registry = _LegacyRegistry()
        for domain in legacy_registry.list_available_domains():
            adapter = legacy_registry.get_adapter(domain)
            if adapter:
                registry.register_adapter(domain, adapter)
    except Exception as exc:  # pragma: no cover - defensive
        logger.warning("Falha ao registrar adaptadores padrão: %s", exc)

