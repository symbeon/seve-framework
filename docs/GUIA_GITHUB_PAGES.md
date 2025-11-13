# 🌐 Guia: Ativar GitHub Pages para SEVE Framework

**Objetivo**: Fazer o portal/showcase aparecer publicamente no GitHub Pages

---

## ✅ **PASSO 1: Arquivos já commitados e pushados**

Os arquivos do showcase já foram enviados para o GitHub:
- ✅ `showcase/index.html`
- ✅ `showcase/README.md`
- ✅ Todos os materiais de apresentação

---

## 🚀 **PASSO 2: Ativar GitHub Pages**

### **Opção A: Via Interface Web (Recomendado)**

1. **Acesse o repositório no GitHub**:
   - https://github.com/symbeon/seve-framework

2. **Vá em Settings**:
   - Clique em "Settings" (no topo do repositório)

3. **Encontre "Pages"**:
   - No menu lateral esquerdo, clique em "Pages"
   - Ou acesse diretamente: https://github.com/symbeon/seve-framework/settings/pages

4. **Configure o Source**:
   - **Source**: Selecione "Deploy from a branch"
   - **Branch**: Selecione "main"
   - **Folder**: Selecione "/showcase"
   - Clique em "Save"

5. **Aguarde o Deploy**:
   - GitHub vai fazer o deploy automaticamente
   - Pode levar 1-5 minutos
   - Você verá uma mensagem verde quando estiver pronto

6. **Acesse seu site**:
   - URL será: `https://symbeon.github.io/seve-framework/`
   - Ou o GitHub mostrará a URL exata

---

### **Opção B: Via GitHub Actions (Avançado)**

Se quiser mais controle, pode criar um workflow:

```yaml
# .github/workflows/pages.yml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]
    paths:
      - 'showcase/**'

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

---

## 🔗 **URL DO SEU SITE**

Após ativar, seu site estará disponível em:

**https://symbeon.github.io/seve-framework/**

Ou verifique a URL exata nas configurações do GitHub Pages.

---

## ✅ **VERIFICAÇÃO**

### **Como saber se está funcionando**:

1. **No GitHub**:
   - Vá em Settings → Pages
   - Deve mostrar "Your site is live at..."

2. **Acesse a URL**:
   - Abra a URL do GitHub Pages
   - Deve ver o portal do SEVE Framework

3. **Teste os links**:
   - Navegue pelas seções
   - Teste os botões
   - Verifique responsividade (mobile)

---

## 🔧 **TROUBLESHOOTING**

### **Problema: Página não aparece**

**Solução**:
- Verifique se o branch está correto (main)
- Verifique se a pasta está correta (/showcase)
- Aguarde alguns minutos (deploy pode demorar)
- Limpe o cache do navegador

### **Problema: Erro 404**

**Solução**:
- Verifique se `index.html` está em `showcase/`
- Verifique se o nome do arquivo está correto (minúsculas)
- Verifique se há commits recentes no branch

### **Problema: CSS não carrega**

**Solução**:
- Verifique se o CSS está inline no HTML (já está)
- Verifique se não há erros no HTML
- Teste em outro navegador

---

## 📝 **ATUALIZAÇÕES FUTURAS**

Para atualizar o site:

1. **Edite os arquivos**:
   - Modifique `showcase/index.html`
   - Ou outros arquivos

2. **Commit e push**:
```bash
git add showcase/
git commit -m "feat: update showcase content"
git push origin main
```

3. **GitHub atualiza automaticamente**:
   - Pode levar 1-5 minutos
   - Site será atualizado automaticamente

---

## 🎨 **CUSTOMIZAÇÃO**

### **Personalizar Conteúdo**:

1. **Email de contato**:
   - Edite `showcase/index.html`
   - Procure por `mailto:contato@seve-framework.ai`
   - Substitua pelo seu email

2. **Links do GitHub**:
   - Procure por `https://github.com/symbeon/seve-framework`
   - Substitua se necessário

3. **Cores**:
   - Edite as variáveis CSS em `:root`
   - No início do arquivo HTML

---

## 📊 **ESTATÍSTICAS**

GitHub Pages fornece estatísticas básicas:
- Acessos (via GitHub Insights)
- Tráfego (via Settings → Pages → View analytics)

---

## 🔒 **SEGURANÇA**

- ✅ GitHub Pages é seguro (HTTPS automático)
- ✅ Não precisa de configuração adicional
- ✅ Atualizações automáticas

---

## ✅ **CHECKLIST FINAL**

- [ ] Arquivos commitados e pushados
- [ ] GitHub Pages ativado
- [ ] Branch configurado (main)
- [ ] Pasta configurada (/showcase)
- [ ] Site acessível na URL
- [ ] Links funcionando
- [ ] Responsivo (teste mobile)
- [ ] Email de contato atualizado

---

**Última Atualização**: 09 de Novembro de 2025

