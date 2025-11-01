# FAQ - Perguntas Frequentes - SEVE Framework

**SEVE Framework v1.0.0**  
**Última Atualização**: 2025-01-29

---

## 📋 **Índice**

- [Instalação e Configuração](#instalação-e-configuração)
- [Licenciamento](#licenciamento)
- [Blockchain e Smart Contracts](#blockchain-e-smart-contracts)
- [Ética e Privacidade](#ética-e-privacidade)
- [Performance e Escalabilidade](#performance-e-escalabilidade)
- [Integração](#integração)
- [Desenvolvimento e Contribuição](#desenvolvimento-e-contribuição)

---

## Instalação e Configuração

### Como instalo o SEVE Framework?

**Resposta**: O SEVE Framework pode ser instalado de duas formas:

**1. Instalação via pip (recomendado para uso):**
```bash
pip install -e .
```

**2. Instalação via script automatizado:**
```bash
python install.py
```

**Pré-requisitos:**
- Python 3.8 ou superior (recomendado 3.11+)
- Node.js 16+ e npm (para smart contracts)
- 4GB+ de RAM recomendado
- GPU opcional (para aceleração de visão computacional)

**Verificar instalação:**
```bash
python -c "from seve_framework import SEVECoreV3; print('✅ SEVE instalado corretamente')"
```

Veja [README.md](../README.md#-quick-start) para mais detalhes.

---

### Qual versão do Python é necessária?

**Resposta**: SEVE Framework requer **Python 3.8 ou superior**. Versões recomendadas:
- **Python 3.11+**: Recomendado para melhor performance
- **Python 3.10**: Totalmente suportado
- **Python 3.9**: Suportado
- **Python 3.8**: Suportado (compatibilidade mínima)

**Verificar versão:**
```bash
python --version
```

---

### Erro ao instalar dependências Python

**Problema comum**: Dependências não instalam ou conflitos de versão.

**Soluções**:

1. **Atualizar pip:**
```bash
pip install --upgrade pip setuptools wheel
```

2. **Instalar em ambiente virtual (recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -e .
```

3. **Problemas com OpenCV:**
```bash
# Windows
pip install opencv-python-headless

# Linux
sudo apt-get install python3-opencv

# Mac
brew install opencv-python
```

4. **Problemas com PyTorch (GPU):**
```bash
# CPU apenas
pip install torch torchvision

# GPU (CUDA 11.x)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

Veja [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) para mais problemas de instalação.

---

### Como configuro as variáveis de ambiente?

**Resposta**: O SEVE Framework usa um arquivo `.env` para configuração. Siga estes passos:

1. **Criar arquivo .env:**
```bash
cp .env.example .env
```

2. **Configurar variáveis principais:**
```env
# Blockchain (para smart contracts)
ALCHEMY_URL=https://eth-sepolia.g.alchemy.com/v2/YOUR_API_KEY
PRIVATE_KEY=your_private_key_here
ETHERSCAN_API_KEY=your_etherscan_key

# Framework
SEVE_MODE=universal
SEVE_ETHICS_LEVEL=strict
SEVE_LOG_LEVEL=INFO
```

3. **Validar configuração:**
```bash
# Script de validação
node scripts/validate-env.js
```

**⚠️ IMPORTANTE**: Nunca commite o arquivo `.env` no Git!

Veja [ENV_SETUP.md](./ENV_SETUP.md) para configuração completa.

---

### O SEVE requer GPU?

**Resposta**: Não obrigatório, mas recomendado para melhor performance.

**Sem GPU**:
- ✅ Todas as funcionalidades funcionam
- ✅ Processamento em CPU (pode ser mais lento)
- ✅ Adequado para desenvolvimento e testes

**Com GPU (CUDA)**:
- ✅ Processamento 10-50x mais rápido
- ✅ Necessário para aplicações em produção com alto volume
- ✅ Requer NVIDIA GPU com CUDA 11.x+

**Instalar suporte GPU (opcional):**
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

---

## Licenciamento

### Qual é a licença do SEVE Framework?

**Resposta**: O SEVE Framework usa a licença **Symbeon-Vault**, uma licença proprietária ética que:

- ✅ Permite uso comercial com licença apropriada
- ✅ Requer atribuição e manutenção de notificação de licença
- ✅ Proíbe redistribuição não autorizada
- ✅ Permite uso acadêmico e de pesquisa com atribuição

**Ver licença completa**: [LICENSE_Symbeon_Vault.md](../LICENSE_Symbeon_Vault.md)

---

### Posso usar SEVE em projetos comerciais?

**Resposta**: Sim, mas requer licenciamento apropriado conforme a licença Symbeon-Vault.

**Para uso comercial:**
- Entre em contato para obter licença comercial: `research@symbeon-tech.com`
- Consulte [MODULE_CLASSIFICATION_BY_NICHE.md](./MODULE_CLASSIFICATION_BY_NICHE.md) para licenciamento por nicho
- Licenças disponíveis por vertical (Retail, Healthcare, Smart City, etc.)

**Para uso acadêmico/pesquisa:**
- Uso permitido com atribuição adequada
- Consulte política de licença para detalhes específicos

---

### Posso modificar o código-fonte?

**Resposta**: A licença Symbeon-Vault permite modificação para uso interno, mas:

- ⚠️ Modificações não podem ser redistribuídas sem autorização
- ✅ Modificações internas são permitidas
- ✅ Contribuições são bem-vindas via pull requests
- ⚠️ Fork público requer acordo de licenciamento

Veja [CONTRIBUTING.md](../CONTRIBUTING.md) para contribuições.

---

## Blockchain e Smart Contracts

### Em quais redes blockchain o SEVE pode ser deployado?

**Resposta**: SEVE suporta múltiplas redes EVM-compatíveis:

**Testnets (Gratuitas)**:
- ✅ **Sepolia** (Ethereum testnet) - Recomendado
- ✅ **Mumbai** (Polygon testnet)
- ✅ **BSC Testnet** (Binance Smart Chain testnet)
- ✅ **Arbitrum Goerli** (Arbitrum testnet)

**Mainnets (Produção)**:
- ✅ **Ethereum** - Custo alto de gas, máxima segurança
- ✅ **Polygon** - Baixo custo, recomendado para produção
- ✅ **Arbitrum** - Custo baixo, alta performance
- ✅ **BSC** - Custo baixo, alternativa para produção

**Como escolher**:
- **Desenvolvimento**: Sepolia (testnet gratuita)
- **Produção com baixo custo**: Polygon
- **Produção com máxima segurança**: Ethereum
- **Produção com performance**: Arbitrum

Veja [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) e [RPC_PROVIDERS.md](./RPC_PROVIDERS.md) para mais informações.

---

### Quanto custa fazer deploy dos smart contracts?

**Resposta**: O custo varia por rede:

**Testnets**: **Gratuito** (fundos via faucets)

**Mainnets (estimativas)**:
- **Ethereum**: $50-200 USD (gas alto)
- **Polygon**: $0.01-0.10 USD (custo muito baixo)
- **Arbitrum**: $0.50-2.00 USD (custo baixo)
- **BSC**: $0.10-0.50 USD (custo baixo)

**Recomendação**: Use Polygon para produção (melhor custo-benefício).

Veja [COST_ANALYSIS.md](../COST_ANALYSIS.md) para análise detalhada.

---

### Como obtenho fundos de teste (testnet)?

**Resposta**: Use faucets para obter tokens de teste gratuitos:

**Sepolia (Ethereum testnet)**:
- Alchemy Faucet: https://sepoliafaucet.com/
- Chainlink Faucet: https://faucets.chain.link/sepolia

**Mumbai (Polygon testnet)**:
- Polygon Faucet: https://faucet.polygon.technology/

**BSC Testnet**:
- BSC Faucet: https://testnet.bnbchain.org/faucet-smart

Veja [TESTNET_PLAYBOOK.md](./TESTNET_PLAYBOOK.md) para guia completo de faucets.

---

### Preciso de API key para blockchain?

**Resposta**: Depende da rede que você quer usar:

**RPCs Públicos (Gratuitos, mas limitados)**:
- ✅ Sepolia: `https://rpc.sepolia.org` (sem API key)
- ⚠️ Limitado a ~100 requisições/minuto
- ⚠️ Pode ter instabilidade

**RPCs Pagos (Recomendados para produção)**:
- ✅ **Alchemy** (Recomendado): https://www.alchemy.com/
- ✅ **Infura**: https://www.infura.io/
- ✅ API keys gratuitas com limites generosos
- ✅ Alta disponibilidade e performance

**Configuração no `.env`:**
```env
ALCHEMY_URL=https://eth-sepolia.g.alchemy.com/v2/YOUR_API_KEY
```

Veja [RPC_PROVIDERS.md](./RPC_PROVIDERS.md) para comparação completa.

---

## Ética e Privacidade

### O SEVE usa reconhecimento facial?

**Resposta**: **Não**. Esta é uma decisão ética fundamental do framework.

**SEVE-Vision NÃO faz reconhecimento facial**, mesmo tendo capacidade técnica. Em vez disso:

- ✅ **Detecta faces** apenas para **anonimização automática**
- ✅ **Foca em eventos** (produtos, comportamentos) não em pessoas
- ✅ **Protege privacidade** desde o design (Privacy by Design)
- ✅ **Observa padrões**, não identidades individuais

**Por quê?**
- Reconhecimento facial é invasivo e discriminatório
- "Watch, not judge" - observar sem julgar identidades
- Privacidade é direito fundamental, não opcional

Veja [WHY_I_CREATED_SEVE.md](./WHY_I_CREATED_SEVE.md#1-vigilância-ética-não-invasiva) para mais detalhes.

---

### Como o SEVE protege privacidade dos dados?

**Resposta**: SEVE implementa múltiplas camadas de proteção:

**1. Anonimização Automática (SEVE-Vision)**:
- Faces detectadas são automaticamente borradas/pixelizadas
- Dados pessoais são mascarados antes de processamento

**2. Pseudonimização (SEVE-Ethics)**:
- Identificadores são substituídos por pseudônimos
- Mapeamento reversível apenas quando necessário e autorizado

**3. Data Minimization (SEVE-Core)**:
- Coleta apenas dados estritamente necessários
- Retenção de dados com políticas claras

**4. Compliance Automático (SEVE-Ethics)**:
- Validação LGPD/GDPR em tempo real
- Consentimento granular

**5. Audit Trail Completo**:
- Todas as operações são registradas
- Transparência total sobre uso de dados

Veja [SEVE_COMPLETE_WHITEPAPER.md](./SEVE_COMPLETE_WHITEPAPER.md) para detalhes técnicos.

---

### O SEVE é GDPR/LGPD compliant?

**Resposta**: **Sim**, o SEVE foi projetado desde o início para compliance automático.

**LGPD (Brasil)**:
- ✅ Consentimento explícito validado
- ✅ Direitos do titular implementados (acesso, exclusão, portabilidade)
- ✅ Anonimização automática de dados
- ✅ Auditoria completa

**GDPR (Europa)**:
- ✅ Data Protection by Design and by Default
- ✅ Privacy Impact Assessment (DPIA) automático
- ✅ Right to be Forgotten implementado
- ✅ Transparência e accountability

**Como funciona**:
- SEVE-Ethics valida todas as operações contra princípios LGPD/GDPR
- Compliance é consequência do design, não add-on

Veja [RESEARCH_BASE_SEVE_INTEGRATION.md](./RESEARCH_BASE_SEVE_INTEGRATION.md#71-lgpd-lei-geral-de-proteção-de-dados) para detalhes técnicos.

---

## Performance e Escalabilidade

### Quão rápido é o SEVE Framework?

**Resposta**: Performance depende do hardware e módulos utilizados.

**Processamento de Imagem (SEVE-Vision)**:
- **CPU**: 100-500ms por imagem (dependendo do tamanho)
- **GPU (CUDA)**: 10-50ms por imagem (10-50x mais rápido)
- **Batch Processing**: Até 100 imagens/segundo com GPU

**Inferência de Modelos**:
- **Latência**: 50-200ms por decisão
- **Throughput**: 100-1000 requisições/segundo (dependendo da configuração)

**Smart Contracts**:
- **Gas Cost**: ~50,000-200,000 gas por operação (dependendo da rede)
- **Confirmação**: 1-2 minutos (Ethereum), <5 segundos (Polygon)

**Benchmarks completos**: Em desenvolvimento - veja [TASKMASH_SUPERSCOPE.md](./TASKMASH_SUPERSCOPE.md)

---

### O SEVE escala para produção?

**Resposta**: **Sim**, a arquitetura modular do SEVE é projetada para escalabilidade:

**Escalabilidade Horizontal**:
- Módulos independentes podem ser distribuídos
- Load balancing entre instâncias
- Stateless design permite múltiplas réplicas

**Escalabilidade Vertical**:
- Processamento paralelo assíncrono
- Cache distribuído (Redis)
- Otimização de recursos

**Limitações atuais**:
- ⚠️ Benchmarks em desenvolvimento
- ⚠️ Testes de carga pendentes
- ✅ Arquitetura permite escalabilidade

**Recomendações para produção**:
- Use GPU para visão computacional
- Configure Redis para cache
- Use múltiplas instâncias para alta carga
- Monitore performance com SEVE-Monitoring

---

### Quantos recursos (CPU, memória) o SEVE consome?

**Resposta**: Depende da configuração e uso:

**Configuração Mínima**:
- **CPU**: 2 cores
- **RAM**: 4GB
- **Disco**: 2GB (sem modelos grandes)
- **Uso**: Desenvolvimento e testes

**Configuração Recomendada (Produção)**:
- **CPU**: 4+ cores (ou GPU NVIDIA)
- **RAM**: 8GB+
- **Disco**: 10GB+ (com modelos pré-treinados)
- **GPU**: Opcional, mas recomendado

**Módulos individuais**:
- **SEVE-Core**: ~200MB RAM
- **SEVE-Vision**: ~500MB RAM (CPU) ou ~2GB VRAM (GPU)
- **SEVE-Ethics**: ~100MB RAM
- **SEVE-Sense**: ~150MB RAM

**Otimizações**:
- Modelos podem ser carregados sob demanda
- Cache reduz uso de memória
- Async processing otimiza CPU

---

## Integração

### Como integro SEVE em minha aplicação Python existente?

**Resposta**: SEVE foi projetado para fácil integração:

**Instalação básica:**
```python
from seve_framework import SEVECoreV3, SEVEConfig
from seve_framework.vision import SEVEVisionModule

# Criar configuração
config = SEVEConfig()

# Inicializar framework
seve = SEVECoreV3(config)
await seve.initialize()

# Usar módulos
vision_result = await seve.vision_module.process_visual_input(image_data)
```

**Integração com FastAPI:**
```python
from fastapi import FastAPI
from seve_framework import SEVECoreV3

app = FastAPI()
seve = SEVECoreV3()

@app.post("/process")
async def process_image(data: dict):
    result = await seve.process_context(data)
    return result
```

Veja [INTEGRATION_GUIDE.md](./integration/INTEGRATION_GUIDE.md) para exemplos completos.

---

### Posso usar apenas módulos específicos do SEVE?

**Resposta**: **Sim**, os módulos são independentes e podem ser usados separadamente:

**Módulos disponíveis**:
- `SEVEVisionModule` - Visão computacional ética
- `SEVESenseModule` - Processamento multimodal
- `SEVEEthicsModule` - Validação ética
- `SEVELinkModule` - Conectividade externa
- `SEVECoreV3` - Orquestração completa

**Exemplo - usar apenas Vision:**
```python
from seve_framework.vision import SEVEVisionModule
from seve_framework.config import SEVEConfig

config = SEVEConfig()
vision = SEVEVisionModule(config)
await vision.initialize()

result = await vision.process_visual_input(image_data)
```

**Observação**: Alguns módulos dependem de SEVE-Core para funcionalidades avançadas.

---

### Como integro SEVE com sistemas ERP?

**Resposta**: SEVE-Link fornece integração com sistemas externos:

**Opções de integração**:
1. **API REST** (via SEVE-Link)
2. **Webhooks** (eventos em tempo real)
3. **Message Queue** (MQTT, RabbitMQ)
4. **Database Direct** (SQL, NoSQL)

**Exemplo básico:**
```python
from seve_framework.link import SEVELinkModule

link = SEVELinkModule(config)
await link.connect_external_system(
    system_type="erp",
    endpoint="https://erp.example.com/api",
    auth={"token": "..."}
)
```

Veja [INTEGRATION_GUIDE.md](./integration/INTEGRATION_GUIDE.md) para exemplos completos de ERP.

---

### Como integro smart contracts SEVE em DeFi?

**Resposta**: Os smart contracts SEVE são ERC-20 padrão e podem ser integrados como qualquer token:

**SEVEToken é compatível com**:
- ✅ Uniswap, SushiSwap (DEXs)
- ✅ Aave, Compound (Lending)
- ✅ Staking protocols
- ✅ Qualquer protocolo DeFi que aceita ERC-20

**Exemplo de integração:**
```solidity
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract MyDeFiProtocol {
    IERC20 seveToken = IERC20(0x...); // Endereço do SEVEToken
    
    function stakeSEVE(uint256 amount) external {
        seveToken.transferFrom(msg.sender, address(this), amount);
        // Sua lógica de staking
    }
}
```

Veja contratos em `contracts/` para referência completa.

---

## Desenvolvimento e Contribuição

### Como contribuo para o SEVE Framework?

**Resposta**: Contribuições são bem-vindas! Siga estes passos:

1. **Fork o repositório** no GitHub
2. **Crie uma branch** para sua feature/fix
3. **Siga os padrões** de código (veja [CONTRIBUTING.md](../CONTRIBUTING.md))
4. **Escreva testes** para novas funcionalidades
5. **Abra um Pull Request**

**Padrões importantes**:
- Código Python: PEP 8
- Código Solidity: Style Guide Solidity
- Testes: Cobertura mínima 80%
- Documentação: Atualize docs relacionados

Veja [CONTRIBUTING.md](../CONTRIBUTING.md) para guia completo.

---

### Como executo os testes?

**Resposta**: SEVE usa pytest para testes Python e Hardhat para testes de smart contracts:

**Testes Python:**
```bash
# Todos os testes
pytest tests/

# Testes específicos
pytest tests/test_vision.py
pytest tests/test_ethics.py

# Com cobertura
pytest tests/ --cov=src/seve_framework --cov-report=html
```

**Testes Smart Contracts:**
```bash
# Compilar contratos
npm run compile

# Executar testes
npm run test

# Teste específico
npx hardhat test test/SEVEToken.test.js
```

**Pré-requisito**: Instale o framework primeiro:
```bash
pip install -e .
```

---

### Onde encontro exemplos de código?

**Resposta**: Exemplos estão disponíveis em múltiplos lugares:

**1. Diretório examples/:**
```bash
python examples/basic_usage.py
python examples/quickstart.py
```

**2. Documentação técnica:**
- [user-guides/tutorials/](./user-guides/tutorials/)
- [README.md](../README.md#-quick-start)

**3. Documentação de módulos:**
- Cada módulo tem exemplos na documentação técnica
- Veja `docs/technical/architecture/`

---

### Qual é a política de versionamento?

**Resposta**: SEVE segue [Semantic Versioning](https://semver.org/) (SemVer):

**Formato**: `MAJOR.MINOR.PATCH`

- **MAJOR**: Mudanças incompatíveis de API
- **MINOR**: Novas funcionalidades compatíveis
- **PATCH**: Correções de bugs compatíveis

**Versão atual**: `1.0.0` (Production Ready)

**Roadmap**:
- **v1.1**: Melhorias incrementais (Q2 2025)
- **v1.2**: Expansão de capacidades (Q3 2025)
- **v2.0**: Mudanças arquiteturais maiores (Q4 2025)

Veja [CHANGELOG.md](../CHANGELOG.md) para histórico completo.

---

## 📞 **Não Encontrou Sua Pergunta?**

Se você não encontrou a resposta que procurava:

- 📚 **Documentação Completa**: [Índice de Documentação](./INDEX.md)
- 🐛 **Reportar Bug**: [GitHub Issues](https://github.com/symbeon/seve-framework/issues)
- 💬 **Comunidade**: [Discord/Telegram](https://community.seve-framework.ai)
- 📧 **Contato Direto**: research@symbeon-tech.com

---

**Última Atualização**: 2025-01-29  
**Mantido por**: Equipe EON - Symbeon Tech
