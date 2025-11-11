# 🔧 Troubleshooting: GitHub Pages Não Aparece

**Problema**: Página não aparece após ativar GitHub Pages

---

## ✅ **VERIFICAÇÕES PASSO A PASSO**

### **1. Verificar se GitHub Pages está Ativado**

1. Acesse: https://github.com/symbeon/seve-framework/settings/pages
2. Verifique se mostra:
   - ✅ "Your site is live at..." (verde)
   - Ou ⚠️ "Your site is ready to be published" (amarelo)

**Se não estiver ativado**:
- Source: "Deploy from a branch"
- Branch: "main"
- Folder: "/showcase"
- Clique em "Save"

---

### **2. Verificar Estrutura de Arquivos**

O arquivo deve estar em:
```
seve-framework/
└── showcase/
    └── index.html  ✅
```

**Verificar**:
- Arquivo existe? ✅
- Nome está correto? (minúsculas: `index.html`)
- Está na pasta `showcase/`?

---

### **3. Aguardar Deploy**

GitHub Pages pode levar:
- **Primeira vez**: 5-10 minutos
- **Atualizações**: 1-5 minutos

**Como verificar**:
- Vá em Settings → Pages
- Veja se há mensagem de "deploy in progress"
- Aguarde até aparecer "Your site is live"

---

### **4. Verificar URL**

A URL correta deve ser:
- **https://symbeon.github.io/seve-framework/**

**Se usar organização**:
- Pode ser: `https://symbeon.github.io/seve-framework/`
- Ou: `https://[usuario].github.io/seve-framework/`

**Verificar**:
- Settings → Pages mostra a URL exata
- Copie e cole a URL mostrada

---

### **5. Limpar Cache do Navegador**

**Problema comum**: Cache antigo

**Solução**:
- Ctrl + F5 (Windows) ou Cmd + Shift + R (Mac)
- Ou abrir em aba anônima/privada
- Ou limpar cache do navegador

---

### **6. Verificar Erros no Deploy**

**Como verificar**:
1. Settings → Pages
2. Veja se há mensagem de erro (vermelho)
3. Clique em "View deployment" para ver logs

**Erros comuns**:
- ❌ "Build failed" → Verificar HTML/CSS
- ❌ "404 Not Found" → Verificar caminho do arquivo
- ❌ "Branch not found" → Verificar branch

---

## 🔧 **SOLUÇÕES ALTERNATIVAS**

### **Solução 1: Usar Branch `gh-pages`**

Se `/showcase` não funcionar:

1. **Criar branch gh-pages**:
```bash
git checkout -b gh-pages
git add showcase/
git commit -m "feat: add showcase for gh-pages"
git push origin gh-pages
```

2. **Configurar Pages**:
   - Source: "Deploy from a branch"
   - Branch: "gh-pages"
   - Folder: "/ (root)"
   - Save

---

### **Solução 2: Mover para Root**

Se quiser usar root:

1. **Mover arquivos**:
```bash
# Mover index.html para root
mv showcase/index.html index.html
```

2. **Configurar Pages**:
   - Source: "Deploy from a branch"
   - Branch: "main"
   - Folder: "/ (root)"
   - Save

---

### **Solução 3: Usar GitHub Actions**

Criar workflow automático:

1. **Criar arquivo**: `.github/workflows/pages.yml`
2. **Conteúdo**:
```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./showcase
```

3. **Configurar Pages**:
   - Source: "GitHub Actions"
   - Save

---

## ✅ **CHECKLIST DE VERIFICAÇÃO**

- [ ] GitHub Pages está ativado?
- [ ] Branch configurado corretamente (main)?
- [ ] Folder configurado corretamente (/showcase)?
- [ ] Arquivo index.html existe em showcase/?
- [ ] Aguardou tempo suficiente (5-10 min)?
- [ ] Limpou cache do navegador?
- [ ] URL está correta?
- [ ] Não há erros no deploy?

---

## 🆘 **SE AINDA NÃO FUNCIONAR**

### **Opção 1: Verificar com Suporte GitHub**
- GitHub Support: https://support.github.com/
- Community Forum: https://github.community/

### **Opção 2: Usar Alternativa**
- **Vercel**: `npx vercel` (mais rápido)
- **Netlify**: Drag & drop (mais fácil)

---

## 📞 **INFORMAÇÕES PARA DIAGNÓSTICO**

Se precisar de ajuda, forneça:
1. URL que está tentando acessar
2. Mensagem que aparece (404, erro, etc.)
3. Status em Settings → Pages
4. Screenshot da configuração

---

**Última Atualização**: 09 de Novembro de 2025

