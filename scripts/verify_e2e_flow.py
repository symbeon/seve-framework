import asyncio
import sys
import os
import logging

# Adicionar src ao path (assumindo execução da raiz do projeto)
src_path = os.path.join(os.getcwd(), 'src')
sys.path.append(src_path)
print(f"DEBUG: Adicionado ao path: {src_path}")
print(f"DEBUG: Conteúdo de src: {os.listdir(src_path) if os.path.exists(src_path) else 'SRC NÃO ENCONTRADO'}")

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("E2E_Test")

try:
    from seve_framework.core import SEVECoreV3
    from seve_framework.config import SEVEConfig, EthicsLevel
    from seve_framework.ethics import SEVEEthicsModule
except ImportError as e:
    logger.error(f"Erro de importação: {e}")
    logger.error("Verifique se o diretório src/seve_framework existe e está no PYTHONPATH")
    sys.exit(1)

async def test_e2e_transaction_flow():
    """
    Testa um fluxo completo de transação:
    Inicialização -> Processamento -> Validação Ética -> Resultado
    """
    print("\n🚀 Iniciando Teste E2E: Fluxo de Transação Ética")
    print("=" * 50)
    
    # 1. Configuração
    config = SEVEConfig(
        ethics_level=EthicsLevel.STRICT,
        guardflow_enabled=True,
        audit_logging_enabled=True
    )
    
    # 2. Inicialização do Core
    print("📦 Inicializando SEVECoreV3...")
    core = SEVECoreV3(config)
    await core.initialize()
    
    if core.is_initialized:
        print("✅ Core inicializado com sucesso")
    else:
        print("❌ Falha na inicialização do Core")
        return
    
    # 3. Dados de Teste (Transação Simulada)
    transaction_data = {
        "transaction_id": "tx_123456",
        "amount": 1000.00,
        "currency": "BRL",
        "user_id": "user_999",
        "data_type": "financial_transaction",
        # Dados para validação ética
        "consent_given": True,
        "has_bias_risk": False,
        "explanation_provided": True
    }
    
    context = {
        "timestamp": 1732960000,
        "location": "Sao Paulo, BR",
        "device": "mobile_app"
    }
    
    print(f"\n🔄 Processando transação: {transaction_data['transaction_id']}")
    
    # 4. Processamento (Simulando pipeline)
    # Na v3, o processamento inclui validação ética automática se configurado
    result = await core.process_context(transaction_data, context)
    
    # 5. Verificações
    print(f"📊 Status do Resultado: {result.status.value}")
    
    if len(result.ethics_assessments) > 0:
        print(f"✅ Avaliações éticas realizadas: {len(result.ethics_assessments)}")
        for assessment in result.ethics_assessments:
            print(f"  - {assessment.rule_name}: {assessment.result.value}")
    else:
        print("❌ Nenhuma avaliação ética realizada!")
    
    # Verificar audit trail
    audit_trail = core.ethics_module.get_audit_trail()
    print(f"✅ Audit trail registrado: {len(audit_trail)} entradas")
    
    # 6. Teste de Bloqueio Ético
    print("\n🚫 Testando Bloqueio Ético (Violação de Privacidade)")
    bad_transaction = {
        "transaction_id": "tx_bad_001",
        "data_type": "facial_recognition",
        "action": "store",
        "consent_given": False  # Violação crítica
    }
    
    print(f"🔄 Processando transação maliciosa...")
    bad_result = await core.process_context(bad_transaction, context)
    
    print(f"📊 Status do Resultado: {bad_result.status.value}")
    
    # Deve ser bloqueado ou marcado como falha ética
    if bad_result.status.value in ["ethics_blocked", "failed", "blocked"]:
        print(f"✅ SUCESSO: Transação anti-ética bloqueada corretamente!")
    else:
        print(f"❌ FALHA: Transação anti-ética NÃO foi bloqueada! Status: {bad_result.status.value}")
        # Debug das avaliações
        for assessment in bad_result.ethics_assessments:
            print(f"  - {assessment.rule_name}: {assessment.result.value} ({assessment.reason})")
    
    print("\n✨ Teste E2E concluído!")

if __name__ == "__main__":
    asyncio.run(test_e2e_transaction_flow())
