# 🌐 Provedores RPC — Infura, Alchemy e RPCs Públicos

## O que é um RPC?
É o ponto de acesso que conecta seu app à blockchain. Sem RPC, seu app não envia/recebe transações.

## Opções

### 1) Infura
- Vantagens: estável, onipresente no ecossistema Ethereum
- Free: ~100k requisições/dia
- Pago: a partir de $50/mês
- URL exemplo (Sepolia): `https://sepolia.infura.io/v3/<INFURA_API_KEY>`

### 2) Alchemy (recomendado para dev)
- Vantagens: free tier generoso e ferramentas
- Free: até 300M compute units/mês
- URL exemplo (Sepolia): `https://eth-sepolia.g.alchemy.com/v2/<ALCHEMY_API_KEY>`

### 3) QuickNode
- Free: até 10M requisições/mês
- URLs por rede (dashboard)

### 4) RPCs Públicos (zero custo, sem conta)
- Ethereum Sepolia: `https://rpc.sepolia.org`
- Polygon Mumbai: `https://rpc-mumbai.maticvigil.com`
- BSC Testnet: `https://data-seed-prebsc-1-s1.binance.org:8545`

## Como configurar no Hardhat
Exemplo (sepolia):
```js
sepolia: {
  url: process.env.ALCHEMY_API_KEY
    ? `https://eth-sepolia.g.alchemy.com/v2/${process.env.ALCHEMY_API_KEY}`
    : "https://rpc.sepolia.org",
  accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
  chainId: 11155111,
}
```

## Boas práticas
- Nunca exponha API keys em repositórios
- Use `.env` e vaults de segredos
- Para dev, prefira Alchemy Free ou RPC público
- Para produção, use provedores gerenciados (SLA)
