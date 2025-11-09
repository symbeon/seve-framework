# 🔐 Como Exportar Chave Privada da MetaMask (Com Segurança)

**⚠️ ATENÇÃO: Use apenas para testnet! NUNCA compartilhe sua chave privada!**

---

## 📋 **PASSO A PASSO**

### **1. Abrir MetaMask**

1. Abra a extensão MetaMask no navegador
2. Faça login na sua carteira

### **2. Acessar Configurações**

1. Clique no ícone de menu (três linhas) no canto superior direito
2. Vá em **"Configurações"** (Settings)

### **3. Acessar Segurança e Privacidade**

1. No menu lateral, clique em **"Segurança e Privacidade"**
2. Role até encontrar **"Exportar Chave Privada"**

### **4. Exportar Chave Privada**

1. Clique em **"Exportar Chave Privada"**
2. Digite sua senha da MetaMask
3. **Copie a chave privada** (começa com `0x`)

### **5. Remover o Prefixo 0x**

A chave privada vem com `0x` no início. Para o `.env`, remova o `0x`:

**Exemplo:**
- MetaMask mostra: `0xabc123...`
- Use no .env: `abc123...` (sem o 0x)

### **6. Adicionar no .env**

Abra o arquivo `.env` e atualize:

```bash
PRIVATE_KEY=abc123... (sua chave sem o 0x)
ALCHEMY_URL=https://eth-sepolia.g.alchemy.com/v2/7L7HVozadjC31jHNhz9pX
NETWORK=sepolia
```

---

## ⚠️ **SEGURANÇA**

### **NUNCA:**

- ❌ Compartilhe sua chave privada
- ❌ Commite o arquivo `.env` no Git
- ❌ Use chave de produção em testnet
- ❌ Envie chave privada por email/mensagem

### **SEMPRE:**

- ✅ Use apenas para testnet
- ✅ Mantenha `.env` no `.gitignore`
- ✅ Use carteira separada para testes
- ✅ Verifique se está na rede correta (Sepolia, não Mainnet)

---

## 🔍 **VERIFICAR SE ESTÁ CORRETO**

Após configurar, execute:

```bash
npx hardhat run scripts/check-balance.js --network sepolia
```

O endereço mostrado deve corresponder ao endereço da sua carteira MetaMask.

---

## ✅ **CHECKLIST**

- [ ] Chave privada exportada da MetaMask
- [ ] Prefixo `0x` removido
- [ ] Adicionada no `.env` como `PRIVATE_KEY=...`
- [ ] Saldo verificado (deve mostrar fundos)
- [ ] Endereço corresponde à MetaMask

---

**Última Atualização**: 07 de Novembro de 2025  
**Mantido por**: Equipe EON - Symbeon Tech

