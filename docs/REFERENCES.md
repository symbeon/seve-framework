# Referências e Créditos - SEVE Framework

**SEVE Framework v1.0.0**  
**Equipe EON - Symbeon Tech**

---

## 📚 Referências Metodológicas e Conceituais

### Framework SiD (Symbiosis in Development)

**Fonte Principal de Inspiração Metodológica**

- **Organização**: Except Integrated Sustainability
- **Website**: https://except.nl/en/consultancy/methodology/sid
- **Licença**: Creative Commons BY-SA-NC
- **Descrição**: Framework de desenvolvimento sistêmico para sustentabilidade usado desde 1999 em centenas de projetos globais
- **Contribuição ao SEVE**: Base conceitual holística, estrutura ELSI (Energy & Materials, Life, Society, Individual), metodologia de sustentabilidade sistêmica

**Documentação da Integração**: [SiD ↔ SEVE Integration](./SID_SEVE_INTEGRATION.md)

---

## 🔗 Bibliotecas e Frameworks de Software

### Blockchain e Smart Contracts

#### OpenZeppelin Contracts
- **Licença**: MIT License
- **Website**: https://www.openzeppelin.com/contracts
- **Versão**: ^4.9.0
- **Contribuição ao SEVE**:
  - `ERC20.sol` - Implementação do padrão ERC-20 para SEVEToken
  - `Ownable.sol` - Controle de propriedade de contratos
  - `ReentrancyGuard.sol` - Proteção contra reentrância
  - `Pausable.sol` - Funcionalidade de pausa de contratos
- **Uso**: Todos os smart contracts do SEVE (SEVEToken, SEVEProtocol, SEVEDAO)

#### Hardhat
- **Licença**: MIT License
- **Website**: https://hardhat.org/
- **Versão**: ^2.17.0
- **Contribuição ao SEVE**: Framework de desenvolvimento, compilação, testes e deploy de smart contracts

#### @nomicfoundation/hardhat-toolbox
- **Licença**: MIT License
- **Website**: https://hardhat.org/hardhat-runner/docs/getting-started
- **Versão**: ^4.0.0
- **Contribuição ao SEVE**: Ferramentas para desenvolvimento Ethereum (testes, deploy, verificação)

---

### Deep Learning e Machine Learning

#### PyTorch
- **Licença**: BSD License
- **Website**: https://pytorch.org/
- **Versão**: >= 1.9.0
- **Contribuição ao SEVE**: Framework de deep learning para modelos de visão computacional e processamento multimodal

#### TorchVision
- **Licença**: BSD License
- **Website**: https://pytorch.org/vision/
- **Versão**: >= 0.10.0
- **Contribuição ao SEVE**: Transformações de imagem, modelos pré-treinados, datasets para visão computacional

#### Hugging Face Transformers
- **Licença**: Apache 2.0 License
- **Website**: https://huggingface.co/transformers
- **Versão**: >= 4.20.0
- **Contribuição ao SEVE**: Modelos de NLP, processamento de texto, análise semântica

#### scikit-learn
- **Licença**: BSD License
- **Website**: https://scikit-learn.org/
- **Versão**: >= 1.0.0
- **Contribuição ao SEVE**: Algoritmos de machine learning, pré-processamento de dados, métricas de avaliação

---

### Computer Vision

#### OpenCV (opencv-python)
- **Licença**: Apache 2.0 License
- **Website**: https://opencv.org/
- **Versão**: >= 4.5.0
- **Contribuição ao SEVE**: Processamento de imagens, detecção de objetos, filtros, transformações, anonimização de faces

#### Pillow (PIL)
- **Licença**: PIL License (HPND)
- **Website**: https://pillow.readthedocs.io/
- **Versão**: >= 8.3.0
- **Contribuição ao SEVE**: Manipulação de imagens, conversão de formatos, processamento de pixels

---

### Web Framework e APIs

#### FastAPI
- **Licença**: MIT License
- **Website**: https://fastapi.tiangolo.com/
- **Versão**: >= 0.68.0
- **Contribuição ao SEVE**: Framework web assíncrono para APIs REST, validação de dados, documentação automática

#### Uvicorn
- **Licença**: BSD License
- **Website**: https://www.uvicorn.org/
- **Versão**: >= 0.15.0
- **Contribuição ao SEVE**: Servidor ASGI para aplicações assíncronas

#### Pydantic
- **Licença**: MIT License
- **Website**: https://pydantic-docs.helpmanual.io/
- **Versão**: >= 1.8.0
- **Contribuição ao SEVE**: Validação de dados, serialização, modelos de dados tipados

---

### Data Science e Processamento

#### NumPy
- **Licença**: BSD License
- **Website**: https://numpy.org/
- **Versão**: >= 1.21.0
- **Contribuição ao SEVE**: Computação numérica, arrays multidimensionais, operações matemáticas

#### Pandas
- **Licença**: BSD License
- **Website**: https://pandas.pydata.org/
- **Versão**: >= 1.3.0
- **Contribuição ao SEVE**: Manipulação e análise de dados estruturados, DataFrames

---

### Segurança e Criptografia

#### cryptography
- **Licença**: Apache 2.0 / BSD License
- **Website**: https://cryptography.io/
- **Versão**: >= 3.4.0
- **Contribuição ao SEVE**: Criptografia, hashing, geração de chaves, proteção de dados

---

### Banco de Dados e Cache

#### Redis
- **Licença**: BSD License
- **Website**: https://redis.io/
- **Versão**: >= 4.0.0
- **Contribuição ao SEVE**: Cache distribuído, armazenamento de sessões, filas de mensagens

#### SQLAlchemy
- **Licença**: MIT License
- **Website**: https://www.sqlalchemy.org/
- **Versão**: >= 1.4.0
- **Contribuição ao SEVE**: ORM para Python, abstração de banco de dados

#### Alembic
- **Licença**: MIT License
- **Website**: https://alembic.sqlalchemy.org/
- **Versão**: >= 1.7.0
- **Contribuição ao SEVE**: Migrações de banco de dados, controle de versão de esquemas

---

### Comunicação e Mensageria

#### httpx
- **Licença**: BSD License
- **Website**: https://www.python-httpx.org/
- **Versão**: >= 0.24.0
- **Contribuição ao SEVE**: Cliente HTTP assíncrono, integração com APIs externas

#### asyncio-mqtt
- **Licença**: MIT License
- **Website**: https://sabuhish.github.io/asyncio-mqtt/
- **Versão**: >= 0.11.0
- **Contribuição ao SEVE**: Comunicação MQTT assíncrona para IoT

---

### Utilidades e Configuração

#### PyYAML
- **Licença**: MIT License
- **Website**: https://pyyaml.org/
- **Versão**: >= 6.0
- **Contribuição ao SEVE**: Parsing de arquivos YAML, configuração

#### Loguru
- **Licença**: MIT License
- **Website**: https://github.com/Delgan/loguru
- **Versão**: >= 0.6.0
- **Contribuição ao SEVE**: Sistema de logging estruturado e simplificado

#### aiofiles
- **Licença**: Apache 2.0 License
- **Website**: https://github.com/Tinche/aiofiles
- **Versão**: >= 0.7.0
- **Contribuição ao SEVE**: Operações assíncronas de arquivo

---

### Blockchain Infrastructure

#### Alchemy
- **Serviço**: Blockchain Developer Platform
- **Website**: https://www.alchemy.com/
- **Contribuição ao SEVE**: RPC endpoints para Ethereum, Polygon, Arbitrum e outras redes blockchain
- **Uso**: Acesso a redes blockchain para deploy e interação com smart contracts

---

## 📋 Padrões e Especificações Técnicas

### Padrões Ethereum

#### ERC-20 (Ethereum Request for Comments 20)
- **Título**: Token Standard
- **Website**: https://eips.ethereum.org/EIPS/eip-20
- **Contribuição ao SEVE**: Padrão implementado pelo SEVEToken para interoperabilidade com exchanges e carteiras

### Padrões de Privacidade e Segurança

#### Privacy by Design
- **Criador**: Dr. Ann Cavoukian (Information and Privacy Commissioner of Ontario, Canadá)
- **Conceito**: Integrar privacidade no design de sistemas desde o início
- **Contribuição ao SEVE**: Princípio fundamental da arquitetura, especialmente em SEVE-Vision e SEVE-Ethics
- **Referência**: https://www.ipc.on.ca/privacy-by-design/

---

## 🏛️ Regulamentações e Compliance

### LGPD (Lei Geral de Proteção de Dados)
- **Jurisdição**: Brasil
- **Lei**: Lei nº 13.709/2018
- **Website**: https://www.gov.br/cidadania/pt-br/acesso-a-informacao/lgpd
- **Contribuição ao SEVE**: Conformidade obrigatória para operação no Brasil, implementada em SEVE-Ethics

### GDPR (General Data Protection Regulation)
- **Jurisdição**: União Europeia
- **Regulamento**: (EU) 2016/679
- **Website**: https://gdpr.eu/
- **Contribuição ao SEVE**: Conformidade obrigatória para operação na UE, implementada em SEVE-Ethics

### AI Act (Artificial Intelligence Act)
- **Jurisdição**: União Europeia
- **Status**: Proposta de regulamento
- **Contribuição ao SEVE**: Framework de conformidade para IA de alto risco, referência para SEVE-Ethics

---

## 📊 Padrões e Framework de Sustentabilidade

### ESG (Environmental, Social, and Governance)
- **Natureza**: Framework de avaliação de sustentabilidade corporativa
- **Dimensões**:
  - **Environmental (E)**: Impacto ambiental
  - **Social (S)**: Impacto social
  - **Governance (G)**: Governança corporativa
- **Contribuição ao SEVE**: Métricas de avaliação implementadas em SEVE-Core, alinhadas com estrutura ELSI do SiD

---

## 🎓 Conceitos e Princípios Fundamentais

### Symbiosis in Development (SiD)
- **Tipo**: Framework metodológico de sustentabilidade sistêmica
- **Organização**: Except Integrated Sustainability
- **Contribuição ao SEVE**: Base conceitual holística, estrutura ELSI, metodologia de sustentabilidade
- **Documentação**: [Integração SiD ↔ SEVE](./SID_SEVE_INTEGRATION.md)

### ELSI Framework (Energy & Materials, Life, Society, Individual)
- **Origem**: SiD Framework
- **Contribuição ao SEVE**: Matriz de correlação estrutural entre módulos SEVE e camadas de impacto ELSI
- **Mapeamento**:
  - **Energy & Materials (E)** ↔ SEVE-Vision + SEVE-Sense
  - **Life (L)** ↔ SEVE-Link
  - **Society (S)** ↔ SEVE-Ethics
  - **Individual (I)** ↔ SEVE-Core

---

## 🔒 Licenças e Atribuições

### Licenças de Bibliotecas Utilizadas

Todas as bibliotecas listadas acima são de código aberto e utilizadas de acordo com suas respectivas licenças (MIT, BSD, Apache 2.0, etc.).

### Licença do SEVE Framework

- **Licença**: Symbeon-Vault (Proprietária)
- **Documento**: [LICENSE_Symbeon_Vault.md](../LICENSE_Symbeon_Vault.md)

---

## 📝 Notas de Atribuição

### Créditos por Categoria

**Frameworks Metodológicos:**
- SiD Framework (Except Integrated Sustainability)

**Bibliotecas de Smart Contracts:**
- OpenZeppelin Contracts (OpenZeppelin)

**Frameworks de Blockchain:**
- Hardhat (Nomic Foundation)

**Bibliotecas de IA/ML:**
- PyTorch, TorchVision (Facebook AI Research)
- Hugging Face Transformers (Hugging Face)
- scikit-learn (scikit-learn developers)

**Computer Vision:**
- OpenCV (Intel, Willow Garage, Itseez)
- Pillow (Python Imaging Library contributors)

**Web Frameworks:**
- FastAPI (Sebastian Ramirez)
- Uvicorn (Encode)

**Data Science:**
- NumPy (NumPy developers)
- Pandas (Pandas developers)

**Blockchain Infrastructure:**
- Alchemy (Alchemy Inc.)

---

## 🌐 Links Úteis

- **SiD Framework**: https://except.nl/en/consultancy/methodology/sid
- **OpenZeppelin Contracts**: https://docs.openzeppelin.com/contracts/
- **Hardhat Documentation**: https://hardhat.org/docs
- **Privacy by Design**: https://www.ipc.on.ca/privacy-by-design/
- **LGPD Portal**: https://www.gov.br/cidadania/pt-br/acesso-a-informacao/lgpd
- **GDPR Portal**: https://gdpr.eu/
- **ERC-20 Standard**: https://eips.ethereum.org/EIPS/eip-20

---

**Última Atualização**: 2025-01-29  
**Mantido por**: Equipe EON - Symbeon Tech

---

*Esta lista de referências é mantida para garantir atribuição adequada a todos os projetos, bibliotecas, padrões e conceitos que contribuíram para o desenvolvimento do SEVE Framework.*

