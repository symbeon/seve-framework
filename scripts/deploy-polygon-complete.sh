#!/bin/bash

# Script completo de deploy em Polygon Mainnet
# Executa deploy dos 3 contratos e ativa monetização

echo "🚀 Deploy Completo em Polygon Mainnet - SEVE Framework"
echo "=================================================="
echo ""

# Verificar se está na rede correta
echo "⚠️  ATENÇÃO: Este script fará deploy em POLYGON MAINNET (produção real)"
echo "   Custo estimado: ~0.26 MATIC (~\$0.25)"
echo ""
read -p "Deseja continuar? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "❌ Deploy cancelado."
    exit 1
fi

# Compilar contratos
echo ""
echo "📦 Compilando contratos..."
npm run compile

if [ $? -ne 0 ]; then
    echo "❌ Erro na compilação. Abortando."
    exit 1
fi

# Deploy Token
echo ""
echo "1️⃣  Deploying SEVE Token..."
npx hardhat run scripts/deploy-token.js --network polygon

if [ $? -ne 0 ]; then
    echo "❌ Erro no deploy do Token. Abortando."
    exit 1
fi

# Deploy Protocol
echo ""
echo "2️⃣  Deploying SEVE Protocol..."
npx hardhat run scripts/deploy-protocol.js --network polygon

if [ $? -ne 0 ]; then
    echo "❌ Erro no deploy do Protocol. Abortando."
    exit 1
fi

# Deploy DAO
echo ""
echo "3️⃣  Deploying SEVE DAO..."
npx hardhat run scripts/deploy-dao.js --network polygon

if [ $? -ne 0 ]; then
    echo "❌ Erro no deploy do DAO. Abortando."
    exit 1
fi

# Ativar monetização
echo ""
echo "4️⃣  Ativando Monetização..."
npx hardhat run scripts/add-version-v1.js --network polygon
npx hardhat run scripts/create-dao-proposal.js --network polygon
npx hardhat run scripts/register-first-agent.js --network polygon

echo ""
echo "✅ Deploy completo concluído!"
echo ""
echo "📚 Próximos passos:"
echo "   1. Verificar contratos no PolygonScan"
echo "   2. Testar funcionalidades"
echo "   3. Documentar deployments"
echo ""

