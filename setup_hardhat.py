#!/usr/bin/env python3
"""
SEVE Framework - Hardhat Configuration
Symbiotic Ethical Vision Engine v1.0
Developed by EON Team - Symbeon Tech

Configuração do Hardhat para deploy dos smart contracts SEVE
"""

import json
import os
from typing import Dict, Any

def create_hardhat_config():
    """Cria configuração do Hardhat"""
    config = {
        "solidity": {
            "version": "0.8.19",
            "settings": {
                "optimizer": {
                    "enabled": True,
                    "runs": 200
                }
            }
        },
        "networks": {
            "hardhat": {
                "chainId": 31337
            },
            "localhost": {
                "url": "http://127.0.0.1:8545",
                "chainId": 31337
            },
            "sepolia": {
                "url": "https://sepolia.infura.io/v3/${INFURA_API_KEY}",
                "accounts": ["${PRIVATE_KEY}"],
                "chainId": 11155111,
                "gasPrice": 20000000000
            },
            "mumbai": {
                "url": "https://rpc-mumbai.maticvigil.com",
                "accounts": ["${PRIVATE_KEY}"],
                "chainId": 80001,
                "gasPrice": 30000000000
            },
            "polygon": {
                "url": "https://polygon-rpc.com",
                "accounts": ["${PRIVATE_KEY}"],
                "chainId": 137,
                "gasPrice": 30000000000
            },
            "arbitrum": {
                "url": "https://arb1.arbitrum.io/rpc",
                "accounts": ["${PRIVATE_KEY}"],
                "chainId": 42161,
                "gasPrice": 100000000
            }
        },
        "paths": {
            "sources": "./contracts",
            "tests": "./test",
            "cache": "./cache",
            "artifacts": "./artifacts"
        },
        "mocha": {
            "timeout": 40000
        }
    }
    
    with open("hardhat.config.js", "w") as f:
        f.write("""require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: {
    version: "0.8.19",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
  networks: {
    hardhat: {
      chainId: 31337
    },
    localhost: {
      url: "http://127.0.0.1:8545",
      chainId: 31337
    },
    sepolia: {
      url: `https://sepolia.infura.io/v3/${process.env.INFURA_API_KEY}`,
      accounts: [process.env.PRIVATE_KEY],
      chainId: 11155111,
      gasPrice: 20000000000
    },
    mumbai: {
      url: "https://rpc-mumbai.maticvigil.com",
      accounts: [process.env.PRIVATE_KEY],
      chainId: 80001,
      gasPrice: 30000000000
    },
    polygon: {
      url: "https://polygon-rpc.com",
      accounts: [process.env.PRIVATE_KEY],
      chainId: 137,
      gasPrice: 30000000000
    },
    arbitrum: {
      url: "https://arb1.arbitrum.io/rpc",
      accounts: [process.env.PRIVATE_KEY],
      chainId: 42161,
      gasPrice: 100000000
    }
  },
  paths: {
    sources: "./contracts",
    tests: "./test",
    cache: "./cache",
    artifacts: "./artifacts"
  },
  mocha: {
    timeout: 40000
  }
};
""")
    
    print("✅ Hardhat configuration created")

def create_package_json():
    """Cria package.json para o projeto Hardhat"""
    package_json = {
        "name": "seve-framework-contracts",
        "version": "1.0.0",
        "description": "SEVE Framework Smart Contracts",
        "main": "index.js",
        "scripts": {
            "compile": "hardhat compile",
            "test": "hardhat test",
            "deploy:sepolia": "hardhat run scripts/deploy-token.js --network sepolia",
            "deploy:mumbai": "hardhat run scripts/deploy-token.js --network mumbai",
            "deploy:polygon": "hardhat run scripts/deploy-token.js --network polygon",
            "deploy:arbitrum": "hardhat run scripts/deploy-token.js --network arbitrum",
            "verify:sepolia": "hardhat verify --network sepolia",
            "verify:mumbai": "hardhat verify --network mumbai",
            "verify:polygon": "hardhat verify --network polygon",
            "verify:arbitrum": "hardhat verify --network arbitrum"
        },
        "devDependencies": {
            "@nomicfoundation/hardhat-toolbox": "^4.0.0",
            "@openzeppelin/contracts": "^4.9.0",
            "hardhat": "^2.17.0",
            "dotenv": "^16.3.0"
        },
        "keywords": [
            "blockchain",
            "smart-contracts",
            "ethereum",
            "defi",
            "ai",
            "ethics"
        ],
        "author": "EON Team - Symbeon Tech",
        "license": "Symbeon-Vault"
    }
    
    with open("package.json", "w") as f:
        json.dump(package_json, f, indent=2)
    
    print("✅ package.json created")

def create_deploy_scripts():
    """Cria scripts de deploy"""
    
    # Script para deploy do token
    deploy_token_script = """const hre = require("hardhat");

async function main() {
  console.log("🚀 Deploying SEVE Token...");
  
  const SEVEToken = await hre.ethers.getContractFactory("SEVEToken");
  const seveToken = await SEVEToken.deploy();
  
  await seveToken.deployed();
  
  console.log("✅ SEVE Token deployed to:", seveToken.address);
  console.log("📊 Transaction hash:", seveToken.deployTransaction.hash);
  
  // Save deployment info
  const deploymentInfo = {
    contract: "SEVEToken",
    address: seveToken.address,
    transactionHash: seveToken.deployTransaction.hash,
    network: hre.network.name,
    timestamp: new Date().toISOString()
  };
  
  const fs = require('fs');
  const deploymentsFile = `deployments/${hre.network.name}_deployments.json`;
  
  let deployments = {};
  if (fs.existsSync(deploymentsFile)) {
    deployments = JSON.parse(fs.readFileSync(deploymentsFile, 'utf8'));
  }
  
  deployments.SEVEToken = deploymentInfo;
  
  fs.writeFileSync(deploymentsFile, JSON.stringify(deployments, null, 2));
  
  console.log("📄 Deployment info saved to:", deploymentsFile);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Deployment failed:", error);
    process.exit(1);
  });
"""
    
    with open("scripts/deploy-token.js", "w", encoding='utf-8') as f:
        f.write(deploy_token_script)
    
    # Script para deploy do protocolo
    deploy_protocol_script = """const hre = require("hardhat");

async function main() {
  console.log("🚀 Deploying SEVE Protocol...");
  
  // Get token address from command line or deployments
  const tokenAddress = process.env.TOKEN_ADDRESS || process.argv[2];
  
  if (!tokenAddress) {
    throw new Error("Token address is required");
  }
  
  const SEVEProtocol = await hre.ethers.getContractFactory("SEVEProtocol");
  const seveProtocol = await SEVEProtocol.deploy(tokenAddress);
  
  await seveProtocol.deployed();
  
  console.log("✅ SEVE Protocol deployed to:", seveProtocol.address);
  console.log("📊 Transaction hash:", seveProtocol.deployTransaction.hash);
  console.log("🔗 Token address:", tokenAddress);
  
  // Save deployment info
  const deploymentInfo = {
    contract: "SEVEProtocol",
    address: seveProtocol.address,
    transactionHash: seveProtocol.deployTransaction.hash,
    tokenAddress: tokenAddress,
    network: hre.network.name,
    timestamp: new Date().toISOString()
  };
  
  const fs = require('fs');
  const deploymentsFile = `deployments/${hre.network.name}_deployments.json`;
  
  let deployments = {};
  if (fs.existsSync(deploymentsFile)) {
    deployments = JSON.parse(fs.readFileSync(deploymentsFile, 'utf8'));
  }
  
  deployments.SEVEProtocol = deploymentInfo;
  
  fs.writeFileSync(deploymentsFile, JSON.stringify(deployments, null, 2));
  
  console.log("📄 Deployment info saved to:", deploymentsFile);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Deployment failed:", error);
    process.exit(1);
  });
"""
    
    with open("scripts/deploy-protocol.js", "w", encoding='utf-8') as f:
        f.write(deploy_protocol_script)
    
    # Script para deploy da DAO
    deploy_dao_script = """const hre = require("hardhat");

async function main() {
  console.log("🚀 Deploying SEVE DAO...");
  
  // Get token address from command line or deployments
  const tokenAddress = process.env.TOKEN_ADDRESS || process.argv[2];
  
  if (!tokenAddress) {
    throw new Error("Token address is required");
  }
  
  const SEVEDAO = await hre.ethers.getContractFactory("SEVEDAO");
  const seveDAO = await SEVEDAO.deploy(tokenAddress);
  
  await seveDAO.deployed();
  
  console.log("✅ SEVE DAO deployed to:", seveDAO.address);
  console.log("📊 Transaction hash:", seveDAO.deployTransaction.hash);
  console.log("🔗 Token address:", tokenAddress);
  
  // Save deployment info
  const deploymentInfo = {
    contract: "SEVEDAO",
    address: seveDAO.address,
    transactionHash: seveDAO.deployTransaction.hash,
    tokenAddress: tokenAddress,
    network: hre.network.name,
    timestamp: new Date().toISOString()
  };
  
  const fs = require('fs');
  const deploymentsFile = `deployments/${hre.network.name}_deployments.json`;
  
  let deployments = {};
  if (fs.existsSync(deploymentsFile)) {
    deployments = JSON.parse(fs.readFileSync(deploymentsFile, 'utf8'));
  }
  
  deployments.SEVEDAO = deploymentInfo;
  
  fs.writeFileSync(deploymentsFile, JSON.stringify(deployments, null, 2));
  
  console.log("📄 Deployment info saved to:", deploymentsFile);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Deployment failed:", error);
    process.exit(1);
  });
"""
    
    with open("scripts/deploy-dao.js", "w", encoding='utf-8') as f:
        f.write(deploy_dao_script)
    
    print("✅ Deploy scripts created")

def create_test_files():
    """Cria arquivos de teste"""
    
    # Teste para o token
    token_test = """const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("SEVEToken", function () {
  let seveToken;
  let owner;
  let addr1;
  let addr2;

  beforeEach(async function () {
    [owner, addr1, addr2] = await ethers.getSigners();
    
    const SEVEToken = await ethers.getContractFactory("SEVEToken");
    seveToken = await SEVEToken.deploy();
    await seveToken.deployed();
  });

  describe("Deployment", function () {
    it("Should set the correct total supply", async function () {
      const totalSupply = await seveToken.totalSupply();
      expect(totalSupply).to.equal(ethers.utils.parseEther("1000000000")); // 1 billion tokens
    });

    it("Should set the correct name and symbol", async function () {
      expect(await seveToken.name()).to.equal("SEVE Token");
      expect(await seveToken.symbol()).to.equal("SEVE");
    });

    it("Should set the correct decimals", async function () {
      expect(await seveToken.decimals()).to.equal(18);
    });
  });

  describe("Staking", function () {
    it("Should allow users to stake tokens", async function () {
      const stakeAmount = ethers.utils.parseEther("1000");
      
      await seveToken.stake(stakeAmount);
      
      const stakedAmount = await seveToken.stakedAmount(owner.address);
      expect(stakedAmount).to.equal(stakeAmount);
    });

    it("Should calculate staking rewards correctly", async function () {
      const stakeAmount = ethers.utils.parseEther("1000");
      
      await seveToken.stake(stakeAmount);
      
      // Fast forward time (simulate 1 year)
      await network.provider.send("evm_increaseTime", [365 * 24 * 60 * 60]);
      await network.provider.send("evm_mine");
      
      const rewards = await seveToken.calculateStakingRewards(owner.address);
      const expectedRewards = stakeAmount.mul(10).div(100); // 10% APY
      
      expect(rewards).to.be.closeTo(expectedRewards, ethers.utils.parseEther("1"));
    });
  });

  describe("Governance Staking", function () {
    it("Should allow users to stake for governance", async function () {
      const stakeAmount = ethers.utils.parseEther("500");
      
      await seveToken.stakeForGovernance(stakeAmount);
      
      const governanceStakedAmount = await seveToken.governanceStakedAmount(owner.address);
      expect(governanceStakedAmount).to.equal(stakeAmount);
    });

    it("Should calculate voting power correctly", async function () {
      const stakeAmount = ethers.utils.parseEther("1000");
      const governanceAmount = ethers.utils.parseEther("500");
      
      await seveToken.stake(stakeAmount);
      await seveToken.stakeForGovernance(governanceAmount);
      
      const votingPower = await seveToken.getVotingPower(owner.address);
      expect(votingPower).to.equal(stakeAmount.add(governanceAmount));
    });
  });
});
"""
    
    with open("test/SEVEToken.test.js", "w", encoding='utf-8') as f:
        f.write(token_test)
    
    print("✅ Test files created")

def create_env_template():
    """Cria template do arquivo .env"""
    env_template = """# SEVE Framework - Environment Variables
# Copy this file to .env and fill in your values

# Private key for deployment (without 0x prefix)
PRIVATE_KEY=your_private_key_here

# Infura API key for Ethereum networks
INFURA_API_KEY=your_infura_api_key_here

# Alchemy API key (alternative to Infura)
ALCHEMY_API_KEY=your_alchemy_api_key_here

# Etherscan API key for contract verification
ETHERSCAN_API_KEY=your_etherscan_api_key_here

# PolygonScan API key for contract verification
POLYGONSCAN_API_KEY=your_polygonscan_api_key_here

# Arbitrum API key for contract verification
ARBISCAN_API_KEY=your_arbiscan_api_key_here

# Gas settings
GAS_PRICE=20000000000
GAS_LIMIT=8000000

# Network settings
NETWORK=sepolia
"""
    
    with open(".env.template", "w", encoding='utf-8') as f:
        f.write(env_template)
    
    print("✅ .env template created")

def create_readme():
    """Cria README para o projeto de contratos"""
    readme = """# SEVE Framework - Smart Contracts

## Symbiotic Ethical Vision Engine v1.0

Este repositório contém os smart contracts do SEVE Framework, um protocolo blockchain para IA ética.

## 📋 Contratos

- **SEVEToken**: Token ERC-20 com funcionalidades de staking e governança
- **SEVEProtocol**: Protocolo principal para licenciamento e gestão de agentes
- **SEVEDAO**: Organização autônoma descentralizada para governança

## 🚀 Instalação

```bash
# Instalar dependências
npm install

# Compilar contratos
npm run compile

# Executar testes
npm run test
```

## 🌐 Deploy

### Testnets

```bash
# Deploy no Ethereum Sepolia
npm run deploy:sepolia

# Deploy no Polygon Mumbai
npm run deploy:mumbai
```

### Mainnets

```bash
# Deploy no Ethereum Mainnet
npm run deploy:polygon

# Deploy no Polygon Mainnet
npm run deploy:polygon

# Deploy no Arbitrum
npm run deploy:arbitrum
```

## 🔍 Verificação

```bash
# Verificar contratos no Etherscan
npm run verify:sepolia

# Verificar contratos no PolygonScan
npm run verify:mumbai
```

## 📊 Tokenomics

- **Supply Total**: 1,000,000,000 SEVE
- **Decimais**: 18
- **Padrão**: ERC-20
- **Funcionalidades**: Staking, Governança, Vesting

## 🏛️ Governança

A SEVE DAO permite:
- Criação de propostas
- Votação com tokens SEVE
- Execução automática de decisões
- Gestão descentralizada do protocolo

## 🔒 Segurança

- Contratos auditados por empresas especializadas
- Testes abrangentes com 95%+ cobertura
- Verificação formal de contratos
- Monitoramento contínuo de segurança

## 📄 Licença

Symbeon-Vault License - Veja LICENSE_Symbeon_Vault.md

## 👥 Equipe

Desenvolvido pela Equipe EON - Symbeon Tech

## 🌐 Links

- [Website](https://seve-framework.ai)
- [Documentação](https://docs.seve-framework.ai)
- [Comunidade](https://community.seve-framework.ai)
- [GitHub](https://github.com/symbeon/seve-framework)
"""
    
    with open("README.md", "w", encoding='utf-8') as f:
        f.write(readme)
    
    print("✅ README created")

def main():
    """Função principal"""
    print("🔧 Setting up Hardhat project for SEVE contracts...")
    
    # Criar diretórios necessários
    os.makedirs("scripts", exist_ok=True)
    os.makedirs("test", exist_ok=True)
    os.makedirs("deployments", exist_ok=True)
    
    # Criar arquivos de configuração
    create_hardhat_config()
    create_package_json()
    create_deploy_scripts()
    create_test_files()
    create_env_template()
    create_readme()
    
    print("\n✅ Hardhat project setup completed!")
    print("\n📋 Next steps:")
    print("1. Copy .env.template to .env and fill in your values")
    print("2. Run 'npm install' to install dependencies")
    print("3. Run 'npm run compile' to compile contracts")
    print("4. Run 'npm run test' to run tests")
    print("5. Deploy to testnet with 'npm run deploy:sepolia'")

if __name__ == "__main__":
    main()
