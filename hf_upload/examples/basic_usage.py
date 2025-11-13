#!/usr/bin/env python3
"""
SEVE Framework - Basic Usage Example
Symbiotic Ethical Vision Engine

This example demonstrates basic usage of the SEVE Framework
in different modes and configurations.
"""

import asyncio
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from seve_framework import (
    SEVEHybridFramework,
    SEVEConfig,
    SEVEMode,
    PrivacyLevel,
    EthicsLevel
)

async def basic_usage_example():
    """Basic usage example of SEVE Framework"""
    print("🤖 SEVE Framework - Basic Usage Example")
    print("=" * 50)
    
    # 1. Create configuration
    config = SEVEConfig(
        mode=SEVEMode.HYBRID,
        privacy_level=PrivacyLevel.HIGH,
        ethics_level=EthicsLevel.STRICT,
        debug=True
    )
    
    print(f"✅ Configuration created:")
    print(f"   Mode: {config.mode.value}")
    print(f"   Privacy Level: {config.privacy_level.value}")
    print(f"   Ethics Level: {config.ethics_level.value}")
    print()
    
    # 2. Create framework
    framework = SEVEHybridFramework(config)
    await framework.initialize()
    
    print("✅ Framework initialized successfully")
    print()
    
    # 3. Prepare demo data
    demo_data = {
        "visual": {
            "image": "demo_image.jpg",
            "objects": ["person", "car", "building"],
            "faces_detected": 2,
            "license_plates": 1
        },
        "sensor": {
            "temperature": 23.5,
            "humidity": 65.2,
            "motion": True,
            "proximity": 2.1,
            "audio_level": 45.0
        }
    }
    
    demo_context = {
        "location": "downtown_intersection",
        "privacy_mode": "strict",
        "consent_given": True,
        "user_preferences": {
            "language": "portuguese",
            "notification_level": "high"
        }
    }
    
    print("🔄 Processing demo data...")
    print(f"   Visual data: {len(demo_data['visual'])} items")
    print(f"   Sensor data: {len(demo_data['sensor'])} readings")
    print(f"   Context: {len(demo_context)} parameters")
    print()
    
    # 4. Process data
    result = await framework.process_context(demo_data, demo_context)
    
    # 5. Display results
    print("📋 Processing Results:")
    print(f"   Status: {result.status.value}")
    print(f"   Processing Time: {result.processing_time_ms:.2f}ms")
    print(f"   Ethics Assessments: {len(result.ethics_assessments)}")
    print(f"   Errors: {len(result.errors)}")
    
    if result.errors:
        print("   Error Details:")
        for error in result.errors:
            print(f"     - {error}")
    
    if result.ethics_assessments:
        print("   Ethics Assessments:")
        for assessment in result.ethics_assessments:
            print(f"     - {assessment.rule_name}: {assessment.result.value}")
            if assessment.suggested_mitigation:
                print(f"       Mitigation: {assessment.suggested_mitigation}")
    
    print()
    
    # 6. Show framework capabilities
    capabilities = framework.get_capabilities()
    print("📊 Framework Capabilities:")
    for key, value in capabilities.items():
        if isinstance(value, dict):
            print(f"   {key}:")
            for sub_key, sub_value in value.items():
                print(f"     {sub_key}: {sub_value}")
        else:
            print(f"   {key}: {value}")
    
    print()
    print("🎉 Basic usage example completed successfully!")
    print("🌍 SEVE Framework is ready for ethical AI applications!")

async def vision_specific_example():
    """Vision-specific usage example"""
    print("\n👁️ SEVE Framework - Vision Specific Example")
    print("=" * 50)
    
    # Create vision-specific configuration
    config = SEVEConfig(
        mode=SEVEMode.VISION_SPECIFIC,
        privacy_level=PrivacyLevel.MAXIMUM,
        ethics_level=EthicsLevel.MAXIMUM,
        debug=True
    )
    
    framework = SEVEHybridFramework(config)
    await framework.initialize()
    
    print("✅ Vision-specific framework initialized")
    print()
    
    # Vision-specific data
    vision_data = {
        "visual": {
            "image_path": "security_camera_feed.jpg",
            "detected_objects": ["person", "vehicle", "traffic_light"],
            "faces_detected": 3,
            "license_plates": 2,
            "text_regions": 1
        },
        "sensor": {
            "lidar": {"distance": 15.5, "objects": 4},
            "radar": {"speed": 45.2, "direction": "north"},
            "temperature": 25.0,
            "motion": True
        }
    }
    
    vision_context = {
        "location": "highway_entrance",
        "privacy_mode": "maximum",
        "anonymization_required": True,
        "consent_given": False,  # This will trigger ethical validation
        "security_level": "high"
    }
    
    print("🔄 Processing vision-specific data...")
    result = await framework.process_context(vision_data, vision_context, use_universal=False)
    
    print(f"📋 Vision Processing Results:")
    print(f"   Status: {result.status.value}")
    print(f"   Processing Time: {result.processing_time_ms:.2f}ms")
    
    if result.status.value == "ethics_blocked":
        print("   🛡️ Decision blocked by ethical validation - this is expected!")
        print("   This demonstrates the GuardFlow system working correctly.")
    
    print()
    print("👁️ Vision-specific example completed!")

async def universal_example():
    """Universal mode usage example"""
    print("\n🌍 SEVE Framework - Universal Mode Example")
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
            ethical_rules=["hipaa_compliance", "medical_privacy", "patient_autonomy"],
            personalization_rules=["patient_preferences", "medical_history"],
            empathy_rules=["medical_empathy", "patient_support"]
        )
        
        # Create Universal framework
        universal_core = SEVEUniversalCore(domain_config)
        
        print("✅ Universal framework initialized for healthcare domain")
        print()
        
        # Universal context
        universal_context = UniversalContext(
            domain=DomainType.HEALTHCARE,
            user_profile={
                "patient_id": "demo_patient_001",
                "age": 45,
                "gender": "female",
                "medical_history": ["diabetes", "hypertension"]
            },
            environmental_data={
                "temperature": 22.0,
                "humidity": 60.0,
                "noise_level": "low"
            },
            cultural_context="brazil",
            temporal_context={
                "hour": 14,
                "day_of_week": "monday",
                "season": "spring"
            },
            metadata={
                "appointment_type": "routine_checkup",
                "doctor_id": "dr_silva",
                "clinic_location": "sao_paulo"
            }
        )
        
        # Universal data
        universal_data = {
            "symptoms": ["fatigue", "headache", "dizziness"],
            "vital_signs": {
                "temperature": 38.5,
                "blood_pressure": "140/90",
                "heart_rate": 95,
                "oxygen_saturation": 98
            },
            "patient_preferences": {
                "language": "portuguese",
                "communication_style": "friendly",
                "privacy_level": "high"
            },
            "medical_data": {
                "current_medications": ["metformin", "lisinopril"],
                "allergies": ["penicillin"],
                "last_checkup": "2024-10-15"
            }
        }
        
        print("🔄 Processing universal healthcare context...")
        result = await universal_core.process_universal_context(universal_context, universal_data)
        
        print("📋 Universal Processing Results:")
        print(f"   Domain Result: {result.get('domain_result', {}).get('summary', 'N/A')}")
        print(f"   Learning Result: {result.get('learning_result', {}).get('insights', 'N/A')}")
        print(f"   Adapted Context: {result.get('adapted_context', {}).get('metadata', {})}")
        
        print()
        print("🌍 Universal mode example completed!")
        
    except ImportError:
        print("❌ Universal components not available.")
        print("   Install seve-universal package to use Universal mode.")
        print("   Run: pip install seve-universal")

async def main():
    """Main function to run all examples"""
    print("🚀 SEVE Framework - Complete Usage Examples")
    print("=" * 60)
    
    try:
        # Run basic example
        await basic_usage_example()
        
        # Run vision-specific example
        await vision_specific_example()
        
        # Run universal example
        await universal_example()
        
        print("\n🎉 All examples completed successfully!")
        print("🌍 SEVE Framework is ready for ethical AI applications!")
        
    except Exception as e:
        print(f"❌ Error running examples: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
