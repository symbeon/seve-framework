# 📧 Guia Rápido: Email Profissional com Zoho Mail (Gratuito)

**Domínio**: symbeon.tech  
**Provedor**: Zoho Mail (Gratuito até 5 usuários)

---

## 🚀 **PASSO A PASSO RÁPIDO**

### **1. Criar Conta Zoho (5 minutos)**

1. Acesse: https://www.zoho.com/mail/
2. Clique em **Sign Up Now** (canto superior direito)
3. Escolha **Mail Free Plan**
4. Preencha:
   - Nome
   - Email pessoal (para verificação)
   - Senha
5. Verifique seu email pessoal

### **2. Adicionar Domínio (5 minutos)**

1. No painel Zoho, clique em **Setup** ou **Add Domain**
2. Digite: `symbeon.tech`
3. Selecione **I own this domain**
4. Clique em **Add**

### **3. Verificar Domínio (10 minutos)**

O Zoho mostrará um **registro TXT** para verificação.

**Na Locaweb**:
1. Acesse: https://painel.locaweb.com.br
2. Vá em **Domínios** → **Gerenciar DNS** → **symbeon.tech**
3. Adicione registro TXT:
   ```
   Tipo: TXT
   Nome: @
   Valor: [copie exatamente do Zoho]
   TTL: 3600
   ```
4. Salve

**Aguarde 5-15 minutos** e volte ao Zoho para verificar.

### **4. Configurar MX Records (10 minutos)**

Após verificação, o Zoho mostrará os registros MX.

**Na Locaweb**, adicione:

```
Registro 1:
Tipo: MX
Nome: @
Prioridade: 10
Valor: mx.zoho.com

Registro 2:
Tipo: MX
Nome: @
Prioridade: 20
Valor: mx2.zoho.com
```

**Importante**: Remova qualquer registro MX antigo se existir.

### **5. Criar Contas de Email (2 minutos)**

1. No Zoho, vá em **Users** ou **Email Accounts**
2. Clique em **Add User** ou **Create Email**
3. Crie:
   - `contato@symbeon.tech`
   - `info@symbeon.tech` (opcional)
4. Defina senhas

### **6. Acessar Email**

1. Acesse: https://mail.zoho.com
2. Login: `contato@symbeon.tech`
3. Senha: [definida no passo 5]

---

## 📱 **CONFIGURAR NO CELULAR/OUTLOOK**

### **IMAP Settings (Zoho)**

```
Servidor IMAP: imap.zoho.com
Porta: 993
SSL: Sim
Usuário: contato@symbeon.tech
Senha: [sua senha]
```

### **SMTP Settings (Zoho)**

```
Servidor SMTP: smtp.zoho.com
Porta: 587
SSL/TLS: Sim
Usuário: contato@symbeon.tech
Senha: [sua senha]
```

---

## ✅ **CHECKLIST**

- [ ] Conta Zoho criada
- [ ] Domínio symbeon.tech adicionado
- [ ] Registro TXT adicionado na Locaweb
- [ ] Domínio verificado no Zoho
- [ ] Registros MX configurados na Locaweb
- [ ] Conta `contato@symbeon.tech` criada
- [ ] Email testado (envio/recebimento)
- [ ] Configurado no celular/Outlook (opcional)

---

## 🎯 **ENDEREÇOS RECOMENDADOS**

Crie estes emails:

- ✅ `contato@symbeon.tech` - **Principal** (já atualizado no site)
- `info@symbeon.tech` - Informações gerais
- `hello@symbeon.tech` - Saudação amigável
- `partnerships@symbeon.tech` - Parcerias
- `investors@symbeon.tech` - Investidores

---

## 💡 **DICAS**

- **Gratuito**: Até 5 contas de email
- **Armazenamento**: 5GB por conta
- **Limite**: 25MB por anexo
- **Suporte**: Email e documentação

---

## 🔗 **LINKS ÚTEIS**

- **Zoho Mail**: https://www.zoho.com/mail/
- **Painel Zoho**: https://mailadmin.zoho.com
- **Acessar Email**: https://mail.zoho.com
- **Documentação**: https://help.zoho.com/portal/en/kb/mail

---

**Tempo Total**: ~30 minutos  
**Custo**: Grátis

---

**Última Atualização**: 11 de Novembro de 2025

