# SEVE CLI - Command Line Interface

## 🚀 Instalação

```bash
# Instalar dependências da CLI
pip install click rich

# Tornar executável (Linux/Mac)
chmod +x seve_cli.py

# Criar alias (opcional)
alias seve='python seve_cli.py'
```

## 📖 Comandos Disponíveis

### 1. Inicialização

```bash
# Inicializar com configuração padrão
python seve_cli.py init

# Inicializar com nível ético específico
python seve_cli.py init --ethics-level strict

# Inicializar com adaptador de domínio
python seve_cli.py init --domain healthcare --ethics-level strict
```

### 2. Validação Ética

```bash
# Validar arquivo de transação
python seve_cli.py validate transaction.json

# Validar com saída para arquivo
python seve_cli.py validate data.json --output results.json

# Validação verbose
python seve_cli.py validate data.json --verbose
```

### 3. Análise Profunda

```bash
# Analisar imagem
python seve_cli.py analyze image.jpg --type image

# Analisar com relatório detalhado
python seve_cli.py analyze video.mp4 --type video --report

# Analisar transação
python seve_cli.py analyze transaction.json --type transaction
```

### 4. Monitoramento em Tempo Real

```bash
# Monitorar fonte de dados
python seve_cli.py monitor --source camera_feed_1

# Monitorar com intervalo customizado
python seve_cli.py monitor --source api_endpoint --interval 10
```

### 5. Auditoria

```bash
# Ver audit trail dos últimos 7 dias
python seve_cli.py audit

# Ver audit trail dos últimos 30 dias
python seve_cli.py audit --days 30

# Exportar audit log
python seve_cli.py audit --days 90 --export audit_log.json
```

### 6. Configuração

```bash
# Ver configuração atual
python seve_cli.py config show

# Alterar configuração
python seve_cli.py config set ethics_level STRICT
python seve_cli.py config set privacy_mode MAXIMUM
```

### 7. Status do Sistema

```bash
# Ver status de todos os módulos
python seve_cli.py status
```

## 🎨 Exemplos de Uso

### Fluxo Completo de Validação

```bash
# 1. Inicializar para domínio de saúde
python seve_cli.py init --domain healthcare --ethics-level strict

# 2. Validar dados médicos
python seve_cli.py validate patient_data.json --output validation_result.json

# 3. Analisar imagens médicas
python seve_cli.py analyze xray.jpg --type image --report

# 4. Ver audit trail
python seve_cli.py audit --days 1
```

### Monitoramento de Varejo

```bash
# 1. Inicializar para varejo
python seve_cli.py init --domain retail --ethics-level balanced

# 2. Monitorar câmeras da loja
python seve_cli.py monitor --source store_camera_1 --interval 5

# 3. Ver status
python seve_cli.py status
```

## 🛠️ Recursos Avançados

### Integração com Scripts

```python
import subprocess
import json

# Validar via CLI
result = subprocess.run(
    ['python', 'seve_cli.py', 'validate', 'data.json', '--output', 'result.json'],
    capture_output=True
)

# Ler resultado
with open('result.json') as f:
    validation = json.load(f)
```

### Pipeline CI/CD

```yaml
# .github/workflows/ethical-validation.yml
name: Ethical Validation

on: [push]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install SEVE
        run: pip install -r requirements.txt
      - name: Run Ethical Validation
        run: python seve_cli.py validate data/transactions.json
```

## 📊 Output Formats

A CLI usa **Rich** para output colorido e formatado:

- ✅ **Tabelas**: Resultados estruturados
- 🎨 **Cores**: Status visual (verde=ok, vermelho=erro, amarelo=aviso)
- 📊 **Progress bars**: Feedback de progresso
- 🎭 **Panels**: Destaque de informações importantes
- 📝 **Syntax highlighting**: JSON e código

## 🔧 Troubleshooting

### CLI não encontrada

```bash
# Verificar se está no PATH
which python
python --version

# Executar diretamente
python /caminho/completo/seve_cli.py --help
```

### Dependências faltando

```bash
pip install click rich
```

### Permissões (Linux/Mac)

```bash
chmod +x seve_cli.py
```

---

**Desenvolvido pela Equipe EON - Symbeon Tech**  
**SEVE Framework v1.0.0-beta**
