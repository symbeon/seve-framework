# Script de commit sistemático para documentação SEVE Framework
# Equipe EON - Symbeon Tech

Write-Host "🚀 Iniciando commits sistemáticos..." -ForegroundColor Green
Write-Host ""

# 1. Documentação operacional principal
Write-Host "📚 Commit 1: Documentação operacional principal..." -ForegroundColor Cyan
git add docs/DEPLOYMENT_GUIDE.md, docs/TESTNET_PLAYBOOK.md, docs/RPC_PROVIDERS.md, docs/ENV_SETUP.md, docs/SECURITY_CHECKLIST.md, docs/INDEX.md
git commit -m "docs: Adicionar documentação operacional completa

- Guia completo de deploy (local, testnet, produção)
- Playbook reutilizável de testnet
- Guia de provedores RPC (Infura, Alchemy, públicos)
- Setup completo de ambiente (.env)
- Checklist de segurança completo
- Índice consolidado de documentação

Mantido por: Equipe EON - Symbeon Tech"

# 2. Configurações DOCSYNC e GIDEN
Write-Host "🔧 Commit 2: Configurações DOCSYNC e GIDEN..." -ForegroundColor Cyan
git add docsync.yaml, giden.yaml
git commit -m "config: Atualizar DOCSYNC e GIDEN para documentação operacional

- DOCSYNC configurado para monitorar docs operacionais
- GIDEN configurado para priorizar guias operacionais
- Templates e validações aplicadas

Ferramentas da Equipe EON integradas"

# 3. README atualizado
Write-Host "📖 Commit 3: README atualizado..." -ForegroundColor Cyan
git add README.md
git commit -m "docs: Atualizar README com links para nova documentação

- Adicionada seção de Documentação Completa
- Links diretos para todos os guias
- Busca rápida por tópico
- Estrutura organizada por categoria

Mantido por: Equipe EON - Symbeon Tech"

# 4. Análise de custos
if (Test-Path "COST_ANALYSIS.md") {
    Write-Host "💰 Commit 4: Análise de custos..." -ForegroundColor Cyan
    git add COST_ANALYSIS.md
    git commit -m "docs: Adicionar análise completa de custos

- Comparação de provedores RPC
- Alternativas gratuitas detalhadas
- Estratégia de desenvolvimento sem custos
- Projeções para produção

Mantido por: Equipe EON - Symbeon Tech"
}

# 5. Outros documentos em docs
Write-Host "📄 Commit 5: Verificando outros documentos..." -ForegroundColor Cyan
$docsFiles = Get-ChildItem -Path "docs" -Filter "*.md" -File | Where-Object { $_.Name -notin @("DEPLOYMENT_GUIDE.md", "TESTNET_PLAYBOOK.md", "RPC_PROVIDERS.md", "ENV_SETUP.md", "SECURITY_CHECKLIST.md", "INDEX.md") }
if ($docsFiles.Count -gt 0) {
    $files = $docsFiles | ForEach-Object { $_.FullName }
    git add $files
    git commit -m "docs: Adicionar documentação adicional

- Documentos complementares
- Templates e exemplos

Mantido por: Equipe EON - Symbeon Tech"
}

# Resumo final
Write-Host ""
Write-Host "✅ Commits concluídos!" -ForegroundColor Green
Write-Host ""
Write-Host "📊 Resumo dos últimos commits:" -ForegroundColor Yellow
git log --oneline -10


