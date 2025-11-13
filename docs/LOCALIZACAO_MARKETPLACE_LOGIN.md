# 📍 Localização do Marketplace e Login

## 🛒 **MARKETPLACE**

### **Arquivos:**
1. **Página Principal do Marketplace:**
   - `showcase/src/pages/MarketplacePageEnhanced.tsx`
   - Rota: `/marketplace`

2. **Página de Detalhes do Agente:**
   - `showcase/src/pages/AgentDetailsPage.tsx`
   - Rota: `/agent/:id`

3. **Página Antiga (mantida):**
   - `showcase/src/pages/MarketplacePage.tsx`
   - Não está sendo usada atualmente

### **Funcionalidades:**
- ✅ Busca por texto
- ✅ Filtros por categoria e módulos
- ✅ Ordenação (rating, downloads, reviews)
- ✅ Preview de agentes
- ✅ Sistema de avaliações
- ✅ Tags e categorias

### **Como Acessar:**
1. Via Header: Clique em "Marketplace" no menu de navegação
2. Via URL: `/marketplace`
3. Via Link: Qualquer link que aponte para `/marketplace`

---

## 🔐 **LOGIN**

### **Arquivos:**
1. **Componente de Login:**
   - `showcase/src/components/LoginModal.tsx`
   - Modal reutilizável

2. **Contexto de Autenticação:**
   - `showcase/src/contexts/AuthContext.tsx`
   - Gerencia estado de autenticação

3. **Onde é Usado:**
   - `showcase/src/components/Header.tsx` - Botão "Entrar"
   - `showcase/src/pages/MarketplacePageEnhanced.tsx` - Proteção de rotas
   - `showcase/src/pages/AgentDetailsPage.tsx` - Proteção de ações

### **Funcionalidades:**
- ✅ Login com email/senha
- ✅ Registro de novo usuário
- ✅ Recuperação de senha
- ✅ OAuth Google (estrutura)
- ✅ OAuth GitHub (estrutura)
- ✅ Persistência com localStorage

### **Como Acessar:**
1. Via Header: Clique no botão "Entrar" no canto superior direito
2. Via Marketplace: Ao tentar acessar conteúdo protegido
3. Via Programático: `setLoginModalOpen(true)`

### **Rotas Protegidas:**
- `/dashboard` - Requer autenticação
- `/builder` - Requer autenticação
- Ações no marketplace (download, teste) - Requer autenticação

---

## 🗺️ **MAPA DE NAVEGAÇÃO**

```
Home (/)
  ├── Header
  │   ├── Marketplace (/marketplace)
  │   └── Login (Modal)
  │
  └── Marketplace (/marketplace)
      ├── Busca e Filtros
      ├── Grid de Agentes
      └── Detalhes do Agente (/agent/:id)
          ├── Visão Geral
          ├── Avaliações
          └── Código
```

---

## 🔧 **INTEGRAÇÃO**

### **Header → Marketplace:**
```tsx
// showcase/src/components/Header.tsx (linha 63-70)
<motion.a
  href="/marketplace"
  whileHover={{ y: -2 }}
  className="text-slate-400 hover:text-slate-200 transition-colors flex items-center gap-2"
>
  <Store size={18} />
  Marketplace
</motion.a>
```

### **Header → Login:**
```tsx
// showcase/src/components/Header.tsx (linha 92-99)
<motion.button
  onClick={() => setLoginModalOpen(true)}
  whileHover={{ scale: 1.05 }}
  whileTap={{ scale: 0.95 }}
  className="px-4 py-2 bg-gradient-accent text-white rounded-lg font-semibold text-sm"
>
  Entrar
</motion.button>
```

### **Marketplace → Login:**
```tsx
// showcase/src/pages/MarketplacePageEnhanced.tsx
const handleAgentClick = (agent: Agent) => {
  if (!isAuthenticated) {
    setLoginModalOpen(true)  // Abre modal de login
    return
  }
  navigate(`/agent/${agent.id}`)
}
```

---

## 📝 **NOTAS**

1. **Marketplace Enhanced** é a versão atual e completa
2. **MarketplacePage.tsx** antiga está mantida mas não é usada
3. **LoginModal** é um componente reutilizável usado em vários lugares
4. **AuthContext** gerencia o estado global de autenticação
5. Todas as rotas protegidas verificam `isAuthenticated` antes de permitir acesso

---

**Última Atualização**: 12 de Novembro de 2025

