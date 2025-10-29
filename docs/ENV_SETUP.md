# 🔐 Setup de Ambiente (.env) - SEVE Framework

Guia completo para configuração segura de variáveis de ambiente para desenvolvimento, testnet e produção.

---

## 📋 **Índice**

1. [Conceitos Fundamentais](#1-conceitos-fundamentais)
2. [Template Completo](#2-template-completo)
3. [Configuração por Ambiente](#3-configuração-por-ambiente)
4. [Exemplos Práticos](#4-exemplos-práticos)
5. [Segurança e Boas Práticas](#5-segurança-e-boas-práticas)
6. [Validação](#6-validação)
7. [Troubleshooting](#7-troubleshooting)
8. [Referências](#8-referências)

---

## 1. **Conceitos Fundamentais**

### **O que é `.env`?**
Arquivo de ambiente que armazena **segredos e configurações** localmente, fora do controle de versão.

### **Por que usar `.env`?**
- ✅ **Segurança**: Segredos não vão para o Git
- ✅ **Flexibilidade**: Diferentes configurações por ambiente
- ✅ **Isolamento**: Cada desenvolvedor tem suas próprias chaves
- ✅ **Privacidade**: Protege credenciais sensíveis

### **Alternativas para Produção**
Em produção, considere usar:
- **HashiCorp Vault**
- **AWS Secrets Manager**
- **Azure Key Vault**
- **Google Secret Manager**
- **Kubernetes Secrets**

---

## 2. **Template Completo**

### **`.env` Completo (Todas as Opções)**

```bash
# ============================================================================
# SEVE Framework - Environment Variables
# ============================================================================
# ATENÇÃO: Este arquivo contém informações sensíveis!
# NUNCA commite este arquivo no Git
# Use .env.example como template público
# ============================================================================

# ----------------------------------------------------------------------------
# WALLET & KEYS
# ----------------------------------------------------------------------------
# Chave privada da carteira (SEM prefixo 0x)
# PARA TESTNET: Use carteira de teste com fundos de faucet
# PARA PRODUÇÃO: Use carteira dedicada com fundos suficientes
PRIVATE_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# ----------------------------------------------------------------------------
# RPC PROVIDERS (Escolha 1 ou use RPC público)
# ----------------------------------------------------------------------------

# Alchemy (Recomendado - Free Tier generoso)
# Crie conta em: https://www.alchemy.com/
# Free: 300M compute units/mês
ALCHEMY_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Infura (Alternativa)
# Crie conta em: https://www.infura.io/
# Free: 100k requisições/dia
INFURA_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# QuickNode (Alternativa)
# Crie conta em: https://www.quicknode.com/
# Free: 10M requisições/mês
QUICKNODE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# ----------------------------------------------------------------------------
# BLOCKCHAIN EXPLORERS (Para verificação de contratos)
# ----------------------------------------------------------------------------

# Etherscan (Ethereum & Sepolia)
# Obtenha em: https://etherscan.io/myapikey
ETHERSCAN_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# PolygonScan (Polygon & Mumbai)
# Obtenha em: https://polygonscan.com/myapikey
POLYGONSCAN_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# BSCScan (BSC & BSC Testnet)
# Obtenha em: https://bscscan.com/myapikey
BSCSCAN_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Arbitrum Explorer
ARBISCAN_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# ----------------------------------------------------------------------------
# GAS SETTINGS (Opcional - Hardhat usa valores padrão se não especificado)
# ----------------------------------------------------------------------------
GAS_PRICE=20000000000      # 20 gwei
GAS_LIMIT=8000000          # 8M gas

# ----------------------------------------------------------------------------
# NETWORK SETTINGS
# ----------------------------------------------------------------------------
NETWORK=sepolia            # sepolia, mumbai, polygon, arbitrum, bscTestnet
CHAIN_ID=11155111         # Chain ID da rede (automático no Hardhat)

# ----------------------------------------------------------------------------
# VERIFICATION SETTINGS
# ----------------------------------------------------------------------------
AUTO_VERIFY=true           # Verificar contratos automaticamente após deploy
VERIFY_CONCURRENCY=5       # Número de verificações paralelas

# ----------------------------------------------------------------------------
# DEVELOPMENT SETTINGS
# ----------------------------------------------------------------------------
DEBUG=false                # Ativar logs de debug
LOG_LEVEL=info            # debug, info, warn, error
```

### **`.env` Mínimo (Testnet com RPC Público)**

```bash
# Configuração mínima para testnet usando RPC público
PRIVATE_KEY=sua_chave_privada_aqui_sem_0x

# Opcional: Para verificar contratos
ETHERSCAN_API_KEY=sua_key_aqui
```

---

## 3. **Configuração por Ambiente**

### **🧪 Desenvolvimento Local**

```bash
# .env.local ou .env.development
PRIVATE_KEY=ac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80
NETWORK=localhost
DEBUG=true
LOG_LEVEL=debug
```

**Nota**: A chave acima é uma chave padrão do Hardhat para desenvolvimento local. **NUNCA** use em produção!

### **🧪 Testnet**

```bash
# .env.testnet
PRIVATE_KEY=sua_chave_privada_de_teste
ALCHEMY_API_KEY=sua_alchemy_key  # Ou use RPC público
NETWORK=sepolia
ETHERSCAN_API_KEY=sua_etherscan_key  # Para verificar contratos
```

**Passos**:
1. Crie uma carteira nova para testes (MetaMask, etc.)
2. Obtenha fundos via faucet: [sepoliafaucet.com](https://sepoliafaucet.com/)
3. Exporte a chave privada (sem 0x)
4. Configure no `.env`

### **🏭 Produção**

```bash
# .env.production (NUNCA commitar!)
PRIVATE_KEY=chave_de_producao_com_fundos_suficientes
ALCHEMY_API_KEY=key_de_producao
NETWORK=polygon  # Polygon é mais barato que Ethereum
POLYGONSCAN_API_KEY=key_para_verificacao
DEBUG=false
LOG_LEVEL=error
AUTO_VERIFY=true
```

**Atenção Crítica**:
- ⚠️ Use carteira dedicada apenas para produção
- ⚠️ Verifique saldo antes de deploy
- ⚠️ Mantenha backup seguro da chave
- ⚠️ Use multi-sig para contratos importantes

---

## 4. **Exemplos Práticos**

### **Exemplo 1: Hardhat Config usando .env**

```javascript
// hardhat.config.js
require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();

module.exports = {
  solidity: {
    version: "0.8.19",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
  networks: {
    sepolia: {
      url: process.env.ALCHEMY_API_KEY
        ? `https://eth-sepolia.g.alchemy.com/v2/${process.env.ALCHEMY_API_KEY}`
        : "https://rpc.sepolia.org",  // Fallback para RPC público
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
      chainId: 11155111,
    },
    polygon: {
      url: `https://polygon-rpc.com`,
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
      chainId: 137,
    },
  },
  etherscan: {
    apiKey: {
      sepolia: process.env.ETHERSCAN_API_KEY,
      polygon: process.env.POLYGONSCAN_API_KEY,
    }
  }
};
```

### **Exemplo 2: Validação de .env**

```javascript
// scripts/validate-env.js
require('dotenv').config();

function validateEnv() {
  const required = ['PRIVATE_KEY'];
  const missing = required.filter(key => !process.env[key]);
  
  if (missing.length > 0) {
    throw new Error(`Missing required env variables: ${missing.join(', ')}`);
  }
  
  // Validar formato da chave privada
  if (process.env.PRIVATE_KEY && !/^[0-9a-f]{64}$/i.test(process.env.PRIVATE_KEY)) {
    throw new Error('PRIVATE_KEY must be 64 hex characters (without 0x)');
  }
  
  console.log('✅ Environment variables validated');
}

validateEnv();
```

---

## 5. **Segurança e Boas Práticas**

### **🔒 Regras de Ouro**

1. **NUNCA commitar `.env`**
   ```bash
   # Garanta que está no .gitignore
   echo ".env" >> .gitignore
   echo ".env.*" >> .gitignore  # Exceto .env.example
   ```

2. **Use `.env.example` como template público**
   ```bash
   # Crie .env.example com valores vazios/exemplo
   cp .env .env.example
   # Remova valores sensíveis
   sed -i 's/=.*/=EXAMPLE_VALUE/g' .env.example
   ```

3. **Carteiras dedicadas por ambiente**
   - 🧪 **Dev**: Carteira local Hardhat (chave padrão OK)
   - 🧪 **Testnet**: Carteira nova apenas para testes
   - 🏭 **Produção**: Carteira dedicada com fundos suficientes

4. **Rotação de chaves**
   - Rotacione API keys regularmente
   - Revogue chaves antigas após atualização
   - Monitore uso de API keys

5. **Backup seguro**
   - Armazene chaves privadas em cofre seguro (ex: password manager)
   - Use multi-sig para produção
   - Documente procedimentos de recuperação

### **⚠️ Sinais de Alerta**

- 🔴 Chave privada commitada no Git
- 🔴 Mesma carteira para dev e produção
- 🔴 Chave compartilhada por email/Slack
- 🔴 Sem backup da chave privada
- 🔴 Carteira de produção sem multi-sig

---

## 6. **Validação**

### **Checklist de Validação**

```bash
# 1. Verificar se .env existe
[ -f .env ] && echo "✅ .env exists" || echo "❌ .env missing"

# 2. Verificar se está no .gitignore
grep -q "^\.env$" .gitignore && echo "✅ .env in .gitignore" || echo "❌ .env NOT in .gitignore"

# 3. Validar formato da chave privada
if [ -f .env ]; then
  PRIVATE_KEY=$(grep "^PRIVATE_KEY=" .env | cut -d'=' -f2)
  if [ ${#PRIVATE_KEY} -eq 64 ]; then
    echo "✅ PRIVATE_KEY format valid"
  else
    echo "❌ PRIVATE_KEY format invalid (should be 64 hex chars)"
  fi
fi
```

### **Script de Validação Automática**

```javascript
// scripts/validate-env.js
require('dotenv').config();

const checks = [
  {
    name: 'PRIVATE_KEY exists',
    check: () => !!process.env.PRIVATE_KEY,
    critical: true
  },
  {
    name: 'PRIVATE_KEY format',
    check: () => /^[0-9a-f]{64}$/i.test(process.env.PRIVATE_KEY || ''),
    critical: true
  },
  {
    name: 'At least one RPC provider',
    check: () => !!(process.env.ALCHEMY_API_KEY || process.env.INFURA_API_KEY),
    critical: false
  }
];

let passed = 0;
let failed = 0;

checks.forEach(({ name, check, critical }) => {
  if (check()) {
    console.log(`✅ ${name}`);
    passed++;
  } else {
    console.log(`${critical ? '❌' : '⚠️'} ${name}`);
    failed++;
    if (critical) process.exit(1);
  }
});

console.log(`\n📊 Results: ${passed} passed, ${failed} failed`);
```

---

## 7. **Troubleshooting**

### **Erro: "Invalid account"**

**Causa**: Chave privada com formato incorreto ou ausente

**Solução**:
```bash
# Verificar formato (deve ter 64 caracteres hex, sem 0x)
echo ${#PRIVATE_KEY}  # Deve retornar 64

# Se tiver 0x, remova
PRIVATE_KEY=$(echo $PRIVATE_KEY | sed 's/^0x//')
```

### **Erro: "Insufficient funds"**

**Causa**: Carteira sem fundos suficientes para gas

**Solução**:
1. Verifique saldo da carteira
2. Para testnet: use faucet
3. Para produção: adicione fundos

### **Erro: "Cannot read properties of undefined"**

**Causa**: Variável de ambiente não carregada

**Solução**:
```bash
# Certifique-se de que dotenv está instalado
npm install dotenv

# Verifique se está no hardhat.config.js
require("dotenv").config();
```

### **Problema: .env não está sendo lido**

**Solução**:
```bash
# 1. Verifique se o arquivo existe
ls -la .env

# 2. Verifique permissões
chmod 600 .env  # Apenas leitura/escrita pelo dono

# 3. Teste carregamento
node -e "require('dotenv').config(); console.log(process.env.PRIVATE_KEY)"
```

---

## 8. **Referências**

- **[Guia de Deploy](./DEPLOYMENT_GUIDE.md)** - Como fazer deploy
- **[Testnet Playbook](./TESTNET_PLAYBOOK.md)** - Workflows de testnet
- **[Provedores RPC](./RPC_PROVIDERS.md)** - Escolha do provedor
- **[Checklist de Segurança](./SECURITY_CHECKLIST.md)** - Validações de segurança

---

**Última Atualização**: 2025-01-29  
**Mantido por**: Equipe EON - Symbeon Tech
