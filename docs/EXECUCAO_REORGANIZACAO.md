# 🔄 Execução da Reorganização de Arquivos

**Data**: 13 de Novembro de 2025  
**Status**: ⏳ **EM EXECUÇÃO**

---

## 🎯 **O QUE VAI SER FEITO**

### **MOVER PARA SYMBEON-ECOSYSTEM**:
1. ✅ `showcase/` → `SYMBEON-ECOSYSTEM/frontend/symbeon-showcase/`
2. ✅ `contracts/*.sol` → `SYMBEON-ECOSYSTEM/smart-contracts/contracts/`
3. ✅ `hardhat.config.js` → `SYMBEON-ECOSYSTEM/smart-contracts/`
4. ✅ Docs do ecosystem → `SYMBEON-ECOSYSTEM/docs/ecosystem/`

### **MANTER NO SEVE-FRAMEWORK**:
- `src/seve/` (código Python do framework)
- `src/seve_framework/` (código Python do framework)
- `docs/` (documentação técnica do framework)
- `tests/` (testes do framework)
- `examples/` (exemplos de uso)

---

## 📋 **COMANDOS A EXECUTAR**

```bash
# 1. Ir para SYMBEON-ECOSYSTEM
cd C:\Users\João\Desktop\PROJETOS\00_ECOSYSTEM_COMERCIAL\SYMBEON-ECOSYSTEM

# 2. Criar estrutura frontend
mkdir -p frontend

# 3. Copiar showcase
cp -r ../SEVE-FRAMEWORK/SEVE-FRAMEWORK/showcase frontend/symbeon-showcase

# 4. Copiar contratos existentes
cp ../SEVE-FRAMEWORK/SEVE-FRAMEWORK/contracts/*.sol smart-contracts/contracts/
cp ../SEVE-FRAMEWORK/SEVE-FRAMEWORK/hardhat.config.js smart-contracts/
cp ../SEVE-FRAMEWORK/SEVE-FRAMEWORK/package.json smart-contracts/

# 5. Commit
git add frontend/ smart-contracts/
git commit -m "feat: add frontend (showcase) and existing smart contracts

- Move showcase from SEVE-FRAMEWORK to frontend/symbeon-showcase
- Move existing contracts (SEVEToken, SEVEProtocol, SEVEDAO)
- Merge with new contracts (SEVEDonation, SEVECertification)
- Complete ecosystem structure"

# 6. Push
git push origin main
```

---

## 🔗 **CRIAR CONEXÃO**

### **No SYMBEON-ECOSYSTEM**
Adicionar no `README.md`:
```markdown
## 🔗 Framework Core
This ecosystem uses the [SEVE Framework](https://github.com/symbeon/seve-framework) as its core technology.
```

### **No SEVE-FRAMEWORK**
Atualizar `README.md`:
```markdown
## 🌐 Ecosystem
This framework is part of the [Symbeon Ecosystem](https://github.com/symbeon/symbeon-ecosystem).

For the complete product (frontend, backend, smart contracts), see the ecosystem repository.
```

---

**Status**: Aguardando execução manual ou confirmação para prosseguir

