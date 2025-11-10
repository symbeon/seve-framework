# Guia de Geração de Figuras para Patentes

## 📋 REQUISITOS INPI

- **Formato**: PDF
- **Resolução**: Mínimo 300 DPI
- **Tamanho**: A4 (210 x 297 mm)
- **Margens**: Mínimo 2,5 cm
- **Legendas**: Em português, abaixo de cada figura
- **Numeração**: Figuras 1, 2, 3, 4...

---

## 🎨 FERRAMENTAS RECOMENDADAS

### 1. **Mermaid → SVG → PDF**
```bash
# Instalar Mermaid CLI
npm install -g @mermaid-js/mermaid-cli

# Gerar SVG
mmdc -i diagrama.mmd -o diagrama.svg

# Converter SVG para PDF (alta resolução)
inkscape diagrama.svg --export-pdf=diagrama.pdf --export-dpi=300
```

### 2. **Draw.io / Lucidchart**
- Exportar como PDF (300 DPI)
- Verificar margens (mínimo 2,5 cm)

### 3. **LaTeX + TikZ**
- Gerar PDF diretamente
- Controle total sobre formatação

---

## 📐 FIGURAS NECESSÁRIAS

### **Patente 1: Validação Ética**

#### Figura 1: Arquitetura Geral
- Diagrama de blocos do sistema
- Componentes principais
- Fluxo de dados

#### Figura 2: Fluxograma de Validação
- Processo de validação ética
- Pontos de interceptação
- Decisão aprovação/bloqueio

#### Figura 3: Integração Blockchain
- Smart contract structure
- Processo de registro
- Hash on-chain / evidência off-chain

#### Figura 4: Compliance Regulatório
- Mapeamento regulatório
- Geração de evidências
- Cobertura automatizada

---

### **Patente 2: Empathy Engine**

#### Figura 1: Arquitetura do UEE
- Componentes principais
- Fluxo de processamento
- Integrações

#### Figura 2: Processamento Multimodal
- Text, Speech, Vision processing
- Fusão de emoções
- Estado emocional final

#### Figura 3: Adaptação Cultural ELSI
- Mapeamento ELSI
- Preferências de comunicação
- Adaptação de templates

#### Figura 4: Validação Ética
- Loop de validação
- Detecção de manipulação
- Geração alternativa

---

## 🔧 COMANDOS ÚTEIS

### Converter Mermaid para PDF

```bash
# 1. Criar arquivo .mmd
cat > figura1.mmd << 'EOF'
graph TB
    A[Input Data] --> B[Context Building]
    B --> C[Rule Resolution]
    C --> D[Rule Evaluation]
    D --> E{Approved?}
    E -->|Yes| F[Output]
    E -->|No| G[Block & Audit]
EOF

# 2. Gerar SVG
mmdc -i figura1.mmd -o figura1.svg -w 2000 -H 1500

# 3. Converter para PDF (300 DPI)
inkscape figura1.svg --export-pdf=figura1.pdf --export-dpi=300
```

---

## ✅ CHECKLIST DE VALIDAÇÃO

- [ ] Resolução: 300 DPI ou superior
- [ ] Tamanho: A4 (210 x 297 mm)
- [ ] Margens: Mínimo 2,5 cm
- [ ] Legenda: Em português, abaixo da figura
- [ ] Numeração: Figura 1, 2, 3, 4...
- [ ] Clareza: Técnica e clara, não apenas ilustrativa
- [ ] Reprodução: Permite reprodução por técnico no assunto

---

**Última Atualização**: 09 de Novembro de 2025

