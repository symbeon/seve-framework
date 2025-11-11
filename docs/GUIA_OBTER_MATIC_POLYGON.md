# 💰 Guia: Como Obter MATIC para Deploy em Polygon Mainnet

**Data**: 09 de Novembro de 2025  
**Objetivo**: Obter MATIC suficiente para deploy (~0.05 MATIC = ~$0.25)

---

## 🎯 **OPÇÕES PARA OBTER MATIC**

### **OPÇÃO 1: Comprar MATIC Diretamente** ✅ (Mais Rápido)

#### **1.1 Exchanges Recomendadas**
- **Binance**: https://www.binance.com/
- **Coinbase**: https://www.coinbase.com/
- **Kraken**: https://www.kraken.com/
- **Crypto.com**: https://crypto.com/

#### **1.2 Processo**
1. Criar conta na exchange
2. Fazer KYC (verificação de identidade)
3. Depositar fiat (BRL, USD, etc.)
4. Comprar MATIC
5. Retirar para sua wallet MetaMask

#### **1.3 Custo**
- **Valor necessário**: ~$0.25 USD (0.05 MATIC)
- **Taxa de exchange**: ~$1-5 USD
- **Taxa de retirada**: ~$0.01-0.10 USD
- **Total**: ~$1.50-5.50 USD

---

### **OPÇÃO 2: Bridge de Ethereum para Polygon** ✅

#### **2.1 Se você tem ETH na Ethereum Mainnet**
1. Acessar **Polygon Bridge**: https://portal.polygon.technology/polygon/bridge
2. Conectar MetaMask
3. Selecionar Ethereum → Polygon
4. Inserir quantidade (mínimo ~0.001 ETH = ~$2-3)
5. Confirmar transação
6. Aguardar ~10-15 minutos

#### **2.2 Custo**
- **Gas na Ethereum**: ~$2-10 USD
- **Valor bridgeado**: ~$2-3 USD
- **Total**: ~$4-13 USD

---

### **OPÇÃO 3: Usar Exchange com Suporte Direto a Polygon** ✅

#### **3.1 Exchanges com Suporte**
- **Binance**: Suporta retirada direta para Polygon
- **Crypto.com**: Suporta retirada direta para Polygon
- **Kucoin**: Suporta retirada direta para Polygon

#### **3.2 Processo**
1. Comprar MATIC na exchange
2. Selecionar retirada para Polygon Network
3. Inserir endereço da MetaMask
4. Confirmar retirada
5. Aguardar confirmação (~5-10 minutos)

#### **3.3 Custo**
- **Valor necessário**: ~$0.25 USD
- **Taxa de exchange**: ~$1-5 USD
- **Taxa de retirada**: ~$0.01-0.10 USD
- **Total**: ~$1.50-5.50 USD

---

### **OPÇÃO 4: Usar Cartão de Crédito/Débito** ✅ (Mais Conveniente)

#### **4.1 Serviços Recomendados**
- **MoonPay**: https://www.moonpay.com/
- **Ramp Network**: https://ramp.network/
- **Transak**: https://transak.com/

#### **4.2 Processo**
1. Acessar serviço
2. Conectar MetaMask
3. Selecionar Polygon Network
4. Inserir valor (mínimo ~$10-20)
5. Pagar com cartão
6. Receber MATIC diretamente na wallet

#### **4.3 Custo**
- **Valor mínimo**: ~$10-20 USD
- **Taxa de serviço**: ~3-5%
- **Total**: ~$10-25 USD

---

## 🎯 **RECOMENDAÇÃO**

### **Para Deploy Rápido** ⚡
**Usar MoonPay/Ramp/Transak** (Opção 4)
- Mais rápido
- Mais conveniente
- Recebe direto na wallet
- Custo: ~$10-25

### **Para Custo Mínimo** 💰
**Comprar em Exchange e Retirar** (Opção 1 ou 3)
- Mais barato
- Requer conta em exchange
- Custo: ~$1.50-5.50

### **Se Já Tem ETH** 🔄
**Usar Polygon Bridge** (Opção 2)
- Usa ETH existente
- Requer gas na Ethereum
- Custo: ~$4-13

---

## 📋 **CHECKLIST APÓS OBTER MATIC**

- [ ] MATIC recebido na MetaMask
- [ ] Rede Polygon configurada na MetaMask
- [ ] Saldo verificado (0.05+ MATIC)
- [ ] Endereço correto confirmado
- [ ] Pronto para deploy

---

## 🔧 **CONFIGURAR POLYGON NA METAMASK**

### **Passo a Passo**

1. **Abrir MetaMask**
2. **Clicar em "Networks"** (topo)
3. **Clicar em "Add Network"**
4. **Inserir Dados**:
   - **Network Name**: Polygon Mainnet
   - **RPC URL**: `https://polygon-rpc.com`
   - **Chain ID**: `137`
   - **Currency Symbol**: `MATIC`
   - **Block Explorer**: `https://polygonscan.com`

5. **Salvar**

---

## ✅ **VERIFICAR SALDO**

Após obter MATIC, verificar:

```bash
node scripts/check-balance-mainnet.js
```

Ou verificar diretamente no PolygonScan:
https://polygonscan.com/address/SEU_ENDERECO

---

## 🚀 **PRÓXIMO PASSO**

Após obter MATIC suficiente (0.05+ MATIC):

```bash
# 1. Compilar contratos
npm run compile

# 2. Deploy em Polygon
npm run deploy:polygon

# 3. Ativar monetização
hardhat run scripts/add-version-v1.js --network polygon
hardhat run scripts/create-dao-proposal.js --network polygon
hardhat run scripts/register-first-agent.js --network polygon
```

---

**Última Atualização**: 09 de Novembro de 2025  
**Status**: ⚠️ **AGUARDANDO SALDO EM POLYGON**

