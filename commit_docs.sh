#!/bin/bash

# Script de commit sistemático para documentação SEVE Framework
# Equipe EON - Symbeon Tech

echo "🚀 Iniciando commits sistemáticos..."

# 1. Documentação operacional principal
echo "📚 Commit 1: Documentação operacional principal..."
git add docs/DEPLOYMENT_GUIDE.md docs/TESTNET_PLAYBOOK.md docs/RPC_PROVIDERS.md docs/ENV_SETUP.md docs/SECURITY_CHECKLIST.md docs/INDEX.md
git commit -m "docs: Adicionar documentação operacional completa

- Guia completo de deploy (local, testnet, produção)
- Playbook reutilizável de testnet
- Guia de provedores RPC (Infura, Alchemy, públicos)
- Setup completo de ambiente (.env)
- Checklist de segurança completo
- Índice consolidado de documentação

Mantido por: Equipe EON - Symbeon Tech"

# 2. Configurações DOCSYNC e GIDEN
echo "🔧 Commit 2: Configurações DOCSYNC e GIDEN..."
git add docsync.yaml giden.yaml
git commit -m "config: Atualizar DOCSYNC e GIDEN para documentação operacional

- DOCSYNC configurado para monitorar docs operacionais
- GIDEN configurado para priorizar guias operacionais
- Templates e validações aplicadas

Ferramentas da Equipe EON integradas"

# 3. README atualizado
echo "📖 Commit 3: README atualizado..."
git add README.md
git commit -m "docs: Atualizar README com links para nova documentação

- Adicionada seção de Documentação Completa
- Links diretos para todos os guias
- Busca rápida por tópico
- Estrutura organizada por categoria

Mantido por: Equipe EON - Symbeon Tech"

# 4. Análise de custos
if [ -f "COST_ANALYSIS.md" ]; then
    echo "💰 Commit 4: Análise de custos..."
    git add COST_ANALYSIS.md
    git commit -m "docs: Adicionar análise completa de custos

- Comparação de provedores RPC
- Alternativas gratuitas detalhadas
- Estratégia de desenvolvimento sem custos
- Projeções para produção

Mantido por: Equipe EON - Symbeon Tech"
fi

# 5. Arquivos gerados/teste
if ls docs/*.md 1> /dev/null 2>&1; then
    echo "📄 Commit 5: Outros documentos..."
    git add docs/*.md
    git commit -m "docs: Adicionar documentação adicional

- Documentos complementares
- Templates e exemplos

Mantido por: Equipe EON - Symbeon Tech"
fi

# 6. Resumo final
echo "✅ Commits concluídos!"
echo ""
echo "📊 Resumo:"
git log --oneline -6


