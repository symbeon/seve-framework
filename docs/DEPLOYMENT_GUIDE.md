# 🚀 SEVE Framework — Guia de Deploy (Local, Testnet e Produção)

Este guia padroniza o processo de deploy dos smart contracts (SEVEToken, SEVEProtocol, SEVEDAO) para uso no SEVE e em outros projetos do ecossistema.

## 1) Pré-requisitos
- Node.js e npm instalados
- Hardhat configurado no projeto (já incluso)
- Chave privada de teste (somente para testnets e mainnet)
- .env configurado (veja `docs/ENV_SETUP.md`)

## 2) Deploy Local (sem custo)
1. Inicie o nó local:
```bash
npx hardhat node --hostname 0.0.0.0 --port 8545
```
2. Em um novo terminal, faça o deploy:
```bash
npx hardhat run scripts/deploy-token.js --network localhost
npx hardhat run scripts/deploy-protocol.js --network localhost
npx hardhat run scripts/deploy-dao.js --network localhost
```
3. Saída e persistência:
- Endereços e tx-hash são salvos em `deployments/localhost_deployments.json`.

## 3) Deploy em Testnet (gratuito)
Opções de RPC (sem custo):
- Sepolia: `https://rpc.sepolia.org`
- Mumbai: `https://rpc-mumbai.maticvigil.com`
- BSC Testnet: `https://data-seed-prebsc-1-s1.binance.org:8545`

Passos:
1. Obtenha fundos de teste no faucet (veja `docs/TESTNET_PLAYBOOK.md`).
2. Configure `.env` (veja `docs/ENV_SETUP.md`).
3. Execute o deploy (exemplo Sepolia):
```bash
npx hardhat run scripts/deploy-token.js --network sepolia
npx hardhat run scripts/deploy-protocol.js --network sepolia
npx hardhat run scripts/deploy-dao.js --network sepolia
```
4. Saída e persistência:
- Endereços e tx-hash são salvos em `deployments/{network}_deployments.json`.

## 4) Deploy em Produção (mainnet)
1. Planejamento de custos (gas):
- Ethereum: alto custo (uso criterioso)
- Polygon: custo muito baixo (recomendado)
- BSC: custo baixo
2. Segurança:
- Use chaves dedicadas e storage seguro de segredos
- Habilite verificação dos contratos (Etherscan/Polygonscan)
3. Execução (exemplo Polygon):
```bash
npx hardhat run scripts/deploy-token.js --network polygon
npx hardhat run scripts/deploy-protocol.js --network polygon
npx hardhat run scripts/deploy-dao.js --network polygon
```

## 5) Verificação dos contratos
Se possuir API keys dos explorers no `.env`:
```bash
npx hardhat verify --network sepolia <ENDERECO_CONTRATO> <args...>
```

## 6) Boas práticas
- Nunca commitar `.env`
- Usar apenas chaves de teste em testnets
- Documentar endereços de deploy no repositório (arquivo deployments/*)
- Rodar testes antes de deploy: `npx hardhat test`

## 7) Troubleshooting rápido
- Erro HH110 (invalid project id): use RPC público ou configure Alchemy/Infura
- Sem saldo: use faucet da testnet
- `deployed()` não existe: use `waitForDeployment()` (ethers v6)

Referências:
- `docs/ENV_SETUP.md`
- `docs/RPC_PROVIDERS.md`
- `docs/TESTNET_PLAYBOOK.md`
- `COST_ANALYSIS.md`
