# Script PowerShell para deploy completo na Polygon Mainnet
# Uso: .\scripts\deploy-polygon.ps1

Write-Host "🚀 Iniciando Deploy na Polygon Mainnet..." -ForegroundColor Green
Write-Host ""

# Verificar se .env existe
if (-not (Test-Path .env)) {
    Write-Host "❌ Arquivo .env não encontrado!" -ForegroundColor Red
    Write-Host "   Crie um arquivo .env com PRIVATE_KEY e POLYGON_RPC_URL" -ForegroundColor Yellow
    exit 1
}

# Compilar contratos
Write-Host "📦 Compilando contratos..." -ForegroundColor Cyan
npx hardhat compile

# Deploy Token
Write-Host ""
Write-Host "1️⃣  Deployando SEVE Token..." -ForegroundColor Cyan
npx hardhat run scripts/deploy-token.js --network polygon

# Aguardar confirmação
Write-Host ""
Write-Host "⏳ Aguardando confirmação..." -ForegroundColor Yellow
Start-Sleep -Seconds 5

# Deploy Protocol
Write-Host ""
Write-Host "2️⃣  Deployando SEVE Protocol..." -ForegroundColor Cyan
npx hardhat run scripts/deploy-protocol.js --network polygon

# Aguardar confirmação
Write-Host ""
Write-Host "⏳ Aguardando confirmação..." -ForegroundColor Yellow
Start-Sleep -Seconds 5

# Deploy DAO
Write-Host ""
Write-Host "3️⃣  Deployando SEVE DAO..." -ForegroundColor Cyan
npx hardhat run scripts/deploy-dao.js --network polygon

Write-Host ""
Write-Host "✅ Deploy completo concluído!" -ForegroundColor Green
Write-Host ""
Write-Host "📋 Próximos passos:" -ForegroundColor Cyan
Write-Host "   1. Verificar contratos no PolygonScan"
Write-Host "   2. Ativar monetização: npm run monetization:activate:polygon"
Write-Host "   3. Testar funcionalidades"

