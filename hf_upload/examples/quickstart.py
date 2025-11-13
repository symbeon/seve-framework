#!/usr/bin/env python3
"""
SEVE Framework - Exemplo de Uso Básico

Este exemplo demonstra como usar os componentes principais
do SEVE Framework para um sistema de checkout inteligente.
"""

import asyncio
import numpy as np
from typing import Dict, List, Any

# Importar componentes do SEVE
from seve import (
    SEVECore, SEVEVision, SEVEEthics, SEVEEmpathy,
    SEVESense, SEVELink, SEVEPersonality, SEVEContext
)


async def main():
    """Exemplo principal de uso do SEVE Framework"""
    
    print("🚀 SEVE Framework - Exemplo de Uso")
    print("=" * 50)
    
    # 1. Inicializar componentes
    print("\n1️⃣ Inicializando componentes...")
    core = SEVECore()
    vision = SEVEVision()
    ethics = SEVEEthics()
    empathy = SEVEEmpathy()
    sense = SEVESense()
    link = SEVELink()
    personality = SEVEPersonality()
    
    print("✅ Componentes inicializados")
    
    # 2. Simular dados de entrada
    print("\n2️⃣ Simulando dados de entrada...")
    
    # Simular stream de imagem
    image_stream = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
    
    # Simular dados de peso
    weight_data = 0.5  # kg
    
    # Simular código de barras
    barcode_data = "1234567890123"
    
    # Simular contexto de checkout
    context = SEVEContext(
        session_id="session_123",
        user_id="user_456",
        checkout_stage="scanning",
        timestamp=1640995200.0,
        metadata={"store_id": "store_001", "lane_id": "lane_01"}
    )
    
    print("✅ Dados simulados")
    
    # 3. Detectar produtos
    print("\n3️⃣ Detectando produtos...")
    products = vision.detect_products(
        image_stream=image_stream,
        weight_data=weight_data,
        barcode_data=barcode_data
    )
    
    print(f"✅ {len(products)} produtos detectados")
    for product in products:
        print(f"   - {product.product_id} (confiança: {product.confidence.value})")
    
    # 4. Calcular scores ESG
    print("\n4️⃣ Calculando scores ESG...")
    esg_scores = ethics.calculate_scores([products[0] if products else None])
    
    print(f"✅ Scores ESG calculados: {esg_scores}")
    
    # 5. Detectar estado emocional
    print("\n5️⃣ Detectando estado emocional...")
    user_interaction = {
        "text": "Estou um pouco frustrado com esse processo",
        "behavior": {"click_speed": 2.0, "error_count": 1}
    }
    
    emotional_state = empathy.detect_emotion(user_interaction, context.__dict__)
    print(f"✅ Estado emocional: {emotional_state.emotion.value} (intensidade: {emotional_state.intensity})")
    
    # 6. Gerar resposta empática
    print("\n6️⃣ Gerando resposta empática...")
    empathetic_response = empathy.generate_empathetic_response(
        emotional_state, context.__dict__
    )
    
    print(f"✅ Resposta empática: {empathetic_response.message}")
    print(f"   Tom: {empathetic_response.tone}")
    print(f"   Ações sugeridas: {empathetic_response.suggested_actions}")
    
    # 7. Coletar dados de sensores
    print("\n7️⃣ Coletando dados de sensores...")
    sensor_data = sense.collect_sensor_data()
    
    print(f"✅ Dados de sensores coletados:")
    print(f"   - Peso: {sensor_data.weight_data} kg")
    print(f"   - Movimento: {sensor_data.motion_data}")
    print(f"   - Ambiental: {sensor_data.environmental_data}")
    
    # 8. Personalizar experiência
    print("\n8️⃣ Personalizando experiência...")
    personality_profile = personality.create_personality_profile(
        context.user_id, {"detailed_info": True, "speed": False}
    )
    
    print(f"✅ Perfil criado: {personality_profile.personality_type.value}")
    
    adapted_response = personality.adapt_response(
        context.user_id,
        "Aqui estão os detalhes do seu produto",
        context.__dict__
    )
    
    print(f"✅ Resposta adaptada: {adapted_response.message}")
    print(f"   Personalidade: {adapted_response.personality_type.value}")
    
    # 9. Processar transação completa
    print("\n9️⃣ Processando transação completa...")
    
    # Converter DetectionResult para Product (simplificado)
    if products:
        from seve.core import Product, ESGScore
        product = Product(
            id=products[0].product_id,
            name="Produto Exemplo",
            category="Alimentação",
            ncm_code="12345678",
            esg_score=ESGScore.GOOD,
            weight=weight_data,
            price=10.50,
            metadata={"detected_by": "vision"}
        )
        
        transaction_result = core.process_transaction([product], context)
        print(f"✅ Transação processada:")
        print(f"   - Produtos: {len(transaction_result['products'])}")
        print(f"   - Score ESG médio: {transaction_result['esg_average']:.2f}")
        print(f"   - Valor total: R$ {transaction_result['total_value']:.2f}")
    
    # 10. Integração ERP (simulada)
    print("\n🔟 Simulando integração ERP...")
    
    # Adicionar conexão ERP
    from seve.link import ERPConnection, ERPType
    erp_connection = ERPConnection(
        erp_type=ERPType.SAP,
        endpoint="https://sap.company.com/api",
        credentials={"username": "user", "password": "pass"}
    )
    
    link.add_erp_connection("sap_001", erp_connection)
    
    # Sincronizar transação
    if products:
        sync_result = await link.sync_transaction(
            {"products": [product.__dict__], "total": 10.50},
            "sap_001"
        )
        
        print(f"✅ Sincronização ERP:")
        print(f"   - Status: {sync_result.status.value}")
        print(f"   - Registros sincronizados: {sync_result.records_synced}")
        print(f"   - Duração: {sync_result.duration:.2f}s")
    
    # 11. Métricas finais
    print("\n📊 Métricas de Performance:")
    print(f"   - Detecção: {vision.get_detection_metrics()}")
    print(f"   - Empatia: {empathy.get_empathy_metrics()}")
    print(f"   - Personalidade: {personality.get_personality_metrics(context.user_id)}")
    
    print("\n🎉 Exemplo concluído com sucesso!")
    print("=" * 50)


if __name__ == "__main__":
    # Executar exemplo
    asyncio.run(main())
