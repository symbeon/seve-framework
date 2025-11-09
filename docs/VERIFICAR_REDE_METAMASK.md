# 🌐 Como Verificar e Trocar Rede na MetaMask

**Para fazer deploy na testnet, você precisa estar na rede Sepolia (testnet)**

---

## 🔍 **VERIFICAR REDE ATUAL**

### **Na MetaMask:**

1. Olhe o **topo esquerdo** da MetaMask
2. Veja qual rede está selecionada:
   - **"Ethereum Mainnet"** = Rede principal (não serve para testnet)
   - **"Sepolia"** = Testnet (correto para deploy)
   - **"Mumbai"** = Polygon testnet
   - **"BSC Testnet"** = Binance testnet

---

## 🔄 **TROCAR PARA SEPOLIA (TESTNET)**

### **Passo a Passo:**

1. **Clique no logo da rede** (topo esquerdo, onde mostra "Ethereum" ou rede atual)

2. **Ativar Testnets:**
   - Role até encontrar **"Show test networks"**
   - **Ative o toggle** (deve ficar azul/ligado)

3. **Selecionar Sepolia:**
   - Procure por **"Sepolia"** na lista
   - Clique em **"Sepolia"**
   - A rede deve mudar para "Sepolia" no topo

4. **Verificar:**
   - No topo deve aparecer **"Sepolia"** (não "Ethereum Mainnet")
   - O saldo pode ser diferente (testnet tem ETH de teste)

---

## 💰 **FUNDOS EM SEPOLIA**

### **Se não tiver fundos em Sepolia:**

1. **Copie seu endereço:**
   - Clique no endereço (0x863de...6DA76)
   - Copie o endereço completo

2. **Acesse um faucet:**
   - https://sepoliafaucet.com/
   - https://faucet.quicknode.com/ethereum/sepolia
   - https://www.alchemy.com/faucets/ethereum-sepolia

3. **Cole o endereço e solicite fundos**

4. **Aguarde confirmação** (1-10 minutos)

---

## ✅ **CHECKLIST ANTES DO DEPLOY**

- [ ] MetaMask está na rede **Sepolia** (não Mainnet)
- [ ] Carteira tem fundos de teste (Sepolia ETH)
- [ ] Endereço copiado (para exportar chave privada)
- [ ] Chave privada exportada e adicionada no `.env`

---

## 🔐 **EXPORTAR CHAVE PRIVADA**

Após verificar que está na rede correta:

1. **Menu** (3 linhas) → **Configurações** → **Segurança**
2. **Exportar Chave Privada**
3. **Digite senha** e copie a chave
4. **Remova o `0x`** e adicione no `.env`:
   ```bash
   PRIVATE_KEY=sua_chave_sem_0x
   ```

---

## 🚀 **DEPOIS DE CONFIGURAR**

1. **Verificar saldo:**
   ```bash
   npx hardhat run scripts/check-balance.js --network sepolia
   ```

2. **Se saldo aparecer, fazer deploy:**
   ```bash
   .\scripts\deploy-testnet.ps1 sepolia
   ```

---

## ⚠️ **IMPORTANTE**

- **NUNCA** use chave privada de carteira com fundos reais em testnet
- **SEMPRE** verifique se está na rede correta antes de fazer transações
- **TESTNET** = Sepolia, Mumbai, BSC Testnet
- **MAINNET** = Ethereum, Polygon, BSC (cuidado!)

---

**Última Atualização**: 07 de Novembro de 2025  
**Mantido por**: Equipe EON - Symbeon Tech

