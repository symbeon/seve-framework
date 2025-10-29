"""
SEVE Framework - Symbiotic Ethical Vision Engine
Universal Adaptive Intelligence Framework

This package provides the main SEVE Framework implementation, combining
both Universal adaptive capabilities and v3.0 specific computer vision
functionality.
"""

from .config import SEVEConfig, SEVEMode, PrivacyLevel, EthicsLevel, setup_config
from .core import SEVEHybridFramework, SEVECoreV3, SEVEUniversalCore
from .vision import SEVEVisionModule
from .sense import SEVESenseModule
from .ethics import SEVEEthicsModule
from .link import SEVELinkModule

# Import Universal components
try:
    from seve_universal import (
        SEVEUniversalCore as UniversalCore,
        DomainConfig,
        DomainType,
        UniversalContext,
        AdaptationLevel,
        UniversalAdapterRegistry,
        UniversalEthicsEngine,
        UniversalEmpathyEngine
    )
    UNIVERSAL_AVAILABLE = True
except ImportError:
    UNIVERSAL_AVAILABLE = False
    UniversalCore = None
    DomainConfig = None
    DomainType = None
    UniversalContext = None
    AdaptationLevel = None
    UniversalAdapterRegistry = None
    UniversalEthicsEngine = None
    UniversalEmpathyEngine = None

__version__ = "1.0.0"
__author__ = "Symbeon Tech - EON Team"
__email__ = "research@symbeon-tech.com"
__license__ = "Symbeon-Vault"

__all__ = [
    # Core Framework
    "SEVEHybridFramework",
    "SEVECoreV3", 
    "SEVEUniversalCore",
    
    # Modules
    "SEVEVisionModule",
    "SEVESenseModule", 
    "SEVEEthicsModule",
    "SEVELinkModule",
    
    # Configuration
    "SEVEConfig",
    "SEVEMode",
    "PrivacyLevel", 
    "EthicsLevel",
    "setup_config",
    
    # Universal Components (if available)
    "UniversalCore",
    "DomainConfig",
    "DomainType", 
    "UniversalContext",
    "AdaptationLevel",
    "UniversalAdapterRegistry",
    "UniversalEthicsEngine",
    "UniversalEmpathyEngine",
    
    # Metadata
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "UNIVERSAL_AVAILABLE"
]

def get_version() -> str:
    """Get SEVE Framework version"""
    return __version__

def get_capabilities() -> dict:
    """Get framework capabilities"""
    capabilities = {
        "version": __version__,
        "universal_available": UNIVERSAL_AVAILABLE,
        "modes": [mode.value for mode in SEVEMode],
        "privacy_levels": [level.value for level in PrivacyLevel],
        "ethics_levels": [level.value for level in EthicsLevel],
        "modules": [
            "SEVEVisionModule",
            "SEVESenseModule", 
            "SEVEEthicsModule",
            "SEVELinkModule"
        ]
    }
    
    if UNIVERSAL_AVAILABLE:
        capabilities["universal_components"] = [
            "SEVEUniversalCore",
            "DomainConfig",
            "UniversalEthicsEngine",
            "UniversalEmpathyEngine"
        ]
    
    return capabilities

def create_framework(config: SEVEConfig) -> SEVEHybridFramework:
    """Create SEVE Framework instance with given configuration"""
    return SEVEHybridFramework(config)

def create_universal_framework(domain_config: DomainConfig) -> UniversalCore:
    """Create Universal Framework instance (if available)"""
    if not UNIVERSAL_AVAILABLE:
        raise ImportError("Universal components not available. Install seve-universal package.")
    
    return UniversalCore(domain_config)

# Framework initialization
def initialize_framework(config_path: str = None) -> SEVEHybridFramework:
    """Initialize SEVE Framework with configuration"""
    config = setup_config(config_path)
    return create_framework(config)

# Demo function
def run_demo():
    """Run SEVE Framework demonstration"""
    print("🤖 SEVE Framework - Symbiotic Ethical Vision Engine")
    print(f"Version: {__version__}")
    print(f"Author: {__author__}")
    print(f"License: {__license__}")
    print()
    
    capabilities = get_capabilities()
    print("📊 Framework Capabilities:")
    for key, value in capabilities.items():
        print(f"  {key}: {value}")
    print()
    
    print("🚀 Initializing SEVE Framework...")
    try:
        framework = initialize_framework()
        print("✅ SEVE Framework initialized successfully!")
        print(f"Mode: {framework.config.mode.value}")
        print(f"Privacy Level: {framework.config.privacy_level.value}")
        print(f"Ethics Level: {framework.config.ethics_level.value}")
    except Exception as e:
        print(f"❌ Error initializing framework: {e}")
    
    print()
    print("🌍 Ready to transform AI with ethical intelligence!")

if __name__ == "__main__":
    run_demo()
