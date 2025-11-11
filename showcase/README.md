# 🌐 SEVE Framework - Showcase Portal

Portal de apresentação do SEVE Framework para investidores, parceiros e comunidade.

---

## 🚀 **Deploy**

### **Opção 1: GitHub Pages (Recomendado - Grátis)**

1. **Fazer push do código**:
```bash
git add showcase/
git commit -m "feat: add showcase portal"
git push origin main
```

2. **Ativar GitHub Pages**:
   - Ir em Settings → Pages
   - Source: Deploy from a branch
   - Branch: main
   - Folder: /showcase
   - Salvar

3. **Acessar**: `https://[seu-usuario].github.io/seve-framework/`

---

### **Opção 2: Vercel (Grátis)**

1. **Instalar Vercel CLI**:
```bash
npm i -g vercel
```

2. **Deploy**:
```bash
cd showcase
vercel
```

3. **Acessar**: URL fornecida pelo Vercel

---

### **Opção 3: Netlify (Grátis)**

1. **Arrastar e soltar** a pasta `showcase` em https://app.netlify.com/drop

2. **Acessar**: URL fornecida pelo Netlify

---

## 📝 **Personalização**

### **Editar Conteúdo**

1. **Email de contato**: Editar `index.html` linha com `mailto:`
2. **Links**: Atualizar links do GitHub e documentação
3. **Cores**: Modificar variáveis CSS em `:root`
4. **Conteúdo**: Editar textos nas seções

---

## 🎨 **Customização Visual**

As cores podem ser alteradas em `index.html`:

```css
:root {
    --primary: #6366f1;      /* Cor principal */
    --primary-dark: #4f46e5; /* Cor principal escura */
    --secondary: #8b5cf6;    /* Cor secundária */
    --dark: #1e1b4b;         /* Cor escura */
    --light: #f8fafc;        /* Cor clara */
}
```

---

## 📱 **Responsivo**

O portal é totalmente responsivo e funciona em:
- ✅ Desktop
- ✅ Tablet
- ✅ Mobile

---

## 🔗 **Links Úteis**

- **GitHub**: https://github.com/symbeon/seve-framework
- **Documentação**: `/docs`
- **Pitch Deck**: `/docs/pitch/PITCH_DECK.md`
- **Executive Summary**: `/docs/executive/EXECUTIVE_SUMMARY.md`

---

**Última Atualização**: 09 de Novembro de 2025

