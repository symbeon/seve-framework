# 🧭 Testnet Playbook - SEVE Framework e Ecossistema

Playbook reutilizável e padronizado para deploy e testes em testnets blockchain, aplicável ao SEVE Framework e qualquer projeto do ecossistema EON.

---

## 📋 **Índice**

1. [Visão Geral](#1-visão-geral)
2. [Seleção de Testnet](#2-seleção-de-testnet)
3. [Obtenção de Fundos](#3-obtenção-de-fundos)
4. [Configuração do Ambiente](#4-configuração-do-ambiente)
5. [Workflow de Deploy](#5-workflow-de-deploy)
6. [Verificação e Validação](#6-verificação-e-validação)
7. [Troubleshooting](#7-troubleshooting)
8. [Padronização](#8-padronização)

---

## 1. **Visão Geral**

### **Objetivo**
Este playbook fornece um processo padronizado e reutilizável para:
- ✅ Deploy de contratos em testnets
- ✅ Testes de integração em ambiente real
- ✅ Validação de funcionalidades antes da produção
- ✅ Aprendizado e experimentação sem custos

### **Quando Usar**
- 🧪 Desenvolvimento de novos contratos
- 🧪 Testes de integração
- 🧪 Validação de upgrade de contratos
- 🧪 Demos e apresentações
- 🧪 Auditoria e revisão de código

### **Custos**
- 💰 **Testnet**: 100% GRATUITO
- 💰 **Faucets**: Tokens de teste gratuitos
- 💰 **RPC Públicos**: Sem custo

---

## 2. **Seleção de Testnet**

### **Testnets Disponíveis**

#### **🔷 Ethereum Sepolia** (Recomendado)
- **RPC Público**: `https://rpc.sepolia.org`
- **Chain ID**: `11155111`
- **Explorer**: [Sepolia Etherscan](https://sepolia.etherscan.io/)
- **Faucet**: [sepoliafaucet.com](https://sepoliafaucet.com/)
- **Vantagens**:
  - ✅ Mais popular e estável
  - ✅ Maior compatibilidade
  - ✅ Melhor suporte de ferramentas
- **Desvantagens**:
  - ⚠️ Pode ter congestionamento ocasional

#### **🟣 Polygon Mumbai**
- **RPC Público**: `https://rpc-mumbai.maticvigil.com`
- **Chain ID**: `80001`
- **Explorer**: [Mumbai PolygonScan](https://mumbai.polygonscan.com/)
- **Faucet**: [Mumbai Faucet](https://faucet.polygon.technology/)
- **Vantagens**:
  - ✅ Confirmações rápidas
  - ✅ Gas fees baixos (mesmo em testnet)
  - ✅ Compatível com Polygon Mainnet
- **Uso**: Ideal para testes de contratos que vão para Polygon

#### **🟡 BSC Testnet**
- **RPC Público**: `https://data-seed-prebsc-1-s1.binance.org:8545`
- **Chain ID**: `97`
- **Explorer**: [BSC Testnet](https://testnet.bscscan.com/)
- **Faucet**: [BSC Faucet](https://testnet.bnbchain.org/faucet-smart)
- **Vantagens**:
  - ✅ Confirmações muito rápidas
  - ✅ Baixo custo de gas
- **Uso**: Para testes específicos de BSC

### **Tabela Comparativa**

| Testnet | Chain ID | RPC Público | Explorer | Gas Speed | Recomendação |
|---------|----------|-------------|----------|-----------|--------------|
| Sepolia | 11155111 | ✅ | ✅ | Médio | ⭐⭐⭐⭐⭐ Principal |
| Mumbai | 80001 | ✅ | ✅ | Rápido | ⭐⭐⭐⭐ Para Polygon |
| BSC Testnet | 97 | ✅ | ✅ | Muito Rápido | ⭐⭐⭐ Para BSC |

### **Recomendação por Caso de Uso**

```
Deploy Principal:      Sepolia
Contratos Polygon:      Mumbai
Contratos BSC:          BSC Testnet
Testes de Performance:  BSC Testnet
Compatibilidade EVM:    Sepolia
```

---

## 3. **Obtenção de Fundos**

### **Faucets Disponíveis**

#### **Ethereum Sepolia**

1. **Sepolia Faucet** (Recomendado)
   - URL: [sepoliafaucet.com](https://sepoliafaucet.com/)
   - Requisitos: Endereço de carteira
   - Limite: 0.5 ETH/24h por endereço
   - Velocidade: Imediato

2. **Chainlink Faucets**
   - URL: [faucets.chain.link](https://faucets.chain.link/)
   - Requisitos: Endereço de carteira
   - Limite: 0.1 ETH/24h
   - Vantagem: Suporta múltiplas testnets

3. **Alchemy Faucet** (Após criar conta)
   - URL: [Alchemy Dashboard](https://www.alchemy.com/)
   - Requisitos: Conta Alchemy + Endereço
   - Limite: 0.5 ETH/dia
   - Vantagem: Mais confiável

#### **Polygon Mumbai**

- **Polygon Faucet**
  - URL: [faucet.polygon.technology](https://faucet.polygon.technology/)
  - Requisitos: Conta GitHub ou Twitter
  - Limite: 0.5 MATIC/24h

#### **BSC Testnet**

- **BSC Faucet**
  - URL: [testnet.bnbchain.org/faucet-smart](https://testnet.bnbchain.org/faucet-smart)
  - Requisitos: Endereço de carteira
  - Limite: 1 BNB/24h

### **Workflow de Obtenção de Fundos**

```bash
# 1. Obter endereço da carteira
#    (MetaMask, WalletConnect, etc.)

# 2. Acessar faucet
#    Exemplo Sepolia: https://sepoliafaucet.com/

# 3. Colar endereço e solicitar fundos

# 4. Aguardar confirmação (geralmente < 1 minuto)

# 5. Verificar saldo no explorer
#    Sepolia: https://sepolia.etherscan.io/address/SEU_ENDERECO
```

### **Verificação de Saldo**

```bash
# Via Hardhat
npx hardhat console --network sepolia
> const provider = ethers.provider;
> const balance = await provider.getBalance("SEU_ENDERECO");
> console.log(ethers.formatEther(balance), "ETH");
```

---

## 4. **Configuração do Ambiente**

### **Pré-requisitos**

1. **Node.js e npm instalados**
   ```bash
   node --version  # >= 18.0.0
   npm --version   # >= 9.0.0
   ```

2. **Hardhat configurado**
   ```bash
   npm install --save-dev hardhat
   npx hardhat init
   ```

3. **Carteira criada**
   - MetaMask, WalletConnect, ou similar
   - Endereço e chave privada exportada

### **Configuração do `.env`**

```bash
# Criar arquivo .env (baseado em .env.example)
cp .env.example .env

# Editar com suas chaves
nano .env  # ou code .env
```

**Conteúdo mínimo do `.env`**:
```bash
PRIVATE_KEY=sua_chave_privada_sem_0x
NETWORK=sepolia
```

**Conteúdo completo** (veja [ENV_SETUP.md](./ENV_SETUP.md)):
```bash
PRIVATE_KEY=sua_chave_privada_sem_0x
ALCHEMY_API_KEY=sua_key_opcional
ETHERSCAN_API_KEY=sua_key_para_verificar
NETWORK=sepolia
```

### **Validação da Configuração**

```bash
# Verificar se variáveis estão carregadas
node -e "require('dotenv').config(); console.log('PRIVATE_KEY:', process.env.PRIVATE_KEY ? '✅' : '❌')"

# Validar formato da chave
node -e "require('dotenv').config(); const key = process.env.PRIVATE_KEY || ''; console.log('Key length:', key.length, key.length === 64 ? '✅' : '❌')"
```

---

## 5. **Workflow de Deploy**

### **Checklist Pré-Deploy**

- [ ] Carteira configurada com fundos suficientes
- [ ] `.env` configurado corretamente
- [ ] Contratos compilados sem erros
- [ ] Testes passando localmente
- [ ] Saldo verificado no explorer

### **Deploy Passo a Passo**

#### **1. Compilar Contratos**

```bash
npx hardhat compile
```

**Verificar saída**:
```
✅ Compiled successfully
✅ Artifacts saved to: artifacts/
```

#### **2. Executar Testes**

```bash
npx hardhat test
```

**Verificar**:
```
✅ All tests passing
✅ Coverage: XX%
```

#### **3. Deploy do Token**

```bash
npx hardhat run scripts/deploy-token.js --network sepolia
```

**Saída esperada**:
```
🚀 Deploying SEVE Token...
✅ SEVE Token deployed to: 0x...
📊 Transaction hash: 0x...
📄 Deployment info saved to: deployments/sepolia_deployments.json
```

#### **4. Deploy do Protocol**

```bash
npx hardhat run scripts/deploy-protocol.js --network sepolia
```

#### **5. Deploy do DAO**

```bash
npx hardhat run scripts/deploy-dao.js --network sepolia
```

### **Script de Deploy Automatizado**

```bash
#!/bin/bash
# deploy-testnet.sh

NETWORK=${1:-sepolia}

echo "🚀 Starting deployment to $NETWORK..."

echo "📦 Compiling contracts..."
npx hardhat compile || exit 1

echo "🧪 Running tests..."
npx hardhat test || exit 1

echo "🚀 Deploying contracts..."
npx hardhat run scripts/deploy-token.js --network $NETWORK
npx hardhat run scripts/deploy-protocol.js --network $NETWORK
npx hardhat run scripts/deploy-dao.js --network $NETWORK

echo "✅ Deployment complete!"
```

---

## 6. **Verificação e Validação**

### **Verificação de Contratos (Etherscan/PolygonScan)**

```bash
# Verificar contrato
npx hardhat verify --network sepolia <ENDERECO_CONTRATO>

# Com argumentos do construtor
npx hardhat verify --network sepolia <ENDERECO> <ARG1> <ARG2>
```

**Saída esperada**:
```
✅ Successfully verified contract on Etherscan
```

### **Validação Funcional**

```bash
# Interagir com contrato via console
npx hardhat console --network sepolia

> const Token = await ethers.getContractFactory("SEVEToken");
> const token = Token.attach("0xENDERECO_DEPLOYADO");
> const totalSupply = await token.totalSupply();
> console.log("Total Supply:", ethers.formatEther(totalSupply));
```

### **Verificação no Explorer**

1. Acesse o explorer da testnet:
   - Sepolia: [sepolia.etherscan.io](https://sepolia.etherscan.io/)
   - Mumbai: [mumbai.polygonscan.com](https://mumbai.polygonscan.com/)

2. Cole o endereço do contrato

3. Verifique:
   - ✅ Código verificado
   - ✅ Transações executadas
   - ✅ Estado atual do contrato

---

## 7. **Troubleshooting**

### **Erro: "invalid project id" (HH110)**

**Causa**: RPC provider inválido ou não configurado

**Soluções**:
```javascript
// Opção 1: Usar RPC público (no hardhat.config.js)
sepolia: {
  url: "https://rpc.sepolia.org",  // RPC público
  accounts: [...]
}

// Opção 2: Configurar Alchemy/Infura
sepolia: {
  url: `https://eth-sepolia.g.alchemy.com/v2/${process.env.ALCHEMY_API_KEY}`,
  accounts: [...]
}
```

### **Erro: "insufficient funds"**

**Causa**: Carteira sem fundos suficientes para gas

**Solução**:
1. Verifique saldo no explorer
2. Use faucet para obter mais fundos
3. Para testnet, geralmente 0.1 ETH é suficiente

### **Erro: "nonce too low"**

**Causa**: Múltiplas transações simultâneas ou nonce desatualizado

**Solução**:
```bash
# Aguarde confirmações das transações anteriores
# Ou reset o nonce manualmente (avancado)
```

### **Erro: "contract deployment failed"**

**Causas comuns**:
- Código do contrato com erro
- Gas limit insuficiente
- Constructor reverts

**Debugging**:
```bash
# Compilar novamente
npx hardhat compile

# Verificar logs detalhados
npx hardhat run scripts/deploy-token.js --network sepolia --verbose
```

### **Problema: Contrato não verificado**

**Solução**:
```bash
# Verificar manualmente
npx hardhat verify --network sepolia <ENDERECO>

# Com API key no .env:
ETHERSCAN_API_KEY=sua_key
```

---

## 8. **Padronização**

### **Aplicação em Outros Projetos**

Este playbook é **100% reutilizável** para qualquer projeto:

1. **Copie este arquivo** para `docs/TESTNET_PLAYBOOK.md`
2. **Adapte scripts** conforme necessário
3. **Mantenha estrutura** padronizada
4. **Documente variações** específicas do projeto

### **Estrutura Padrão de Deploy**

```
projeto/
├── contracts/
├── scripts/
│   ├── deploy-token.js
│   ├── deploy-protocol.js
│   └── deploy-dao.js
├── deployments/
│   └── {network}_deployments.json
├── .env
├── .env.example
└── docs/
    └── TESTNET_PLAYBOOK.md  ← Este arquivo
```

### **Checklist de Qualidade**

Antes de considerar deploy completo:

- [ ] Todos os contratos deployados com sucesso
- [ ] Todos os contratos verificados no explorer
- [ ] Testes de integração passando
- [ ] Endereços documentados em `deployments/`
- [ ] Documentação atualizada
- [ ] Team notificado dos endereços

---

## 📚 **Referências**

- **[Guia de Deploy](./DEPLOYMENT_GUIDE.md)** - Deploy detalhado
- **[Setup de Ambiente](./ENV_SETUP.md)** - Configuração completa
- **[Provedores RPC](./RPC_PROVIDERS.md)** - Escolha de provedor
- **[Checklist de Segurança](./SECURITY_CHECKLIST.md)** - Validações de segurança

---

**Última Atualização**: 2025-01-29  
**Mantido por**: Equipe EON - Symbeon Tech  
**Aplicável a**: SEVE Framework e todos os projetos do ecossistema EON
