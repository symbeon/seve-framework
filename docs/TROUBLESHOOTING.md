# Troubleshooting Guide - SEVE Framework

**SEVE Framework v1.0.0**  
**Última Atualização**: 2025-01-29

---

## 📋 **Índice de Problemas**

- [Instalação](#problemas-de-instalação)
- [Configuração](#problemas-de-configuração)
- [Blockchain](#problemas-com-blockchain)
- [Módulos SEVE](#problemas-com-módulos-seve)
- [Performance](#problemas-de-performance)
- [Testes](#problemas-com-testes)

---

## 🔍 **Problemas por Categoria**

## Problemas de Instalação

### Erro: "ModuleNotFoundError: No module named 'seve_framework'"

**Sintoma**: Ao tentar importar SEVE, recebe erro de módulo não encontrado.

**Causa**: Framework não foi instalado ou não está no PATH do Python.

**Solução**:
```bash
# 1. Instalar em modo desenvolvimento
pip install -e .

# 2. Verificar instalação
python -c "from seve_framework import SEVECoreV3; print('✅ Instalado')"

# 3. Se ainda não funcionar, verificar PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
```

**Prevenção**: Sempre instale o framework antes de usar:
```bash
pip install -e .
```

---

### Erro: "Failed to build wheel for opencv-python"

**Sintoma**: Falha ao instalar OpenCV durante `pip install -e .`

**Causa**: OpenCV requer compilação ou dependências do sistema faltando.

**Solução**:

**Windows:**
```bash
pip install opencv-python-headless
```

**Linux:**
```bash
sudo apt-get update
sudo apt-get install python3-opencv
# Ou
pip install opencv-python-headless
```

**Mac:**
```bash
brew install opencv-python
# Ou
pip install opencv-python-headless
```

**Alternativa**: Instalar apenas dependências essenciais primeiro:
```bash
pip install numpy pillow
pip install -e . --no-deps
pip install opencv-python  # Depois, separadamente
```

---

### Erro: "No matching distribution found for torch"

**Sintoma**: PyTorch não instala ou versão incompatível.

**Causa**: PyTorch requer instalação específica por sistema operacional.

**Solução**:

**CPU apenas (mais simples):**
```bash
pip install torch torchvision
```

**GPU (CUDA 11.8):**
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

**Verificar instalação PyTorch:**
```python
import torch
print(torch.__version__)
print(torch.cuda.is_available())  # True se GPU disponível
```

---

### Erro: "Python version must be >= 3.8"

**Sintoma**: Erro durante instalação indicando versão Python incompatível.

**Causa**: Versão do Python muito antiga.

**Solução**:
```bash
# Verificar versão atual
python --version

# SEVE requer Python 3.8+
# Instalar Python 3.11 (recomendado)
# Windows: Baixar de python.org
# Linux: sudo apt-get install python3.11
# Mac: brew install python@3.11
```

---

### Erro ao executar testes: "pytest: command not found"

**Sintoma**: Não consegue executar testes.

**Causa**: Dependências de desenvolvimento não instaladas.

**Solução**:
```bash
# Instalar dependências de desenvolvimento
pip install -e .[dev]
# Ou
pip install pytest pytest-asyncio pytest-cov
```

---

## Problemas de Configuração

### Erro: "Cannot read properties of undefined" (Hardhat)

**Sintoma**: Hardhat não consegue ler variáveis de ambiente.

**Causa**: `dotenv` não carregado ou `.env` não existe.

**Solução**:
```bash
# 1. Verificar se dotenv está instalado
npm install dotenv

# 2. Verificar se está no hardhat.config.js
# Deve ter no início:
require("dotenv").config();

# 3. Verificar se .env existe
ls -la .env  # Linux/Mac
dir .env    # Windows

# 4. Testar carregamento
node -e "require('dotenv').config(); console.log(process.env.PRIVATE_KEY)"
```

---

### Erro: ".env não está sendo lido"

**Sintoma**: Variáveis de ambiente não são carregadas.

**Solução**:
```bash
# 1. Verificar se arquivo existe
ls -la .env

# 2. Verificar permissões (Linux/Mac)
chmod 600 .env  # Apenas leitura/escrita pelo dono

# 3. Verificar formato do arquivo
# Deve estar na raiz do projeto
# Formato correto: CHAVE=valor (sem espaços)

# 4. Verificar se está no .gitignore
grep "^\.env$" .gitignore

# 5. Testar manualmente
node -e "require('dotenv').config(); console.log(Object.keys(process.env).filter(k => k.includes('SEVE') || k.includes('PRIVATE')))"
```

**Formato correto do .env:**
```env
PRIVATE_KEY=ac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80
ALCHEMY_URL=https://eth-sepolia.g.alchemy.com/v2/YOUR_KEY
```

---

### Erro: "Invalid account" ou "Invalid private key"

**Sintoma**: Chave privada rejeitada durante deploy.

**Causa**: Formato incorreto da chave privada.

**Solução**:
```bash
# Verificar formato (deve ter 64 caracteres hex, SEM 0x)
# No .env, deve ser:
PRIVATE_KEY=ac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80

# Se tiver 0x no início, remova:
# ERRADO: PRIVATE_KEY=0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80
# CORRETO: PRIVATE_KEY=ac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80

# Validar formato
node -e "
const key = process.env.PRIVATE_KEY || '';
console.log('Length:', key.length);
console.log('Is hex:', /^[0-9a-f]{64}$/i.test(key));
"
```

---

### Erro: Variáveis de ambiente não definidas

**Sintoma**: Scripts falham porque variáveis não estão definidas.

**Solução**:
```bash
# 1. Carregar .env manualmente antes de executar
export $(cat .env | xargs)
python seu_script.py

# 2. Ou usar python-dotenv no código Python
from dotenv import load_dotenv
load_dotenv()

# 3. Validar que variáveis estão carregadas
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('PRIVATE_KEY:', 'OK' if os.getenv('PRIVATE_KEY') else 'MISSING')"
```

---

## Problemas com Blockchain

### Erro HH110: "Invalid project ID"

**Sintoma**: Erro ao conectar com rede blockchain via Hardhat.

**Causa**: RPC URL incorreta ou API key inválida.

**Solução**:

**Opção 1: Usar RPC Público (Gratuito, mas limitado)**
```javascript
// hardhat.config.js
networks: {
  sepolia: {
    url: "https://rpc.sepolia.org",  // RPC público
    accounts: [process.env.PRIVATE_KEY],
  }
}
```

**Opção 2: Configurar Alchemy (Recomendado)**
```bash
# 1. Obter API key em https://www.alchemy.com/
# 2. Adicionar no .env:
ALCHEMY_URL=https://eth-sepolia.g.alchemy.com/v2/YOUR_API_KEY

# 3. Usar no hardhat.config.js:
url: process.env.ALCHEMY_URL || "https://rpc.sepolia.org"
```

Veja [RPC_PROVIDERS.md](./RPC_PROVIDERS.md) para comparação completa de provedores.

---

### Erro: "Insufficient funds" ou "insufficient balance"

**Sintoma**: Deploy falha por falta de fundos.

**Causa**: Carteira não tem ETH/tokens suficientes para gas.

**Solução**:

**Para Testnet:**
1. Obter fundos via faucet:
   - **Sepolia**: https://sepoliafaucet.com/
   - **Mumbai**: https://faucet.polygon.technology/
2. Verificar saldo:
```bash
npx hardhat run scripts/check-balance.js --network sepolia
```

**Para Produção:**
1. Adicionar fundos à carteira
2. Verificar saldo antes de deploy
3. Estimar gas costs antes de executar

**Verificar saldo:**
```javascript
const balance = await ethers.provider.getBalance(account);
console.log(`Balance: ${ethers.formatEther(balance)} ETH`);
```

---

### Erro: "Network not configured"

**Sintoma**: Rede blockchain não encontrada no hardhat.config.js.

**Causa**: Rede não está configurada ou nome incorreto.

**Solução**:
```javascript
// hardhat.config.js deve ter a rede configurada:
networks: {
  sepolia: {
    url: process.env.ALCHEMY_URL || "https://rpc.sepolia.org",
    accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
    chainId: 11155111,  // Importante!
  }
}

// Verificar se rede existe
npx hardhat networks
```

---

### Erro: "deployed() is not a function" ou "waitForDeployment()"

**Sintoma**: Erro ao aguardar deploy do contrato.

**Causa**: Mudança na API do Ethers.js v6.

**Solução**:

**Ethers.js v6 (correto):**
```javascript
const contract = await MyContract.deploy(args);
await contract.waitForDeployment();
const address = await contract.getAddress();
```

**Ethers.js v5 (antigo):**
```javascript
const contract = await MyContract.deploy(args);
await contract.deployed();
const address = contract.address;
```

**Verificar versão:**
```bash
npm list ethers
```

---

### Erro: "Transaction reverted" durante deploy

**Sintoma**: Transação de deploy é revertida.

**Possíveis causas e soluções**:

1. **Construtor requer argumentos que não foram passados:**
```javascript
// Verificar construtor do contrato
// Passar todos os argumentos necessários
const contract = await MyContract.deploy(arg1, arg2, ...);
```

2. **Gas limit muito baixo:**
```javascript
// Aumentar gas limit
const contract = await MyContract.deploy(args, {
  gasLimit: 5000000  // Ajustar conforme necessário
});
```

3. **Rede incorreta ou Chain ID errado:**
```javascript
// Verificar chain ID da rede
// Sepolia: 11155111
// Mumbai: 80001
```

---

## Problemas com Módulos SEVE

### Erro: "SEVEVisionModule not initialized"

**Sintoma**: Tentativa de usar módulo antes de inicialização.

**Causa**: Módulo precisa ser inicializado com `await initialize()`.

**Solução**:
```python
from seve_framework.vision import SEVEVisionModule
from seve_framework.config import SEVEConfig

config = SEVEConfig()
vision = SEVEVisionModule(config)

# IMPORTANTE: Inicializar antes de usar
await vision.initialize()

# Agora pode usar
result = await vision.process_visual_input(image_data)
```

---

### Erro: "Module 'seve_framework.vision' has no attribute 'process_image'"

**Sintoma**: Método não encontrado no módulo.

**Causa**: Nome do método incorreto ou módulo diferente.

**Solução**:
```python
# Verificar métodos disponíveis
from seve_framework.vision import SEVEVisionModule
import inspect

vision = SEVEVisionModule(config)
await vision.initialize()

# Listar métodos disponíveis
print([m for m in dir(vision) if not m.startswith('_')])

# Método correto é:
result = await vision.process_visual_input(image_data)  # ✅
# Não: vision.process_image()  # ❌
```

---

### Erro: "Ethics validation failed" ou decisões bloqueadas

**Sintoma**: SEVE-Ethics bloqueia operações que parecem válidas.

**Causa**: Configuração de ética muito restritiva ou dados inválidos.

**Solução**:
```python
from seve_framework.config import SEVEConfig, EthicsLevel

# 1. Reduzir nível de ética (temporariamente para debug)
config = SEVEConfig(ethics_level=EthicsLevel.MODERATE)

# 2. Verificar motivo do bloqueio
ethics_result = await ethics_module.validate_decision(decision_data)
for assessment in ethics_result:
    if assessment.result == ValidationResult.BLOCKED:
        print(f"Bloqueado por: {assessment.reason}")
        print(f"Regra: {assessment.rule_name}")
```

**Debug detalhado:**
```python
# Habilitar logs de ética
import logging
logging.getLogger('seve_framework.ethics').setLevel(logging.DEBUG)
```

---

### Erro: "Image processing failed" ou "cv2.error"

**Sintoma**: Erro ao processar imagens com OpenCV.

**Causa**: Imagem inválida, formato não suportado ou OpenCV não instalado corretamente.

**Solução**:
```python
# 1. Verificar se imagem existe e é válida
import cv2
image = cv2.imread("path/to/image.jpg")
if image is None:
    print("❌ Imagem não encontrada ou formato inválido")

# 2. Verificar formato suportado
# Suporta: .jpg, .jpeg, .png, .bmp

# 3. Verificar instalação OpenCV
import cv2
print(f"OpenCV version: {cv2.__version__}")
```

---

### Erro: "Connection failed" em SEVE-Link

**Sintoma**: Falha ao conectar com sistemas externos.

**Causa**: Endpoint incorreto, sem internet ou configuração errada.

**Solução**:
```python
# 1. Verificar conectividade
from seve_framework.link import SEVELinkModule

link = SEVELinkModule(config)
await link.initialize()

# 2. Testar conexão
try:
    await link.test_connection("https://api.example.com")
except Exception as e:
    print(f"Erro de conexão: {e}")
    # Verificar: URL, autenticação, firewall, internet
```

---

## Problemas de Performance

### SEVE está muito lento

**Sintoma**: Processamento demora muito tempo.

**Soluções**:

**1. Usar GPU (se disponível):**
```bash
# Instalar PyTorch com CUDA
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# Verificar se GPU está sendo usada
python -c "import torch; print('CUDA available:', torch.cuda.is_available())"
```

**2. Reduzir tamanho de imagens:**
```python
# Antes de processar, redimensionar
image = cv2.resize(image, (224, 224))  # Reduzir resolução
```

**3. Processamento em batch:**
```python
# Processar múltiplas imagens de uma vez
results = await vision_module.process_batch(image_list)
```

**4. Cache de resultados:**
```python
# Usar cache para evitar reprocessamento
from seve_framework.link import cache_result
```

---

### Erro: "Out of memory" ou "CUDA out of memory"

**Sintoma**: Sistema fica sem memória durante processamento.

**Solução**:

**1. Reduzir batch size:**
```python
# Processar menos imagens por vez
config.batch_size = 4  # Ao invés de 32
```

**2. Liberar memória GPU:**
```python
import torch
torch.cuda.empty_cache()
```

**3. Usar processamento em CPU:**
```python
# Forçar CPU ao invés de GPU
config.device = "cpu"
```

**4. Reduzir resolução de imagens:**
```python
# Processar imagens menores
image = cv2.resize(image, (128, 128))  # Reduzir ainda mais
```

---

## Problemas com Testes

### Erro: "pytest: no tests found"

**Sintoma**: Pytest não encontra testes.

**Causa**: Estrutura de testes incorreta ou pytest não instalado.

**Solução**:
```bash
# 1. Verificar se pytest está instalado
pip install pytest pytest-asyncio

# 2. Executar do diretório raiz
cd SEVE-FRAMEWORK
pytest tests/

# 3. Executar teste específico
pytest tests/test_basic.py -v
```

---

### Erro: "RuntimeError: Event loop is closed" (testes async)

**Sintoma**: Erro ao executar testes assíncronos.

**Causa**: Event loop do asyncio não configurado corretamente.

**Solução**:
```python
# No arquivo de teste, usar pytest-asyncio
import pytest

@pytest.mark.asyncio
async def test_async_function():
    # Seu código async aqui
    result = await seve.process_context(data)
    assert result is not None
```

**Instalar pytest-asyncio:**
```bash
pip install pytest-asyncio
```

---

### Erro: "Module not found" nos testes

**Sintoma**: Testes não encontram módulos do SEVE.

**Causa**: Framework não instalado ou PYTHONPATH incorreto.

**Solução**:
```bash
# 1. Instalar framework primeiro
pip install -e .

# 2. Executar testes do diretório raiz
cd SEVE-FRAMEWORK
pytest tests/

# 3. Verificar imports nos testes
# Devem ser: from seve_framework import ...
```

---

## 🛠️ **Ferramentas de Diagnóstico**

### Verificar Saúde do Sistema

**Python:**
```bash
# Verificar se framework está instalado
python -c "from seve_framework import SEVECoreV3; print('✅ OK')"

# Verificar versão
python -c "from seve_framework import __version__; print(__version__)"

# Verificar capacidades
python -c "from seve_framework import get_capabilities; import json; print(json.dumps(get_capabilities(), indent=2))"
```

**Node.js/Hardhat:**
```bash
# Verificar instalação
npm list hardhat

# Verificar compilação
npm run compile

# Verificar redes configuradas
npx hardhat networks
```

---

### Verificar Configuração

**Validar .env:**
```bash
# Script de validação (criar scripts/validate-env.js)
node scripts/validate-env.js
```

**Validar Python config:**
```python
from seve_framework.config import SEVEConfig

config = SEVEConfig()
print("Mode:", config.mode)
print("Privacy Level:", config.privacy_level)
print("Ethics Level:", config.ethics_level)
```

---

### Logs Detalhados

**Habilitar debug logs:**
```bash
# Python
export SEVE_LOG_LEVEL=DEBUG
python your_script.py

# Ou no código
import logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('seve_framework').setLevel(logging.DEBUG)
```

**Hardhat logs:**
```bash
# Executar com verbose
npx hardhat run scripts/deploy.js --network sepolia --verbose
```

---

### Verificar Dependências

**Python:**
```bash
# Listar dependências instaladas
pip list | grep -E "(torch|opencv|fastapi|pydantic)"

# Verificar versões específicas
pip show torch opencv-python fastapi
```

**Node.js:**
```bash
# Verificar dependências
npm list

# Verificar versão específica
npm list hardhat @openzeppelin/contracts
```

---

## 📊 **Checklist de Diagnóstico Rápido**

Execute estes comandos para diagnosticar problemas comuns:

```bash
# 1. Verificar Python
python --version  # Deve ser 3.8+

# 2. Verificar instalação SEVE
python -c "from seve_framework import __version__; print(__version__)"

# 3. Verificar Node.js
node --version  # Deve ser 16+

# 4. Verificar Hardhat
npx hardhat --version

# 5. Verificar .env
[ -f .env ] && echo "✅ .env exists" || echo "❌ .env missing"

# 6. Validar .env
node scripts/validate-env.js  # Se existir

# 7. Verificar compilação de contratos
npm run compile

# 8. Verificar testes Python
pytest tests/test_sanity.py -v

# 9. Verificar testes Solidity
npm run test
```

---

## 📞 **Precisa de Mais Ajuda?**

Se você não conseguiu resolver seu problema:

1. **Verificar FAQ**: [FAQ.md](./FAQ.md) - Perguntas frequentes
2. **Verificar Documentação**: [INDEX.md](./INDEX.md) - Índice completo
3. **GitHub Issues**: [Reportar problema](https://github.com/symbeon/seve-framework/issues)
   - Inclua: versão Python, versão Node, mensagem de erro completa, steps para reproduzir
4. **Comunidade**: [Discord/Telegram](https://community.seve-framework.ai)
5. **Email**: research@symbeon-tech.com

**Ao reportar problemas, inclua**:
- Versão do Python (`python --version`)
- Versão do Node.js (`node --version`)
- Versão do SEVE (`python -c "from seve_framework import __version__; print(__version__)"`)
- Mensagem de erro completa
- Passos para reproduzir o problema
- Sistema operacional

---

**Última Atualização**: 2025-01-29  
**Mantido por**: Equipe EON - Symbeon Tech
