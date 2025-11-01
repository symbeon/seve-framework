#!/usr/bin/env python3
"""
SEVE Universal - Exemplo de Adaptação Multi-Domínio

Demonstra como o SEVE Universal se adapta a diferentes domínios
de aplicação mantendo suas capacidades universais.
"""

import asyncio
from typing import Dict, Any

from seve_universal import (
    SEVEUniversalCore, DomainConfig, UniversalContext, DomainType, AdaptationLevel
)
from seve_universal.adapters import UniversalAdapterRegistry


async def demonstrate_healthcare_domain():
    """Demonstra adaptação para domínio de saúde"""
    print("🏥 === DOMÍNIO DE SAÚDE ===")
    
    # Configurar para saúde
    config = DomainConfig(
        domain_type=DomainType.HEALTHCARE,
        domain_name="Medical AI Assistant",
        cultural_context="brazil",
        adaptation_level=AdaptationLevel.ADVANCED,
        ethical_rules=["hipaa", "medical_privacy", "patient_safety"],
        personalization_rules=["patient_preferences", "medical_history"],
        empathy_rules=["medical_empathy", "family_support"]
    )
    
    # Inicializar SEVE Universal
    seve = SEVEUniversalCore(config)
    
    # Contexto de paciente
    context = UniversalContext(
        domain=DomainType.HEALTHCARE,
        user_profile={
            "patient_id": "P001",
            "age": 45,
            "medical_history": ["diabetes", "hypertension"],
            "preferences": {"language": "portuguese", "communication_style": "gentle"}
        },
        environmental_data={"hospital": "Hospital São Paulo", "department": "cardiology"},
        cultural_context="brazil",
        temporal_context={"time": "morning", "urgency": "routine"},
        metadata={}
    )
    
    # Dados médicos
    medical_data = {
        "patient_id": "P001",
        "vitals": {"blood_pressure": "140/90", "heart_rate": 85, "temperature": 36.5},
        "symptoms": ["chest_pain", "shortness_of_breath"],
        "diagnosis": "angina",
        "treatment": "nitroglycerin"
    }
    
    # Processar contexto universal
    result = await seve.process_universal_context(context, medical_data)
    
    print(f"✅ Resultado Saúde: {result['domain_result']}")
    print(f"📊 Métricas: {seve.get_domain_metrics()}")


async def demonstrate_education_domain():
    """Demonstra adaptação para domínio educacional"""
    print("\n🎓 === DOMÍNIO EDUCACIONAL ===")
    
    # Configurar para educação
    config = DomainConfig(
        domain_type=DomainType.EDUCATION,
        domain_name="Adaptive Learning Platform",
        cultural_context="brazil",
        adaptation_level=AdaptationLevel.INTERMEDIATE,
        ethical_rules=["student_privacy", "educational_standards"],
        personalization_rules=["learning_style", "academic_level"],
        empathy_rules=["student_support", "motivational_encouragement"]
    )
    
    # Inicializar SEVE Universal
    seve = SEVEUniversalCore(config)
    
    # Contexto de estudante
    context = UniversalContext(
        domain=DomainType.EDUCATION,
        user_profile={
            "student_id": "S001",
            "age": 16,
            "learning_style": "visual",
            "academic_level": "high_school",
            "preferences": {"subject": "mathematics", "difficulty": "intermediate"}
        },
        environmental_data={"school": "Escola Estadual", "classroom": "A1"},
        cultural_context="brazil",
        temporal_context={"time": "afternoon", "session": "study"},
        metadata={}
    )
    
    # Dados educacionais
    education_data = {
        "student_id": "S001",
        "subject": "algebra",
        "current_topic": "quadratic_equations",
        "progress": {"completed": 0.6, "accuracy": 0.75},
        "assessment_results": [{"score": 85, "difficulty": "medium"}]
    }
    
    # Processar contexto universal
    result = await seve.process_universal_context(context, education_data)
    
    print(f"✅ Resultado Educação: {result['domain_result']}")
    print(f"📊 Métricas: {seve.get_domain_metrics()}")


async def demonstrate_business_domain():
    """Demonstra adaptação para domínio empresarial"""
    print("\n🏢 === DOMÍNIO EMPRESARIAL ===")
    
    # Configurar para negócios
    config = DomainConfig(
        domain_type=DomainType.BUSINESS,
        domain_name="Corporate AI Assistant",
        cultural_context="global",
        adaptation_level=AdaptationLevel.EXPERT,
        ethical_rules=["corporate_compliance", "data_protection"],
        personalization_rules=["role_based", "performance_metrics"],
        empathy_rules=["leadership_support", "team_dynamics"]
    )
    
    # Inicializar SEVE Universal
    seve = SEVEUniversalCore(config)
    
    # Contexto empresarial
    context = UniversalContext(
        domain=DomainType.BUSINESS,
        user_profile={
            "employee_id": "E001",
            "role": "manager",
            "department": "engineering",
            "experience_level": "senior",
            "preferences": {"communication": "direct", "leadership_style": "collaborative"}
        },
        environmental_data={"company": "TechCorp", "office": "São Paulo"},
        cultural_context="global",
        temporal_context={"time": "morning", "meeting": "team_review"},
        metadata={}
    )
    
    # Dados empresariais
    business_data = {
        "employee_id": "E001",
        "team_size": 8,
        "performance_metrics": {"productivity": 0.85, "satisfaction": 0.92},
        "current_projects": ["mobile_app", "api_integration"],
        "goals": ["increase_productivity", "team_development"]
    }
    
    # Processar contexto universal
    result = await seve.process_universal_context(context, business_data)
    
    print(f"✅ Resultado Negócios: {result['domain_result']}")
    print(f"📊 Métricas: {seve.get_domain_metrics()}")


async def demonstrate_domain_switching():
    """Demonstra mudança dinâmica de domínio"""
    print("\n🔄 === MUDANÇA DINÂMICA DE DOMÍNIO ===")
    
    # Começar com saúde
    config = DomainConfig(
        domain_type=DomainType.HEALTHCARE,
        domain_name="Multi-Domain AI",
        cultural_context="brazil",
        adaptation_level=AdaptationLevel.ADVANCED
    )
    
    seve = SEVEUniversalCore(config)
    print(f"🏥 Domínio inicial: {seve.get_domain_metrics()['domain']}")
    
    # Mudar para educação
    education_config = DomainConfig(
        domain_type=DomainType.EDUCATION,
        domain_name="Multi-Domain AI",
        cultural_context="brazil",
        adaptation_level=AdaptationLevel.ADVANCED
    )
    
    seve.switch_domain(education_config)
    print(f"🎓 Domínio alterado para: {seve.get_domain_metrics()['domain']}")
    
    # Mudar para negócios
    business_config = DomainConfig(
        domain_type=DomainType.BUSINESS,
        domain_name="Multi-Domain AI",
        cultural_context="global",
        adaptation_level=AdaptationLevel.ADVANCED
    )
    
    seve.switch_domain(business_config)
    print(f"🏢 Domínio alterado para: {seve.get_domain_metrics()['domain']}")


async def demonstrate_custom_adapter():
    """Demonstra adaptador customizado"""
    print("\n🛠️ === ADAPTADOR CUSTOMIZADO ===")
    
    from seve_universal.core import DomainAdapter
    
    class CustomDomainAdapter(DomainAdapter):
        """Adaptador customizado para domínio específico"""
        
        def adapt_to_context(self, context):
            context.metadata.update({"custom_domain": True})
            return context
        
        def extract_domain_features(self, data):
            return {"custom_features": data}
        
        def apply_domain_rules(self, decision):
            return {"custom_decision": decision}
    
    # Registrar adaptador customizado
    registry = UniversalAdapterRegistry()
    registry.register_custom_adapter("custom_domain", CustomDomainAdapter())
    
    print("✅ Adaptador customizado registrado")
    print(f"📋 Adaptadores disponíveis: {len(registry.list_available_domains())}")


async def main():
    """Função principal"""
    print("🚀 SEVE Universal - Demonstração Multi-Domínio")
    print("=" * 60)
    
    # Demonstrar diferentes domínios
    await demonstrate_healthcare_domain()
    await demonstrate_education_domain()
    await demonstrate_business_domain()
    
    # Demonstrar mudança de domínio
    await demonstrate_domain_switching()
    
    # Demonstrar adaptador customizado
    await demonstrate_custom_adapter()
    
    print("\n🎉 Demonstração concluída!")
    print("=" * 60)
    print("💡 O SEVE Universal demonstrou adaptação a múltiplos domínios")
    print("🌍 Mantendo capacidades universais de personalização, empatia e ética")


if __name__ == "__main__":
    # Executar demonstração
    asyncio.run(main())
