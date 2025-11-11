# Script completo de deploy em Polygon Mainnet (PowerShell)
# Executa deploy dos 3 contratos e ativa monetização

Write-Host "🚀 Deploy Completo em Polygon Mainnet - SEVE Framework" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se está na rede correta
Write-Host "⚠️  ATENÇÃO: Este script fará deploy em POLYGON MAINNET (produção real)" -ForegroundColor Yellow
Write-Host "   Custo estimado: ~0.26 MATIC (~`$0.25)" -ForegroundColor Yellow
Write-Host ""
$confirm = Read-Host "Deseja continuar? (yes/no)"

if ($confirm -ne "yes") {
    Write-Host "❌ Deploy cancelado." -ForegroundColor Red
    exit 1
}

# Compilar contratos
Write-Host ""
Write-Host "📦 Compilando contratos..." -ForegroundColor Cyan
npm run compile

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Erro na compilação. Abortando." -ForegroundColor Red
    exit 1
}

# Deploy Token
Write-Host ""
Write-Host "1️⃣  Deploying SEVE Token..." -ForegroundColor Cyan
npx hardhat run scripts/deploy-token.js --network polygon

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Erro no deploy do Token. Abortando." -ForegroundColor Red
    exit 1
}

# Deploy Protocol
Write-Host ""
Write-Host "2️⃣  Deploying SEVE Protocol..." -ForegroundColor Cyan
npx hardhat run scripts/deploy-protocol.js --network polygon

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Erro no deploy do Protocol. Abortando." -ForegroundColor Red
    exit 1
}

# Deploy DAO
Write-Host ""
Write-Host "3️⃣  Deploying SEVE DAO..." -ForegroundColor Cyan
npx hardhat run scripts/deploy-dao.js --network polygon

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Erro no deploy do DAO. Abortando." -ForegroundColor Red
    exit 1
}

# Ativar monetização
Write-Host ""
Write-Host "4️⃣  Ativando Monetização..." -ForegroundColor Cyan
npx hardhat run scripts/add-version-v1.js --network polygon
npx hardhat run scripts/create-dao-proposal.js --network polygon
npx hardhat run scripts/register-first-agent.js --network polygon

Write-Host ""
Write-Host "✅ Deploy completo concluído!" -ForegroundColor Green
Write-Host ""
Write-Host "📚 Próximos passos:" -ForegroundColor Cyan
Write-Host "   1. Verificar contratos no PolygonScan"
Write-Host "   2. Testar funcionalidades"
Write-Host "   3. Documentar deployments"
Write-Host ""

