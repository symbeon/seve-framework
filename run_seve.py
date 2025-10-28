#!/usr/bin/env python3
"""
SEVE Framework - Main Demo Script
Symbiotic Ethical Vision Engine

This script demonstrates the complete SEVE Framework functionality,
including both Universal and v3.0 specific capabilities.
"""

import asyncio
import logging
import sys
import argparse
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from seve_framework import (
    SEVEHybridFramework,
    SEVEConfig,
    SEVEMode,
    PrivacyLevel,
    EthicsLevel,
    setup_config
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def run_basic_demo():
    """Run basic SEVE Framework demonstration"""
    print("🤖 SEVE Framework - Basic Demo")
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
    print(f"🔒 Privacy level: {config.privacy_level.value}")
    print(f"⚖️ Ethics level: {config.ethics_level.value}")
    print()
    
    # Demo capabilities
    capabilities = framework.get_capabilities()
    print("📊 Framework Capabilities:")
    for key, value in capabilities.items():
        print(f"  {key}: {value}")
    print()
    
    # Demo processing
    demo_data = {
        "visual": {
            "image": "demo_image.jpg",
            "objects": ["person", "car", "building"],
            "faces_detected": 2
        },
        "sensor": {
            "temperature": 23.5,
            "humidity": 65.2,
            "motion": True,
            "proximity": 2.1
        }
    }
    
    demo_context = {
        "location": "demo_location",
        "privacy_mode": "strict",
        "user_consent": True
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

async def run_universal_demo():
    """Run Universal mode demonstration"""
    print("🌍 SEVE Framework - Universal Mode Demo")
    print("=" * 50)
    
    try:
        # Import Universal components
        from seve_universal import (
            SEVEUniversalCore,
            DomainConfig,
            DomainType,
            UniversalContext
        )
        
        # Create Universal configuration
        domain_config = DomainConfig(
            domain_type=DomainType.HEALTHCARE,
            domain_name="Medical AI Assistant",
            cultural_context="brazil",
            ethical_rules=["hipaa_compliance", "medical_privacy"],
            personalization_rules=["patient_preferences"],
            empathy_rules=["medical_empathy"]
        )
        
        # Create Universal framework
        universal_core = SEVEUniversalCore(domain_config)
        
        print(f"✅ Universal Core initialized for domain: {domain_config.domain_name}")
        print(f"🌍 Domain: {domain_config.domain_type.value}")
        print(f"🇧🇷 Cultural context: {domain_config.cultural_context}")
        print()
        
        # Demo Universal processing
        universal_context = UniversalContext(
            domain=DomainType.HEALTHCARE,
            user_profile={"patient_id": "demo_patient", "age": 45},
            environmental_data={"temperature": 22.0, "humidity": 60.0},
            cultural_context="brazil",
            temporal_context={"hour": 14, "day_of_week": "monday"},
            metadata={"medical_history": "diabetes"}
        )
        
        demo_data = {
            "symptoms": ["fever", "headache"],
            "vital_signs": {"temperature": 38.5, "blood_pressure": "140/90"},
            "patient_preferences": {"language": "portuguese", "communication_style": "friendly"}
        }
        
        print("🔄 Processing Universal context...")
        result = await universal_core.process_universal_context(universal_context, demo_data)
        
        print("📋 Universal Processing Result:")
        print(f"  Domain Result: {result.get('domain_result', {})}")
        print(f"  Learning Result: {result.get('learning_result', {})}")
        print(f"  Adapted Context: {result.get('adapted_context', {}).get('metadata', {})}")
        
        print()
        print("🌍 Universal mode demonstration completed!")
        
    except ImportError:
        print("❌ Universal components not available. Install seve-universal package.")
        print("   Run: pip install seve-universal")

async def run_v3_demo():
    """Run v3.0 specific mode demonstration"""
    print("👁️ SEVE Framework - v3.0 Vision Specific Demo")
    print("=" * 50)
    
    # Create v3.0 configuration
    config = SEVEConfig(
        mode=SEVEMode.VISION_SPECIFIC,
        privacy_level=PrivacyLevel.MAXIMUM,
        ethics_level=EthicsLevel.MAXIMUM,
        debug=True
    )
    
    # Create framework
    framework = SEVEHybridFramework(config)
    await framework.initialize()
    
    print(f"✅ v3.0 Framework initialized")
    print(f"🔒 Privacy level: {config.privacy_level.value}")
    print(f"⚖️ Ethics level: {config.ethics_level.value}")
    print()
    
    # Demo v3.0 specific processing
    vision_data = {
        "visual": {
            "image_path": "demo_camera_feed.jpg",
            "detected_objects": ["person", "vehicle", "traffic_light"],
            "faces_detected": 3,
            "license_plates": 2
        },
        "sensor": {
            "lidar": {"distance": 15.5, "objects": 4},
            "radar": {"speed": 45.2, "direction": "north"},
            "temperature": 25.0,
            "motion": True
        }
    }
    
    context = {
        "location": "intersection_downtown",
        "privacy_mode": "maximum",
        "anonymization_required": True,
        "consent_given": False  # This will trigger ethical validation
    }
    
    print("🔄 Processing v3.0 vision data...")
    result = await framework.process_context(vision_data, context, use_universal=False)
    
    print(f"📋 v3.0 Result Status: {result.status.value}")
    print(f"⏱️ Processing Time: {result.processing_time_ms:.2f}ms")
    print(f"🔒 Ethics Assessments: {len(result.ethics_assessments)}")
    
    # Show ethics assessments
    for assessment in result.ethics_assessments:
        print(f"  ⚖️ {assessment.rule_name}: {assessment.result.value}")
        if assessment.suggested_mitigation:
            print(f"    🔧 Mitigation: {assessment.suggested_mitigation}")
    
    if result.status.value == "ethics_blocked":
        print("🛡️ Decision blocked by ethical validation - this is expected behavior!")
    
    print()
    print("👁️ v3.0 Vision Specific mode demonstration completed!")

async def run_hybrid_demo():
    """Run hybrid mode demonstration"""
    print("🔄 SEVE Framework - Hybrid Mode Demo")
    print("=" * 50)
    
    # Create hybrid configuration
    config = SEVEConfig(
        mode=SEVEMode.HYBRID,
        privacy_level=PrivacyLevel.HIGH,
        ethics_level=EthicsLevel.STRICT,
        debug=True
    )
    
    # Create framework
    framework = SEVEHybridFramework(config)
    await framework.initialize()
    
    print(f"✅ Hybrid Framework initialized")
    print(f"🔄 Mode: {config.mode.value}")
    print(f"🔒 Privacy level: {config.privacy_level.value}")
    print(f"⚖️ Ethics level: {config.ethics_level.value}")
    print()
    
    # Demo hybrid processing - Universal mode
    print("🌍 Testing Universal mode...")
    universal_data = {
        "user_input": "I need help with my project",
        "context": "educational",
        "preferences": {"language": "portuguese"}
    }
    
    universal_context = {
        "domain": "education",
        "user_profile": {"student_id": "demo_student"},
        "cultural_context": "brazil"
    }
    
    result1 = await framework.process_context(universal_data, universal_context, use_universal=True)
    print(f"  Universal Result: {result1.status.value}")
    
    # Demo hybrid processing - v3.0 mode
    print("👁️ Testing v3.0 mode...")
    vision_data = {
        "visual": {"image": "demo.jpg", "objects": ["person"]},
        "sensor": {"temperature": 24.0, "motion": False}
    }
    
    vision_context = {
        "location": "office",
        "privacy_mode": "high"
    }
    
    result2 = await framework.process_context(vision_data, vision_context, use_universal=False)
    print(f"  v3.0 Result: {result2.status.value}")
    
    # Show framework status
    status = framework.get_status()
    print()
    print("📊 Hybrid Framework Status:")
    print(f"  v3 Core Available: {status['v3_core']['initialized']}")
    print(f"  Universal Core Available: {status.get('universal_core', {}).get('available', False)}")
    print(f"  Mode: {status['framework']['mode']}")
    
    print()
    print("🔄 Hybrid mode demonstration completed!")

async def run_comprehensive_demo():
    """Run comprehensive demonstration of all modes"""
    print("🚀 SEVE Framework - Comprehensive Demo")
    print("=" * 60)
    
    demos = [
        ("Basic Framework", run_basic_demo),
        ("Universal Mode", run_universal_demo),
        ("v3.0 Vision Specific", run_v3_demo),
        ("Hybrid Mode", run_hybrid_demo)
    ]
    
    for demo_name, demo_func in demos:
        print(f"\n{'='*20} {demo_name} {'='*20}")
        try:
            await demo_func()
        except Exception as e:
            print(f"❌ Error in {demo_name}: {e}")
            logger.error(f"Demo {demo_name} failed: {e}")
        
        print("\n" + "="*60)
    
    print("\n🎉 Comprehensive demonstration completed!")
    print("🌍 SEVE Framework is ready for ethical AI applications!")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="SEVE Framework Demo")
    parser.add_argument(
        "--mode",
        choices=["basic", "universal", "v3", "hybrid", "comprehensive"],
        default="comprehensive",
        help="Demo mode to run"
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Configuration file path"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging"
    )
    
    args = parser.parse_args()
    
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Run selected demo
    demos = {
        "basic": run_basic_demo,
        "universal": run_universal_demo,
        "v3": run_v3_demo,
        "hybrid": run_hybrid_demo,
        "comprehensive": run_comprehensive_demo
    }
    
    demo_func = demos[args.mode]
    
    try:
        asyncio.run(demo_func())
    except KeyboardInterrupt:
        print("\n👋 Demo interrupted by user")
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        logger.error(f"Demo failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
