# Testing Guide - SEVE Framework

**SEVE Framework v1.0.0**  
**Última Atualização**: 2025-01-29

---

## 📋 **Visão Geral**

Este guia completo explica como testar o SEVE Framework, incluindo:
- Estrutura de testes
- Como executar testes
- Como escrever novos testes
- Testes de smart contracts
- Cobertura e qualidade

---

## 🏗️ **Estrutura de Testes**

### Organização

```
SEVE-FRAMEWORK/
├── tests/                    # Testes Python
│   ├── test_basic.py        # Testes básicos
│   ├── test_comprehensive.py # Testes abrangentes
│   └── test_sanity.py       # Testes de sanidade
├── test/                     # Testes Solidity
│   └── SEVEToken.test.js    # Testes de smart contracts
└── pytest.ini               # Configuração pytest
```

---

## 🧪 **Tipos de Testes**

### 1. Testes Unitários

Testam componentes individuais isoladamente.

**Exemplo**:
```python
import pytest
from seve_framework.config import SEVEConfig, SEVEMode, PrivacyLevel

@pytest.mark.asyncio
async def test_config_creation():
    """Testa criação de configuração"""
    config = SEVEConfig(
        mode=SEVEMode.HYBRID,
        privacy_level=PrivacyLevel.HIGH
    )
    assert config.mode == SEVEMode.HYBRID
    assert config.privacy_level == PrivacyLevel.HIGH
```

---

### 2. Testes de Integração

Testam interação entre múltiplos módulos.

**Exemplo**:
```python
import pytest
from seve_framework import SEVEHybridFramework, SEVEConfig

@pytest.mark.asyncio
async def test_framework_integration():
    """Testa integração entre módulos"""
    config = SEVEConfig()
    framework = SEVEHybridFramework(config)
    await framework.initialize()
    
    data = {
        "visual": {"image": "test.jpg"},
        "sensor": {"temperature": 25.0}
    }
    
    result = await framework.process_context(data)
    assert result.status == ProcessingStatus.COMPLETED
```

---

### 3. Testes End-to-End (E2E)

Testam fluxos completos do sistema.

**Exemplo**:
```python
@pytest.mark.asyncio
async def test_full_pipeline():
    """Testa pipeline completo: Vision -> Ethics -> Link"""
    framework = SEVEHybridFramework(SEVEConfig())
    await framework.initialize()
    
    # Simular fluxo completo
    image_data = load_test_image()
    result = await framework.process_context({
        "visual": {"image": image_data}
    })
    
    # Validar resultado completo
    assert result.status == ProcessingStatus.COMPLETED
    assert result.ethics_assessments  # Deve ter avaliações éticas
```

---

### 4. Testes de Ética

Testam validação ética e bloqueios.

**Exemplo**:
```python
@pytest.mark.ethics
@pytest.mark.asyncio
async def test_ethics_blocking():
    """Testa bloqueio de operações não éticas"""
    ethics = SEVEEthicsModule(SEVEConfig(ethics_level=EthicsLevel.STRICT))
    await ethics.initialize()
    
    decision = {
        "action": "store_facial_data",
        "consent": False
    }
    
    validation = await ethics.validate_decision(decision)
    assert validation.result == ValidationResult.BLOCKED
```

---

### 5. Testes de Performance

Testam velocidade e uso de recursos.

**Exemplo**:
```python
@pytest.mark.performance
@pytest.mark.asyncio
async def test_processing_performance():
    """Testa performance de processamento"""
    framework = SEVEHybridFramework(SEVEConfig())
    await framework.initialize()
    
    import time
    start = time.time()
    
    for _ in range(100):
        await framework.process_context(test_data)
    
    elapsed = time.time() - start
    assert elapsed < 10.0  # Deve processar 100 itens em <10s
```

---

## 🚀 **Como Executar Testes**

### Python Tests

#### Todos os Testes
```bash
pytest tests/ -v
```

#### Testes Específicos
```bash
# Por arquivo
pytest tests/test_basic.py -v

# Por marcador
pytest tests/ -m ethics -v
pytest tests/ -m vision -v
pytest tests/ -m integration -v

# Por padrão de nome
pytest tests/ -k "test_config" -v
```

#### Com Cobertura
```bash
# Cobertura completa
pytest tests/ --cov=src/seve_framework --cov-report=html

# Ver relatório
open htmlcov/index.html  # Mac/Linux
start htmlcov/index.html # Windows
```

#### Testes Verbosos
```bash
pytest tests/ -v -s  # -s mostra prints
pytest tests/ -vv    # Muito verboso
```

---

### Solidity Tests (Hardhat)

#### Todos os Testes
```bash
npm run test
# Ou
npx hardhat test
```

#### Testes Específicos
```bash
# Por arquivo
npx hardhat test test/SEVEToken.test.js

# Por padrão
npx hardhat test --grep "stake"
```

#### Testes Verbosos
```bash
npx hardhat test --verbose
```

#### Gas Reporting
```bash
REPORT_GAS=true npx hardhat test
```

---

## 📝 **Como Escrever Testes**

### Estrutura de Teste Python

```python
import pytest
from seve_framework import SEVEConfig, SEVEHybridFramework

class TestMyComponent:
    """Test suite para MyComponent"""
    
    @pytest.fixture
    def config(self):
        """Fixture de configuração"""
        return SEVEConfig()
    
    @pytest.fixture
    def component(self, config):
        """Fixture do componente"""
        return MyComponent(config)
    
    @pytest.mark.asyncio
    async def test_basic_functionality(self, component):
        """Testa funcionalidade básica"""
        await component.initialize()
        result = await component.do_something()
        assert result is not None
    
    @pytest.mark.parametrize("input_value,expected", [
        (1, 2),
        (2, 4),
        (3, 6),
    ])
    def test_parametrized(self, input_value, expected):
        """Teste parametrizado"""
        assert input_value * 2 == expected
```

---

### Estrutura de Teste Solidity

```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("SEVEToken", function () {
    let token;
    let owner;
    let addr1;
    let addr2;

    beforeEach(async function () {
        [owner, addr1, addr2] = await ethers.getSigners();
        
        const SEVEToken = await ethers.getContractFactory("SEVEToken");
        token = await SEVEToken.deploy();
        await token.waitForDeployment();
    });

    describe("Deployment", function () {
        it("Should set the right owner", async function () {
            expect(await token.owner()).to.equal(owner.address);
        });

        it("Should assign the total supply to owner", async function () {
            const totalSupply = await token.totalSupply();
            expect(await token.balanceOf(owner.address)).to.equal(totalSupply);
        });
    });

    describe("Staking", function () {
        it("Should allow staking tokens", async function () {
            const amount = ethers.parseEther("1000");
            await token.stake(amount);
            
            expect(await token.stakedAmount(owner.address)).to.equal(amount);
        });
    });
});
```

---

## 🎯 **Fixtures e Mocks**

### Fixtures Python

```python
import pytest
from unittest.mock import Mock, AsyncMock

@pytest.fixture
def mock_vision_module():
    """Mock do módulo Vision"""
    mock = AsyncMock(spec=SEVEVisionModule)
    mock.process_visual_input.return_value = {
        "detected_objects": ["person", "car"],
        "faces_detected": 0,
        "anonymization_applied": True
    }
    return mock

@pytest.fixture
def mock_ethics_module():
    """Mock do módulo Ethics"""
    mock = AsyncMock(spec=SEVEEthicsModule)
    mock.validate_decision.return_value = ValidationResult.APPROVED
    return mock

@pytest.mark.asyncio
async def test_with_mocks(mock_vision_module, mock_ethics_module):
    """Teste usando mocks"""
    result = await mock_vision_module.process_visual_input("test.jpg")
    assert result["faces_detected"] == 0
```

---

### Fixtures Hardhat

```javascript
// fixtures.js
async function deployTokenFixture() {
    const [owner, addr1, addr2] = await ethers.getSigners();
    
    const SEVEToken = await ethers.getContractFactory("SEVEToken");
    const token = await SEVEToken.deploy();
    await token.waitForDeployment();
    
    return { token, owner, addr1, addr2 };
}

// Reutilizar em testes
const { loadFixture } = require("@nomicfoundation/hardhat-network-helpers");

describe("SEVEToken", function () {
    it("Should work with fixture", async function () {
        const { token, owner } = await loadFixture(deployTokenFixture);
        expect(await token.owner()).to.equal(owner.address);
    });
});
```

---

## 📊 **Marcadores de Teste**

### Marcadores Python (pytest)

```python
# pytest.ini define marcadores:
# markers =
#     unit: Unit tests
#     integration: Integration tests
#     ethics: Ethics-related tests
#     vision: Vision module tests
#     performance: Performance tests
#     slow: Slow running tests

@pytest.mark.unit
def test_unit():
    pass

@pytest.mark.integration
@pytest.mark.asyncio
async def test_integration():
    pass

@pytest.mark.ethics
def test_ethics():
    pass

@pytest.mark.slow
def test_slow():
    pass  # Pular com: pytest -m "not slow"
```

---

## 🧩 **Exemplos de Testes Completos**

### Teste de SEVE-Core

```python
import pytest
from seve_framework.core import SEVECoreV3, ProcessingStatus
from seve_framework.config import SEVEConfig

class TestSEVECoreV3:
    @pytest.fixture
    def core(self):
        return SEVECoreV3(SEVEConfig())
    
    @pytest.mark.asyncio
    async def test_initialization(self, core):
        """Testa inicialização"""
        assert not core.is_initialized
        await core.initialize()
        assert core.is_initialized
    
    @pytest.mark.asyncio
    async def test_process_context(self, core):
        """Testa processamento de contexto"""
        await core.initialize()
        
        data = {"visual": {"image": "test.jpg"}}
        result = await core.process_context(data)
        
        assert result.status in [
            ProcessingStatus.COMPLETED,
            ProcessingStatus.ETHICS_BLOCKED
        ]
```

---

### Teste de SEVE-Vision

```python
import pytest
from seve_framework.vision import SEVEVisionModule
from seve_framework.config import SEVEConfig, PrivacyLevel

class TestSEVEVision:
    @pytest.fixture
    def vision(self):
        config = SEVEConfig(privacy_level=PrivacyLevel.MAXIMUM)
        return SEVEVisionModule(config)
    
    @pytest.mark.asyncio
    async def test_anonymization(self, vision):
        """Testa anonimização automática"""
        await vision.initialize()
        
        # Imagem com faces
        result = await vision.process_visual_input("face_image.jpg")
        
        assert result.anonymization_applied == True
        assert result.faces_detected > 0
```

---

### Teste de SEVE-Ethics

```python
import pytest
from seve_framework.ethics import SEVEEthicsModule, ValidationResult
from seve_framework.config import SEVEConfig, EthicsLevel

class TestSEVEEthics:
    @pytest.fixture
    def ethics(self):
        config = SEVEConfig(ethics_level=EthicsLevel.STRICT)
        return SEVEEthicsModule(config)
    
    @pytest.mark.asyncio
    @pytest.mark.ethics
    async def test_block_facial_recognition(self, ethics):
        """Testa bloqueio de reconhecimento facial"""
        await ethics.initialize()
        
        decision = {
            "action": "facial_recognition",
            "consent": False
        }
        
        validation = await ethics.validate_decision(decision)
        assert validation.result == ValidationResult.BLOCKED
```

---

### Teste de Smart Contract

```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("SEVEToken Staking", function () {
    let token;
    let owner, user1;

    beforeEach(async function () {
        [owner, user1] = await ethers.getSigners();
        
        const SEVEToken = await ethers.getContractFactory("SEVEToken");
        token = await SEVEToken.deploy();
        await token.waitForDeployment();
        
        // Transferir tokens para user1
        await token.transfer(user1.address, ethers.parseEther("10000"));
    });

    it("Should allow staking", async function () {
        const amount = ethers.parseEther("1000");
        await token.connect(user1).stake(amount);
        
        expect(await token.stakedAmount(user1.address)).to.equal(amount);
        expect(await token.isStaking(user1.address)).to.be.true;
    });

    it("Should calculate rewards correctly", async function () {
        await token.connect(user1).stake(ethers.parseEther("1000"));
        
        // Avançar tempo (1 ano)
        await ethers.provider.send("evm_increaseTime", [365 * 24 * 60 * 60]);
        await ethers.provider.send("evm_mine");
        
        const rewards = await token.calculateStakingRewards(user1.address);
        // 10% APY = 100 tokens por ano
        expect(rewards).to.be.closeTo(ethers.parseEther("100"), ethers.parseEther("1"));
    });
});
```

---

## 🔍 **Testes de Segurança**

### Testes Python

```python
@pytest.mark.security
def test_private_key_not_exposed():
    """Testa que chaves privadas não são expostas"""
    # Verificar logs, outputs, etc.
    pass

@pytest.mark.security
def test_sql_injection_protection():
    """Testa proteção contra SQL injection"""
    malicious_input = "'; DROP TABLE users; --"
    # Tentar usar em query
    # Verificar que é sanitizado
    pass
```

---

### Testes Solidity

```javascript
describe("Security", function () {
    it("Should prevent reentrancy attacks", async function () {
        // Testar proteção ReentrancyGuard
    });

    it("Should validate inputs", async function () {
        // Testar que valores inválidos são rejeitados
        await expect(
            token.stake(0)
        ).to.be.revertedWith("Amount must be greater than 0");
    });

    it("Should respect access control", async function () {
        // Testar que apenas owner pode pausar
        await expect(
            token.connect(user1).pause()
        ).to.be.revertedWith("Ownable: caller is not the owner");
    });
});
```

---

## 📈 **Cobertura de Testes**

### Metas de Cobertura

- **Python**: 95%+ de cobertura
- **Solidity**: 95%+ de cobertura
- **Crítico**: 100% de cobertura (ethics, security)

### Verificar Cobertura

```bash
# Python
pytest tests/ --cov=src/seve_framework --cov-report=term-missing

# Ver linhas não cobertas
pytest tests/ --cov=src/seve_framework --cov-report=html
open htmlcov/index.html
```

### Linhas Não Cobertas

Se houver linhas não cobertas, adicionar testes:

```python
# Exemplo: Cobrir edge case
@pytest.mark.asyncio
async def test_edge_case_not_covered():
    """Cobre linha específica não testada"""
    # Teste que executa código não coberto
    pass
```

---

## ⚙️ **Configuração**

### pytest.ini

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
asyncio_mode = auto
markers =
    unit: Unit tests
    integration: Integration tests
    ethics: Ethics-related tests
    vision: Vision module tests
    performance: Performance tests
    slow: Slow running tests
    security: Security tests
```

### hardhat.config.js (Test Config)

```javascript
module.exports = {
    solidity: "0.8.19",
    networks: {
        hardhat: {
            chainId: 31337,
            forking: {
                url: process.env.ALCHEMY_URL
            }
        }
    },
    mocha: {
        timeout: 20000
    }
};
```

---

## 🔄 **CI/CD Integration**

### GitHub Actions Example

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  test-python:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - run: pip install -e .[dev]
      - run: pytest tests/ --cov=src/seve_framework
      
  test-solidity:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
        with:
          node-version: '18'
      - run: npm install
      - run: npm run test
```

---

## 🐛 **Troubleshooting de Testes**

### Problema: "RuntimeError: Event loop is closed"

**Solução**: Usar `pytest-asyncio` corretamente:
```python
@pytest.mark.asyncio
async def test_async():
    # Código async
    pass
```

---

### Problema: "ModuleNotFoundError"

**Solução**: Instalar framework em modo desenvolvimento:
```bash
pip install -e .
```

---

### Problema: Testes muito lentos

**Solução**: Usar mocks para operações lentas:
```python
@patch('seve_framework.vision.load_model')
async def test_with_mock(mock_load):
    mock_load.return_value = Mock()
    # Teste rápido
```

---

## 📚 **Boas Práticas**

### 1. Nomes Descritivos
```python
# ✅ Bom
def test_vision_module_anonymizes_faces_automatically():

# ❌ Ruim
def test_vision():
```

### 2. Um Teste, Uma Coisa
```python
# ✅ Bom - Testa uma coisa
def test_staking_allows_deposit():
    pass

def test_staking_calculates_rewards():
    pass

# ❌ Ruim - Testa múltiplas coisas
def test_staking():
    # Testa deposit, rewards, unstake, etc.
    pass
```

### 3. Arrange-Act-Assert
```python
def test_example():
    # Arrange: Preparar
    config = SEVEConfig()
    framework = SEVEHybridFramework(config)
    
    # Act: Executar
    result = await framework.process_context(data)
    
    # Assert: Verificar
    assert result.status == ProcessingStatus.COMPLETED
```

### 4. Usar Fixtures
```python
# ✅ Bom - Reutilizar configuração
@pytest.fixture
def framework():
    return SEVEHybridFramework(SEVEConfig())

# ❌ Ruim - Repetir código
def test_one():
    framework = SEVEHybridFramework(SEVEConfig())
    # ...

def test_two():
    framework = SEVEHybridFramework(SEVEConfig())  # Repetido
    # ...
```

---

## 📞 **Recursos Adicionais**

- [pytest Documentation](https://docs.pytest.org/)
- [Hardhat Testing Guide](https://hardhat.org/hardhat-runner/docs/guides/test-contracts)
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Padrões de contribuição
- [API Reference](./api/README.md) - Documentação da API

---

**Última Atualização**: 2025-01-29  
**Mantido por**: Equipe EON - Symbeon Tech

