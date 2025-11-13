"""Example: Universal Mode - Retail"""

import asyncio
from seve_framework.universal import (
    SEVEUniversalCore, DomainConfig, DomainType, UniversalContext
)
from seve_framework.universal.adapters import RetailAdapter


async def main() -> None:
    config = DomainConfig(
        domain_type=DomainType.RETAIL,
        domain_name="Retail Assistant",
        cultural_context="brazil",
    )

    core = SEVEUniversalCore(config)
    core.domain_adapter_registry.register_adapter(DomainType.RETAIL, RetailAdapter())

    context = UniversalContext(
        domain=DomainType.RETAIL,
        user_profile={"customer": {"id": "C123", "name": "Ana"}},
        environmental_data={"store": "Loja Centro"},
        cultural_context="brazil",
        temporal_context={"timestamp": 1234567890},
        metadata={}
    )

    data = {
        "customer": {"id": "C123", "name": "Ana"},
        "products": [{"id": "P1", "name": "Produto 1"}],
        "history": [{"id": "O1", "date": "2025-01-15"}],
        "inventory": {"P1": 50},
        "esg": {"environmental_score": 85, "social_score": 90},
    }

    result = await core.process_universal_context(context, data)
    print("Features:", result["domain_features"])  # noqa: T201
    print("Result:", result["domain_result"])      # noqa: T201


if __name__ == "__main__":
    asyncio.run(main())
