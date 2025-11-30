"""
SEVE Universal - Universal Adaptive Intelligence Engine

Framework de IA adaptativa universal que transcende contextos específicos,
oferecendo capacidades de personalização, empatia e ética para qualquer domínio.
"""

from .core import (
    SEVEUniversalCore,
    DomainConfig,
    DomainType,
    UniversalContext,
    AdaptationLevel
)

from .adapters import (
    UniversalAdapterRegistry,
    HealthcareAdapter,
    EducationAdapter,
    BusinessAdapter,
    SmartCityAdapter,
    GamingAdapter,
    RetailAdapter,
    FinanceAdapter,
    ManufacturingAdapter
)

from .ethics import (
    UniversalEthicsEngine,
    EthicalPrinciple,
    EthicalComplianceLevel,
    EthicalRule,
    EthicalAssessment
)

from .empathy import (
    UniversalEmpathyEngine,
    EmpathyType,
    EmotionalState,
    EmpathyContext,
    EmpathyResponse
)

__version__ = "1.0.0"
__author__ = "SEVE Universal Team"
__email__ = "research@seve-universal.ai"

__all__ = [
    # Core components
    "SEVEUniversalCore",
    "DomainConfig", 
    "DomainType",
    "UniversalContext",
    "AdaptationLevel",
    
    # Adapters
    "UniversalAdapterRegistry",
    "HealthcareAdapter",
    "EducationAdapter", 
    "BusinessAdapter",
    "SmartCityAdapter",
    "GamingAdapter",
    "RetailAdapter",
    "FinanceAdapter",
    "ManufacturingAdapter",
    
    # Ethics
    "UniversalEthicsEngine",
    "EthicalPrinciple",
    "EthicalComplianceLevel",
    "EthicalRule",
    "EthicalAssessment",
    
    # Empathy
    "UniversalEmpathyEngine",
    "EmpathyType",
    "EmotionalState",
    "EmpathyContext",
    "EmpathyResponse"
]
