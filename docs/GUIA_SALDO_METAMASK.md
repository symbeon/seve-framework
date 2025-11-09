# 💰 Guia: Verificar Saldo e Deploy na Mainnet

**Data**: 09 de Novembro de 2025  
**Objetivo**: Verificar saldo na MetaMask e decidir onde fazer deploy

---

## 🔍 **VERIFICAR SALDO**

### **Opção 1: Via MetaMask (Mais Fácil)**

1. Abra a MetaMask
2. Selecione a rede que deseja verificar:
   - **Polygon Mainnet**
   - **Ethereum Mainnet**
   - **Arbitrum One**
   - **BSC Mainnet**
3. Veja o saldo diretamente na interface

### **Opção 2: Via Script (Mais Detalhado)**

```bash
# Verificar saldo em todas as mainnets
npx hardhat run scripts/check-balance-mainnet.js
```

Este script verifica:
- ✅ Saldo em cada rede
- ✅ Se é suficiente para deploy
- ✅ Links para explorer
- ✅ Recomendações baseadas no saldo

---

## 💡 **O QUE VOCÊ PODE FAZER COM SEU SALDO**

### **Cenário 1: Você tem MATIC (Polygon)** ✅ **IDEAL**

**Saldo necessário**: ~0.01 MATIC ($0.20)

**O que fazer:**
1. ✅ **Deploy em Polygon Mainnet** (recomendado!)
   - Custo: $0.20 para deploy completo
   - Transações: $0.001-0.02 cada
   - **Melhor custo-benefício**

**Comandos:**
```bash
# 1. Configurar Polygon no hardhat.config.js (já está!)
# 2. Verificar saldo
npx hardhat run scripts/check-balance-mainnet.js

# 3. Deploy em Polygon
npx hardhat run scripts/deploy-token.js --network polygon
npx hardhat run scripts/deploy-protocol.js --network polygon
npx hardhat run scripts/deploy-dao.js --network polygon
```

---

### **Cenário 2: Você tem ETH (Ethereum)** ⚠️ **CARO**

**Saldo necessário**: ~0.25 ETH ($500-1,245)

**O que fazer:**
1. ⚠️ **Deploy em Ethereum Mainnet** (caro!)
   - Custo: $500-1,245 para deploy completo
   - Transações: $5-20 cada
   - **Não recomendado para começar**

2. ✅ **Melhor opção: Converter para MATIC e usar Polygon**
   - Use uma bridge (ex: Polygon Bridge)
   - Ou compre MATIC diretamente
   - Deploy em Polygon é 100-1000x mais barato!

**Comandos (se quiser usar Ethereum mesmo):**
```bash
# 1. Verificar saldo
npx hardhat run scripts/check-balance-mainnet.js

# 2. Deploy em Ethereum (CUIDADO: CARO!)
npx hardhat run scripts/deploy-token.js --network ethereum
npx hardhat run scripts/deploy-protocol.js --network ethereum
npx hardhat run scripts/deploy-dao.js --network ethereum
```

---

### **Cenário 3: Você tem ETH (Arbitrum)** ✅ **BOA OPÇÃO**

**Saldo necessário**: ~0.001 ETH ($1.66)

**O que fazer:**
1. ✅ **Deploy em Arbitrum Mainnet**
   - Custo: $1.66 para deploy completo
   - Transações: $0.10-0.50 cada
   - **Balance entre custo e segurança**

**Comandos:**
```bash
# 1. Verificar saldo
npx hardhat run scripts/check-balance-mainnet.js

# 2. Deploy em Arbitrum
npx hardhat run scripts/deploy-token.js --network arbitrum
npx hardhat run scripts/deploy-protocol.js --network arbitrum
npx hardhat run scripts/deploy-dao.js --network arbitrum
```

---

### **Cenário 4: Você tem BNB (BSC)** ✅ **ALTERNATIVA**

**Saldo necessário**: ~0.003 BNB ($0.75)

**O que fazer:**
1. ✅ **Deploy em BSC Mainnet**
   - Custo: $0.75 para deploy completo
   - Transações: $0.02-0.10 cada
   - **Boa alternativa ao Polygon**

**Comandos:**
```bash
# 1. Verificar saldo
npx hardhat run scripts/check-balance-mainnet.js

# 2. Deploy em BSC
npx hardhat run scripts/deploy-token.js --network bsc
npx hardhat run scripts/deploy-protocol.js --network bsc
npx hardhat run scripts/deploy-dao.js --network bsc
```

---

## 🎯 **RECOMENDAÇÃO BASEADA NO SALDO**

### **Se você tem:**

| Token | Saldo | Recomendação |
|-------|-------|--------------|
| **MATIC** | > 0.01 | ✅ **Deploy em Polygon** (melhor opção!) |
| **ETH (Ethereum)** | > 0.25 | ⚠️ Pode fazer, mas Polygon é melhor |
| **ETH (Arbitrum)** | > 0.001 | ✅ Deploy em Arbitrum (boa opção) |
| **BNB** | > 0.003 | ✅ Deploy em BSC (alternativa) |

### **Se você não tem saldo suficiente:**

**Opção 1: Comprar tokens**
- **MATIC**: Compre em exchange (Binance, Coinbase, etc.)
- **ETH**: Compre em exchange
- **BNB**: Compre em exchange

**Opção 2: Usar testnet primeiro**
- Deploy em Sepolia (gratuito)
- Testar funcionalidades
- Depois migrar para mainnet

---

## 📊 **COMPARAÇÃO DE CUSTOS**

### **Deploy Completo (3 Contratos)**

| Rede | Custo | Recomendação |
|------|-------|--------------|
| **Polygon** | $0.20 | ✅ **MELHOR** |
| **BSC** | $0.75 | ✅ Boa alternativa |
| **Arbitrum** | $1.66 | ✅ Balance custo/segurança |
| **Ethereum** | $500-1,245 | ❌ Muito caro |

### **Custo por Transação**

| Rede | Custo | Volume |
|------|-------|--------|
| **Polygon** | $0.001-0.02 | ✅ Alto volume |
| **BSC** | $0.02-0.10 | ✅ Alto volume |
| **Arbitrum** | $0.10-0.50 | ✅ Médio volume |
| **Ethereum** | $5-20 | ❌ Baixo volume |

---

## 🚀 **PRÓXIMOS PASSOS**

### **1. Verificar Saldo**

```bash
npx hardhat run scripts/check-balance-mainnet.js
```

### **2. Escolher Rede**

- **Polygon** (recomendado): Mais barato
- **Arbitrum**: Balance custo/segurança
- **BSC**: Alternativa
- **Ethereum**: Só se tiver orçamento alto

### **3. Fazer Deploy**

```bash
# Exemplo Polygon
npx hardhat run scripts/deploy-token.js --network polygon
npx hardhat run scripts/deploy-protocol.js --network polygon
npx hardhat run scripts/deploy-dao.js --network polygon
```

### **4. Verificar no Explorer**

- **Polygon**: https://polygonscan.com
- **Ethereum**: https://etherscan.io
- **Arbitrum**: https://arbiscan.io
- **BSC**: https://bscscan.com

---

## 📚 **DOCUMENTAÇÃO RELACIONADA**

- **Análise de Custo**: `docs/ANALISE_CUSTO_MAINNET.md`
- **Deployment Guide**: `docs/DEPLOYMENT_GUIDE.md`
- **Troubleshooting**: `docs/TROUBLESHOOTING_DEPLOY.md`

---

**Última Atualização**: 09 de Novembro de 2025  
**Mantido por**: Equipe EON - Symbeon Tech

