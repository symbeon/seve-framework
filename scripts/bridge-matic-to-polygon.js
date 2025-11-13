require("dotenv").config();
const hre = require("hardhat");
const { ethers } = require("ethers");

/**
 * Script para fazer bridge de MATIC da Ethereum para Polygon
 * Usa o contrato oficial do Polygon PoS Bridge
 */

// Endereços dos contratos do Polygon Bridge na Ethereum
const POLYGON_BRIDGE_CONTRACTS = {
  // RootChainManager - contrato principal do bridge
  ROOT_CHAIN_MANAGER: "0xA0c68C638235ee32657e8f720a23ceC1bFc77C77",
  // ERC20Predicate - para tokens ERC20
  ERC20_PREDICATE: "0x40ec5B33f54e0E8A33A975908C5BA1c14e5BbbDf",
  // MATIC token na Ethereum
  MATIC_TOKEN_ETH: "0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0"
};

async function main() {
  console.log("🌉 Bridge de MATIC: Ethereum → Polygon\n");

  // Verificar configuração
  if (!process.env.PRIVATE_KEY) {
    console.error("❌ PRIVATE_KEY não encontrado no .env");
    process.exit(1);
  }

  const wallet = new ethers.Wallet(process.env.PRIVATE_KEY);
  console.log(`📧 Endereço: ${wallet.address}\n`);

  // Conectar à Ethereum Mainnet
  const ethRpc = process.env.ETHEREUM_RPC || "https://eth.llamarpc.com";
  const ethProvider = new ethers.JsonRpcProvider(ethRpc);
  const ethWallet = wallet.connect(ethProvider);

  // Verificar saldo na Ethereum
  console.log("🔍 Verificando saldo na Ethereum...");
  const maticToken = new ethers.Contract(
    POLYGON_BRIDGE_CONTRACTS.MATIC_TOKEN_ETH,
    [
      "function balanceOf(address) view returns (uint256)",
      "function approve(address,uint256) returns (bool)",
      "function allowance(address,address) view returns (uint256)"
    ],
    ethWallet
  );

  const balance = await maticToken.balanceOf(wallet.address);
  const balanceFormatted = ethers.formatEther(balance);
  const balanceNumber = parseFloat(balanceFormatted);

  console.log(`💰 Saldo na Ethereum: ${balanceFormatted} MATIC\n`);

  if (balanceNumber < 0.1) {
    console.error("❌ Saldo insuficiente! Precisa de pelo menos 0.1 MATIC");
    process.exit(1);
  }

  // Quantidade para bridge (recomendado: 0.2 MATIC)
  const amountToBridge = ethers.parseEther("0.2");
  const amountFormatted = ethers.formatEther(amountToBridge);

  console.log(`🌉 Preparando bridge de ${amountFormatted} MATIC...\n`);

  // Verificar se precisa aprovar
  console.log("1️⃣  Verificando aprovação...");
  const allowance = await maticToken.allowance(
    wallet.address,
    POLYGON_BRIDGE_CONTRACTS.ERC20_PREDICATE
  );

  if (allowance < amountToBridge) {
    console.log("   ⚠️  Aprovação necessária...");
    console.log("   📝 Aprovando tokens...");
    
    const approveTx = await maticToken.approve(
      POLYGON_BRIDGE_CONTRACTS.ERC20_PREDICATE,
      amountToBridge
    );
    console.log(`   ⏳ Aguardando confirmação: ${approveTx.hash}`);
    await approveTx.wait();
    console.log("   ✅ Aprovação confirmada!\n");
  } else {
    console.log("   ✅ Aprovação já existe\n");
  }

  // Fazer o bridge usando RootChainManager
  console.log("2️⃣  Iniciando bridge...");
  console.log("   ⚠️  ATENÇÃO: Este processo pode levar 10-30 minutos");
  console.log("   ⚠️  Você precisará fazer o exit na Polygon depois\n");

  // ABI simplificado do RootChainManager
  const rootChainManagerAbi = [
    "function depositFor(address user, address rootToken, bytes calldata depositData) external"
  ];

  const rootChainManager = new ethers.Contract(
    POLYGON_BRIDGE_CONTRACTS.ROOT_CHAIN_MANAGER,
    rootChainManagerAbi,
    ethWallet
  );

  // Preparar dados do deposit
  const depositData = ethers.AbiCoder.defaultAbiCoder().encode(
    ["uint256"],
    [amountToBridge]
  );

  try {
    console.log("   📤 Enviando transação...");
    const tx = await rootChainManager.depositFor(
      wallet.address, // user
      POLYGON_BRIDGE_CONTRACTS.MATIC_TOKEN_ETH, // rootToken
      depositData,
      { gasLimit: 500000 } // Gas limit alto para bridge
    );

    console.log(`   ⏳ Transaction hash: ${tx.hash}`);
    console.log(`   🔗 Etherscan: https://etherscan.io/tx/${tx.hash}`);
    console.log("\n   ⏳ Aguardando confirmação (pode levar alguns minutos)...");
    
    const receipt = await tx.wait();
    console.log(`\n   ✅ Bridge iniciado!`);
    console.log(`   📊 Block: ${receipt.blockNumber}`);
    console.log(`   ⏱️  Gas usado: ${receipt.gasUsed.toString()}\n`);

    console.log("=".repeat(50));
    console.log("🌉 BRIDGE INICIADO COM SUCESSO!");
    console.log("=".repeat(50));
    console.log("\n📋 PRÓXIMOS PASSOS:");
    console.log("   1. Aguardar 10-30 minutos para checkpoint");
    console.log("   2. Verificar status em: https://portal.polygon.technology/");
    console.log("   3. Quando aparecer 'Ready to claim', fazer o exit");
    console.log("   4. Após exit, verificar saldo na Polygon:");
    console.log("      npm run verify:ready:polygon");
    console.log("\n💡 Alternativa mais rápida:");
    console.log("   Comprar MATIC direto na Polygon (sem esperar bridge)");
    console.log("");

  } catch (error) {
    console.error("\n❌ Erro ao fazer bridge:", error.message);
    
    if (error.message.includes("insufficient funds")) {
      console.error("\n💡 Você precisa de ETH para pagar o gas!");
      console.error("   O bridge requer ETH na Ethereum para a taxa de gas");
    }
    
    process.exit(1);
  }
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Erro:", error);
    process.exit(1);
  });

