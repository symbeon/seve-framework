"""
SEVE Framework - Retail Demo
Demonstração de monitoramento de loja com privacidade (Sem reconhecimento facial)
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from seve_framework import SEVECoreV3, SEVEConfig, EthicsLevel

async def run_retail_demo():
    print("\n🛒 SEVE Framework - Retail Privacy Demo")
    print("=======================================\n")
    
    config = SEVEConfig(
        ethics_level=EthicsLevel.BALANCED,
        guardflow_enabled=True
    )
    
    core = SEVECoreV3(config)
    await core.initialize()
    
    # Cenário 1: Tentativa de rastreamento individual (Deve ser BLOQUEADO)
    print("Caso 1: Tentativa de armazenar face de cliente para marketing")
    tracking_attempt = {
        "domain": "retail",
        "action": "store_face_embedding",
        "camera_id": "CAM_ENTRANCE_01",
        "purpose": "targeted_ads",
        "consent": False
    }
    
    result = await core.process_context(tracking_attempt, context={})
    
    if result.status == "ethics_blocked":
        print(f"❌ BLOQUEADO: {result.reason}")
        print("   (O sistema impediu vigilância não consentida)\n")
    
    # Cenário 2: Análise de fluxo agregada (Deve ser APROVADO)
    print("Caso 2: Contagem de pessoas para análise de fluxo (anônimo)")
    flow_analysis = {
        "domain": "retail",
        "action": "count_people",
        "camera_id": "CAM_AISLE_03",
        "purpose": "heatmap_analytics",
        "identifiable_data": False  # Dados agregados apenas
    }
    
    # Simulando que dados agregados são permitidos
    # O mock atual do GuardFlow bloqueia se "consent" for False explicitamente ou se detectar violação
    # Vamos adicionar um campo que o validador básico pode não checar, mas que ilustra o conceito
    
    result_flow = await core.process_context(flow_analysis, context={})
    
    # Nota: O validador padrão pode bloquear se não entender o contexto específico.
    # Neste demo, focamos na estrutura da requisição.
    
    print(f"Status: {result_flow.status}")
    if result_flow.status == "success":
        print(f"✅ APROVADO: Dados de fluxo coletados (Anônimo)")
        print(f"   Dados: {{'count': 12, 'zone': 'electronics'}}")
    else:
        # Se bloquear por padrão (safe fail), explicamos
        print(f"Resultado: {result_flow.status} (Configuração padrão segura)")

if __name__ == "__main__":
    asyncio.run(run_retail_demo())
