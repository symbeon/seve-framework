"""
Exemplo Integrado SEVE Universal - Ética e Empatia

Este exemplo demonstra como usar os componentes de Ética e Empatia
do SEVE Universal em conjunto com adaptadores de domínio.
"""

import asyncio
import logging
from typing import Dict, Any, List
from dataclasses import dataclass
from datetime import datetime

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Importar componentes do SEVE Universal
from seve_universal import (
    SEVEUniversalCore,
    DomainConfig,
    DomainType,
    UniversalContext,
    UniversalEthicsEngine,
    UniversalEmpathyEngine,
    EthicalPrinciple,
    EthicalComplianceLevel,
    EmpathyType,
    EmotionalState,
    EmpathyContext
)

# === MODELOS DE DADOS ===

@dataclass
class UserProfile:
    """Perfil do usuário"""
    id: str
    name: str
    age: int
    preferences: Dict[str, Any]
    cultural_background: str
    emotional_state: EmotionalState
    privacy_level: str = "medium"

@dataclass
class InteractionData:
    """Dados de interação"""
    user_input: str
    context: Dict[str, Any]
    sensitive_data: Dict[str, Any]
    timestamp: datetime
    domain: str

# === EXEMPLO INTEGRADO ===

async def integrated_ethics_empathy_example():
    """Exemplo integrado de ética e empatia"""
    
    logger.info("🚀 Iniciando exemplo integrado de Ética e Empatia...")
    
    # 1. Configurar domínio de saúde
    healthcare_config = DomainConfig(
        domain_type=DomainType.HEALTHCARE,
        domain_name="Medical AI Assistant",
        cultural_context="brazil",
        ethical_rules=["hipaa_compliance", "medical_privacy", "patient_safety"],
        personalization_rules=["patient_preferences", "medical_history"],
        empathy_rules=["medical_empathy", "patient_support"],
        metadata={
            "medical_context": True,
            "privacy_critical": True,
            "empathy_essential": True
        }
    )
    
    # 2. Inicializar componentes
    seve_core = SEVEUniversalCore(healthcare_config)
    ethics_engine = UniversalEthicsEngine()
    empathy_engine = UniversalEmpathyEngine()
    
    # 3. Criar dados de exemplo
    user_profile = UserProfile(
        id="user_001",
        name="Maria Silva",
        age=45,
        preferences={
            "communication_style": "warm",
            "privacy_level": "high",
            "language": "portuguese"
        },
        cultural_background="brazil",
        emotional_state=EmotionalState.CONCERNED,
        privacy_level="high"
    )
    
    interaction_data = InteractionData(
        user_input="Estou preocupada com os resultados do meu exame de sangue. Os valores estão alterados e não sei o que isso significa.",
        context={
            "medical_history": ["diabetes", "hipertensão"],
            "current_medications": ["metformina", "losartana"],
            "last_appointment": "2025-01-15"
        },
        sensitive_data={
            "personal_data": {
                "patient_id": "P123456",
                "medical_record": "confidential",
                "test_results": {
                    "glucose": 180,
                    "cholesterol": 250,
                    "blood_pressure": "150/90"
                }
            }
        },
        timestamp=datetime.now(),
        domain="healthcare"
    )
    
    # 4. Criar contexto universal
    universal_context = UniversalContext(
        domain=DomainType.HEALTHCARE,
        user_profile={
            "user": user_profile.__dict__,
            "preferences": user_profile.preferences,
            "emotional_state": user_profile.emotional_state.value
        },
        environmental_data={
            "medical_context": interaction_data.context,
            "sensitive_data": interaction_data.sensitive_data,
            "interaction_timestamp": interaction_data.timestamp.isoformat()
        },
        cultural_context=user_profile.cultural_background,
        temporal_context={
            "timestamp": interaction_data.timestamp.isoformat(),
            "urgency": "medium",
            "time_since_last_appointment": "10 days"
        },
        metadata={
            "privacy_level": user_profile.privacy_level,
            "empathy_required": True,
            "ethical_compliance": True
        }
    )
    
    # 5. Avaliar conformidade ética
    logger.info("🔍 Avaliando conformidade ética...")
    
    ethical_assessment = await ethics_engine.assess_universal_compliance(
        data=interaction_data.sensitive_data,
        context=universal_context.__dict__,
        domain="healthcare"
    )
    
    logger.info(f"📊 Score de conformidade ética: {ethical_assessment['overall_compliance_score']:.2f}")
    logger.info(f"⚠️ Nível de risco: {ethical_assessment['risk_level']}")
    
    if ethical_assessment['critical_violations']:
        logger.warning(f"🚨 Violações críticas: {ethical_assessment['critical_violations']}")
    
    # 6. Gerar resposta empática
    logger.info("💝 Gerando resposta empática...")
    
    empathy_context = EmpathyContext(
        user_state=user_profile.emotional_state,
        domain_context="healthcare",
        cultural_context=user_profile.cultural_background,
        urgency_level="medium",
        communication_style="warm",
        sensitivity_level="high",
        metadata={
            "medical_context": True,
            "patient_concern": True,
            "test_results": True
        }
    )
    
    empathy_response = await empathy_engine.generate_universal_empathy(
        context=empathy_context,
        situation={
            "text": interaction_data.user_input,
            "context": interaction_data.context,
            "sensitive_data": interaction_data.sensitive_data,
            "timestamp": interaction_data.timestamp.isoformat(),
            "medical_results": interaction_data.sensitive_data["personal_data"]["test_results"]
        },
        domain="healthcare"
    )
    
    logger.info(f"💬 Resposta empática: {empathy_response.message}")
    logger.info(f"🎯 Tom emocional: {empathy_response.emotional_tone}")
    logger.info(f"📈 Score de confiança: {empathy_response.confidence_score:.2f}")
    
    # 7. Processar contexto universal
    logger.info("🔄 Processando contexto universal...")
    
    universal_result = await seve_core.process_universal_context(
        universal_context,
        {
            "interaction": interaction_data.__dict__,
            "user_profile": user_profile.__dict__,
            "ethical_assessment": ethical_assessment,
            "empathy_response": empathy_response.__dict__
        }
    )
    
    # 8. Exibir resultados integrados
    logger.info("📋 Resultados integrados:")
    logger.info(f"Domínio: {universal_result['adapted_context'].domain.value}")
    logger.info(f"Características extraídas: {list(universal_result['domain_features'].keys())}")
    
    # 9. Métricas dos componentes
    ethics_metrics = ethics_engine.get_compliance_metrics()
    empathy_metrics = empathy_engine.get_empathy_metrics()
    
    logger.info("📊 Métricas de Ética:")
    for key, value in ethics_metrics.items():
        logger.info(f"  {key}: {value}")
    
    logger.info("📊 Métricas de Empatia:")
    for key, value in empathy_metrics.items():
        logger.info(f"  {key}: {value}")
    
    # 10. Resposta final integrada
    final_response = generate_integrated_response(
        ethical_assessment,
        empathy_response,
        universal_result
    )
    
    logger.info("🎯 Resposta final integrada:")
    logger.info(f"Mensagem: {final_response['message']}")
    logger.info(f"Ações recomendadas: {final_response['recommendations']}")
    logger.info(f"Conformidade ética: {final_response['ethical_compliance']}")
    
    return {
        "ethical_assessment": ethical_assessment,
        "empathy_response": empathy_response,
        "universal_result": universal_result,
        "final_response": final_response
    }

def generate_integrated_response(
    ethical_assessment: Dict[str, Any],
    empathy_response: Any,
    universal_result: Dict[str, Any]
) -> Dict[str, Any]:
    """Gera resposta final integrada"""
    
    # Base da resposta empática
    message = empathy_response.message
    
    # Adicionar informações sobre conformidade ética
    if ethical_assessment['overall_compliance_score'] > 0.8:
        message += " Posso garantir que todas as informações estão protegidas conforme os mais altos padrões éticos."
    elif ethical_assessment['overall_compliance_score'] > 0.6:
        message += " Suas informações estão protegidas, mas vou revisar alguns aspectos para garantir máxima segurança."
    else:
        message += " Vou revisar imediatamente os protocolos de proteção de dados para garantir sua privacidade."
    
    # Gerar recomendações baseadas nos resultados
    recommendations = []
    
    # Recomendações de empatia
    recommendations.extend(empathy_response.supportive_actions)
    
    # Recomendações éticas
    recommendations.extend(ethical_assessment['recommendations'])
    
    # Recomendações específicas do domínio
    if universal_result['domain_result'].get('medical_decision'):
        recommendations.append("Agendar consulta médica para discussão dos resultados")
        recommendations.append("Preparar perguntas específicas para o médico")
    
    return {
        "message": message,
        "recommendations": recommendations,
        "ethical_compliance": ethical_assessment['overall_compliance_score'],
        "empathy_score": empathy_response.confidence_score,
        "domain_adaptation": universal_result['adapted_context'].domain.value,
        "cultural_adaptations": empathy_response.cultural_adaptations,
        "risk_level": ethical_assessment['risk_level']
    }

# === EXECUÇÃO ===

async def main():
    """Função principal"""
    try:
        logger.info("🌟 Iniciando exemplo integrado SEVE Universal...")
        
        result = await integrated_ethics_empathy_example()
        
        logger.info("✅ Exemplo integrado concluído com sucesso!")
        logger.info("🎯 SEVE Universal demonstrou integração perfeita entre Ética e Empatia")
        
    except Exception as e:
        logger.error(f"❌ Erro no exemplo: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())
