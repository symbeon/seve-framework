"""
Exemplo de Uso do SEVE Universal - Domínio de Varejo

Este exemplo demonstra como usar o SEVE Universal para o domínio de varejo,
conectando com o projeto original de ESG e análise de produtos.
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
from seve_universal import SEVEUniversalCore, DomainConfig, DomainType, UniversalContext

# === MODELOS DE DADOS DE VAREJO ===

@dataclass
class Product:
    """Produto no contexto de varejo"""
    id: str
    name: str
    category: str
    ncm_code: str
    price: float
    weight: float
    esg_score: float
    sustainability_rating: str
    metadata: Dict[str, Any]

@dataclass
class Customer:
    """Perfil do cliente"""
    id: str
    name: str
    preferences: Dict[str, Any]
    purchase_history: List[Dict[str, Any]]
    sustainability_preference: str
    budget_range: tuple

@dataclass
class Transaction:
    """Transação de varejo"""
    id: str
    customer_id: str
    products: List[Product]
    total_value: float
    timestamp: datetime
    context: Dict[str, Any]

# === EXEMPLO DE USO ===

async def retail_domain_example():
    """Exemplo completo de uso do SEVE Universal para varejo"""
    
    # 1. Configurar domínio de varejo
    retail_config = DomainConfig(
        domain_type=DomainType.RETAIL,
        domain_name="ESG Retail Assistant",
        cultural_context="brazil",
        ethical_rules=["customer_privacy", "esg_compliance", "sustainability"],
        personalization_rules=["customer_preferences", "purchase_behavior"],
        empathy_rules=["customer_support", "sustainability_guidance"],
        metadata={
            "esg_focus": True,
            "sustainability_tracking": True,
            "customer_centric": True
        }
    )
    
    # 2. Inicializar SEVE Universal
    seve = SEVEUniversalCore(retail_config)
    
    # 3. Criar dados de exemplo
    products = [
        Product(
            id="prod_001",
            name="Café Orgânico Fair Trade",
            category="Bebidas",
            ncm_code="0901.11.00",
            price=25.90,
            weight=0.5,
            esg_score=0.85,
            sustainability_rating="A+",
            metadata={"organic": True, "fair_trade": True, "local": False}
        ),
        Product(
            id="prod_002",
            name="Sabão Ecológico",
            category="Higiene",
            ncm_code="3401.11.00",
            price=12.50,
            weight=0.3,
            esg_score=0.92,
            sustainability_rating="A+",
            metadata={"biodegradable": True, "vegan": True, "local": True}
        ),
        Product(
            id="prod_003",
            name="Biscoito Industrial",
            category="Alimentos",
            ncm_code="1905.90.00",
            price=8.90,
            weight=0.2,
            esg_score=0.45,
            sustainability_rating="C",
            metadata={"processed": True, "preservatives": True, "local": False}
        )
    ]
    
    customer = Customer(
        id="cust_001",
        name="Maria Silva",
        preferences={
            "sustainability_focus": "high",
            "organic_preference": True,
            "local_products": True,
            "price_sensitivity": "medium"
        },
        purchase_history=[
            {"product_id": "prod_001", "quantity": 2, "date": "2025-01-20"},
            {"product_id": "prod_002", "quantity": 1, "date": "2025-01-18"}
        ],
        sustainability_preference="high",
        budget_range=(50.0, 100.0)
    )
    
    transaction = Transaction(
        id="trans_001",
        customer_id="cust_001",
        products=products,
        total_value=sum(p.price for p in products),
        timestamp=datetime.now(),
        context={
            "store_location": "São Paulo",
            "season": "summer",
            "promotion_active": False
        }
    )
    
    # 4. Criar contexto universal
    universal_context = UniversalContext(
        domain=DomainType.RETAIL,
        user_profile={
            "customer": customer.__dict__,
            "preferences": customer.preferences,
            "sustainability_focus": customer.sustainability_preference
        },
        environmental_data={
            "store_context": transaction.context,
            "seasonal_factors": {"summer": True, "high_temperature": True},
            "market_conditions": {"demand": "high", "competition": "medium"}
        },
        cultural_context="brazil",
        temporal_context={
            "timestamp": transaction.timestamp.isoformat(),
            "day_of_week": transaction.timestamp.weekday(),
            "time_of_day": transaction.timestamp.hour
        },
        metadata={
            "transaction_id": transaction.id,
            "esg_analysis": True,
            "sustainability_tracking": True
        }
    )
    
    # 5. Processar contexto universal
    logger.info("🛒 Processando contexto de varejo com SEVE Universal...")
    
    result = await seve.process_universal_context(
        universal_context, 
        {
            "products": [p.__dict__ for p in products],
            "transaction": transaction.__dict__,
            "customer": customer.__dict__
        }
    )
    
    # 6. Exibir resultados
    logger.info("📊 Resultados do processamento:")
    logger.info(f"Domínio: {result['adapted_context'].domain.value}")
    logger.info(f"Características extraídas: {list(result['domain_features'].keys())}")
    logger.info(f"Decisão adaptada: {result['domain_result']}")
    
    # 7. Análise ESG específica
    esg_analysis = analyze_esg_impact(products, customer)
    logger.info("🌱 Análise ESG:")
    logger.info(f"Score médio ESG: {esg_analysis['average_esg_score']:.2f}")
    logger.info(f"Alinhamento com preferências: {esg_analysis['preference_alignment']:.2f}")
    logger.info(f"Recomendações: {esg_analysis['recommendations']}")
    
    # 8. Métricas do domínio
    metrics = seve.get_domain_metrics()
    logger.info("📈 Métricas do domínio:")
    for key, value in metrics.items():
        logger.info(f"  {key}: {value}")
    
    return result

def analyze_esg_impact(products: List[Product], customer: Customer) -> Dict[str, Any]:
    """Analisa impacto ESG dos produtos"""
    
    # Calcular score médio ESG
    avg_esg_score = sum(p.esg_score for p in products) / len(products)
    
    # Verificar alinhamento com preferências do cliente
    sustainability_alignment = 0.0
    if customer.sustainability_preference == "high":
        sustainability_alignment = avg_esg_score
    elif customer.sustainability_preference == "medium":
        sustainability_alignment = avg_esg_score * 0.8
    else:
        sustainability_alignment = avg_esg_score * 0.6
    
    # Gerar recomendações
    recommendations = []
    if avg_esg_score < 0.6:
        recommendations.append("Considerar produtos mais sustentáveis")
    if sustainability_alignment < 0.7:
        recommendations.append("Ajustar mix de produtos para preferências do cliente")
    
    return {
        "average_esg_score": avg_esg_score,
        "preference_alignment": sustainability_alignment,
        "recommendations": recommendations,
        "sustainability_rating": "A+" if avg_esg_score > 0.8 else "B" if avg_esg_score > 0.6 else "C"
    }

# === EXECUÇÃO ===

async def main():
    """Função principal"""
    try:
        logger.info("🚀 Iniciando exemplo de varejo com SEVE Universal...")
        
        result = await retail_domain_example()
        
        logger.info("✅ Exemplo concluído com sucesso!")
        logger.info("🎯 SEVE Universal adaptou-se perfeitamente ao domínio de varejo")
        
    except Exception as e:
        logger.error(f"❌ Erro no exemplo: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())
