const hre = require("hardhat");
require("dotenv").config();

async function main() {
  console.log("💰 Verificando Saldo na Testnet...\n");
  
  const network = hre.network.name;
  console.log(`🌐 Network: ${network}`);
  
  if (!process.env.PRIVATE_KEY) {
    console.error("❌ PRIVATE_KEY não configurada no .env");
    process.exit(1);
  }
  
  const wallet = new hre.ethers.Wallet(process.env.PRIVATE_KEY);
  const provider = hre.ethers.provider;
  const signer = wallet.connect(provider);
  
  const address = await signer.getAddress();
  console.log(`📧 Endereço: ${address}`);
  
  const balance = await provider.getBalance(address);
  const balanceInEth = hre.ethers.formatEther(balance);
  
  console.log(`💰 Saldo: ${balanceInEth} ETH`);
  
  // Verificar se tem fundos suficientes (0.01 ETH mínimo)
  const minBalance = hre.ethers.parseEther("0.01");
  if (balance < minBalance) {
    console.log("\n⚠️  Saldo insuficiente para deploy!");
    console.log("💡 Obtenha fundos de teste em:");
    if (network === "sepolia") {
      console.log("   https://sepoliafaucet.com/");
      console.log("   https://faucet.quicknode.com/ethereum/sepolia");
    } else if (network === "mumbai") {
      console.log("   https://faucet.polygon.technology/");
    } else if (network === "bscTestnet") {
      console.log("   https://testnet.bnbchain.org/faucet-smart");
    }
    process.exit(1);
  } else {
    console.log("\n✅ Saldo suficiente para deploy!");
  }
  
  // Mostrar explorer
  console.log("\n🔗 Explorer:");
  if (network === "sepolia") {
    console.log(`   https://sepolia.etherscan.io/address/${address}`);
  } else if (network === "mumbai") {
    console.log(`   https://mumbai.polygonscan.com/address/${address}`);
  } else if (network === "bscTestnet") {
    console.log(`   https://testnet.bscscan.com/address/${address}`);
  }
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Erro:", error.message);
    process.exit(1);
  });

