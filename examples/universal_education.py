"""Example: Universal Mode - Education"""

import asyncio
from seve_framework.universal import (
    SEVEUniversalCore, DomainConfig, DomainType, UniversalContext
)
from seve_framework.universal.adapters import EducationAdapter


async def main() -> None:
    config = DomainConfig(
        domain_type=DomainType.EDUCATION,
        domain_name="Education Platform",
        cultural_context="usa",
    )

    core = SEVEUniversalCore(config)
    core.domain_adapter_registry.register_adapter(DomainType.EDUCATION, EducationAdapter())

    context = UniversalContext(
        domain=DomainType.EDUCATION,
        user_profile={"student_id": "S456"},
        environmental_data={"school": "Tech High"},
        cultural_context="usa",
        temporal_context={"timestamp": 1234567890},
        metadata={}
    )

    data = {
        "learning_style": "visual",
        "level": "high_school",
        "subject": "mathematics",
        "progress": {"completed": 75, "total": 100},
        "assessments": [{"score": 85, "date": "2025-01-15"}],
    }

    result = await core.process_universal_context(context, data)
    print("Features:", result["domain_features"])  # noqa: T201
    print("Result:", result["domain_result"])      # noqa: T201


if __name__ == "__main__":
    asyncio.run(main())
