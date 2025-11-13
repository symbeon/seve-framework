"""
SEVE Framework - Core Implementation
Symbiotic Ethical Vision Engine

This module implements the core SEVE Framework functionality,
combining Universal adaptive capabilities with v3.0 specific
computer vision features.
"""

import asyncio
import logging
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
import time

from .config import SEVEConfig, SEVEMode, PrivacyLevel, EthicsLevel
from .vision import SEVEVisionModule
from .sense import SEVESenseModule
from .ethics import SEVEEthicsModule
from .link import SEVELinkModule

# Import Universal components from integrated package
try:
    from .universal import (
        SEVEUniversalCore,
        DomainConfig,
        DomainType,
        UniversalContext,
        UniversalEthicsEngine,
        UniversalEmpathyEngine
    )
    UNIVERSAL_AVAILABLE = True
except ImportError as e:
    logger.warning(f"Universal components not available: {e}")
    UNIVERSAL_AVAILABLE = False
    SEVEUniversalCore = None
    DomainConfig = None
    DomainType = None
    UniversalContext = None
    UniversalEthicsEngine = None
    UniversalEmpathyEngine = None

logger = logging.getLogger(__name__)

class ProcessingStatus(Enum):
    """Status of processing operations"""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    ETHICS_BLOCKED = "ethics_blocked"

@dataclass
class ProcessingResult:
    """Result of SEVE processing operation"""
    status: ProcessingStatus
    data: Dict[str, Any]
    metadata: Dict[str, Any] = field(default_factory=dict)
    processing_time_ms: float = 0.0
    ethics_assessments: List[Dict[str, Any]] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

class SEVECoreV3:
    """
    SEVE Core v3.0 - Specific Computer Vision Implementation
    
    Implements the v3.0 architecture with specialized modules
    for computer vision, ethics, and connectivity.
    """
    
    def __init__(self, config: SEVEConfig):
        self.config = config
        self.vision_module = SEVEVisionModule(config)
        self.sense_module = SEVESenseModule(config)
        self.ethics_module = SEVEEthicsModule(config)
        self.link_module = SEVELinkModule(config)
        
        # Processing state
        self.is_initialized = False
        self.processing_count = 0
        
        logger.info(f"SEVE Core v3.0 initialized with mode: {config.mode.value}")
    
    async def initialize(self) -> None:
        """Initialize all modules"""
        try:
            await self.vision_module.initialize()
            await self.sense_module.initialize()
            await self.ethics_module.initialize()
            await self.link_module.initialize()
            
            self.is_initialized = True
            logger.info("SEVE Core v3.0 fully initialized")
        except Exception as e:
            logger.error(f"Error initializing SEVE Core v3.0: {e}")
            raise
    
    async def process_context(
        self,
        input_data: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> ProcessingResult:
        """
        Process data through the v3.0 pipeline
        
        Args:
            input_data: Dictionary containing visual and sensor data
            context: Additional context information
            
        Returns:
            ProcessingResult with status and processed data
        """
        start_time = time.time()
        
        if not self.is_initialized:
            await self.initialize()
        
        try:
            # 1. Process Visual Input
            vision_results = {}
            if "visual" in input_data:
                vision_results = await self.vision_module.process_visual_input(
                    input_data["visual"], context or {}
                )
            
            # 2. Process Sensor Input
            sense_results = {}
            if "sensor" in input_data:
                sense_results = await self.sense_module.process_sensor_input(
                    input_data["sensor"], context or {}
                )
            
            # 3. Fuse Data and Make Decision
            fused_data = {
                "visual": vision_results,
                "sensor": sense_results,
                "context": context or {},
                "timestamp": time.time()
            }
            
            # 4. Ethical Validation (GuardFlow)
            ethics_assessments = await self.ethics_module.validate_decision(fused_data)
            
            # Check if decision is ethically compliant
            is_compliant = all(
                assessment.get("is_compliant", True) 
                for assessment in ethics_assessments
            )
            
            if not is_compliant:
                logger.warning("Decision blocked by ethical validation")
                return ProcessingResult(
                    status=ProcessingStatus.ETHICS_BLOCKED,
                    data=fused_data,
                    ethics_assessments=ethics_assessments,
                    processing_time_ms=(time.time() - start_time) * 1000
                )
            
            # 5. External Communication
            transmission_success = await self.link_module.transmit_output(
                fused_data, context or {}
            )
            
            processing_time = (time.time() - start_time) * 1000
            self.processing_count += 1
            
            return ProcessingResult(
                status=ProcessingStatus.COMPLETED,
                data=fused_data,
                metadata={
                    "processing_count": self.processing_count,
                    "transmission_success": transmission_success,
                    "vision_processed": bool(vision_results),
                    "sensor_processed": bool(sense_results)
                },
                processing_time_ms=processing_time,
                ethics_assessments=ethics_assessments
            )
            
        except Exception as e:
            logger.error(f"Error processing context: {e}")
            return ProcessingResult(
                status=ProcessingStatus.FAILED,
                data=input_data,
                processing_time_ms=(time.time() - start_time) * 1000,
                errors=[str(e)]
            )
    
    def get_status(self) -> Dict[str, Any]:
        """Get current status of SEVE Core v3.0"""
        return {
            "initialized": self.is_initialized,
            "processing_count": self.processing_count,
            "config": self.config.to_dict(),
            "modules": {
                "vision": self.vision_module.get_status(),
                "sense": self.sense_module.get_status(),
                "ethics": self.ethics_module.get_status(),
                "link": self.link_module.get_status()
            }
        }

class SEVEHybridFramework:
    """
    SEVE Hybrid Framework
    
    Combines Universal adaptive capabilities with v3.0 specific
    computer vision functionality, allowing operation in multiple modes.
    """
    
    def __init__(self, config: SEVEConfig):
        self.config = config
        self.v3_core = SEVECoreV3(config)
        self.universal_core = None
        
        # Initialize Universal core if available
        if UNIVERSAL_AVAILABLE and config.mode in [SEVEMode.UNIVERSAL, SEVEMode.HYBRID]:
            try:
                # Create a default domain config for Universal mode
                domain_config = DomainConfig(
                    domain_type=DomainType.BUSINESS,  # Default domain
                    domain_name="SEVE Hybrid Framework",
                    cultural_context="global",
                    ethical_rules=["privacy_protection", "fairness", "transparency"],
                    personalization_rules=["adaptive_learning"],
                    empathy_rules=["contextual_empathy"]
                )
                self.universal_core = SEVEUniversalCore(domain_config)
                logger.info("Universal core initialized for hybrid mode")
            except Exception as e:
                logger.warning(f"Could not initialize Universal core: {e}")
                self.universal_core = None
        
        logger.info(f"SEVE Hybrid Framework initialized in {config.mode.value} mode")
    
    async def initialize(self) -> None:
        """Initialize the hybrid framework"""
        await self.v3_core.initialize()
        
        if self.universal_core:
            # Universal core doesn't have explicit initialize method
            # but we can verify it's ready
            logger.info("Universal core ready")
    
    async def process_context(
        self,
        input_data: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None,
        use_universal: bool = None
    ) -> ProcessingResult:
        """
        Process data through the appropriate pipeline
        
        Args:
            input_data: Input data dictionary
            context: Additional context
            use_universal: Force Universal mode (None = auto-detect)
            
        Returns:
            ProcessingResult with processed data
        """
        # Determine which core to use
        if use_universal is None:
            use_universal = (
                self.config.mode == SEVEMode.UNIVERSAL or
                (self.config.mode == SEVEMode.HYBRID and self.universal_core)
            )
        
        if use_universal and self.universal_core:
            # Use Universal core for adaptive processing
            try:
                # Convert to Universal context format
                universal_context = UniversalContext(
                    domain=DomainType.BUSINESS,  # Default domain
                    user_profile=context.get("user_profile", {}),
                    environmental_data=context.get("environmental_data", {}),
                    cultural_context=context.get("cultural_context", "global"),
                    temporal_context=context.get("temporal_context", {}),
                    metadata=context or {}
                )
                
                # Process with Universal core
                universal_result = await self.universal_core.process_universal_context(
                    universal_context, input_data
                )
                
                # Convert back to ProcessingResult format
                return ProcessingResult(
                    status=ProcessingStatus.COMPLETED,
                    data=universal_result,
                    metadata={"mode": "universal", "domain": "adaptive"}
                )
                
            except Exception as e:
                logger.error(f"Universal processing failed, falling back to v3.0: {e}")
                # Fall back to v3.0 processing
                return await self.v3_core.process_context(input_data, context)
        else:
            # Use v3.0 core for specific processing
            return await self.v3_core.process_context(input_data, context)
    
    def switch_mode(self, new_mode: SEVEMode) -> None:
        """Switch framework operating mode"""
        self.config.mode = new_mode
        logger.info(f"Framework mode switched to: {new_mode.value}")
    
    def get_capabilities(self) -> Dict[str, Any]:
        """Get framework capabilities"""
        capabilities = {
            "version": "1.0.0",
            "mode": self.config.mode.value,
            "v3_core_available": True,
            "universal_core_available": self.universal_core is not None,
            "privacy_level": self.config.privacy_level.value,
            "ethics_level": self.config.ethics_level.value,
            "modules": {
                "vision": True,
                "sense": True,
                "ethics": True,
                "link": True
            }
        }
        
        if self.universal_core:
            capabilities["universal_features"] = {
                "domain_adaptation": True,
                "empathy_engine": True,
                "universal_ethics": True,
                "cultural_adaptation": True
            }
        
        return capabilities
    
    def get_status(self) -> Dict[str, Any]:
        """Get comprehensive framework status"""
        status = {
            "framework": {
                "mode": self.config.mode.value,
                "initialized": True,
                "capabilities": self.get_capabilities()
            },
            "v3_core": self.v3_core.get_status()
        }
        
        if self.universal_core:
            status["universal_core"] = {
                "available": True,
                "domain": "adaptive",
                "config": self.universal_core.config.__dict__ if hasattr(self.universal_core, 'config') else {}
            }
        
        return status

# Convenience functions
def create_v3_framework(config: SEVEConfig) -> SEVECoreV3:
    """Create SEVE v3.0 framework instance"""
    return SEVECoreV3(config)

def create_hybrid_framework(config: SEVEConfig) -> SEVEHybridFramework:
    """Create SEVE hybrid framework instance"""
    return SEVEHybridFramework(config)

# Demo function
async def run_demo():
    """Run SEVE Framework demonstration"""
    print("🤖 SEVE Framework - Hybrid Mode Demo")
    print("=" * 50)
    
    # Create configuration
    config = SEVEConfig(
        mode=SEVEMode.HYBRID,
        privacy_level=PrivacyLevel.HIGH,
        ethics_level=EthicsLevel.STRICT,
        debug=True
    )
    
    # Create framework
    framework = SEVEHybridFramework(config)
    await framework.initialize()
    
    print(f"✅ Framework initialized in {config.mode.value} mode")
    print(f"📊 Capabilities: {framework.get_capabilities()}")
    print()
    
    # Demo processing
    demo_data = {
        "visual": {"image": "demo_image.jpg", "objects": ["person", "car"]},
        "sensor": {"temperature": 25.5, "motion": True}
    }
    
    demo_context = {
        "location": "demo_location",
        "privacy_mode": "strict"
    }
    
    print("🔄 Processing demo data...")
    result = await framework.process_context(demo_data, demo_context)
    
    print(f"📋 Result Status: {result.status.value}")
    print(f"⏱️ Processing Time: {result.processing_time_ms:.2f}ms")
    print(f"🔒 Ethics Assessments: {len(result.ethics_assessments)}")
    
    if result.errors:
        print(f"❌ Errors: {result.errors}")
    else:
        print("✅ Processing completed successfully!")
    
    print()
    print("🌍 SEVE Framework ready for ethical AI applications!")

if __name__ == "__main__":
    asyncio.run(run_demo())
