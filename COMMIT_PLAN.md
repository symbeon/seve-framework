<!-- markdownlint-disable MD022 MD032 MD012 MD040 -->
# 📋 Plano de Commits Sistemáticos

**Data**: 09 de Novembro de 2025
**Objetivo**: Organizar commits de forma sistemática e profissional

---

## 🎯 **ESTRUTURA DE COMMITS**

### **1. Commit: Blockchain Infrastructure**

**Mensagem**: `feat(blockchain): add smart contracts and deployment infrastructure`

**Arquivos**:

- `contracts/SEVEToken.sol`
- `contracts/SEVEProtocol.sol`
- `contracts/SEVEDAO.sol`
- `scripts/deploy-token.js`
- `scripts/deploy-protocol.js`
- `scripts/deploy-dao.js`
- `scripts/deploy-testnet.sh`
- `scripts/deploy-testnet.ps1`
- `hardhat.config.js`
- `.gitignore` (atualizado)

**Descrição**: Adiciona smart contracts completos (Token, Protocol, DAO) e scripts de deploy para testnets e mainnets.

---

### **2. Commit: Deployment Documentation**

**Mensagem**: `docs(deploy): add comprehensive deployment guides and troubleshooting`

**Arquivos**:

- `docs/DEPLOYMENT_SUCCESS.md`
- `docs/GUIA_DEPLOY_TESTNET.md`
- `docs/PASSO_A_PASSO_DEPLOY.md`
- `docs/TROUBLESHOOTING_DEPLOY.md`
- `docs/INSTRUCOES_FAUCET.md`
- `docs/COMO_EXPORTAR_CHAVE_METAMASK.md`
- `docs/DIFERENCA_SRP_VS_PRIVATE_KEY.md`
- `docs/DIFERENCA_ENDERECO_VS_CHAVE.md`
- `docs/VERIFICAR_REDE_METAMASK.md`

**Descrição**: Documentação completa para deploy em testnets e mainnets, incluindo troubleshooting e guias passo a passo.

---

### **3. Commit: Strategic Analysis**

**Mensagem**: `docs(strategy): add strategic analysis and cost evaluation`

**Arquivos**:

- `docs/ANALISE_ESTRATEGICA_DEPLOY.md`
- `docs/ANALISE_CUSTO_MAINNET.md`
- `docs/ESTRATEGIA_SALDO_ATUAL.md`
- `docs/TROUBLESHOOTING_CONVERSAO.md`
- `docs/GUIA_SALDO_METAMASK.md`
- `docs/VIABILIDADE_LICENCIAMENTO_ETICO.md`
- `docs/ESTRATEGIA_DISTRIBUICAO_LICENCIAMENTO.md`

**Descrição**: Análises estratégicas de deploy, custos, viabilidade de licenciamento e estratégias de distribuição.

---

### **4. Commit: Testing Infrastructure**

**Mensagem**: `test(blockchain): add test scripts for deployed contracts`

**Arquivos**:

- `scripts/test-sepolia-contracts.js`
- `scripts/check-balance.js`
- `scripts/check-balance-mainnet.js`
- `test/test_sepolia_contracts.js`
- `test/SEVEToken.test.js` (se modificado)

**Descrição**: Scripts de teste para validar contratos deployados e verificar saldos em diferentes redes.

---

### **5. Commit: Hugging Face Preparation**

**Mensagem**: `feat(distribution): add Hugging Face publication preparation`

**Arquivos**:

- `scripts/prepare_huggingface.py`
- `CHECKLIST_PUBLICACAO_HF.md`
- `docs/GUIA_PUBLICACAO_HUGGING_FACE.md`
- `docs/CUSTO_REAL_HUGGING_FACE.md`
- `model_card.md`

**Descrição**: Preparação para publicação no Hugging Face, incluindo scripts de automação e documentação.

---

### **6. Commit: Strategic Positioning**

**Mensagem**: `docs(strategy): add strategic positioning and foundation roadmap`

**Arquivos**:

- `docs/ESTRATEGIA_FUNDACAO_IA_ETICA.md`
- `docs/ESTRATEGIA_PUBLICACAO_ACADEMICA.md`
- `docs/MANIFESTO_IA_ETICA.md`
- `docs/WHITE_PAPER_EXECUTIVO.md`
- `docs/POSICIONAMENTO_ESTRATEGICO_COMPLETO.md`
- `docs/RESUMO_EXECUTIVO_FUNDACAO.md`
- `docs/INDICE_ESTRATEGIA_COMPLETA.md`
- `docs/PLANO_ACAO_IMEDIATA.md`
- `docs/artigos/` (se houver)

**Descrição**: Estratégia completa de posicionamento como fundação de IA ética, incluindo roadmap e white paper.

---

## 🚀 **EXECUÇÃO DOS COMMITS**

### **Ordem Recomendada:**

1. Blockchain Infrastructure (base)
2. Testing Infrastructure (validação)
3. Deployment Documentation (guia)
4. Strategic Analysis (análise)
5. Strategic Positioning (visão)
6. Hugging Face Preparation (distribuição)

---

## 📝 **FORMATO DE COMMIT**

```text
<tipo>(<escopo>): <descrição curta>

<descrição detalhada (opcional)>

<rodapé (opcional)>
```

**Tipos**:

- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `test`: Testes
- `refactor`: Refatoração
- `chore`: Tarefas de manutenção

**Escopos**:

- `blockchain`: Smart contracts
- `deploy`: Deploy e infraestrutura
- `strategy`: Estratégia e análise
- `distribution`: Distribuição e publicação
- `docs`: Documentação geral

---

## ✅ **CHECKLIST PRÉ-COMMIT**

- [ ] Todos os arquivos testados
- [ ] Documentação atualizada
- [ ] `.gitignore` configurado
- [ ] Sem arquivos sensíveis (`.env`, chaves privadas)
- [ ] Commits organizados por categoria
- [ ] Mensagens de commit claras e descritivas

---

**Última Atualização**: 09 de Novembro de 2025
**Mantido por**: Equipe EON - Symbeon Tech
