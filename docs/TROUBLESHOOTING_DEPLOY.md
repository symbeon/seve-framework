# 🔧 Troubleshooting: Deploy na Testnet

**Problemas Comuns e Soluções**

---

## ❌ **Erro: UND_ERR_HEADERS_TIMEOUT**

### **Causa**
Timeout na conexão com o RPC público. O RPC pode estar lento ou indisponível.

### **Soluções**

#### **1. Usar RPC Provider (Recomendado)**

**Alchemy** (Gratuito):
1. Criar conta: https://www.alchemy.com/
2. Criar novo app (Ethereum Sepolia)
3. Copiar HTTP URL
4. Adicionar no `.env`:
   ```bash
   ALCHEMY_URL=https://eth-sepolia.g.alchemy.com/v2/SUA_KEY
   ```

**Infura** (Gratuito):
1. Criar conta: https://infura.io/
2. Criar novo projeto (Ethereum Sepolia)
3. Copiar Endpoint URL
4. Adicionar no `.env`:
   ```bash
   INFURA_URL=https://sepolia.infura.io/v3/SUA_KEY
   ```

#### **2. Aumentar Timeout**

Editar `hardhat.config.js`:
```javascript
networks: {
  sepolia: {
    url: process.env.ALCHEMY_URL || "https://rpc.sepolia.org",
    timeout: 120000, // 2 minutos
    accounts: [process.env.PRIVATE_KEY || ""],
    chainId: 11155111,
  }
}
```

#### **3. Tentar Outra Testnet**

**Polygon Mumbai** (geralmente mais rápido):
```bash
npx hardhat run scripts/deploy-token.js --network mumbai
```

**BSC Testnet** (muito rápido):
```bash
npx hardhat run scripts/deploy-token.js --network bscTestnet
```

---

## ❌ **Erro: Insufficient funds**

### **Causa**
Carteira não tem fundos suficientes para pagar gas.

### **Solução**
1. Verificar saldo no explorer:
   - Sepolia: https://sepolia.etherscan.io/
   - Mumbai: https://mumbai.polygonscan.com/
   - BSC: https://testnet.bscscan.com/

2. Obter fundos no faucet:
   - **Sepolia**: https://sepoliafaucet.com/
   - **Mumbai**: https://faucet.polygon.technology/
   - **BSC**: https://testnet.bnbchain.org/faucet-smart

3. Aguardar confirmação (pode levar alguns minutos)

---

## ❌ **Erro: Nonce too high**

### **Causa**
Nonce da transação está incorreto.

### **Solução**
1. Verificar nonce atual no explorer
2. Resetar nonce (usar MetaMask ou similar)
3. Aguardar algumas confirmações
4. Tentar novamente

---

## ❌ **Erro: Invalid project ID**

### **Causa**
RPC provider retornou erro de autenticação.

### **Solução**
1. Verificar se a API key está correta
2. Verificar se o projeto está ativo
3. Verificar se está usando a URL correta
4. Tentar criar novo projeto

---

## ❌ **Erro: Contract already deployed**

### **Causa**
Contrato já foi deployado anteriormente.

### **Solução**
1. Verificar `deployments/{network}_deployments.json`
2. Usar endereço existente
3. Ou usar novo endereço de deployer

---

## ❌ **Erro: Compilation failed**

### **Causa**
Erro no código Solidity.

### **Solução**
1. Verificar logs de compilação
2. Corrigir erros no código
3. Recompilar:
   ```bash
   npx hardhat clean
   npx hardhat compile
   ```

---

## ⚠️ **Problemas de Rede**

### **RPC Público Lento**

**Sintomas**:
- Timeouts frequentes
- Transações demoram muito

**Solução**:
- Usar RPC provider (Alchemy/Infura)
- Ou tentar em horário de menor tráfego

### **Rede Congestionada**

**Sintomas**:
- Transações ficam pendentes
- Gas price muito alto

**Solução**:
- Aguardar confirmação
- Ou usar outra testnet (Mumbai/BSC)

---

## ✅ **Checklist de Verificação**

Antes de tentar deploy novamente:

- [ ] PRIVATE_KEY configurada no .env
- [ ] Carteira tem fundos suficientes
- [ ] RPC provider configurado (se usar)
- [ ] Rede está correta (testnet, não mainnet)
- [ ] Contratos compilam sem erros
- [ ] Testes passam localmente
- [ ] Conexão de internet estável

---

## 📞 **Ainda com Problemas?**

1. **Verificar logs completos**:
   ```bash
   npx hardhat run scripts/deploy-token.js --network sepolia --verbose
   ```

2. **Testar conexão RPC**:
   ```bash
   node -e "const { ethers } = require('ethers'); const provider = new ethers.JsonRpcProvider('https://rpc.sepolia.org'); provider.getBlockNumber().then(console.log).catch(console.error);"
   ```

3. **Verificar configuração**:
   ```bash
   npx hardhat run scripts/deploy-token.js --network sepolia --show-stack-traces
   ```

---

**Última Atualização**: 07 de Novembro de 2025  
**Mantido por**: Equipe EON - Symbeon Tech

