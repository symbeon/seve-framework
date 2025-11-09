# 💰 Instruções: Obter Fundos de Teste (Faucet)

**Para fazer deploy na testnet, você precisa de fundos de teste (ETH/MATIC/BNB)**

---

## 🎯 **PROBLEMA ATUAL**

- **Saldo**: 0.0 ETH
- **Necessário**: ~0.034 ETH (para gas do deploy)
- **Solução**: Obter fundos no faucet

---

## 📋 **PASSO A PASSO**

### **1. Obter Endereço da Carteira**

Execute:
```bash
npx hardhat run scripts/check-balance.js --network sepolia
```

O script mostrará o endereço da sua carteira.

### **2. Acessar Faucet**

Escolha um dos faucets abaixo:

#### **Sepolia Faucet** (Recomendado)
- **URL**: https://sepoliafaucet.com/
- **Quantidade**: 0.5 ETH
- **Limite**: 1x por dia

#### **QuickNode Faucet**
- **URL**: https://faucet.quicknode.com/ethereum/sepolia
- **Quantidade**: 0.1 ETH
- **Requer**: Conta QuickNode (gratuita)

#### **Alchemy Faucet**
- **URL**: https://www.alchemy.com/faucets/ethereum-sepolia
- **Quantidade**: 0.5 ETH
- **Requer**: Conta Alchemy (gratuita)

### **3. Colar Endereço**

1. Copie o endereço da sua carteira (do passo 1)
2. Cole no campo do faucet
3. Complete o captcha/verificação
4. Clique em "Send Me ETH" ou similar

### **4. Aguardar Confirmação**

- ⏱️ Pode levar de 1 a 10 minutos
- ✅ Verifique no explorer: https://sepolia.etherscan.io/

### **5. Verificar Saldo**

Execute novamente:
```bash
npx hardhat run scripts/check-balance.js --network sepolia
```

Deve mostrar saldo > 0.01 ETH.

### **6. Executar Deploy**

Agora você pode fazer o deploy:
```bash
.\scripts\deploy-testnet.ps1 sepolia
```

---

## 🔄 **ALTERNATIVAS**

### **Se Sepolia Estiver Lento**

#### **Polygon Mumbai** (Geralmente Mais Rápido)

1. **Faucet**: https://faucet.polygon.technology/
2. **Deploy**: `.\scripts\deploy-testnet.ps1 mumbai`

#### **BSC Testnet** (Muito Rápido)

1. **Faucet**: https://testnet.bnbchain.org/faucet-smart
2. **Deploy**: `.\scripts\deploy-testnet.ps1 bscTestnet`

---

## ⚠️ **PROBLEMAS COMUNS**

### **Faucet Não Funciona**

- Tente outro faucet
- Aguarde alguns minutos e tente novamente
- Verifique se o endereço está correto

### **Fundos Não Chegam**

- Verifique no explorer: https://sepolia.etherscan.io/
- Pode levar até 10 minutos
- Verifique se o endereço está correto

### **Limite Atingido**

- Aguarde 24 horas
- Ou use outro faucet
- Ou use outra testnet (Mumbai/BSC)

---

## ✅ **CHECKLIST**

- [ ] Endereço da carteira obtido
- [ ] Fundos solicitados no faucet
- [ ] Confirmação recebida (verificar no explorer)
- [ ] Saldo verificado (> 0.01 ETH)
- [ ] Pronto para deploy!

---

**Última Atualização**: 07 de Novembro de 2025  
**Mantido por**: Equipe EON - Symbeon Tech

