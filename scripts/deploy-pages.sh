#!/bin/bash

# Script para deploy do showcase no GitHub Pages via terminal

echo "🚀 Deploy do SEVE Framework Showcase"
echo ""

# Verificar se está no diretório correto
if [ ! -d "showcase" ]; then
    echo "❌ Pasta showcase não encontrada!"
    echo "   Execute este script da raiz do projeto"
    exit 1
fi

# Verificar se git está configurado
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Não é um repositório git!"
    exit 1
fi

echo "✅ Verificações passadas"
echo ""

# Opção 1: Usar GitHub CLI (se disponível)
if command -v gh &> /dev/null; then
    echo "📦 Usando GitHub CLI..."
    echo ""
    echo "⚠️  GitHub Pages precisa ser configurado manualmente:"
    echo "   1. Acesse: https://github.com/symbeon/seve-framework/settings/pages"
    echo "   2. Source: Deploy from a branch"
    echo "   3. Branch: main"
    echo "   4. Folder: /showcase"
    echo ""
    echo "💡 Ou use Vercel (mais rápido):"
    echo "   cd showcase && npx vercel"
    exit 0
fi

# Opção 2: Usar Vercel (recomendado)
echo "📦 Usando Vercel (mais rápido e fácil)..."
echo ""
cd showcase

if command -v vercel &> /dev/null; then
    echo "🚀 Iniciando deploy com Vercel..."
    vercel --prod
else
    echo "📥 Instalando Vercel CLI..."
    npx vercel --prod
fi

echo ""
echo "✅ Deploy concluído!"
echo "   URL será fornecida pelo Vercel"

