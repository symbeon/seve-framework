# 🔐 Diferença: Secret Recovery Phrase vs Private Key

**⚠️ IMPORTANTE**: São coisas diferentes!

---

## 📋 **SECRET RECOVERY PHRASE (SRP)**

### **O que é:**
- **12 ou 24 palavras** em inglês
- Exemplo: "course ball goose adult valve hundred dinner chimney hint offer deliver athlete"
- Usada para **restaurar a carteira inteira**

### **Quando usar:**
- ✅ Restaurar carteira em novo dispositivo
- ✅ Recuperar acesso se perder senha
- ✅ Backup completo da carteira

### **Quando NÃO usar:**
- ❌ Para deploy de smart contracts
- ❌ Para configurar Hardhat
- ❌ Para scripts de deploy

---

## 🔑 **PRIVATE KEY (Chave Privada)**

### **O que é:**
- **Chave hexadecimal** de 64 caracteres
- Formato: `0x` seguido de 64 caracteres hexadecimais
- Exemplo: `0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef`
- Específica para **UMA conta** dentro da carteira

### **Quando usar:**
- ✅ Deploy de smart contracts
- ✅ Configurar Hardhat
- ✅ Scripts de deploy
- ✅ Integração com ferramentas de desenvolvimento

### **Quando NÃO usar:**
- ❌ Para restaurar carteira inteira
- ❌ Para backup completo

---

## 🔍 **COMO ENCONTRAR A PRIVATE KEY**

### **Na MetaMask:**

1. **Feche a tela da Secret Recovery Phrase** (se estiver aberta)

2. **Acesse Configurações:**
   - Clique no **menu** (3 linhas no canto superior direito)
   - Vá em **"Configurações"** (Settings)

3. **Acesse Segurança:**
   - Clique em **"Segurança e Privacidade"** (Security & Privacy)
   - Role até encontrar **"Exportar Chave Privada"** (Export Private Key)

4. **Selecione a Conta:**
   - Selecione a conta que tem fundos (ex: "Symb_#01")
   - Digite sua **senha da MetaMask**

5. **Copie a Chave:**
   - A chave aparecerá como: `0x1234567890abcdef...`
   - **Copie essa chave completa**

6. **Para usar no .env:**
   - **Remova o `0x`** do início
   - Adicione no `.env`: `PRIVATE_KEY=1234567890abcdef...`

---

## 📊 **COMPARAÇÃO**

| Característica | Secret Recovery Phrase | Private Key |
|----------------|----------------------|-------------|
| **Formato** | 12-24 palavras | 64 caracteres hex |
| **Tamanho** | ~100+ caracteres | 66 caracteres (com 0x) |
| **Uso** | Restaurar carteira | Deploy/scripts |
| **Escopo** | Carteira inteira | Uma conta |
| **Exemplo** | "course ball goose..." | `0x1234...cdef` |

---

## ⚠️ **SEGURANÇA**

### **NUNCA:**
- ❌ Compartilhe Secret Recovery Phrase
- ❌ Compartilhe Private Key
- ❌ Commite no Git
- ❌ Envie por email/mensagem

### **SEMPRE:**
- ✅ Use apenas para testnet
- ✅ Mantenha `.env` no `.gitignore`
- ✅ Use carteira separada para testes
- ✅ Verifique rede antes de usar

---

## ✅ **PARA O DEPLOY**

**Você precisa da:**
- ✅ **Private Key** (não Secret Recovery Phrase)
- ✅ Da conta específica com fundos em Sepolia
- ✅ No formato correto (sem `0x` no `.env`)

---

**Última Atualização**: 07 de Novembro de 2025  
**Mantido por**: Equipe EON - Symbeon Tech

