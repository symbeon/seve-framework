# 🚀 Plano de Deploy: Polygon Mainnet - SEVE Framework

**Data**: 09 de Novembro de 2025  
**Objetivo**: Deploy dos smart contracts na Polygon Mainnet para produção comercial  
**Status**: ⚠️ **PREPARAÇÃO**

---

## 🎯 **OBJETIVO**

Deploy completo dos smart contracts SEVE na Polygon Mainnet:
1. SEVEToken (ERC-20)
2. SEVEProtocol (Licenciamento)
3. SEVEDAO (Governança)

**Custo Estimado**: ~$0.20 USD (muito mais barato que Ethereum!)

---

## 📋 **CHECKLIST PRÉ-DEPLOY**

### **1. Preparação**
- [ ] Verificar saldo de MATIC na wallet
- [ ] Configurar RPC URL para Polygon (Alchemy ou Infura)
- [ ] Verificar PRIVATE_KEY no .env
- [ ] Compilar contratos
- [ ] Testar deploy localmente (opcional)

### **2. Deploy**
- [ ] Deploy SEVEToken
- [ ] Deploy SEVEProtocol (com endereço do token)
- [ ] Deploy SEVEDAO (com endereço do token)
- [ ] Salvar deployments em `deployments/polygon_deployments.json`

### **3. Ativação**
- [ ] Adicionar versão v1.0.0 ao protocolo
- [ ] Criar primeira proposta no DAO
- [ ] Registrar primeiro agente
- [ ] Verificar todas as transações

### **4. Validação**
- [ ] Verificar contratos no PolygonScan
- [ ] Testar funcionalidades básicas
- [ ] Validar endereços e hashes

---

## 💰 **CUSTOS ESTIMADOS**

### **Deploy**
- **SEVEToken**: ~$0.06 USD
- **SEVEProtocol**: ~$0.07 USD
- **SEVEDAO**: ~$0.07 USD
- **Total**: ~$0.20 USD

### **Ativação**
- **Add Version**: ~$0.002 USD
- **Create Proposal**: ~$0.01 USD
- **Register Agent**: ~$0.002 USD
- **Total**: ~$0.014 USD

### **Total Geral**: ~$0.21 USD

**Recomendação**: Ter pelo menos **0.1 MATIC** na wallet (~$0.08 USD)

---

## 🔧 **CONFIGURAÇÃO NECESSÁRIA**

### **1. RPC URL para Polygon**

**Opção 1: Alchemy (Recomendado)**
```
POLYGON_RPC_URL=https://polygon-mainnet.g.alchemy.com/v2/YOUR_API_KEY
```

**Opção 2: Infura**
```
POLYGON_RPC_URL=https://polygon-mainnet.infura.io/v3/YOUR_PROJECT_ID
```

**Opção 3: Public RPC**
```
POLYGON_RPC_URL=https://polygon-rpc.com
```

### **2. Atualizar hardhat.config.js**

Adicionar configuração específica para Polygon:
```javascript
polygon: {
  url: process.env.POLYGON_RPC_URL || "https://polygon-rpc.com",
  accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
  chainId: 137,
  gasPrice: 30000000000, // 30 gwei
  timeout: 120000
}
```

---

## 📝 **SCRIPTS DE DEPLOY**

### **Script 1: Deploy Token**
```bash
npx hardhat run scripts/deploy-token.js --network polygon
```

### **Script 2: Deploy Protocol**
```bash
npx hardhat run scripts/deploy-protocol.js --network polygon
```

### **Script 3: Deploy DAO**
```bash
npx hardhat run scripts/deploy-dao.js --network polygon
```

### **Script Combinado** (criar):
```bash
npm run deploy:polygon
```

---

## ⚠️ **PONTOS DE ATENÇÃO**

### **1. Saldo de MATIC**
- Verificar saldo antes de deploy
- Ter pelo menos 0.1 MATIC
- Considerar gas para todas as transações

### **2. Gas Price**
- Polygon geralmente tem gas price baixo (30 gwei)
- Pode ajustar se necessário
- Verificar gas price atual antes de deploy

### **3. Confirmações**
- Polygon confirma transações em ~2-3 segundos
- Aguardar confirmação antes de próxima transação
- Verificar no PolygonScan

### **4. Segurança**
- **NUNCA** commitar PRIVATE_KEY
- Usar variáveis de ambiente
- Verificar endereços antes de confirmar

---

## 🔗 **LINKS ÚTEIS**

- **PolygonScan**: https://polygonscan.com/
- **Polygon RPC**: https://polygon-rpc.com/
- **Gas Tracker**: https://polygonscan.com/gastracker
- **Faucet**: Não necessário (mainnet)

---

## ✅ **PRÓXIMOS PASSOS APÓS DEPLOY**

1. **Verificar Contratos no PolygonScan**
2. **Ativar Monetização** (add version, create proposal, register agent)
3. **Testar Funcionalidades**
4. **Documentar Endereços**
5. **Anunciar Deploy**

---

**Última Atualização**: 09 de Novembro de 2025
