#!/bin/bash

# Script para deploy completo na Polygon Mainnet
# Uso: ./scripts/deploy-polygon.sh

set -e

echo "🚀 Iniciando Deploy na Polygon Mainnet..."
echo ""

# Verificar se .env existe
if [ ! -f .env ]; then
    echo "❌ Arquivo .env não encontrado!"
    echo "   Crie um arquivo .env com PRIVATE_KEY e POLYGON_RPC_URL"
    exit 1
fi

# Compilar contratos
echo "📦 Compilando contratos..."
npx hardhat compile

# Deploy Token
echo ""
echo "1️⃣  Deployando SEVE Token..."
npx hardhat run scripts/deploy-token.js --network polygon

# Aguardar confirmação
echo ""
echo "⏳ Aguardando confirmação..."
sleep 5

# Deploy Protocol
echo ""
echo "2️⃣  Deployando SEVE Protocol..."
npx hardhat run scripts/deploy-protocol.js --network polygon

# Aguardar confirmação
echo ""
echo "⏳ Aguardando confirmação..."
sleep 5

# Deploy DAO
echo ""
echo "3️⃣  Deployando SEVE DAO..."
npx hardhat run scripts/deploy-dao.js --network polygon

echo ""
echo "✅ Deploy completo concluído!"
echo ""
echo "📋 Próximos passos:"
echo "   1. Verificar contratos no PolygonScan"
echo "   2. Ativar monetização: npm run monetization:activate:polygon"
echo "   3. Testar funcionalidades"

