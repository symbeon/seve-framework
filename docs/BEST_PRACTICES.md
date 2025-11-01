# Best Practices Guide - SEVE Framework

**SEVE Framework v1.0.0**  
**Última Atualização**: 2025-01-29

---

## 📋 **Visão Geral**

Este guia documenta as melhores práticas e convenções para desenvolvimento no SEVE Framework, incluindo:
- Convenções de código Python
- Convenções de código Solidity
- Padrões de arquitetura
- Error handling
- Logging
- Segurança
- Ética

---

## 🐍 **Python Best Practices**

### Convenções de Código

#### PEP 8 Compliance

SEVE Framework segue **PEP 8** como base, com algumas exceções documentadas.

**Indentação**: 4 espaços (nunca tabs)
```python
# ✅ Correto
def function():
    if condition:
        do_something()

# ❌ Errado
def function():
	if condition:  # Tab
		do_something()
```

**Linha máxima**: 100 caracteres (flexível para strings longas)
```python
# ✅ Aceitável
message = (
    "This is a very long message that needs to be split "
    "across multiple lines for better readability"
)
```

**Imports**: Organizados e agrupados
```python
# ✅ Correto
# Standard library
import os
import sys
from pathlib import Path

# Third-party
import numpy as np
import torch

# Local
from seve_framework.core import SEVECoreV3
from seve_framework.config import SEVEConfig
```

---

### Nomenclatura

**Classes**: PascalCase
```python
# ✅ Correto
class SEVEVisionModule:
    pass

class EthicalAssessment:
    pass

# ❌ Errado
class seve_vision_module:  # snake_case
    pass
```

**Funções e Variáveis**: snake_case
```python
# ✅ Correto
def process_visual_input():
    user_data = {}
    processing_result = None

# ❌ Errado
def processVisualInput():  # camelCase
    userData = {}
```

**Constantes**: UPPER_SNAKE_CASE
```python
# ✅ Correto
MAX_BATCH_SIZE = 32
DEFAULT_TIMEOUT = 30
PRIVACY_LEVEL_MAXIMUM = "maximum"

# ❌ Errado
maxBatchSize = 32  # camelCase
default_timeout = 30  # Variável, não constante
```

**Privados**: Prefixo `_`
```python
# ✅ Correto
class MyClass:
    def __init__(self):
        self._internal_state = {}  # Privado
        self.public_attr = None     # Público
    
    def _helper_method(self):      # Método privado
        pass
```

---

### Type Hints

**Sempre usar type hints** em funções públicas e classes.

```python
# ✅ Correto
from typing import Dict, List, Optional, Union

def process_data(
    data: Dict[str, Any],
    context: Optional[Dict[str, Any]] = None
) -> ProcessingResult:
    """Process data with optional context."""
    pass

async def validate_decision(
    decision_data: Dict[str, Any]
) -> EthicsValidationResult:
    """Validate decision ethically."""
    pass
```

**Tipos Complexos**:
```python
from typing import Dict, List, Tuple, Optional, Union
from dataclasses import dataclass

@dataclass
class Result:
    status: str
    data: Dict[str, Any]
    errors: List[str]
```

---

### Async/Await

**Sempre usar async/await** para operações I/O e processamento.

```python
# ✅ Correto
async def process_image(image_data: bytes) -> VisionResult:
    result = await self._detect_objects(image_data)
    return result

# ❌ Errado (bloqueante)
def process_image(image_data: bytes) -> VisionResult:
    result = self._detect_objects(image_data)  # Bloqueia
    return result
```

**Inicialização Assíncrona**:
```python
# ✅ Correto
async def initialize(self) -> None:
    await self.vision_module.initialize()
    await self.ethics_module.initialize()

# ❌ Errado
def initialize(self) -> None:
    self.vision_module.initialize()  # Não é async
```

---

### Error Handling

**Usar exceções específicas** e fornecer mensagens claras.

```python
# ✅ Correto
from seve_framework.exceptions import SEVEValidationError, SEVEProcessingError

async def process_data(data: Dict[str, Any]) -> ProcessingResult:
    if not data:
        raise SEVEValidationError("Data cannot be empty")
    
    try:
        result = await self._process(data)
        return result
    except Exception as e:
        logger.error(f"Error processing data: {e}")
        raise SEVEProcessingError(f"Failed to process data: {e}") from e
```

**Try-Except Específico**:
```python
# ✅ Correto
try:
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {path}")
except FileNotFoundError:
    raise
except Exception as e:
    logger.error(f"Unexpected error loading image: {e}")
    raise

# ❌ Evitar
try:
    # Todo o código
except:  # Muito genérico
    pass  # Silencia erros
```

---

### Logging

**Usar logging estruturado** com níveis apropriados.

```python
import logging

logger = logging.getLogger(__name__)

# ✅ Correto
logger.debug("Processing image: %s", image_path)
logger.info("Framework initialized successfully")
logger.warning("High memory usage: %d MB", memory_usage)
logger.error("Failed to process data: %s", error, exc_info=True)

# ❌ Evitar
print("Error occurred")  # Use logger
logger.error("Error")    # Sem contexto
```

**Estruture logs**:
```python
logger.info(
    "Processing completed",
    extra={
        "processing_time_ms": elapsed,
        "status": result.status,
        "module": "SEVE-Vision"
    }
)
```

---

### Docstrings

**Sempre documentar** classes e funções públicas.

```python
def process_visual_input(
    self,
    image_data: Union[bytes, str, np.ndarray]
) -> VisionProcessingResult:
    """
    Process visual input (image/video) with automatic anonymization.
    
    This method processes images or video frames, detecting objects and
    automatically anonymizing faces and other sensitive data according
    to the configured privacy level.
    
    Args:
        image_data: Image data as bytes, file path, or numpy array
        
    Returns:
        VisionProcessingResult containing:
        - detected_objects: List of detected objects
        - faces_detected: Number of faces detected
        - anonymization_applied: Whether anonymization was applied
        
    Raises:
        SEVEValidationError: If image_data is invalid
        SEVEProcessingError: If processing fails
        
    Example:
        >>> result = await vision.process_visual_input("image.jpg")
        >>> print(result.detected_objects)
        ['person', 'car', 'building']
    """
    pass
```

---

## 🔷 **Solidity Best Practices**

### Style Guide

#### Nomenclatura

**Contratos**: PascalCase
```solidity
// ✅ Correto
contract SEVEToken is ERC20 {
}

// ❌ Errado
contract seveToken {  // camelCase
}
```

**Funções**: camelCase
```solidity
// ✅ Correto
function stakeTokens(uint256 amount) external {
}

function calculateRewards(address user) public view returns (uint256) {
}

// ❌ Errado
function stake_tokens(uint256 amount) {  // snake_case
}
```

**Variáveis**: camelCase
```solidity
// ✅ Correto
uint256 public totalStaked;
mapping(address => uint256) public stakedAmount;

// ❌ Errado
uint256 public total_staked;  // snake_case
```

**Constantes**: UPPER_SNAKE_CASE
```solidity
// ✅ Correto
uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18;
uint256 public constant STAKING_REWARD_RATE = 10;

// ❌ Errado
uint256 public constant totalSupply = ...;  // camelCase
```

---

### Security Patterns

#### Reentrancy Protection

**Sempre usar ReentrancyGuard** para funções que transferem tokens.

```solidity
// ✅ Correto
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract SEVEToken is ERC20, ReentrancyGuard {
    function unstake(uint256 amount) external nonReentrant {
        // Lógica de unstake
        _transfer(address(this), msg.sender, amount);
    }
}

// ❌ Perigoso (sem proteção)
function unstake(uint256 amount) external {
    _transfer(address(this), msg.sender, amount);  // Vulnerável
}
```

#### Checks-Effects-Interactions Pattern

```solidity
// ✅ Correto
function unstake(uint256 amount) external nonReentrant {
    // 1. Checks
    require(amount > 0, "Amount must be greater than 0");
    require(isStaking[msg.sender], "Not staking");
    require(stakedAmount[msg.sender] >= amount, "Insufficient staked");
    
    // 2. Effects (mudar estado primeiro)
    stakedAmount[msg.sender] -= amount;
    totalStaked -= amount;
    
    // 3. Interactions (transferir depois)
    _transfer(address(this), msg.sender, amount);
}
```

#### Input Validation

**Sempre validar inputs**:
```solidity
// ✅ Correto
function stake(uint256 amount) external {
    require(amount > 0, "Amount must be greater than 0");
    require(balanceOf(msg.sender) >= amount, "Insufficient balance");
    // ...
}

// ❌ Errado
function stake(uint256 amount) external {
    // Sem validação
    // ...
}
```

---

### Gas Optimization

#### Use `uint256` por padrão
```solidity
// ✅ Correto (mais eficiente)
uint256 public amount;

// ⚠️ Evitar (pode aumentar gas)
uint8 public smallAmount;  // Só se realmente necessário
```

#### Pack Structs
```solidity
// ✅ Otimizado (menos slots)
struct User {
    uint128 balance;  // Packed
    uint128 rewards; // Packed
    address user;    // Slot completo
}

// ❌ Não otimizado
struct User {
    uint256 balance;  // Slot completo
    uint256 rewards;  // Slot completo
    address user;     // Slot completo
}
```

#### Use Events para Dados Não Críticos
```solidity
// ✅ Correto
event UserUpdated(
    address indexed user,
    string metadata
);

// Em vez de armazenar string no storage
```

---

## 🏗️ **Architecture Patterns**

### Modularidade

**Módulos independentes**:
```python
# ✅ Correto - Módulos podem ser usados separadamente
from seve_framework.vision import SEVEVisionModule
from seve_framework.ethics import SEVEEthicsModule

vision = SEVEVisionModule(config)
ethics = SEVEEthicsModule(config)

# ❌ Evitar - Acoplamento forte
class SEVE:
    def __init__(self):
        self.vision = Vision()  # Não pode ser usado sozinho
        self.ethics = Ethics()  # Depende de Vision
```

---

### Dependency Injection

**Passar dependências explicitamente**:
```python
# ✅ Correto
class SEVECoreV3:
    def __init__(self, config: SEVEConfig):
        self.config = config
        self.vision_module = SEVEVisionModule(config)
        self.ethics_module = SEVEEthicsModule(config)

# ❌ Evitar
class SEVECoreV3:
    def __init__(self):
        self.config = SEVEConfig()  # Hardcoded
        self.vision_module = SEVEVisionModule()  # Sem config
```

---

### Error Handling Pattern

**Camadas de tratamento de erro**:
```python
# ✅ Correto
async def process_context(self, data: Dict[str, Any]) -> ProcessingResult:
    try:
        # Validação
        self._validate_input(data)
        
        # Processamento
        vision_result = await self.vision_module.process_visual_input(...)
        
        # Validação ética
        ethics_result = await self.ethics_module.validate_decision(...)
        
        if ethics_result.result == ValidationResult.BLOCKED:
            return ProcessingResult(
                status=ProcessingStatus.ETHICS_BLOCKED,
                errors=[ethics_result.reason]
            )
        
        return ProcessingResult(status=ProcessingStatus.COMPLETED, ...)
        
    except SEVEValidationError as e:
        logger.error(f"Validation error: {e}")
        return ProcessingResult(status=ProcessingStatus.FAILED, errors=[str(e)])
    except Exception as e:
        logger.exception("Unexpected error")
        return ProcessingResult(status=ProcessingStatus.FAILED, errors=[str(e)])
```

---

## 🔒 **Security Best Practices**

### Python

#### Never Hardcode Secrets
```python
# ✅ Correto
import os
api_key = os.getenv("API_KEY")

# ❌ Nunca fazer
api_key = "sk_live_1234567890"  # Hardcoded secret
```

#### Validate All Inputs
```python
# ✅ Correto
def process_user_data(user_data: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(user_data, dict):
        raise ValueError("user_data must be a dictionary")
    
    if "email" in user_data:
        email = user_data["email"]
        if not isinstance(email, str) or "@" not in email:
            raise ValueError("Invalid email format")
    
    # Processar
    return processed_data
```

#### Use Cryptography Library
```python
# ✅ Correto
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)
encrypted = cipher.encrypt(b"sensitive data")

# ❌ Evitar
encrypted = base64.b64encode(b"data")  # Não é criptografia real
```

---

### Solidity

#### Use OpenZeppelin
```solidity
// ✅ Correto
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// ❌ Evitar - Implementar do zero (mais propenso a erros)
```

#### Access Control
```solidity
// ✅ Correto
import "@openzeppelin/contracts/access/Ownable.sol";

contract MyContract is Ownable {
    function criticalFunction() external onlyOwner {
        // Apenas owner pode executar
    }
}

// ❌ Perigoso
contract MyContract {
    address public owner;
    
    function criticalFunction() external {
        require(msg.sender == owner);  // Pode ter bugs
    }
}
```

---

## ⚖️ **Ethical Best Practices**

### Privacy by Design

**Anonimizar desde o início**:
```python
# ✅ Correto
async def process_image(self, image: bytes) -> VisionResult:
    # Anonimizar ANTES de processar
    anonymized_image = await self._anonymize_faces(image)
    result = await self._detect_objects(anonymized_image)
    return result

# ❌ Evitar
async def process_image(self, image: bytes) -> VisionResult:
    result = await self._detect_objects(image)  # Processa com dados sensíveis
    # Anonimizar depois (pode ser tarde demais)
    anonymized = await self._anonymize_faces(image)
```

---

### Consent Management

**Sempre verificar consentimento**:
```python
# ✅ Correto
async def process_personal_data(self, data: Dict, context: Dict) -> Result:
    if not context.get("consent_given", False):
        raise SEVEEthicsError("Consent required for personal data processing")
    
    # Processar apenas se consentido
    return await self._process(data)
```

---

### Bias Detection

**Testar modelos para viés**:
```python
# ✅ Correto
async def validate_model_bias(self, model, test_data: List) -> BiasReport:
    """Validar modelo para viés potencial"""
    results = []
    for data in test_data:
        result = await model.predict(data)
        results.append(result)
    
    # Verificar distribuição de resultados
    bias_report = self._analyze_bias(results)
    
    if bias_report.has_bias:
        logger.warning(f"Potential bias detected: {bias_report.details}")
    
    return bias_report
```

---

## 📝 **Code Organization**

### Estrutura de Arquivos

```
seve_framework/
├── __init__.py          # Exports públicos
├── config.py            # Configuração
├── core.py              # Core framework
├── vision.py            # Módulo Vision
├── sense.py             # Módulo Sense
├── ethics.py            # Módulo Ethics
├── link.py              # Módulo Link
└── exceptions.py        # Exceções customizadas
```

---

### Separation of Concerns

**Cada módulo tem responsabilidade única**:
```python
# ✅ Correto - Módulos separados
# vision.py - Apenas visão computacional
class SEVEVisionModule:
    async def process_visual_input(self, ...):
        # Apenas processamento visual
        pass

# ethics.py - Apenas validação ética
class SEVEEthicsModule:
    async def validate_decision(self, ...):
        # Apenas validação ética
        pass

# ❌ Evitar - Responsabilidades misturadas
class VisionModule:
    async def process_visual_input(self, ...):
        # Processamento visual
        pass
    
    async def validate_ethics(self, ...):  # Não deveria estar aqui
        # Validação ética
        pass
```

---

## 🧪 **Testing Best Practices**

### Test Organization

**Um arquivo de teste por módulo**:
```
tests/
├── test_core.py         # Testes de SEVE-Core
├── test_vision.py       # Testes de SEVE-Vision
├── test_ethics.py       # Testes de SEVE-Ethics
└── test_integration.py # Testes de integração
```

**Um teste por funcionalidade**:
```python
# ✅ Correto
def test_staking_allows_deposit():
    pass

def test_staking_calculates_rewards():
    pass

# ❌ Evitar
def test_staking():
    # Testa múltiplas coisas
    test_deposit()
    test_rewards()
    test_unstake()
```

---

## 📚 **Documentation Best Practices**

### Code Comments

**Comentários explicam "por quê", não "o quê"**:
```python
# ✅ Bom
# Usar OpenCV porque é mais rápido que PIL para este caso
image = cv2.imread(path)

# ❌ Ruim (óbvio)
# Carregar imagem
image = cv2.imread(path)
```

---

### README e Docs

**Manter documentação atualizada**:
- Atualizar README quando adicionar features
- Documentar breaking changes no CHANGELOG
- Manter exemplos de código funcionais

---

## 🎯 **Convenções Específicas SEVE**

### Configuração

**Usar Enums, não strings**:
```python
# ✅ Correto
from seve_framework.config import SEVEMode, PrivacyLevel, EthicsLevel

config = SEVEConfig(
    mode=SEVEMode.HYBRID,
    privacy_level=PrivacyLevel.HIGH,
    ethics_level=EthicsLevel.STRICT
)

# ❌ Evitar
config = SEVEConfig(
    mode="hybrid",  # String pode ter typos
    privacy_level="high"
)
```

---

### Async First

**Todos os módulos são assíncronos**:
```python
# ✅ Correto
async def process(self, data):
    result = await self.module.process(data)
    return result

# ❌ Evitar
def process(self, data):
    result = self.module.process(data)  # Não async
    return result
```

---

## 📖 **Referências**

- [PEP 8](https://pep8.org/) - Python style guide
- [Solidity Style Guide](https://docs.soliditylang.org/en/latest/style-guide.html)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/)
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Guia de contribuição
- [TESTING.md](./TESTING.md) - Guia de testes

---

**Última Atualização**: 2025-01-29  
**Mantido por**: Equipe EON - Symbeon Tech

