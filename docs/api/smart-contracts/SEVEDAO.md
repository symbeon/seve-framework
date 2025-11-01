# SEVEDAO - API Reference

**Smart Contract**: SEVEDAO.sol  
**Versão**: 1.0.0

---

## 📋 **Visão Geral**

SEVEDAO é uma Organização Autônoma Descentralizada (DAO) para governança do SEVE Framework:
- Criação e votação em propostas
- Execução de decisões da comunidade
- Tipos de propostas: Técnicas, Financeiras, Parcerias, Governance
- Quorum e supermaioria configuráveis

---

## 🔧 **Funções Públicas**

### `createProposal(string memory title, string memory description, ProposalType proposalType, bytes memory data)`

Criar nova proposta.

**Parâmetros:**
- `title` (string): Título da proposta
- `description` (string): Descrição detalhada
- `proposalType` (ProposalType): Tipo de proposta (TECHNICAL, FINANCIAL, PARTNERSHIP, GOVERNANCE)
- `data` (bytes): Dados codificados para execução (opcional)

**Retorno**: `uint256` - ID da proposta criada

**Eventos Emitidos:**
- `ProposalCreated(uint256 indexed proposalId, address indexed proposer, string title, ProposalType proposalType)`

**Exemplo:**
```solidity
bytes memory callData = abi.encodeWithSignature("updateFee(uint256)", newFee);
uint256 proposalId = seveDAO.createProposal(
    "Atualizar Taxa do Protocolo",
    "Proposta para atualizar taxa de 1% para 0.5%",
    ProposalType.FINANCIAL,
    callData
);
```

**Requisitos:**
- Apenas proposers autorizados
- `title` e `description` não vazios
- Contrato não pausado

**Período de votação**: `votingPeriod` (padrão: 7 dias)

---

### `vote(uint256 proposalId, bool support)`

Votar em uma proposta.

**Parâmetros:**
- `proposalId` (uint256): ID da proposta
- `support` (bool): `true` para sim, `false` para não

**Retorno**: Nenhum

**Eventos Emitidos:**
- `VoteCast(uint256 indexed proposalId, address indexed voter, bool support, uint256 votingPower)`

**Exemplo:**
```solidity
// Votar a favor
seveDAO.vote(proposalId, true);

// Votar contra
seveDAO.vote(proposalId, false);
```

**Requisitos:**
- Proposta existe
- Votação em andamento
- Não votou anteriormente
- Poder de voto > 0 (via SEVEToken)

**Poder de voto**: `seveToken.getVotingPower(msg.sender)`

---

### `executeProposal(uint256 proposalId)`

Executar proposta aprovada.

**Parâmetros:**
- `proposalId` (uint256): ID da proposta

**Retorno**: Nenhum

**Eventos Emitidos:**
- `ProposalExecuted(uint256 indexed proposalId)`

**Requisitos:**
- Proposta existe
- Votação encerrada
- `executionDelay` passou desde o fim da votação
- Quorum atingido
- Maioria ou supermaioria (dependendo do tipo)
- Não executada anteriormente

**Delays**:
- `executionDelay`: 1 dia (padrão)
- Permite tempo para review antes de execução

---

### `getProposal(uint256 proposalId)`

Obter informações de uma proposta.

**Parâmetros:**
- `proposalId` (uint256): ID da proposta

**Retorno**: `Proposal` struct

**Estrutura Proposal:**
```solidity
struct Proposal {
    uint256 id;
    address proposer;
    string title;
    string description;
    uint256 votesFor;
    uint256 votesAgainst;
    uint256 startTime;
    uint256 endTime;
    bool executed;
    ProposalType proposalType;
    bytes data;
}
```

---

### `getVote(uint256 proposalId, address voter)`

Obter voto de um eleitor em uma proposta.

**Parâmetros:**
- `proposalId` (uint256): ID da proposta
- `voter` (address): Endereço do eleitor

**Retorno**: `Vote` struct

**Estrutura Vote:**
```solidity
struct Vote {
    bool hasVoted;
    bool support;
    uint256 votingPower;
}
```

---

### `canExecute(uint256 proposalId)`

Verificar se proposta pode ser executada.

**Parâmetros:**
- `proposalId` (uint256): ID da proposta

**Retorno**: `bool` - Se pode ser executada

**Verifica**:
- Votação encerrada
- `executionDelay` passou
- Quorum atingido
- Maioria/supermaioria atingida
- Não executada

---

### `getProposalStatus(uint256 proposalId)`

Obter status textual da proposta.

**Retorno**: `string` - Status ("Pending", "Active", "Succeeded", "Defeated", "Executed")

---

## 🔐 **Funções Apenas Owner**

### `setVotingPeriod(uint256 newPeriod)`

Atualizar período de votação.

**Parâmetros:**
- `newPeriod` (uint256): Novo período em segundos

**Requisitos:**
- Apenas owner

**Padrão**: 7 dias

---

### `setExecutionDelay(uint256 newDelay)`

Atualizar delay de execução.

**Parâmetros:**
- `newDelay` (uint256): Novo delay em segundos

**Padrão**: 1 dia

---

### `setQuorumThreshold(uint256 newThreshold)`

Atualizar threshold de quorum (em % do supply total).

**Parâmetros:**
- `newThreshold` (uint256): Novo threshold em percentual

**Padrão**: 10%

---

### `setSupermajorityThreshold(uint256 newThreshold)`

Atualizar threshold de supermaioria (em %).

**Parâmetros:**
- `newThreshold` (uint256): Novo threshold em percentual

**Padrão**: 66%

---

### `authorizeProposer(address proposer)`

Autorizar endereço para criar propostas.

**Parâmetros:**
- `proposer` (address): Endereço a autorizar

---

### `revokeProposer(address proposer)`

Revogar autorização de proposer.

**Parâmetros:**
- `proposer` (address): Endereço a revogar

---

## 📊 **Tipos de Proposta**

### `ProposalType` Enum

```solidity
enum ProposalType {
    TECHNICAL,      // Mudanças técnicas no protocolo
    FINANCIAL,      // Decisões financeiras
    PARTNERSHIP,    // Propostas de parceria
    GOVERNANCE      // Mudanças de governança
}
```

**Thresholds por Tipo:**
- **TECHNICAL**: Requer supermaioria (66%)
- **FINANCIAL**: Requer supermaioria (66%)
- **PARTNERSHIP**: Requer maioria simples (50%+)
- **GOVERNANCE**: Requer supermaioria (66%)

---

## 📊 **Variáveis Públicas**

### Constantes e Configurações

- `votingPeriod`: Período de votação (padrão: 7 dias)
- `executionDelay`: Delay antes de execução (padrão: 1 dia)
- `quorumThreshold`: Threshold de quorum (padrão: 10% do supply)
- `supermajorityThreshold`: Threshold de supermaioria (padrão: 66%)

### Mappings

- `proposals(uint256)`: Propostas por ID
- `votes(uint256)(address)`: Votos por proposta e eleitor
- `authorizedProposers(address)`: Se endereço pode criar propostas

### Contadores

- `proposalCount`: Total de propostas criadas

---

## 📡 **Eventos**

### `ProposalCreated`
```solidity
event ProposalCreated(
    uint256 indexed proposalId,
    address indexed proposer,
    string title,
    ProposalType proposalType
);
```

### `VoteCast`
```solidity
event VoteCast(
    uint256 indexed proposalId,
    address indexed voter,
    bool support,
    uint256 votingPower
);
```

### `ProposalExecuted`
```solidity
event ProposalExecuted(
    uint256 indexed proposalId
);
```

### `ProposalTypeUpdated`
```solidity
event ProposalTypeUpdated(
    uint256 indexed proposalId,
    ProposalType newType
);
```

---

## 💡 **Fluxo Completo de Governance**

### 1. Criar Proposta (Proposer Autorizado)
```solidity
// Proposta técnica: Atualizar versão
bytes memory data = abi.encodeWithSignature(
    "addVersion(string,uint256,bytes32,string)",
    "1.1.0",
    12000 * 10**18,
    newCodeHash,
    "New features"
);

uint256 proposalId = seveDAO.createProposal(
    "Adicionar Versão 1.1.0",
    "Proposta para adicionar nova versão com melhorias",
    ProposalType.TECHNICAL,
    data
);
```

### 2. Votação (Comunidade)
```solidity
// Usuários votam
seveDAO.vote(proposalId, true);  // A favor
seveDAO.vote(proposalId, false); // Contra
```

### 3. Verificar Status
```solidity
// Verificar se pode executar
bool canExec = seveDAO.canExecute(proposalId);

// Ver status
string memory status = seveDAO.getProposalStatus(proposalId);
```

### 4. Executar (Após delay)
```solidity
// Executar proposta aprovada
seveDAO.executeProposal(proposalId);
```

---

## 📝 **Exemplo de Uso Completo**

```solidity
// 1. Setup (Owner)
seveDAO.setVotingPeriod(7 days);
seveDAO.setQuorumThreshold(10); // 10%
seveDAO.setSupermajorityThreshold(66); // 66%
seveDAO.authorizeProposer(proposerAddress);

// 2. Criar proposta financeira
bytes memory callData = abi.encodeWithSignature(
    "setProtocolFeeRate(uint256)",
    50 // 0.5%
);

uint256 proposalId = seveDAO.createProposal(
    "Reduzir Taxa do Protocolo",
    "Reduzir de 1% para 0.5% para aumentar adoção",
    ProposalType.FINANCIAL,
    callData
);

// 3. Usuários votam (precisam ter SEVE staked)
seveDAO.vote(proposalId, true);

// 4. Verificar resultados
Proposal memory proposal = seveDAO.getProposal(proposalId);
uint256 totalVotes = proposal.votesFor + proposal.votesAgainst;
uint256 supportPercentage = (proposal.votesFor * 100) / totalVotes;

// 5. Executar se aprovada
if (seveDAO.canExecute(proposalId)) {
    seveDAO.executeProposal(proposalId);
}
```

---

## ⚠️ **Considerações Importantes**

### Segurança

1. **Execution Delay**: Delay de 1 dia permite review antes de execução
2. **Quorum**: Requer participação mínima (10% do supply)
3. **Supermajority**: Mudanças importantes requerem 66% de aprovação
4. **Reentrancy**: Protegido com `ReentrancyGuard`

### Thresholds

- **Quorum**: 10% do supply total deve votar
- **Supermajoria**: 66% dos votos devem ser a favor (para tipos importantes)
- **Maioria**: 50%+ dos votos (para parcerias)

### Poder de Voto

Poder de voto baseado em:
- Tokens staked (via `seveToken.getVotingPower()`)
- Tokens em governance staking

---

**Mantido por**: Equipe EON - Symbeon Tech

