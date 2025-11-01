# SEVEProtocol - API Reference

**Smart Contract**: SEVEProtocol.sol  
**Versão**: 1.0.0

---

## 📋 **Visão Geral**

SEVEProtocol gerencia:
- Licenciamento de versões do SEVE Framework
- Registro e verificação de agentes AI
- Gestão de preços e versões
- Receita do protocolo

---

## 🔧 **Funções Públicas**

### `purchaseLicense(string memory version, uint256 duration, string memory capabilities)`

Comprar licença para uma versão do SEVE Framework.

**Parâmetros:**
- `version` (string): Versão do framework (ex: "1.0.0")
- `duration` (uint256): Duração da licença em dias
- `capabilities` (string): Capacidades necessárias (JSON string)

**Retorno**: Nenhum

**Eventos Emitidos:**
- `LicensePurchased(address indexed buyer, string version, uint256 price, uint256 duration, bytes32 codeHash)`

**Exemplo:**
```solidity
// Comprar licença para versão 1.0.0 por 365 dias
seveProtocol.purchaseLicense(
    "1.0.0",
    365,
    '{"modules": ["vision", "ethics"]}'
);
```

**Requisitos:**
- Versão disponível
- `duration > 0`
- Saldo suficiente de SEVEToken
- Contrato não pausado

**Preço**: Pro-rated baseado em `versionPricing[version].price * duration / 365`

---

### `registerAgent(string memory capabilities, bytes32 agentHash, string memory metadata)`

Registrar um agente AI no protocolo.

**Parâmetros:**
- `capabilities` (string): Capacidades do agente (JSON string)
- `agentHash` (bytes32): Hash do código do agente
- `metadata` (string): Metadados do agente (JSON string)

**Retorno**: Nenhum

**Eventos Emitidos:**
- `AgentRegistered(address indexed agent, string capabilities, bytes32 agentHash)`

**Exemplo:**
```solidity
bytes32 hash = keccak256(abi.encodePacked(agentCode));
seveProtocol.registerAgent(
    '{"vision": true, "ethics": true}',
    hash,
    '{"name": "MyAgent", "version": "1.0"}'
);
```

**Requisitos:**
- Agente não registrado anteriormente
- `agentHash != 0`
- Hash não registrado anteriormente

---

### `updateAgentPerformance(address agent, uint256 score)`

Atualizar score de performance de um agente.

**Parâmetros:**
- `agent` (address): Endereço do agente
- `score` (uint256): Novo score (0-100)

**Retorno**: Nenhum

**Eventos Emitidos:**
- `PerformanceUpdated(address indexed agent, uint256 score)`

**Requisitos:**
- Apenas agentes autorizados ou owner
- `score <= 100`

---

### `verifyAgent(address agent, bool verified)`

Verificar/desverificar um agente.

**Parâmetros:**
- `agent` (address): Endereço do agente
- `verified` (bool): Status de verificação

**Retorno**: Nenhum

**Eventos Emitidos:**
- `AgentVerified(address indexed agent, bool verified)`

**Requisitos:**
- Apenas owner ou licensors autorizados

---

### `getLicenseCount(address licensee)`

Obter número de licenças de um endereço.

**Parâmetros:**
- `licensee` (address): Endereço do licenciado

**Retorno**: `uint256` - Número de licenças

---

### `getLicense(address licensee, uint256 index)`

Obter licença específica por índice.

**Parâmetros:**
- `licensee` (address): Endereço do licenciado
- `index` (uint256): Índice da licença

**Retorno**: `License` struct

**Estrutura License:**
```solidity
struct License {
    address licensee;
    string version;
    uint256 duration;
    uint256 price;
    bool active;
    uint256 timestamp;
    bytes32 codeHash;
    string capabilities;
}
```

---

### `isLicenseValid(address licensee, string memory version)`

Verificar se licença é válida para uma versão.

**Parâmetros:**
- `licensee` (address): Endereço do licenciado
- `version` (string): Versão a verificar

**Retorno**: `bool` - Se licença é válida e ativa

**Exemplo:**
```solidity
bool valid = seveProtocol.isLicenseValid(userAddress, "1.0.0");
```

---

## 🔐 **Funções Apenas Owner/Licensor**

### `addVersion(string memory version, uint256 price, bytes32 codeHash, string memory description)`

Adicionar nova versão do framework.

**Parâmetros:**
- `version` (string): Versão (ex: "1.1.0")
- `price` (uint256): Preço anual em SEVE tokens
- `codeHash` (bytes32): Hash do código da versão
- `description` (string): Descrição da versão

**Retorno**: Nenhum

**Eventos Emitidos:**
- `VersionAdded(string version, uint256 price, bytes32 codeHash)`

**Requisitos:**
- Apenas owner ou licensors autorizados

---

### `setProtocolFeeRate(uint256 newFeeRate)`

Atualizar taxa do protocolo.

**Parâmetros:**
- `newFeeRate` (uint256): Nova taxa em basis points (100 = 1%)

**Retorno**: Nenhum

**Eventos Emitidos:**
- `ProtocolFeeUpdated(uint256 newFeeRate)`

**Requisitos:**
- Apenas owner

**Taxa padrão**: 100 (1%)

---

### `authorizeLicensor(address licensor)`

Autorizar endereço para emitir licenças.

**Parâmetros:**
- `licensor` (address): Endereço a autorizar

**Requisitos:**
- Apenas owner

---

### `revokeLicensor(address licensor)`

Revogar autorização de licensor.

**Parâmetros:**
- `licensor` (address): Endereço a revogar

**Requisitos:**
- Apenas owner

---

## 📊 **Variáveis Públicas**

### Mappings

- `licenses(address)`: Array de licenças por endereço
- `agents(address)`: Informações do agente por endereço
- `versionPricing(string)`: Informações de preço por versão
- `authorizedLicensors(address)`: Se endereço está autorizado a licenciar
- `registeredCodeHashes(bytes32)`: Se hash de código está registrado

### Estruturas

**Agent:**
```solidity
struct Agent {
    address agentAddress;
    string capabilities;
    uint256 performanceScore;
    bool verified;
    uint256 registrationTime;
    bytes32 agentHash;
    string metadata;
}
```

**VersionInfo:**
```solidity
struct VersionInfo {
    uint256 price;
    bool available;
    string description;
    bytes32 codeHash;
    uint256 timestamp;
}
```

### Totais

- `totalLicensesSold`: Total de licenças vendidas
- `totalRevenue`: Receita total do protocolo
- `protocolFeeRate`: Taxa do protocolo (basis points)

---

## 📡 **Eventos**

### `LicensePurchased`
```solidity
event LicensePurchased(
    address indexed buyer,
    string version,
    uint256 price,
    uint256 duration,
    bytes32 codeHash
);
```

### `AgentRegistered`
```solidity
event AgentRegistered(
    address indexed agent,
    string capabilities,
    bytes32 agentHash
);
```

### `PerformanceUpdated`
```solidity
event PerformanceUpdated(
    address indexed agent,
    uint256 score
);
```

### `AgentVerified`
```solidity
event AgentVerified(
    address indexed agent,
    bool verified
);
```

### `VersionAdded`
```solidity
event VersionAdded(
    string version,
    uint256 price,
    bytes32 codeHash
);
```

### `ProtocolFeeUpdated`
```solidity
event ProtocolFeeUpdated(
    uint256 newFeeRate
);
```

---

## 💡 **Fluxo de Licenciamento**

### 1. Adicionar Versão (Owner)
```solidity
bytes32 codeHash = keccak256(abi.encodePacked(versionCode));
seveProtocol.addVersion(
    "1.0.0",
    10000 * 10**18, // 10,000 SEVE tokens/ano
    codeHash,
    "SEVE Framework v1.0.0 - Production Ready"
);
```

### 2. Comprar Licença (Usuário)
```solidity
// Aprovar tokens primeiro
seveToken.approve(address(seveProtocol), 10000 * 10**18);

// Comprar licença
seveProtocol.purchaseLicense(
    "1.0.0",
    365,
    '{"modules": ["vision", "ethics", "sense", "link"]}'
);
```

### 3. Verificar Licença (Sistema)
```solidity
bool valid = seveProtocol.isLicenseValid(userAddress, "1.0.0");
require(valid, "License required");
```

---

## 📝 **Exemplo de Uso Completo**

```solidity
// 1. Setup (Owner)
seveProtocol.addVersion("1.0.0", 10000 * 10**18, codeHash, "Production");
seveProtocol.setProtocolFeeRate(100); // 1%

// 2. Usuário compra licença
seveToken.approve(address(seveProtocol), 10000 * 10**18);
seveProtocol.purchaseLicense("1.0.0", 365, capabilities);

// 3. Verificar licença
bool hasLicense = seveProtocol.isLicenseValid(msg.sender, "1.0.0");

// 4. Registrar agente
bytes32 agentHash = keccak256(abi.encodePacked(agentCode));
seveProtocol.registerAgent(capabilities, agentHash, metadata);

// 5. Atualizar performance do agente
seveProtocol.updateAgentPerformance(agentAddress, 95);

// 6. Verificar agente (Owner)
seveProtocol.verifyAgent(agentAddress, true);
```

---

**Mantido por**: Equipe EON - Symbeon Tech

