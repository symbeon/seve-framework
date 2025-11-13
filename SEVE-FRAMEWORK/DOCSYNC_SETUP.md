# 📚 DOCSYNC Setup para SEVE Framework

**Data**: 07 de Novembro de 2025  
**Status**: ✅ Configurado

---

## 🎯 Objetivo

O DOCSYNC foi configurado para organizar e sincronizar os arquivos de documentação do SEVE Framework, mantendo uma estrutura consistente e facilitando a manutenção.

---

## 📋 Arquivos Criados

### 1. **`docsync.yaml`**
Arquivo de configuração principal do DOCSYNC para o SEVE Framework.

**Localização**: `SEVE-FRAMEWORK/docsync.yaml`

**Principais configurações**:
- ✅ Diretórios monitorados: `docs/`, `src/`, `tests/`, `examples/`, `contracts/`, `config/`, `scripts/`
- ✅ Padrões de arquivos: `*.md`, `*.py`, `*.sol`, `*.yaml`, `*.json`
- ✅ Exclusões: `__pycache__`, `.git`, `node_modules`, `.venv`, `cache`, `logs`
- ✅ Organização automática de arquivos raiz
- ✅ Validação de markdown
- ✅ Monitoramento e logging

### 2. **`scripts/organize_with_docsync.py`**
Script Python para executar a organização dos arquivos usando a configuração DOCSYNC.

**Funcionalidades**:
- ✅ Carrega configuração do `docsync.yaml`
- ✅ Organiza arquivos na raiz do projeto
- ✅ Organiza arquivos dentro dos diretórios configurados
- ✅ Modo dry-run para simulação
- ✅ Logging detalhado
- ✅ Estatísticas de organização

---

## 🚀 Como Usar

### 1. **Executar em Modo Dry-Run (Simulação)**

```bash
cd SEVE-FRAMEWORK
python scripts/organize_with_docsync.py --config docsync.yaml --dry-run
```

Este comando simula a organização sem mover arquivos, mostrando o que seria feito.

### 2. **Executar Organização Real**

```bash
cd SEVE-FRAMEWORK
python scripts/organize_with_docsync.py --config docsync.yaml
```

⚠️ **Atenção**: Este comando moverá arquivos de acordo com a configuração. Certifique-se de ter backup ou execute primeiro em modo dry-run.

### 3. **Usar DOCSYNC Completo (Futuro)**

Quando o DOCSYNC estiver totalmente instalado e configurado:

```bash
cd C:\Users\João\Desktop\PROJETOS\04_DEVELOPER_TOOLS\DOCSYNC
python run_sync.py --config C:\Users\João\Desktop\PROJETOS\00_ECOSYSTEM_COMERCIAL\SEVE-FRAMEWORK\SEVE-FRAMEWORK\docsync.yaml
```

---

## 📁 Estrutura de Organização

### Arquivos na Raiz
Arquivos `.md` na raiz (exceto `README.md`, `LICENSE`) serão movidos para:
- `docs/root/`

### Diretórios Monitorados
- **`docs/`**: Documentação técnica, API, guias, desenvolvimento
- **`src/`**: Código fonte Python
- **`tests/`**: Testes automatizados
- **`examples/`**: Exemplos de uso
- **`contracts/`**: Contratos Solidity
- **`config/`**: Arquivos de configuração
- **`scripts/`**: Scripts utilitários

---

## ⚙️ Configuração Detalhada

### Diretórios Excluídos
- `**/__pycache__`
- `**/.git`
- `**/node_modules`
- `**/.venv`
- `**/cache`
- `**/logs`
- `**/artifacts`
- `**/Desktop/**`
- `**/legacy/guardflow_code/SEVE-UNIVERSAL/_git_legacy/**`

### Validação
- ✅ Verificação de metadados
- ✅ Validação de links
- ✅ Verificação de estrutura
- ✅ Consistência de documentação
- ✅ Markdownlint

### Monitoramento
- ✅ Logging em `logs/docsync.log`
- ✅ Métricas de mudanças de arquivos
- ✅ Status de sincronização
- ✅ Resultados de validação

---

## 📝 Próximos Passos

1. **Instalar Dependências do DOCSYNC** (quando necessário):
   ```bash
   cd C:\Users\João\Desktop\PROJETOS\04_DEVELOPER_TOOLS\DOCSYNC
   pip install -r requirements.txt
   ```

2. **Executar Primeira Organização**:
   ```bash
   cd SEVE-FRAMEWORK
   python scripts/organize_with_docsync.py --config docsync.yaml --dry-run
   ```

3. **Revisar Resultados** e executar organização real se satisfatório.

4. **Integrar com CI/CD** (opcional):
   - Adicionar validação automática de documentação
   - Executar organização em commits

---

## 🔧 Personalização

Para personalizar a organização, edite o arquivo `docsync.yaml`:

- **Adicionar diretórios**: Edite a seção `directories`
- **Alterar padrões**: Modifique `patterns` em cada diretório
- **Ajustar exclusões**: Edite `exclude_globally`
- **Configurar validação**: Modifique a seção `validation`

---

## 📊 Status Atual

- ✅ Arquivo de configuração criado
- ✅ Script de organização criado
- ✅ Estrutura de diretórios definida
- ⚠️ Primeira execução pendente (dry-run recomendado)

---

**Documentação mantida pela Equipe EON - Symbeon Tech**

