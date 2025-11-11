# 🚀 Plano de Deploy: Polygon Mainnet - SEVE Framework

**Data**: 09 de Novembro de 2025  
**Objetivo**: Deploy completo em Polygon Mainnet para produção comercial  
**Custo Estimado**: ~$0.20 USD (muito barato!)

---

## 🎯 **OBJETIVO**

Deploy dos 3 smart contracts do SEVE Framework em Polygon Mainnet:
1. **SEVEToken** (ERC-20)
2. **SEVEProtocol** (Licenciamento)
3. **SEVEDAO** (Governança)

---

## 📊 **PRÉ-REQUISITOS**

### **1. Saldo Necessário**
- **Mínimo**: 0.01 MATIC (~$0.20)
- **Recomendado**: 0.05 MATIC (~$1.00) para margem de segurança

### **2. Configuração**
- ✅ `.env` com `PRIVATE_KEY` configurada
- ✅ `hardhat.config.js` com rede Polygon configurada
- ✅ Contratos compilados

### **3. Verificações**
- [ ] Saldo suficiente em Polygon
- [ ] Private key segura e correta
- [ ] RPC URL funcionando
- [ ] Contratos testados

---

## 🔧 **PASSO A PASSO**

### **FASE 1: Preparação**

#### **1.1 Verificar Saldo**
```bash
node scripts/check-balance-mainnet.js
```

#### **1.2 Compilar Contratos**
```bash
npm run compile
```

#### **1.3 Verificar Configuração**
- Confirmar `PRIVATE_KEY` no `.env`
- Confirmar RPC URL do Polygon
- Confirmar `chainId: 137` no hardhat.config.js

---

### **FASE 2: Deploy dos Contratos**

#### **2.1 Deploy SEVEToken**
```bash
npm run deploy:polygon
# ou
hardhat run scripts/deploy-token.js --network polygon
```

**Resultado Esperado**:
- Endereço do contrato
- Transaction hash
- Salvo em `deployments/polygon_deployments.json`

#### **2.2 Deploy SEVEProtocol**
```bash
hardhat run scripts/deploy-protocol.js --network polygon
```

**Resultado Esperado**:
- Endereço do contrato
- Token address vinculado
- Transaction hash

#### **2.3 Deploy SEVEDAO**
```bash
hardhat run scripts/deploy-dao.js --network polygon
```

**Resultado Esperado**:
- Endereço do contrato
- Token address vinculado
- Transaction hash

---

### **FASE 3: Ativação de Monetização**

#### **3.1 Adicionar Versão v1.0.0**
```bash
# Criar script adaptado para Polygon
hardhat run scripts/add-version-v1.js --network polygon
```

#### **3.2 Criar Proposta no DAO**
```bash
hardhat run scripts/create-dao-proposal.js --network polygon
```

#### **3.3 Registrar Primeiro Agente**
```bash
hardhat run scripts/register-first-agent.js --network polygon
```

---

### **FASE 4: Verificação e Validação**

#### **4.1 Verificar Contratos no Explorer**
- PolygonScan: https://polygonscan.com/
- Verificar código fonte (se possível)
- Verificar transações

#### **4.2 Testar Funcionalidades**
- Transferência de tokens
- Compra de licença (teste)
- Criação de proposta
- Registro de agente

#### **4.3 Documentar Deployments**
- Atualizar `deployments/polygon_deployments.json`
- Criar documento de confirmação
- Atualizar README com endereços

---

## 💰 **CUSTOS ESTIMADOS**

### **Deploy**
- **SEVEToken**: ~0.07 MATIC (~$0.06)
- **SEVEProtocol**: ~0.07 MATIC (~$0.07)
- **SEVEDAO**: ~0.07 MATIC (~$0.07)
- **Total**: ~0.21 MATIC (~$0.20)

### **Ativação**
- **Add Version**: ~0.01 MATIC (~$0.01)
- **Create Proposal**: ~0.02 MATIC (~$0.02)
- **Register Agent**: ~0.02 MATIC (~$0.02)
- **Total**: ~0.05 MATIC (~$0.05)

### **TOTAL GERAL**: ~0.26 MATIC (~$0.25)

---

## ⚠️ **PONTOS DE ATENÇÃO**

### **1. Segurança**
- ✅ Private key nunca deve ser commitada
- ✅ Usar `.env` para variáveis sensíveis
- ✅ Verificar endereços antes de confirmar

### **2. Gas Price**
- Polygon geralmente tem gas price baixo (30 gwei)
- Pode ajustar se necessário no hardhat.config.js

### **3. Confirmações**
- Polygon confirma transações em ~2-3 segundos
- Aguardar pelo menos 1 confirmação antes de continuar

### **4. Backup**
- Fazer backup de `deployments/polygon_deployments.json`
- Salvar transaction hashes
- Documentar todos os endereços

---

## 📋 **CHECKLIST COMPLETO**

### **Antes do Deploy**
- [ ] Saldo suficiente em Polygon (0.05+ MATIC)
- [ ] Private key configurada no `.env`
- [ ] RPC URL funcionando
- [ ] Contratos compilados
- [ ] Testes passando (se aplicável)

### **Durante o Deploy**
- [ ] Deploy SEVEToken
- [ ] Deploy SEVEProtocol
- [ ] Deploy SEVEDAO
- [ ] Verificar cada deployment

### **Após o Deploy**
- [ ] Adicionar versão v1.0.0
- [ ] Criar proposta no DAO
- [ ] Registrar primeiro agente
- [ ] Verificar no PolygonScan
- [ ] Testar funcionalidades básicas
- [ ] Documentar tudo

---

## 🎯 **RESULTADO ESPERADO**

Após o deploy completo, teremos:

1. ✅ **3 Contratos Deployados** em Polygon Mainnet
2. ✅ **Versão v1.0.0** disponível para licenciamento
3. ✅ **DAO Ativo** com primeira proposta
4. ✅ **Primeiro Agente** registrado
5. ✅ **Monetização Ativa** em produção

---

## 📚 **DOCUMENTAÇÃO RELACIONADA**

- **Análise de Custos**: `docs/ANALISE_CUSTO_MAINNET.md`
- **Deployment Guide**: `docs/DEPLOYMENT_GUIDE.md`
- **Testnet Success**: `docs/DEPLOYMENT_SUCCESS.md`
- **Monetization Plan**: `docs/PLANO_MONETIZACAO_BLOCKCHAIN.md`

---

**Última Atualização**: 09 de Novembro de 2025  
**Status**: ⚠️ **AGUARDANDO EXECUÇÃO**

