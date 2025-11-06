"""Example: Universal Mode - Healthcare"""

import asyncio
from seve_framework.universal import (
    SEVEUniversalCore, DomainConfig, DomainType, UniversalContext, AdaptationLevel
)
from seve_framework.universal.adapters import HealthcareAdapter


async def main() -> None:
    config = DomainConfig(
        domain_type=DomainType.HEALTHCARE,
        domain_name="Medical Assistant",
        cultural_context="brazil",
        adaptation_level=AdaptationLevel.ADVANCED,
        ethical_rules=["hipaa_compliance", "medical_privacy"],
    )

    core = SEVEUniversalCore(config)
    core.domain_adapter_registry.register_adapter(DomainType.HEALTHCARE, HealthcareAdapter())

    context = UniversalContext(
        domain=DomainType.HEALTHCARE,
        user_profile={"patient_id": "P123", "age": 45},
        environmental_data={"hospital": "General", "department": "Cardiology"},
        cultural_context="brazil",
        temporal_context={"timestamp": 1234567890},
        metadata={}
    )

    medical_data = {
        "patient_id": "P123",
        "vitals": {"heart_rate": 72, "blood_pressure": "120/80"},
        "symptoms": ["chest_pain"],
        "history": ["hypertension"],
    }

    result = await core.process_universal_context(context, medical_data)
    print("Domain Features:", result["domain_features"])  # noqa: T201
    print("Domain Result:", result["domain_result"])      # noqa: T201


if __name__ == "__main__":
    asyncio.run(main())
