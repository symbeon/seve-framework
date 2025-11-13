# 🔍 Como Verificar Saldo de MATIC na Polygon

**Endereço da Wallet**: `0x863de15091DfE5C044Dc1bD54f85210B6Bb6DA76`

---

## 🌐 **Verificar no PolygonScan**

Acesse diretamente:
**https://polygonscan.com/address/0x863de15091DfE5C044Dc1bD54f85210B6Bb6DA76**

Você verá:
- Saldo atual de MATIC
- Histórico de transações
- Status do swap (se ainda estiver processando)

---

## ✅ **Verificações**

### **1. Swap Completou?**
- Verificar no PolygonScan se a transação do swap foi confirmada
- Verificar se o MATIC chegou na wallet

### **2. Endereço Correto?**
- Confirmar que o MATIC foi enviado para: `0x863de15091DfE5C044Dc1bD54f85210B6Bb6DA76`
- Se foi enviado para outro endereço, atualizar PRIVATE_KEY no .env

### **3. Saldo Suficiente?**
- **Mínimo necessário**: 0.1 MATIC
- **Recomendado**: 0.2 MATIC

---

## 🚀 **Quando MATIC Estiver Disponível**

Execute:
```bash
npm run verify:ready:polygon
```

Se mostrar saldo suficiente, execute o deploy:
```bash
npm run deploy:polygon
```

---

**Última Atualização**: 09 de Novembro de 2025

