# 📁 Plano de Reorganização de Arquivos - Symbeon

**Data**: 13 de Novembro de 2025  
**Objetivo**: Organizar arquivos corretamente entre SEVE-FRAMEWORK e SYMBEON-ECOSYSTEM

---

## 🎯 **ESTRUTURA IDEAL**

### **SEVE-FRAMEWORK** (Framework Core)
```
SEVE-FRAMEWORK/
├── src/                        # Código Python do framework
│   ├── seve/                   # Módulos core
│   └── seve_framework/         # Framework completo
├── tests/                      # Testes do framework
├── docs/                       # Documentação técnica do framework
│   ├── technical/
│   ├── api/
│   └── adr/
├── examples/                   # Exemplos de uso
├── pyproject.toml
├── requirements.txt
├── README.md
└── LICENSE
```

**O que fica**: Apenas o core do SEVE Framework (Python)

---

### **SYMBEON-ECOSYSTEM** (Ecossistema Completo)
```
SYMBEON-ECOSYSTEM/
├── backend/
│   ├── rust-core/              # ✅ Já criado
│   └── python-services/        # ✅ Já criado
├── smart-contracts/            # ✅ Já criado
│   ├── contracts/
│   │   ├── SEVEToken.sol           # ← MOVER do SEVE-FRAMEWORK
│   │   ├── SEVEProtocol.sol        # ← MOVER do SEVE-FRAMEWORK
│   │   ├── SEVEDAO.sol             # ← MOVER do SEVE-FRAMEWORK
│   │   ├── SEVEDonation.sol        # ✅ Já criado
│   │   └── SEVECertification.sol   # ✅ Já criado
│   └── ...
├── frontend/
│   └── symbeon-showcase/       # ← MOVER de SEVE-FRAMEWORK/showcase
├── docs/
│   ├── ecosystem/              # Docs do ecosystem
│   └── framework/              # Link para SEVE-FRAMEWORK/docs
├── database/                   # ✅ Já criado
├── infrastructure/             # ✅ Já criado
└── README.md
```

**O que vem para cá**: Showcase, contratos existentes, documentação do ecosystem

---

## 📦 **O QUE MOVER**

### **De SEVE-FRAMEWORK → SYMBEON-ECOSYSTEM**

#### **1. Showcase (Frontend)** ✅ **MOVER**
```
SEVE-FRAMEWORK/showcase/ 
→ SYMBEON-ECOSYSTEM/frontend/symbeon-showcase/
```

**Arquivos**:
- Todo o diretório `showcase/`
- package.json, vite.config.ts, etc.
- src/ completo
- Mantém histórico git

#### **2. Smart Contracts Existentes** ✅ **MOVER**
```
SEVE-FRAMEWORK/contracts/
→ SYMBEON-ECOSYSTEM/smart-contracts/contracts/
```

**Arquivos**:
- SEVEToken.sol
- SEVEProtocol.sol
- SEVEDAO.sol

**Merge com**:
- SEVEDonation.sol (já criado)
- SEVECertification.sol (já criado)

#### **3. Hardhat Config** ✅ **MOVER**
```
SEVE-FRAMEWORK/hardhat.config.js
→ SYMBEON-ECOSYSTEM/smart-contracts/
```

#### **4. Documentação do Ecosystem** ✅ **MOVER**
```
SEVE-FRAMEWORK/docs/
├── ARQUITETURA_ECOSSISTEMA_SEVE.md           → SYMBEON-ECOSYSTEM/docs/
├── PLANO_IMPLEMENTACAO_SYMBEON_ECOSYSTEM.md  → SYMBEON-ECOSYSTEM/docs/
├── ESTRATEGIA_CERTIFICACAO_ETICA.md          → SYMBEON-ECOSYSTEM/docs/
├── POSICIONAMENTO_CERTIFICACAO_ETICA.md      → SYMBEON-ECOSYSTEM/docs/
└── ... (docs relacionados ao ecosystem)
```

---

### **O QUE FICA NO SEVE-FRAMEWORK**

#### **1. Core do Framework** ✅ **MANTER**
```
SEVE-FRAMEWORK/
├── src/
│   ├── seve/                   # Módulos Python
│   └── seve_framework/         # Framework completo
├── tests/                      # Testes
├── examples/                   # Exemplos de uso
├── pyproject.toml
├── requirements.txt
```

#### **2. Documentação Técnica** ✅ **MANTER**
```
SEVE-FRAMEWORK/docs/
├── technical/                  # Arquitetura técnica do framework
├── api/                        # API reference do framework
├── adr/                        # Decisões arquiteturais
├── ARCHITECTURE.md             # Arquitetura do framework
├── OVERVIEW.md
├── TECHNICAL_DOCUMENTATION.md
└── SYSTEMATIC_KNOWLEDGE_BASE.md
```

#### **3. Documentação Universal** ✅ **MANTER**
```
SEVE-UNIVERSAL/
├── src/
├── docs/
└── README.md
```

---

## 🔗 **CONEXÕES ENTRE REPOSITÓRIOS**

### **Opção 1: Git Submodules** (Recomendado)

No `SYMBEON-ECOSYSTEM`:
```bash
# Adicionar SEVE-FRAMEWORK como submodule
git submodule add https://github.com/symbeon/seve-framework.git framework

# Estrutura resultante
SYMBEON-ECOSYSTEM/
├── backend/
├── frontend/
├── framework/                  # ← Submodule do SEVE-FRAMEWORK
└── ...
```

**Vantagens**:
- ✅ Mantém separação clara
- ✅ Versionamento independente
- ✅ Fácil atualização

---

### **Opção 2: Monorepo** (Alternativa)

Criar um único repositório grande:
```
SYMBEON-MONOREPO/
├── packages/
│   ├── seve-framework/         # Framework Python
│   ├── backend-rust/           # Backend Rust
│   ├── backend-python/         # Backend Python
│   ├── smart-contracts/        # Contratos
│   └── symbeon-showcase/       # Frontend
└── ...
```

**Vantagens**:
- ✅ Tudo em um lugar
- ✅ CI/CD simplificado
- ⚠️ Repositório grande

---

### **Opção 3: Repositórios Separados + Referências** (Atual)

Manter separado mas com referências:
```
symbeon/seve-framework          # Framework core (Python)
symbeon/symbeon-ecosystem       # Ecosystem completo (Rust + Python + Frontend)
```

**No ecosystem, referenciar framework**:
- README.md: Link para framework
- requirements.txt: `seve-framework @ git+https://github.com/symbeon/seve-framework.git`

**Vantagens**:
- ✅ Simples e claro
- ✅ Fácil manutenção
- ✅ Versionamento independente

---

## 🎯 **RECOMENDAÇÃO**

**Opção 1: Git Submodules** para manter separação mas com integração fácil.

---

## 📋 **PLANO DE EXECUÇÃO**

### **Passo 1: Copiar Showcase** ✅
```bash
# No SYMBEON-ECOSYSTEM
mkdir -p frontend
cp -r ../SEVE-FRAMEWORK/SEVE-FRAMEWORK/showcase frontend/symbeon-showcase

# Commit
git add frontend/symbeon-showcase
git commit -m "feat: add symbeon showcase frontend"
git push
```

### **Passo 2: Copiar Smart Contracts** ✅
```bash
# No SYMBEON-ECOSYSTEM
cp ../SEVE-FRAMEWORK/SEVE-FRAMEWORK/contracts/*.sol smart-contracts/contracts/
cp ../SEVE-FRAMEWORK/SEVE-FRAMEWORK/hardhat.config.js smart-contracts/

# Commit
git add smart-contracts/contracts/
git commit -m "feat: add existing SEVE smart contracts (Token, Protocol, DAO)"
git push
```

### **Passo 3: Adicionar Submodule (Opcional)** ✅
```bash
# No SYMBEON-ECOSYSTEM
git submodule add https://github.com/symbeon/seve-framework.git framework

# Commit
git add .gitmodules framework
git commit -m "feat: add SEVE Framework as submodule"
git push
```

### **Passo 4: Atualizar READMEs** ✅
```bash
# SYMBEON-ECOSYSTEM/README.md
# Adicionar seção:
## 🔗 Related Repositories
- [SEVE Framework](https://github.com/symbeon/seve-framework) - Core Python framework

# SEVE-FRAMEWORK/README.md
# Adicionar seção:
## 🌐 Ecosystem
This framework is part of the [Symbeon Ecosystem](https://github.com/symbeon/symbeon-ecosystem)
```

### **Passo 5: Atualizar Showcase** ✅
```bash
# SYMBEON-ECOSYSTEM/frontend/symbeon-showcase/package.json
# Adicionar dependency (se necessário):
"dependencies": {
  "seve-framework": "git+https://github.com/symbeon/seve-framework.git"
}
```

---

## 🎯 **RESULTADO FINAL**

### **SEVE-FRAMEWORK**
- Apenas framework Python
- Documentação técnica do framework
- Exemplos de uso
- Testes
- **Foco**: Core tecnológico

### **SYMBEON-ECOSYSTEM**
- Frontend (showcase)
- Backend (Rust + Python)
- Smart contracts (todos)
- Database
- Infrastructure
- Documentação do ecosystem
- **Foco**: Produto completo e monetização

---

**Quer que eu execute esse plano de reorganização agora?**

Posso:
1. Copiar showcase para SYMBEON-ECOSYSTEM/frontend/
2. Copiar smart contracts existentes
3. Adicionar SEVE-FRAMEWORK como submodule
4. Atualizar READMEs
5. Fazer commits e push

