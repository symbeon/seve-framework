# 🔐 Script para Atualizar PRIVATE_KEY no .env
# Uso: .\scripts\update-private-key.ps1

param(
    [Parameter(Mandatory=$true)]
    [string]$PrivateKey
)

Write-Host "`n🔐 Atualizando PRIVATE_KEY no .env...`n" -ForegroundColor Cyan

# Remover prefixo 0x se existir
if ($PrivateKey.StartsWith("0x")) {
    $PrivateKey = $PrivateKey.Substring(2)
    Write-Host "⚠️  Prefixo 0x removido" -ForegroundColor Yellow
}

# Verificar comprimento (deve ser 64 caracteres hex)
if ($PrivateKey.Length -ne 64) {
    Write-Host "❌ Erro: Chave privada deve ter 64 caracteres (sem 0x)" -ForegroundColor Red
    Write-Host "   Comprimento atual: $($PrivateKey.Length)" -ForegroundColor Yellow
    exit 1
}

# Ler .env atual
$envPath = ".env"
if (-not (Test-Path $envPath)) {
    Write-Host "❌ Arquivo .env não encontrado!" -ForegroundColor Red
    exit 1
}

$envContent = Get-Content $envPath -Raw

# Atualizar ou adicionar PRIVATE_KEY
if ($envContent -match "PRIVATE_KEY=") {
    $envContent = $envContent -replace "PRIVATE_KEY=.*", "PRIVATE_KEY=$PrivateKey"
    Write-Host "✅ PRIVATE_KEY atualizada" -ForegroundColor Green
} else {
    $envContent += "`nPRIVATE_KEY=$PrivateKey`n"
    Write-Host "✅ PRIVATE_KEY adicionada" -ForegroundColor Green
}

# Salvar .env
$envContent | Out-File -FilePath $envPath -Encoding UTF8 -NoNewline

Write-Host "`n✅ Arquivo .env atualizado!" -ForegroundColor Green
Write-Host "`n🔍 Verificando endereço e saldo...`n" -ForegroundColor Cyan

# Verificar endereço e saldo
npx hardhat run scripts/check-balance.js --network sepolia 2>&1

