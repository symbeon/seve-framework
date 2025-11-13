# Script PowerShell para deploy do showcase

Write-Host "🚀 Deploy do SEVE Framework Showcase" -ForegroundColor Green
Write-Host ""

# Verificar se está no diretório correto
if (-not (Test-Path "showcase")) {
    Write-Host "❌ Pasta showcase não encontrada!" -ForegroundColor Red
    Write-Host "   Execute este script da raiz do projeto" -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Pasta showcase encontrada" -ForegroundColor Green
Write-Host ""

# Verificar GitHub CLI
if (Get-Command gh -ErrorAction SilentlyContinue) {
    Write-Host "📦 GitHub CLI encontrado" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "⚠️  GitHub Pages precisa ser configurado manualmente:" -ForegroundColor Yellow
    Write-Host "   1. Acesse: https://github.com/symbeon/seve-framework/settings/pages"
    Write-Host "   2. Source: Deploy from a branch"
    Write-Host "   3. Branch: main"
    Write-Host "   4. Folder: /showcase"
    Write-Host ""
    Write-Host "💡 Ou use Vercel (mais rápido):" -ForegroundColor Cyan
    Write-Host "   cd showcase; npx vercel --prod"
    exit 0
}

# Usar Vercel (recomendado)
Write-Host "📦 Usando Vercel (mais rápido e fácil)..." -ForegroundColor Cyan
Write-Host ""

Set-Location showcase

if (Get-Command vercel -ErrorAction SilentlyContinue) {
    Write-Host "🚀 Iniciando deploy com Vercel..." -ForegroundColor Green
    vercel --prod
} else {
    Write-Host "📥 Usando Vercel via npx..." -ForegroundColor Cyan
    npx vercel --prod
}

Write-Host ""
Write-Host "✅ Deploy concluído!" -ForegroundColor Green
Write-Host "   URL será fornecida pelo Vercel" -ForegroundColor Cyan

