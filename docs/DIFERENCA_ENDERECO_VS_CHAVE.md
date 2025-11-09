# 🔐 Diferença: Endereço vs Chave Privada

**⚠️ IMPORTANTE**: São coisas completamente diferentes!

---

## 📧 **ENDEREÇO (Wallet Address)**

### **O que é:**
- **Endereço público** da carteira
- Formato: `0x` + 40 caracteres hexadecimais
- Exemplo: `0x863de15091DfE5C044Dc1bD54f85210B6Bb6DA76`
- **Pode ser compartilhado publicamente**

### **Para que serve:**
- ✅ Receber fundos
- ✅ Verificar saldo no explorer
- ✅ Identificar carteira
- ✅ Compartilhar para receber pagamentos

### **O que NÃO faz:**
- ❌ Não permite fazer deploy
- ❌ Não permite assinar transações
- ❌ Não permite enviar fundos

---

## 🔑 **CHAVE PRIVADA (Private Key)**

### **O que é:**
- **Chave secreta** da carteira
- Formato: `0x` + 64 caracteres hexadecimais
- Exemplo: `0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef`
- **NUNCA compartilhe!**

### **Para que serve:**
- ✅ Fazer deploy de contratos
- ✅ Assinar transações
- ✅ Enviar fundos
- ✅ Configurar ferramentas de desenvolvimento

### **Segurança:**
- ⚠️ Quem tem a chave privada tem controle total da carteira
- ⚠️ Use apenas para testnet
- ⚠️ Nunca commite no Git
- ⚠️ Mantenha em `.env` (que está no `.gitignore`)

---

## 📊 **COMPARAÇÃO**

| Característica | Endereço | Chave Privada |
|----------------|----------|---------------|
| **Formato** | `0x` + 40 chars | `0x` + 64 chars |
| **Tamanho** | 42 caracteres | 66 caracteres |
| **Visibilidade** | Público | Secreto |
| **Uso** | Receber/Verificar | Deploy/Enviar |
| **Compartilhar** | ✅ Sim | ❌ NUNCA |
| **Exemplo** | `0x863de...6DA76` | `0x1234...cdef` |

---

## 🔍 **COMO ENCONTRAR A CHAVE PRIVADA**

### **Na MetaMask:**

1. **Menu** (3 linhas) → **Configurações**
2. **Segurança e Privacidade**
3. **Exportar Chave Privada** (não "Exportar Endereço")
4. **Selecione a conta** (ex: `0x863de...6DA76`)
5. **Digite senha**
6. **Copie a chave** (vem com `0x`)

### **Formato Esperado:**

```
0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
```

**Para usar no `.env`**, remova o `0x`:
```bash
PRIVATE_KEY=1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
```

---

## ✅ **PARA O DEPLOY**

**Você precisa:**
- ✅ **Chave Privada** (não endereço)
- ✅ Da conta específica: `0x863de15091DfE5C044Dc1bD54f85210B6Bb6DA76`
- ✅ No formato correto (sem `0x` no `.env`)

**Você NÃO precisa:**
- ❌ Endereço (já temos: `0x863de...6DA76`)
- ❌ Secret Recovery Phrase

---

## 🔐 **VERIFICAÇÃO**

Após configurar a chave privada, execute:

```bash
npx hardhat run scripts/check-balance.js --network sepolia
```

**Deve mostrar:**
```
📧 Endereço: 0x863de15091DfE5C044Dc1bD54f85210B6Bb6DA76
💰 Saldo: 0.2 ETH
✅ Saldo suficiente para deploy!
```

Se o endereço corresponder, a chave privada está correta!

---

## ⚠️ **SEGURANÇA**

### **Endereço (0x863de...6DA76):**
- ✅ Pode compartilhar
- ✅ Pode usar em explorers
- ✅ Pode mostrar publicamente

### **Chave Privada:**
- ❌ NUNCA compartilhe
- ❌ NUNCA commite no Git
- ❌ NUNCA envie por email/mensagem
- ✅ Use apenas para testnet
- ✅ Mantenha em `.env` (no `.gitignore`)

---

**Última Atualização**: 07 de Novembro de 2025  
**Mantido por**: Equipe EON - Symbeon Tech

