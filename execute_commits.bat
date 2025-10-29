@echo off
echo ========================================
echo SEVE Framework - Commits Sistematicos
echo Equipe EON - Symbeon Tech
echo ========================================
echo.

echo [1/6] Adicionando documentacao operacional principal...
git add docs/DEPLOYMENT_GUIDE.md docs/TESTNET_PLAYBOOK.md docs/RPC_PROVIDERS.md docs/ENV_SETUP.md docs/SECURITY_CHECKLIST.md docs/INDEX.md
git commit -m "docs: Adicionar documentacao operacional completa" -m "- Guia completo de deploy (local, testnet, producao)" -m "- Playbook reutilizavel de testnet" -m "- Guia de provedores RPC (Infura, Alchemy, publicos)" -m "- Setup completo de ambiente (.env)" -m "- Checklist de seguranca completo" -m "- Indice consolidado de documentacao" -m "" -m "Mantido por: Equipe EON - Symbeon Tech"

echo [2/6] Adicionando configuracoes DOCSYNC e GIDEN...
git add docsync.yaml giden.yaml
git commit -m "config: Atualizar DOCSYNC e GIDEN para documentacao operacional" -m "- DOCSYNC configurado para monitorar docs operacionais" -m "- GIDEN configurado para priorizar guias operacionais" -m "- Templates e validacoes aplicadas" -m "" -m "Ferramentas da Equipe EON integradas"

echo [3/6] Atualizando README...
git add README.md
git commit -m "docs: Atualizar README com links para nova documentacao" -m "- Adicionada secao de Documentacao Completa" -m "- Links diretos para todos os guias" -m "- Busca rapida por topico" -m "- Estrutura organizada por categoria" -m "" -m "Mantido por: Equipe EON - Symbeon Tech"

echo [4/6] Verificando analise de custos...
if exist COST_ANALYSIS.md (
    git add COST_ANALYSIS.md
    git commit -m "docs: Adicionar analise completa de custos" -m "- Comparacao de provedores RPC" -m "- Alternativas gratuitas detalhadas" -m "- Estrategia de desenvolvimento sem custos" -m "- Projecoes para producao" -m "" -m "Mantido por: Equipe EON - Symbeon Tech"
)

echo [5/6] Adicionando sumario executivo...
if exist EXECUTIVE_SUMMARY.md (
    git add EXECUTIVE_SUMMARY.md
    git commit -m "docs: Adicionar sumario executivo da documentacao" -m "- Resumo executivo completo" -m "- Status e entregas principais" -m "- Pronto para uso imediato" -m "" -m "Mantido por: Equipe EON - Symbeon Tech"
)

echo [6/6] Finalizando...
git log --oneline -10

echo.
echo ========================================
echo Commits concluidos com sucesso!
echo ========================================


