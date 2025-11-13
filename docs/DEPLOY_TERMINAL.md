# 🖥️ Deploy pelo Terminal - Guia Completo

**Opções para fazer deploy do showcase pelo terminal**

---

## 🚀 **OPÇÃO 1: Vercel (Mais Rápido - Recomendado)**

### **Primeira Vez**:
```bash
cd showcase
npx vercel --prod
```

**O que acontece**:
1. Vercel pede login (criar conta grátis)
2. Faz algumas perguntas (aceitar padrões)
3. Deploy automático
4. Fornece URL (ex: `seve-framework.vercel.app`)

**Vantagens**:
- ✅ Muito rápido (1-2 minutos)
- ✅ Grátis
- ✅ HTTPS automático
- ✅ Deploy automático em cada push

---

## 🔧 **OPÇÃO 2: GitHub CLI**

### **Configurar Pages via CLI**:
```bash
# Abrir repositório no navegador
gh repo view symbeon/seve-framework --web

# Ou configurar manualmente via web
gh browse --repo symbeon/seve-framework settings/pages
```

**Nota**: GitHub Pages ainda precisa ser configurado manualmente na web, mas o CLI ajuda a abrir rapidamente.

---

## 📜 **OPÇÃO 3: Script Automatizado**

### **PowerShell**:
```powershell
.\scripts\deploy-pages.ps1
```

### **Bash**:
```bash
./scripts/deploy-pages.sh
```

**O que faz**:
- Verifica estrutura
- Oferece opções (Vercel ou GitHub)
- Executa deploy

---

## 🎯 **RECOMENDAÇÃO: Vercel**

**Por quê**:
- ✅ Mais rápido (1-2 min vs 5-10 min)
- ✅ Mais fácil (menos configuração)
- ✅ Mais confiável
- ✅ URL personalizada

**Como fazer**:
```bash
cd showcase
npx vercel --prod
```

**Siga as instruções**:
- Login (primeira vez)
- Aceitar configurações padrão
- Aguardar deploy
- Copiar URL fornecida

---

## 📋 **COMPARAÇÃO**

| Opção | Tempo | Dificuldade | URL |
|-------|-------|-------------|-----|
| **Vercel** | 1-2 min | ⭐ Fácil | `seve-framework.vercel.app` |
| **GitHub Pages** | 5-10 min | ⭐⭐ Média | `symbeon.github.io/seve-framework` |
| **Netlify** | 2-3 min | ⭐ Fácil | `seve-framework.netlify.app` |

---

## ✅ **APÓS DEPLOY**

### **Vercel**:
- URL será fornecida
- Pode adicionar domínio customizado depois
- Deploy automático em cada push (se configurar)

### **GitHub Pages**:
- URL: https://symbeon.github.io/seve-framework/
- Atualiza automaticamente em cada push

---

## 🔄 **ATUALIZAÇÕES FUTURAS**

### **Vercel**:
- Editar arquivos
- `git push` (se configurado)
- Ou `npx vercel --prod` novamente

### **GitHub Pages**:
- Editar arquivos
- `git push`
- Atualiza automaticamente

---

**Última Atualização**: 09 de Novembro de 2025

