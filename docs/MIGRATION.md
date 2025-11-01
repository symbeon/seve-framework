# Migration Guide - SEVE Framework

**SEVE Framework v1.0.0**  
**Última Atualização**: 2025-01-29

---

## 📋 **Visão Geral**

Este guia ajuda você a migrar entre versões do SEVE Framework, incluindo:
- Breaking changes entre versões
- Mudanças de API
- Atualização de dependências
- Migração de configurações
- Migração de smart contracts

---

## 🔄 **Migração Entre Versões**

### v0.x → v1.0.0

**Status**: ⚠️ **Breaking Changes**

Esta é a primeira versão estável (Production Ready) do SEVE Framework. Versões anteriores (v0.x) eram experimentais.

#### Breaking Changes Principais

**1. Renomeação de Classes e Módulos**

```python
# ❌ v0.x (Antigo)
from seve_framework import SEVECoreV2, SEVEUniversal

# ✅ v1.0.0 (Novo)
from seve_framework import SEVECoreV3, SEVEHybridFramework
```

**2. Mudanças na Configuração**

```python
# ❌ v0.x
config = SEVEConfig(mode="universal", privacy="high")

# ✅ v1.0.0
from seve_framework.config import SEVEConfig, SEVEMode, PrivacyLevel
config = SEVEConfig(
    mode=SEVEMode.UNIVERSAL,
    privacy_level=PrivacyLevel.HIGH
)
```

**3. Mudanças em SEVE-Vision**

```python
# ❌ v0.x
result = vision.process_image("image.jpg")

# ✅ v1.0.0
result = await vision.process_visual_input("image.jpg")
```

**4. Mudanças em SEVE-Ethics**

```python
# ❌ v0.x
validation = ethics.validate(decision_data)

# ✅ v1.0.0
validation = await ethics.validate_decision(decision_data)
```

**5. Smart Contracts - Novo Deploy Necessário**

Smart contracts foram redesenhados. **Não há compatibilidade com versões anteriores**.

**Ação**: Fazer novo deploy dos contratos.

---

### Checklist de Migração v0.x → v1.0.0

- [ ] **Atualizar Dependências**
  ```bash
  pip install --upgrade seve-framework
  npm install --save-dev @openzeppelin/contracts@latest
  ```

- [ ] **Revisar Imports**
  - Verificar todos os imports de `seve_framework`
  - Atualizar para novas classes (SEVECoreV3, SEVEHybridFramework)

- [ ] **Atualizar Configurações**
  - Converter strings para Enums (SEVEMode, PrivacyLevel, EthicsLevel)
  - Revisar `config/default.yaml`

- [ ] **Atualizar Código Assíncrono**
  - Adicionar `await` onde necessário
  - Verificar uso de `async`/`await` em todas as chamadas de módulos

- [ ] **Atualizar Configurações de Blockchain**
  - Revisar `hardhat.config.js`
  - Verificar variáveis de ambiente em `.env`
  - Fazer novo deploy de contratos (não há migração automática)

- [ ] **Atualizar Testes**
  - Atualizar testes para novas APIs
  - Usar `pytest-asyncio` para testes assíncronos
  - Atualizar mocks e fixtures

- [ ] **Revisar Documentação**
  - Atualizar exemplos de código
  - Revisar README e guias

- [ ] **Executar Testes**
  ```bash
  pytest tests/ -v
  npm run test
  ```

---

## 🔧 **Guia Passo a Passo**

### Passo 1: Backup

Antes de iniciar a migração:

```bash
# Fazer backup do projeto
cp -r seve-project seve-project-backup

# Fazer backup de configurações
cp config/default.yaml config/default.yaml.backup
cp .env .env.backup
```

---

### Passo 2: Atualizar Dependências Python

```bash
# Atualizar pip
pip install --upgrade pip setuptools wheel

# Atualizar SEVE Framework
pip install --upgrade seve-framework

# Verificar versão
python -c "from seve_framework import __version__; print(__version__)"
# Deve mostrar: 1.0.0
```

---

### Passo 3: Atualizar Dependências Node.js

```bash
# Atualizar pacotes
npm update

# Verificar versões
npm list @openzeppelin/contracts
npm list hardhat
```

---

### Passo 4: Atualizar Código Python

#### 4.1 Atualizar Imports

```python
# Antes (v0.x)
from seve_framework.core import SEVECoreV2
from seve_framework.vision import SEVEVision
from seve_framework.ethics import GuardFlow

# Depois (v1.0.0)
from seve_framework import (
    SEVEHybridFramework,
    SEVECoreV3,
    SEVEVisionModule,
    SEVEEthicsModule
)
```

#### 4.2 Atualizar Configuração

```python
# Antes (v0.x)
config = {
    "mode": "universal",
    "privacy": "high",
    "ethics": "strict"
}

# Depois (v1.0.0)
from seve_framework.config import SEVEConfig, SEVEMode, PrivacyLevel, EthicsLevel

config = SEVEConfig(
    mode=SEVEMode.UNIVERSAL,
    privacy_level=PrivacyLevel.HIGH,
    ethics_level=EthicsLevel.STRICT
)
```

#### 4.3 Atualizar Inicialização

```python
# Antes (v0.x)
framework = SEVECoreV2(config)
framework.init()

# Depois (v1.0.0)
framework = SEVEHybridFramework(config)
await framework.initialize()
```

#### 4.4 Atualizar Chamadas de Módulos

```python
# Antes (v0.x)
result = vision.process_image("image.jpg")
validation = ethics.validate(decision_data)

# Depois (v1.0.0)
result = await vision.process_visual_input("image.jpg")
validation = await ethics.validate_decision(decision_data)
```

---

### Passo 5: Atualizar Smart Contracts

**⚠️ IMPORTANTE**: Smart contracts não são compatíveis com versões anteriores. É necessário fazer novo deploy.

#### 5.1 Backup de Endereços Antigos

```javascript
// Salvar endereços dos contratos antigos
const oldContracts = {
    token: "0x...", // Endereço antigo
    protocol: "0x...",
    dao: "0x..."
};
```

#### 5.2 Deploy Novos Contratos

```bash
# Compilar novos contratos
npm run compile

# Deploy em testnet primeiro (recomendado)
npx hardhat run scripts/deploy-token.js --network sepolia
npx hardhat run scripts/deploy-protocol.js --network sepolia
npx hardhat run scripts/deploy-dao.js --network sepolia
```

#### 5.3 Atualizar Configurações

```javascript
// Atualizar endereços nos arquivos de configuração
const NEW_CONTRACTS = {
    token: "0x...", // Novo endereço
    protocol: "0x...",
    dao: "0x..."
};
```

#### 5.4 Migração de Dados (se aplicável)

Se você tinha dados em contratos antigos:
- Tokens: Usuários precisam transferir tokens para novo contrato (ou emitir novos)
- Licenças: Precisam ser reemitidas no novo protocolo
- Propostas DAO: Não são migráveis, novas propostas devem ser criadas

---

### Passo 6: Atualizar Configurações

#### 6.1 Arquivo de Configuração YAML

```yaml
# config/default.yaml (v1.0.0)
mode: universal  # ou "hybrid", "vision_specific"
privacy_level: high  # ou "minimal", "standard", "maximum"
ethics_level: strict  # ou "basic", "standard", "maximum"
debug: false
```

#### 6.2 Variáveis de Ambiente

```bash
# .env - Verificar e atualizar
SEVE_MODE=universal
SEVE_ETHICS_LEVEL=strict
SEVE_LOG_LEVEL=INFO

# Blockchain
ALCHEMY_URL=https://eth-sepolia.g.alchemy.com/v2/YOUR_KEY
PRIVATE_KEY=your_key_here
```

---

### Passo 7: Atualizar Testes

#### 7.1 Testes Python

```python
# tests/test_basic.py (v1.0.0)
import pytest
from seve_framework import SEVEHybridFramework, SEVEConfig

@pytest.mark.asyncio
async def test_framework():
    config = SEVEConfig()
    framework = SEVEHybridFramework(config)
    await framework.initialize()
    
    # Testar funcionalidades
    result = await framework.process_context(data, context)
    assert result.status == ProcessingStatus.COMPLETED
```

#### 7.2 Testes de Smart Contracts

```javascript
// test/SEVEToken.test.js
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("SEVEToken", function () {
    it("Should deploy with correct supply", async function () {
        const SEVEToken = await ethers.getContractFactory("SEVEToken");
        const token = await SEVEToken.deploy();
        await token.waitForDeployment();
        
        const totalSupply = await token.totalSupply();
        expect(totalSupply).to.equal(ethers.parseEther("1000000000"));
    });
});
```

---

### Passo 8: Validação

#### 8.1 Testes Automatizados

```bash
# Python
pytest tests/ -v --cov=src/seve_framework

# Smart Contracts
npm run test
```

#### 8.2 Testes Manuais

1. **Verificar Inicialização**
   ```python
   from seve_framework import SEVEHybridFramework, SEVEConfig
   framework = SEVEHybridFramework(SEVEConfig())
   await framework.initialize()
   print("✅ Framework inicializado")
   ```

2. **Verificar Módulos**
   ```python
   assert framework.vision_module is not None
   assert framework.ethics_module is not None
   # etc.
   ```

3. **Verificar Smart Contracts**
   ```bash
   npx hardhat verify --network sepolia <CONTRACT_ADDRESS>
   ```

---

## 📊 **Tabela de Compatibilidade**

| Versão | Python | Node.js | Breaking Changes | Migração |
|--------|--------|---------|------------------|----------|
| v0.1.0 | 3.8+ | 16+ | - | - |
| v0.2.0 | 3.8+ | 16+ | Alguns | Manual |
| v1.0.0 | 3.8+ | 16+ | ⚠️ Muitos | Este guia |

---

## ⚠️ **Problemas Comuns**

### Erro: "Module not found: seve_framework"

**Causa**: Framework não foi instalado corretamente.

**Solução**:
```bash
pip install -e .
# Ou
pip install seve-framework
```

---

### Erro: "AttributeError: 'SEVECoreV2' has no attribute 'initialize'"

**Causa**: Usando API antiga (v0.x).

**Solução**: Atualizar para `SEVECoreV3` ou `SEVEHybridFramework` e usar `await initialize()`.

---

### Erro: "TypeError: object NoneType can't be used in 'await' expression"

**Causa**: Esquecendo de adicionar `await` ou função não é async.

**Solução**: Verificar se função é `async` e usar `await` corretamente.

---

### Erro: "Invalid contract address"

**Causa**: Endereço do contrato não foi atualizado após deploy.

**Solução**: Atualizar endereços nos arquivos de configuração.

---

## 🔄 **Migração de Dados**

### Migração de Configurações

Se você tinha configurações customizadas em v0.x:

```python
# Script de migração
import yaml

def migrate_config(old_config_path, new_config_path):
    with open(old_config_path) as f:
        old_config = yaml.safe_load(f)
    
    new_config = {
        "mode": map_mode(old_config.get("mode", "universal")),
        "privacy_level": map_privacy(old_config.get("privacy", "standard")),
        "ethics_level": map_ethics(old_config.get("ethics", "standard"))
    }
    
    with open(new_config_path, 'w') as f:
        yaml.dump(new_config, f)

def map_mode(old_mode):
    mapping = {
        "universal": "universal",
        "vision": "vision_specific",
        "hybrid": "hybrid"
    }
    return mapping.get(old_mode, "universal")
```

---

## 📚 **Referências**

- [CHANGELOG.md](../CHANGELOG.md) - Histórico completo de mudanças
- [API Reference](./api/README.md) - Documentação completa da API
- [FAQ](./FAQ.md) - Perguntas frequentes sobre migração
- [Troubleshooting](./TROUBLESHOOTING.md) - Problemas comuns

---

## 🆘 **Precisa de Ajuda?**

Se você encontrar problemas durante a migração:

1. **Verificar Documentação**: [INDEX.md](./INDEX.md)
2. **FAQ**: [FAQ.md](./FAQ.md)
3. **Troubleshooting**: [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)
4. **GitHub Issues**: [Reportar problema](https://github.com/symbeon/seve-framework/issues)
5. **Comunidade**: [Discord/Telegram](https://community.seve-framework.ai)

---

**Última Atualização**: 2025-01-29  
**Mantido por**: Equipe EON - Symbeon Tech

