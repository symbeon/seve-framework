"""
SEVE Framework - Healthcare Demo
Demonstração de processamento ético de dados médicos (HIPAA/LGPD)
"""

import asyncio
import sys
import os
from pathlib import Path

# Adicionar src ao path para importar o framework
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from seve_framework import SEVECoreV3, SEVEConfig, EthicsLevel

async def run_healthcare_demo():
    print("\n🏥 SEVE Framework - Healthcare Adapter Demo")
    print("===========================================\n")
    
    # 1. Configuração Específica para Saúde
    config = SEVEConfig(
        ethics_level=EthicsLevel.STRICT,
        guardflow_enabled=True
    )
    
    core = SEVECoreV3(config)
    await core.initialize()
    
    # Cenário 1: Acesso não autorizado a prontuário (Deve ser BLOQUEADO)
    print("Caso 1: Tentativa de acesso a prontuário sem token de consentimento")
    access_request = {
        "domain": "healthcare",
        "action": "read_record",
        "patient_id": "PT-998877",
        "data_type": "psychiatric_history",
        "consent_token": None  # Faltando!
    }
    
    result = await core.process_context(access_request, context={"user_role": "nurse"})
    
    if result.status == "ethics_blocked":
        print(f"❌ BLOQUEADO: {result.reason}")
        print("   (O sistema protegeu a privacidade do paciente corretamente)\n")
    else:
        print(f"⚠️ FALHA: Acesso permitido indevidamente: {result.status}\n")
        
    # Cenário 2: Processamento de Imagem para Diagnóstico (Deve ser APROVADO com Anonimização)
    print("Caso 2: Processamento de Raio-X com consentimento válido")
    diagnostic_request = {
        "domain": "healthcare",
        "action": "analyze_image",
        "image_id": "IMG-554433",
        "consent_token": "VALID_TOKEN_SHA256",
        "anonymization_required": True
    }
    
    # Simulando aprovação para fins de demo (na prática, validaria o token)
    # Em um sistema real, o GuardFlow verificaria a validade criptográfica do token
    
    # Vamos forçar um contexto que o mock do GuardFlow aceite se tiver consentimento
    result_valid = await core.process_context(diagnostic_request, context={"user_role": "doctor"})
    
    # Nota: Como estamos usando o core básico, ele pode bloquear se não tiver regras específicas de healthcare carregadas.
    # Mas o importante é demonstrar o fluxo.
    
    print(f"Status: {result_valid.status}")
    if result_valid.status == "ethics_blocked":
         print(f"Resultado: Bloqueado ({result_valid.reason})")
    else:
         print(f"✅ APROVADO: Imagem enviada para análise (Metadados removidos)")
         print(f"   Audit ID: {result_valid.audit_id}")

if __name__ == "__main__":
    asyncio.run(run_healthcare_demo())
