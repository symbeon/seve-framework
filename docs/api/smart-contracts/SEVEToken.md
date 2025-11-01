# SEVEToken - API Reference

**Smart Contract**: SEVEToken.sol  
**Padrão**: ERC-20  
**Versão**: 1.0.0

---

## 📋 **Visão Geral**

SEVEToken é um token ERC-20 que serve como base para o ecossistema SEVE Framework, incluindo:
- Staking com recompensas (10% APY)
- Governance staking (8% APY)
- Votação em propostas DAO
- Tokenomics com distribuição controlada

---

## 🔧 **Funções Públicas**

### `stake(uint256 amount)`

Stake tokens para receber recompensas.

**Parâmetros:**
- `amount` (uint256): Quantidade de tokens para fazer stake

**Retorno**: Nenhum

**Eventos Emitidos:**
- `TokensStaked(address indexed user, uint256 amount, uint256 timestamp)`

**Exemplo:**
```solidity
// Stake 1000 tokens (assumindo 18 decimais)
seveToken.stake(1000 * 10**18);
```

**Requisitos:**
- `amount > 0`
- Saldo suficiente na carteira
- Contrato não pausado

---

### `unstake(uint256 amount)`

Unstake tokens e reivindicar recompensas acumuladas.

**Parâmetros:**
- `amount` (uint256): Quantidade de tokens para fazer unstake

**Retorno**: Nenhum

**Eventos Emitidos:**
- `TokensUnstaked(address indexed user, uint256 amount, uint256 reward)`

**Exemplo:**
```solidity
// Unstake 500 tokens (receberá 500 + recompensas)
seveToken.unstake(500 * 10**18);
```

**Requisitos:**
- `amount > 0`
- Está fazendo stake
- Saldo staked suficiente

---

### `claimStakingRewards()`

Reivindicar recompensas de staking sem fazer unstake.

**Retorno**: Nenhum

**Eventos Emitidos:**
- `TokensUnstaked(address indexed user, uint256 amount, uint256 reward)` (amount = 0)

**Exemplo:**
```solidity
// Reivindicar recompensas acumuladas
seveToken.claimStakingRewards();
```

**Requisitos:**
- Está fazendo stake
- Recompensas > 0

---

### `calculateStakingRewards(address user)`

Calcular recompensas de staking para um usuário.

**Parâmetros:**
- `user` (address): Endereço do usuário

**Retorno**: `uint256` - Quantidade de recompensas calculadas

**Exemplo:**
```solidity
uint256 rewards = seveToken.calculateStakingRewards(userAddress);
```

**Taxa APY**: 10% ao ano

---

### `stakeForGovernance(uint256 amount)`

Stake tokens para participação em governance.

**Parâmetros:**
- `amount` (uint256): Quantidade de tokens

**Retorno**: Nenhum

**Eventos Emitidos:**
- `GovernanceStaked(address indexed user, uint256 amount)`

**Exemplo:**
```solidity
// Stake para governance
seveToken.stakeForGovernance(5000 * 10**18);
```

**Taxa APY**: 8% ao ano

---

### `unstakeGovernance(uint256 amount)`

Unstake tokens de governance e reivindicar recompensas.

**Parâmetros:**
- `amount` (uint256): Quantidade de tokens

**Retorno**: Nenhum

**Eventos Emitidos:**
- `GovernanceUnstaked(address indexed user, uint256 amount, uint256 reward)`

---

### `claimGovernanceRewards()`

Reivindicar recompensas de governance sem fazer unstake.

---

### `calculateGovernanceRewards(address user)`

Calcular recompensas de governance para um usuário.

**Taxa APY**: 8% ao ano

---

### `getVotingPower(address user)`

Obter poder de voto de um usuário para governance.

**Parâmetros:**
- `user` (address): Endereço do usuário

**Retorno**: `uint256` - Poder de voto total (staking + governance staking)

**Exemplo:**
```solidity
uint256 votingPower = seveToken.getVotingPower(msg.sender);
```

---

## 🔐 **Funções Apenas Owner**

### `pause()`

Pausar contrato em caso de emergência.

**Requisitos:**
- Apenas owner

---

### `unpause()`

Despausar contrato.

**Requisitos:**
- Apenas owner

---

## 📊 **Variáveis Públicas**

### Constantes

- `TOTAL_SUPPLY`: 1.000.000.000 * 10^18 (1 bilhão de tokens)
- `MAX_SUPPLY`: 1.000.000.000 * 10^18
- `TEAM_ALLOCATION`: 200.000.000 * 10^18 (20%)
- `DEVELOPMENT_ALLOCATION`: 300.000.000 * 10^18 (30%)
- `COMMUNITY_ALLOCATION`: 250.000.000 * 10^18 (25%)
- `PARTNERSHIP_ALLOCATION`: 150.000.000 * 10^18 (15%)
- `RESERVE_ALLOCATION`: 100.000.000 * 10^18 (10%)
- `STAKING_REWARD_RATE`: 10 (10% APY)
- `GOVERNANCE_STAKING_RATE`: 8 (8% APY)

### Mappings

- `stakedAmount(address)`: Quantidade staked por usuário
- `stakingStartTime(address)`: Início do staking
- `isStaking(address)`: Se usuário está fazendo stake
- `governanceStakedAmount(address)`: Quantidade staked para governance
- `isGovernanceStaking(address)`: Se está fazendo governance staking

### Totais

- `totalStaked`: Total de tokens em staking
- `totalGovernanceStaked`: Total de tokens em governance staking

---

## 📡 **Eventos**

### `TokensStaked`
```solidity
event TokensStaked(
    address indexed user,
    uint256 amount,
    uint256 timestamp
);
```

### `TokensUnstaked`
```solidity
event TokensUnstaked(
    address indexed user,
    uint256 amount,
    uint256 reward
);
```

### `GovernanceStaked`
```solidity
event GovernanceStaked(
    address indexed user,
    uint256 amount
);
```

### `GovernanceUnstaked`
```solidity
event GovernanceUnstaked(
    address indexed user,
    uint256 amount,
    uint256 reward
);
```

---

## 🔗 **Integração ERC-20**

SEVEToken implementa todas as funções padrão ERC-20:
- `transfer(address to, uint256 amount)`
- `transferFrom(address from, address to, uint256 amount)`
- `approve(address spender, uint256 amount)`
- `balanceOf(address account)`
- `totalSupply()`
- `allowance(address owner, address spender)`

---

## 📝 **Exemplo de Uso Completo**

```solidity
// 1. Verificar saldo
uint256 balance = seveToken.balanceOf(msg.sender);

// 2. Fazer stake
seveToken.stake(1000 * 10**18);

// 3. Verificar recompensas acumuladas
uint256 rewards = seveToken.calculateStakingRewards(msg.sender);

// 4. Reivindicar recompensas
seveToken.claimStakingRewards();

// 5. Stake para governance
seveToken.stakeForGovernance(5000 * 10**18);

// 6. Verificar poder de voto
uint256 votingPower = seveToken.getVotingPower(msg.sender);

// 7. Unstake
seveToken.unstake(500 * 10**18);
```

---

**Mantido por**: Equipe EON - Symbeon Tech

