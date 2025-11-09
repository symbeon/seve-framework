# 🚀 Guia Completo: Deploy na Testnet - SEVE Framework

**Data**: 07 de Novembro de 2025  
**Versão**: SEVE Framework v1.0.0  
**Objetivo**: Deploy completo dos smart contracts na testnet

---

## 📋 **ÍNDICE**

1. [Pré-requisitos](#1-pré-requisitos)
2. [Preparação](#2-preparação)
3. [Deploy Automatizado](#3-deploy-automatizado)
4. [Deploy Manual](#4-deploy-manual)
5. [Verificação](#5-verificação)
6. [Troubleshooting](#6-troubleshooting)

---

## 1. **PRÉ-REQUISITOS**

### **Software Necessário**

- ✅ **Node.js** v18+ instalado
- ✅ **npm** ou **yarn** instalado
- ✅ **Git** instalado

### **Contas e Chaves**

- ✅ **Carteira de Teste** (MetaMask ou similar)
- ✅ **Chave Privada de Teste** (NUNCA use chave principal!)
- ✅ **Faucet de Testnet** (para obter tokens de teste)

### **Verificar Instalação**

```bash
node --version  # Deve ser v18+
npm --version   # Deve ser 9+
```

---

## 2. **PREPARAÇÃO**

### **2.1. Instalar Dependências**

```bash
cd SEVE-FRAMEWORK
npm install
```

**Verificar**:
```bash
npx hardhat --version  # Deve mostrar versão do Hardhat
```

### **2.2. Criar Carteira de Teste**

**Opção 1: MetaMask (Recomendado)**
1. Instalar MetaMask: https://metamask.io/
2. Criar nova carteira
3. Exportar chave privada (Settings → Security → Export Private Key)
4. **⚠️ IMPORTANTE**: Use apenas para testes, nunca para produção!

**Opção 2: Gerar Chave via Node.js**
```bash
node -e "const crypto = require('crypto'); console.log('Private Key:', crypto.randomBytes(32).toString('hex'));"
```

### **2.3. Obter Fundos de Teste**

#### **Ethereum Sepolia** (Recomendado)
- **Faucet**: https://sepoliafaucet.com/
- **Alternativa**: https://faucet.quicknode.com/ethereum/sepolia
- **Quantidade**: 0.1-0.5 ETH suficiente

#### **Polygon Mumbai**
- **Faucet**: https://faucet.polygon.technology/
- **Quantidade**: 0.1-1 MATIC suficiente

#### **BSC Testnet**
- **Faucet**: https://testnet.bnbchain.org/faucet-smart
- **Quantidade**: 0.1-1 BNB suficiente

### **2.4. Configurar .env**

Criar arquivo `.env` na raiz do projeto:

```bash
# SEVE Framework - Environment Variables
PRIVATE_KEY=sua_chave_privada_sem_0x
ALCHEMY_URL=https://eth-sepolia.g.alchemy.com/v2/SUA_KEY
ETHERSCAN_API_KEY=sua_key_para_verificar
NETWORK=sepolia
```

**⚠️ IMPORTANTE**:
- NUNCA commite o arquivo `.env`!
- Use apenas chaves de teste!
- Remova o prefixo `0x` da chave privada

**Obter Alchemy URL (Opcional)**:
1. Criar conta: https://www.alchemy.com/
2. Criar novo app (Ethereum Sepolia)
3. Copiar HTTP URL

**Obter Etherscan API Key (Opcional)**:
1. Criar conta: https://etherscan.io/register
2. API Keys: https://etherscan.io/myapikey
3. Criar nova API key

---

## 3. **DEPLOY AUTOMATIZADO**

### **3.1. Windows (PowerShell)**

```powershell
.\scripts\deploy-testnet.ps1 sepolia
```

### **3.2. Linux/Mac (Bash)**

```bash
chmod +x scripts/deploy-testnet.sh
./scripts/deploy-testnet.sh sepolia
```

### **3.3. O Que o Script Faz**

1. ✅ Verifica configuração (.env)
2. ✅ Compila contratos
3. ✅ Executa testes
4. ✅ Deploy do SEVEToken
5. ✅ Deploy do SEVEProtocol
6. ✅ Deploy do SEVEDAO
7. ✅ Salva informações em `deployments/{network}_deployments.json`

---

## 4. **DEPLOY MANUAL**

### **4.1. Compilar Contratos**

```bash
npx hardhat compile
```

**Verificar saída**:
```
✅ Compiled successfully
✅ Artifacts saved to: artifacts/
```

### **4.2. Executar Testes**

```bash
npx hardhat test
```

**Verificar**: Todos os testes devem passar

### **4.3. Deploy do Token**

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

**Copiar endereço do Token** para usar nos próximos deploys.

### **4.4. Deploy do Protocol**

```bash
# Substituir 0x... pelo endereço do Token
TOKEN_ADDRESS=0x... npx hardhat run scripts/deploy-protocol.js --network sepolia
```

**Ou editar o script** para ler do arquivo de deployment automaticamente.

### **4.5. Deploy do DAO**

```bash
# Substituir 0x... pelo endereço do Token
TOKEN_ADDRESS=0x... npx hardhat run scripts/deploy-dao.js --network sepolia
```

---

## 5. **VERIFICAÇÃO**

### **5.1. Verificar no Explorer**

#### **Ethereum Sepolia**
- **Explorer**: https://sepolia.etherscan.io/
- **Buscar**: Endereço do contrato
- **Verificar**: Transação de deploy

#### **Polygon Mumbai**
- **Explorer**: https://mumbai.polygonscan.com/
- **Buscar**: Endereço do contrato

#### **BSC Testnet**
- **Explorer**: https://testnet.bscscan.com/
- **Buscar**: Endereço do contrato

### **5.2. Verificar Código Fonte (Opcional)**

```bash
npx hardhat verify --network sepolia <ENDERECO_CONTRATO> <args...>
```

**Exemplo**:
```bash
npx hardhat verify --network sepolia 0x... --constructor-args arguments.js
```

### **5.3. Testar Contratos**

```bash
# Testar transferência de tokens
npx hardhat run scripts/test-token.js --network sepolia

# Testar protocolo
npx hardhat run scripts/test-protocol.js --network sepolia

# Testar DAO
npx hardhat run scripts/test-dao.js --network sepolia
```

---

## 6. **TROUBLESHOOTING**

### **Erro: "HH110: Invalid project ID"**

**Causa**: RPC público pode estar indisponível

**Solução**:
1. Usar Alchemy ou Infura (configurar no `.env`)
2. Ou usar outro RPC público

### **Erro: "Insufficient funds"**

**Causa**: Saldo insuficiente na carteira

**Solução**:
1. Verificar saldo no explorer
2. Obter mais fundos no faucet
3. Aguardar confirmação (pode levar alguns minutos)

### **Erro: "Nonce too high"**

**Causa**: Nonce da transação está incorreto

**Solução**:
1. Resetar nonce (usar MetaMask ou similar)
2. Aguardar algumas confirmações
3. Tentar novamente

### **Erro: "Contract already deployed"**

**Causa**: Contrato já foi deployado

**Solução**:
1. Verificar `deployments/{network}_deployments.json`
2. Usar endereço existente
3. Ou usar novo endereço de deployer

### **Erro: "Compilation failed"**

**Causa**: Erro no código Solidity

**Solução**:
1. Verificar logs de compilação
2. Corrigir erros no código
3. Recompilar

---

## 7. **REDES DISPONÍVEIS**

### **Ethereum Sepolia** (Recomendado)
- **Network**: `sepolia`
- **Chain ID**: `11155111`
- **RPC**: `https://rpc.sepolia.org`
- **Explorer**: https://sepolia.etherscan.io/

### **Polygon Mumbai**
- **Network**: `mumbai`
- **Chain ID**: `80001`
- **RPC**: `https://rpc-mumbai.maticvigil.com`
- **Explorer**: https://mumbai.polygonscan.com/

### **BSC Testnet**
- **Network**: `bscTestnet`
- **Chain ID**: `97`
- **RPC**: `https://data-seed-prebsc-1-s1.binance.org:8545`
- **Explorer**: https://testnet.bscscan.com/

---

## 8. **ARQUIVOS DE DEPLOYMENT**

Após o deploy, os endereços são salvos em:
- `deployments/sepolia_deployments.json`
- `deployments/mumbai_deployments.json`
- `deployments/bscTestnet_deployments.json`

**Estrutura**:
```json
{
  "SEVEToken": {
    "contract": "SEVEToken",
    "address": "0x...",
    "transactionHash": "0x...",
    "network": "sepolia",
    "timestamp": "2025-11-07T..."
  },
  "SEVEProtocol": {
    ...
  },
  "SEVEDAO": {
    ...
  }
}
```

---

## 9. **PRÓXIMOS PASSOS**

Após deploy bem-sucedido:

1. ✅ **Verificar contratos** no explorer
2. ✅ **Testar funcionalidades** básicas
3. ✅ **Configurar frontend** (se aplicável)
4. ✅ **Documentar endereços** para referência
5. ✅ **Preparar para mainnet** (quando pronto)

---

## 10. **SEGURANÇA**

### **⚠️ IMPORTANTE**

- ✅ **NUNCA** use chaves de produção em testnet
- ✅ **NUNCA** commite arquivo `.env`
- ✅ **SEMPRE** use carteiras dedicadas para testes
- ✅ **SEMPRE** verifique endereços antes de interagir
- ✅ **SEMPRE** teste localmente antes de testnet

### **Checklist de Segurança**

- [ ] Chave privada é de teste apenas
- [ ] Arquivo `.env` está no `.gitignore`
- [ ] Carteira tem fundos suficientes
- [ ] Rede está correta (testnet, não mainnet)
- [ ] Endereços foram verificados

---

## 📚 **REFERÊNCIAS**

- **Guia de Deploy**: `docs/DEPLOYMENT_GUIDE.md`
- **Testnet Playbook**: `docs/TESTNET_PLAYBOOK.md`
- **Configuração de Ambiente**: `docs/ENV_SETUP.md`
- **Hardhat Docs**: https://hardhat.org/docs

---

**Última Atualização**: 07 de Novembro de 2025  
**Mantido por**: Equipe EON - Symbeon Tech  
**Versão**: 1.0

