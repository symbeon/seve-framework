"""Universal adaptive components for the SEVE Framework.

This package consolidates the legacy SEVE-Universal implementation inside the
modern v1.0.0 codebase, exposing domain adapters, the universal core, empathy
engine and ethics engine so that the hybrid runtime can operate without
external dependencies.
"""

from .core import (
    SEVEUniversalCore,
    DomainAdapter,
    DomainAdapterRegistry,
    DomainConfig,
    DomainType,
    UniversalContext,
    UniversalContextManager,
    UniversalLearningModule,
)
from .adapters import UniversalAdapterRegistry
from .empathy import (
    UniversalEmpathyEngine,
    DomainEmpathyEngine,
    EmpathyContext,
    EmpathyResponse,
    EmpathyType,
    EmotionalState,
)
from .ethics import (
    DomainEthicsEngine,
    EthicalAssessment,
    EthicalComplianceLevel,
    EthicalPrinciple,
    EthicalRule,
    UniversalEthicsEngine,
)

__all__ = [
    "SEVEUniversalCore",
    "DomainAdapter",
    "DomainAdapterRegistry",
    "DomainConfig",
    "DomainType",
    "UniversalContext",
    "UniversalContextManager",
    "UniversalLearningModule",
    "UniversalAdapterRegistry",
    "UniversalEmpathyEngine",
    "DomainEmpathyEngine",
    "EmpathyContext",
    "EmpathyResponse",
    "EmpathyType",
    "EmotionalState",
    "UniversalEthicsEngine",
    "DomainEthicsEngine",
    "EthicalAssessment",
    "EthicalComplianceLevel",
    "EthicalPrinciple",
    "EthicalRule",
]

