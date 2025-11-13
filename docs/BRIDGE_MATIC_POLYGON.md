# 🌉 Como Fazer Bridge de MATIC para Polygon

**Status**: MATIC está na wallet, mas pode estar na rede errada

---

## 🔍 **VERIFICAÇÃO**

### **1. Verificar Rede Atual**
Na sua wallet (MetaMask/Symb):
- Verificar se está conectado à **Polygon Mainnet**
- Se estiver em **Ethereum Mainnet**, o MATIC precisa ser "bridged"

### **2. Endereço da Wallet**
- **Endereço verificado**: `0x863de15091DfE5C044Dc1bD54f85210B6Bb6DA76`
- Confirmar que este é o endereço que tem o MATIC

---

## 🌉 **OPÇÕES DE BRIDGE**

### **Opção 1: Bridge Oficial Polygon**
1. Acessar: https://portal.polygon.technology/
2. Conectar wallet
3. Selecionar: **Ethereum** → **Polygon**
4. Token: **MATIC**
5. Quantidade: 23.69276 MATIC (ou o necessário)
6. Confirmar transação

**Tempo**: ~10-30 minutos  
**Custo**: Taxa de gas na Ethereum

---

### **Opção 2: Bridge via Wallet (Symb)**
1. Na sua wallet, procurar opção de "Bridge"
2. Selecionar rede origem: **Ethereum**
3. Selecionar rede destino: **Polygon**
4. Token: **MATIC**
5. Confirmar transação

---

### **Opção 3: Comprar MATIC Direto na Polygon**
1. Usar exchange (Binance, Coinbase, etc.)
2. Comprar MATIC
3. Retirar diretamente para **Polygon Mainnet**
4. Endereço: `0x863de15091DfE5C044Dc1bD54f85210B6Bb6DA76`

---

## ✅ **APÓS BRIDGE**

### **1. Verificar Saldo na Polygon**
```bash
npm run verify:ready:polygon
```

### **2. Executar Deploy**
```bash
npm run deploy:polygon
```

---

## 🔧 **ALTERNATIVA: Verificar Endereço**

Se o MATIC já está na Polygon mas em outro endereço:

1. **Obter PRIVATE_KEY** da wallet que tem o MATIC na Polygon
2. **Atualizar .env** com a PRIVATE_KEY correta
3. **Verificar novamente**:
```bash
npm run verify:ready:polygon
```

---

**Última Atualização**: 09 de Novembro de 2025

