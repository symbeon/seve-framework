# 🚀 SEVE Framework - Quick Start Guide
## Inicie em 5 Minutos

Este guia vai te ajudar a rodar sua primeira validação ética com o SEVE Framework.

---

### 1️⃣ Instalação

**Pré-requisitos**: Python 3.8+

```bash
# 1. Clone o repositório
git clone https://github.com/symbeon/seve-framework.git
cd seve-framework

# 2. Crie um ambiente virtual (recomendado)
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt
```

---

### 2️⃣ Sua Primeira Validação Ética

Crie um arquivo chamado `meu_teste.py`:

```python
import asyncio
from seve_framework import SEVECoreV3, SEVEConfig, EthicsLevel

async def main():
    # 1. Configurar o framework
    config = SEVEConfig(
        ethics_level=EthicsLevel.STRICT,  # Nível rigoroso
        guardflow_enabled=True            # Ativar bloqueio preventivo
    )
    
    # 2. Inicializar o core
    print("🔄 Inicializando SEVE...")
    core = SEVECoreV3(config)
    await core.initialize()
    
    # 3. Definir uma transação de exemplo (com violação de privacidade)
    transacao_risco = {
        "id": "tx_123",
        "tipo": "reconhecimento_facial",
        "dados": "imagem_face_raw.jpg",
        "consentimento": False  # ❌ VIOLAÇÃO!
    }
    
    # 4. Processar
    print(f"\n🔍 Analisando transação: {transacao_risco['id']}")
    resultado = await core.process_context(transacao_risco, context={})
    
    # 5. Ver resultado
    if resultado.status == "ethics_blocked":
        print(f"✅ SUCESSO: O sistema bloqueou uma violação ética!")
        print(f"🛑 Motivo: {resultado.reason}")
        print(f"📋 Audit ID: {resultado.audit_id}")
    else:
        print(f"⚠️ ALERTA: A transação passou (não esperado).")

if __name__ == "__main__":
    asyncio.run(main())
```

Execute:
```bash
python meu_teste.py
```

---

### 3️⃣ Usando a CLI (Interface de Linha de Comando)

O SEVE possui uma CLI poderosa para operações rápidas.

```bash
# 1. Inicializar configuração
python seve_cli.py init --ethics-level balanced

# 2. Verificar status dos módulos
python seve_cli.py status

# 3. Simular uma validação
python seve_cli.py validate examples/data/sample_transaction.json
```

---

### 4️⃣ Próximos Passos

- 🏥 **[Exemplo Healthcare](examples/healthcare_demo.py)** - Veja como processar dados médicos
- 🛒 **[Exemplo Retail](examples/retail_demo.py)** - Monitoramento de loja sem violar privacidade
- 📚 **[Documentação Completa](README.md)** - Explore a arquitetura

---

**Precisa de ajuda?** Abra uma [Issue](https://github.com/symbeon/seve-framework/issues) no GitHub.
