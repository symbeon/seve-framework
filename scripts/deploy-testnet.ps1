# 🚀 Script de Deploy Automatizado para Testnet - SEVE Framework (PowerShell)
# Uso: .\scripts\deploy-testnet.ps1 [sepolia|mumbai|bscTestnet]

param(
    [string]$Network = "sepolia"
)

$ErrorActionPreference = "Stop"

Write-Host "🚀 SEVE Framework - Deploy para Testnet" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host "🌐 Network: $Network" -ForegroundColor Cyan
Write-Host ""

# Verificar se estamos no diretório correto
if (-not (Test-Path "contracts")) {
    Write-Host "❌ Execute este script na raiz do projeto SEVE-FRAMEWORK" -ForegroundColor Red
    exit 1
}

# Verificar se .env existe
if (-not (Test-Path ".env")) {
    Write-Host "❌ Arquivo .env não encontrado!" -ForegroundColor Red
    Write-Host "📝 Criando template..." -ForegroundColor Yellow
    
    @"
# SEVE Framework - Environment Variables
PRIVATE_KEY=sua_chave_privada_sem_0x
ALCHEMY_URL=https://eth-sepolia.g.alchemy.com/v2/SUA_KEY
ETHERSCAN_API_KEY=sua_key_para_verificar
NETWORK=$Network
"@ | Out-File -FilePath ".env" -Encoding UTF8
    
    Write-Host "⚠️  Configure o arquivo .env antes de continuar!" -ForegroundColor Yellow
    exit 1
}

# Verificar se PRIVATE_KEY está configurada
$envContent = Get-Content ".env" -Raw
if ($envContent -notmatch "PRIVATE_KEY=.*" -or $envContent -match "PRIVATE_KEY=sua_chave" -or $envContent -match "PRIVATE_KEY=$") {
    Write-Host "❌ PRIVATE_KEY não configurada no .env!" -ForegroundColor Red
    Write-Host "⚠️  Configure sua chave privada de teste no arquivo .env" -ForegroundColor Yellow
    exit 1
}

Write-Host "📦 Compilando contratos..." -ForegroundColor Cyan
npx hardhat compile
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Erro na compilação!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "🧪 Executando testes..." -ForegroundColor Cyan
npx hardhat test
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  Alguns testes falharam. Continuar mesmo assim? (S/N)" -ForegroundColor Yellow
    $response = Read-Host
    if ($response -ne "S" -and $response -ne "s") {
        exit 1
    }
}

Write-Host ""
Write-Host "🚀 Iniciando deploy para $Network..." -ForegroundColor Green
Write-Host ""

# Criar diretório de deployments se não existir
if (-not (Test-Path "deployments")) {
    New-Item -ItemType Directory -Path "deployments" | Out-Null
}

# Deploy do Token
Write-Host "1️⃣  Deploying SEVE Token..." -ForegroundColor Yellow
npx hardhat run scripts/deploy-token.js --network $Network
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Erro no deploy do Token!" -ForegroundColor Red
    exit 1
}

# Ler endereço do token do arquivo de deployment
$TokenFile = "deployments/${Network}_deployments.json"
if (-not (Test-Path $TokenFile)) {
    Write-Host "❌ Arquivo de deployment não encontrado: $TokenFile" -ForegroundColor Red
    exit 1
}

$DeploymentData = Get-Content $TokenFile | ConvertFrom-Json
$TokenAddress = $DeploymentData.SEVEToken.address

if (-not $TokenAddress) {
    Write-Host "❌ Não foi possível obter o endereço do Token!" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Token deployed: $TokenAddress" -ForegroundColor Green
Write-Host ""

# Deploy do Protocol
Write-Host "2️⃣  Deploying SEVE Protocol..." -ForegroundColor Yellow
$env:TOKEN_ADDRESS = $TokenAddress
npx hardhat run scripts/deploy-protocol.js --network $Network
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Erro no deploy do Protocol!" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Protocol deployed" -ForegroundColor Green
Write-Host ""

# Deploy do DAO
Write-Host "3️⃣  Deploying SEVE DAO..." -ForegroundColor Yellow
$env:TOKEN_ADDRESS = $TokenAddress
npx hardhat run scripts/deploy-dao.js --network $Network
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Erro no deploy do DAO!" -ForegroundColor Red
    exit 1
}

Write-Host "✅ DAO deployed" -ForegroundColor Green
Write-Host ""

Write-Host "🎉 Deploy concluído com sucesso!" -ForegroundColor Green
Write-Host ""
Write-Host "📄 Informações de deployment salvas em: deployments/${Network}_deployments.json" -ForegroundColor Cyan
Write-Host ""
Write-Host "📋 Próximos passos:" -ForegroundColor Yellow
Write-Host "   1. Verificar contratos no explorer" -ForegroundColor White
Write-Host "   2. Testar funcionalidades" -ForegroundColor White
Write-Host "   3. Configurar frontend" -ForegroundColor White
Write-Host ""

