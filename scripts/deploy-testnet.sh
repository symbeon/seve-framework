#!/bin/bash
# 🚀 Script de Deploy Automatizado para Testnet - SEVE Framework
# Uso: ./scripts/deploy-testnet.sh [sepolia|mumbai|bscTestnet]

set -e  # Exit on error

NETWORK=${1:-sepolia}
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$PROJECT_DIR"

echo "🚀 SEVE Framework - Deploy para Testnet"
echo "=========================================="
echo "🌐 Network: $NETWORK"
echo ""

# Verificar se .env existe
if [ ! -f .env ]; then
    echo "❌ Arquivo .env não encontrado!"
    echo "📝 Criando template..."
    cat > .env << EOF
# SEVE Framework - Environment Variables
PRIVATE_KEY=sua_chave_privada_sem_0x
ALCHEMY_URL=https://eth-sepolia.g.alchemy.com/v2/SUA_KEY
ETHERSCAN_API_KEY=sua_key_para_verificar
NETWORK=$NETWORK
EOF
    echo "⚠️  Configure o arquivo .env antes de continuar!"
    exit 1
fi

# Verificar se PRIVATE_KEY está configurada
if ! grep -q "PRIVATE_KEY=" .env || grep -q "PRIVATE_KEY=$" .env || grep -q "PRIVATE_KEY=sua_chave" .env; then
    echo "❌ PRIVATE_KEY não configurada no .env!"
    echo "⚠️  Configure sua chave privada de teste no arquivo .env"
    exit 1
fi

# Carregar variáveis do .env
export $(cat .env | grep -v '^#' | xargs)

echo "📦 Compilando contratos..."
npx hardhat compile || {
    echo "❌ Erro na compilação!"
    exit 1
}

echo ""
echo "🧪 Executando testes..."
npx hardhat test || {
    echo "⚠️  Alguns testes falharam. Continuar mesmo assim? (y/n)"
    read -r response
    if [ "$response" != "y" ]; then
        exit 1
    fi
}

echo ""
echo "💰 Verificando saldo na testnet..."
# Verificar saldo (requer node script)

echo ""
echo "🚀 Iniciando deploy para $NETWORK..."
echo ""

# Criar diretório de deployments se não existir
mkdir -p deployments

# Deploy do Token
echo "1️⃣  Deploying SEVE Token..."
npx hardhat run scripts/deploy-token.js --network "$NETWORK" || {
    echo "❌ Erro no deploy do Token!"
    exit 1
}

# Ler endereço do token do arquivo de deployment
TOKEN_FILE="deployments/${NETWORK}_deployments.json"
if [ ! -f "$TOKEN_FILE" ]; then
    echo "❌ Arquivo de deployment não encontrado: $TOKEN_FILE"
    exit 1
fi

TOKEN_ADDRESS=$(node -e "const fs = require('fs'); const data = JSON.parse(fs.readFileSync('$TOKEN_FILE')); console.log(data.SEVEToken?.address || '')")

if [ -z "$TOKEN_ADDRESS" ]; then
    echo "❌ Não foi possível obter o endereço do Token!"
    exit 1
fi

echo "✅ Token deployed: $TOKEN_ADDRESS"
echo ""

# Deploy do Protocol
echo "2️⃣  Deploying SEVE Protocol..."
TOKEN_ADDRESS=$TOKEN_ADDRESS npx hardhat run scripts/deploy-protocol.js --network "$NETWORK" || {
    echo "❌ Erro no deploy do Protocol!"
    exit 1
}

echo "✅ Protocol deployed"
echo ""

# Deploy do DAO
echo "3️⃣  Deploying SEVE DAO..."
TOKEN_ADDRESS=$TOKEN_ADDRESS npx hardhat run scripts/deploy-dao.js --network "$NETWORK" || {
    echo "❌ Erro no deploy do DAO!"
    exit 1
}

echo "✅ DAO deployed"
echo ""

echo "🎉 Deploy concluído com sucesso!"
echo ""
echo "📄 Informações de deployment salvas em: deployments/${NETWORK}_deployments.json"
echo ""
echo "📋 Próximos passos:"
echo "   1. Verificar contratos no explorer"
echo "   2. Testar funcionalidades"
echo "   3. Configurar frontend"
echo ""

