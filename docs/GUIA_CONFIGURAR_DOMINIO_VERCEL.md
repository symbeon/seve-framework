# 🌐 Guia: Configurar symbeon.tech no Vercel

**Data**: 11 de Novembro de 2025  
**Domínio**: symbeon.tech

---

## 📋 **PRÉ-REQUISITOS**

- ✅ Domínio `symbeon.tech` registrado e ativo
- ✅ Acesso ao painel de gerenciamento do domínio
- ✅ Projeto Vercel com deploy funcionando

---

## 🚀 **PASSO A PASSO**

### **Opção 1: Via Dashboard Vercel (Recomendado)**

#### **1. Acessar Configurações do Projeto**

1. Acesse: https://vercel.com/dashboard
2. Selecione o projeto `showcase`
3. Vá em **Settings** → **Domains**

#### **2. Adicionar Domínio**

1. Clique em **Add Domain**
2. Digite: `symbeon.tech`
3. Clique em **Add**

#### **3. Configurar DNS no Registrador**

O Vercel mostrará os registros DNS necessários. Você precisará adicionar no painel do seu registrador:

**Registros DNS necessários:**

```
Tipo: A
Nome: @
Valor: 76.76.21.21

Tipo: CNAME
Nome: www
Valor: cname.vercel-dns.com
```

**OU (se o Vercel fornecer registros específicos):**

Siga exatamente os registros que o Vercel mostrar na tela.

#### **4. Configurar no Painel do Domínio**

1. Acesse o painel do seu registrador (onde você comprou o domínio)
2. Vá em **DNS Management** ou **Zona DNS**
3. Adicione os registros fornecidos pelo Vercel
4. Salve as alterações

#### **5. Aguardar Propagação**

- DNS pode levar de 5 minutos a 48 horas para propagar
- Normalmente leva 1-2 horas
- Você pode verificar com: https://dnschecker.org

---

### **Opção 2: Via Vercel CLI**

```bash
# Adicionar domínio via CLI
npx vercel domains add symbeon.tech

# Verificar status
npx vercel domains ls
```

---

## 🔍 **VERIFICAÇÃO**

### **1. Verificar DNS**

Use ferramentas online:
- https://dnschecker.org
- https://www.whatsmydns.net

Digite `symbeon.tech` e verifique se os registros estão corretos.

### **2. Verificar SSL**

O Vercel configura SSL automaticamente via Let's Encrypt. Aguarde alguns minutos após a propagação DNS.

### **3. Testar Acesso**

Após propagação:
- Acesse: `https://symbeon.tech`
- Deve redirecionar para o showcase

---

## ⚙️ **CONFIGURAÇÕES AVANÇADAS**

### **Redirect www para não-www (ou vice-versa)**

No Vercel Dashboard:
1. Settings → Domains
2. Configure redirect automático

### **Subdomínios**

Para adicionar subdomínios (ex: `seve.symbeon.tech`):

1. No Vercel: Add Domain → `seve.symbeon.tech`
2. No registrador: Adicione CNAME:
   ```
   Tipo: CNAME
   Nome: seve
   Valor: cname.vercel-dns.com
   ```

---

## 🐛 **TROUBLESHOOTING**

### **Problema: DNS não propaga**

**Solução**:
- Aguarde até 48 horas
- Verifique se os registros estão corretos
- Limpe cache DNS: `ipconfig /flushdns` (Windows)

### **Problema: SSL não funciona**

**Solução**:
- Aguarde alguns minutos após DNS propagar
- Vercel configura SSL automaticamente
- Verifique se o domínio está apontando corretamente

### **Problema: Domínio não aparece no Vercel**

**Solução**:
- Verifique se você tem permissão no projeto
- Verifique se o domínio está ativo no registrador
- Tente adicionar novamente

---

## 📝 **CHECKLIST**

- [ ] Domínio registrado e ativo
- [ ] Acesso ao painel do registrador
- [ ] Projeto Vercel funcionando
- [ ] Domínio adicionado no Vercel
- [ ] Registros DNS configurados
- [ ] Aguardando propagação DNS
- [ ] SSL configurado automaticamente
- [ ] Teste de acesso bem-sucedido

---

## 🔗 **LINKS ÚTEIS**

- **Vercel Dashboard**: https://vercel.com/dashboard
- **Vercel Domains Docs**: https://vercel.com/docs/concepts/projects/domains
- **DNS Checker**: https://dnschecker.org
- **What's My DNS**: https://www.whatsmydns.net

---

**Última Atualização**: 11 de Novembro de 2025

