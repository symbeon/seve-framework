# ⚙️ Configuração Vercel - SEVE Framework Showcase

**Status**: Projeto sendo criado no Vercel

---

## ✅ **CONFIGURAÇÕES CORRETAS**

### **Na Tela do Vercel:**

1. **Vercel Team**: 
   - ✅ "sh1w4's projects" (já está correto)

2. **Project Name**: 
   - ✅ "seve-framework" (já está correto)
   - Ou pode mudar para "seve-framework-showcase"

3. **Framework Preset**: 
   - ⚠️ **MUDAR**: De "FastAPI" para **"Other"** ou **"Static"**
   - Como é HTML estático, não precisa de framework

4. **Root Directory**: 
   - ⚠️ **MUDAR**: De "./" para **"./showcase"**
   - Ou deixar "./" se já estiver na pasta showcase

5. **Build and Output Settings** (expandir):
   - Build Command: **deixar vazio** (não precisa build)
   - Output Directory: **"."** (raiz da pasta showcase)

---

## 🎯 **PASSO A PASSO**

### **1. Ajustar Configurações**:
- Framework Preset: **Other** ou **Static**
- Root Directory: **./showcase** (se estiver na raiz do repo)
- Ou **./** (se já estiver na pasta showcase)

### **2. Expandir "Build and Output Settings"**:
- Build Command: **deixar vazio**
- Output Directory: **"."**

### **3. Clicar em "Deploy"**

### **4. Aguardar Deploy**:
- Vercel vai fazer deploy automaticamente
- Pode levar 1-2 minutos

### **5. Acessar URL**:
- Vercel vai fornecer URL (ex: `seve-framework.vercel.app`)
- Ou URL customizada se configurada

---

## ⚠️ **IMPORTANTE**

### **Se Root Directory estiver errado**:
- Se estiver na raiz do repo: usar **"./showcase"**
- Se já estiver na pasta showcase: usar **"./"**

### **Se Framework estiver errado**:
- **Não usar FastAPI** (é para Python)
- Usar **"Other"** ou **"Static"** (HTML estático)

---

## ✅ **APÓS DEPLOY**

1. **URL será fornecida** pelo Vercel
2. **Site estará acessível** imediatamente
3. **Atualizações automáticas** em cada push (se configurado)

---

**Última Atualização**: 09 de Novembro de 2025

