const hre = require("hardhat");

async function main() {
  console.log("💰 Verificando Saldo em Mainnets...\n");
  
  const networks = [
    { name: "polygon", display: "Polygon Mainnet", token: "MATIC" },
    { name: "ethereum", display: "Ethereum Mainnet", token: "ETH" },
    { name: "arbitrum", display: "Arbitrum Mainnet", token: "ETH" },
    { name: "bsc", display: "BSC Mainnet", token: "BNB" }
  ];
  
  const signers = await hre.ethers.getSigners();
  const account = signers[0].address;
  
  console.log(`📧 Endereço: ${account}\n`);
  
  for (const network of networks) {
    try {
      // Tentar conectar à rede
      const provider = new hre.ethers.JsonRpcProvider(
        getRpcUrl(network.name)
      );
      
      const balance = await provider.getBalance(account);
      const balanceFormatted = hre.ethers.formatEther(balance);
      const balanceNumber = parseFloat(balanceFormatted);
      
      console.log(`🌐 ${network.display}:`);
      console.log(`   Saldo: ${balanceFormatted} ${network.token}`);
      
      // Verificar se tem saldo suficiente
      if (network.name === "polygon") {
        const minRequired = 0.01; // ~$0.20 para deploy
        if (balanceNumber >= minRequired) {
          console.log(`   ✅ Suficiente para deploy (~$0.20)`);
        } else {
          console.log(`   ⚠️  Insuficiente. Precisa de pelo menos ${minRequired} MATIC`);
        }
      } else if (network.name === "ethereum") {
        const minRequired = 0.25; // ~$500 para deploy
        if (balanceNumber >= minRequired) {
          console.log(`   ✅ Suficiente para deploy (~$500-1,245)`);
        } else {
          console.log(`   ⚠️  Insuficiente. Precisa de pelo menos ${minRequired} ETH`);
        }
      } else if (network.name === "arbitrum") {
        const minRequired = 0.001; // ~$1.66 para deploy
        if (balanceNumber >= minRequired) {
          console.log(`   ✅ Suficiente para deploy (~$1.66)`);
        } else {
          console.log(`   ⚠️  Insuficiente. Precisa de pelo menos ${minRequired} ETH`);
        }
      } else if (network.name === "bsc") {
        const minRequired = 0.003; // ~$0.75 para deploy
        if (balanceNumber >= minRequired) {
          console.log(`   ✅ Suficiente para deploy (~$0.75)`);
        } else {
          console.log(`   ⚠️  Insuficiente. Precisa de pelo menos ${minRequired} BNB`);
        }
      }
      
      console.log(`   🔗 Explorer: ${getExplorerUrl(network.name, account)}\n`);
      
    } catch (error) {
      console.log(`   ❌ Erro ao verificar ${network.display}: ${error.message}\n`);
    }
  }
  
  console.log("\n💡 RECOMENDAÇÃO:");
  console.log("   Se você tem saldo em Polygon: Deploy em Polygon (mais barato!)");
  console.log("   Se você tem saldo em Ethereum: Considere Polygon primeiro");
  console.log("   Veja: docs/ANALISE_CUSTO_MAINNET.md para detalhes\n");
}

function getRpcUrl(network) {
  const rpcUrls = {
    polygon: process.env.POLYGON_RPC || "https://polygon-rpc.com",
    ethereum: process.env.ETHEREUM_RPC || "https://eth.llamarpc.com",
    arbitrum: process.env.ARBITRUM_RPC || "https://arb1.arbitrum.io/rpc",
    bsc: process.env.BSC_RPC || "https://bsc-dataseed.binance.org"
  };
  return rpcUrls[network] || rpcUrls.polygon;
}

function getExplorerUrl(network, address) {
  const explorers = {
    polygon: `https://polygonscan.com/address/${address}`,
    ethereum: `https://etherscan.io/address/${address}`,
    arbitrum: `https://arbiscan.io/address/${address}`,
    bsc: `https://bscscan.com/address/${address}`
  };
  return explorers[network] || explorers.polygon;
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Erro:", error);
    process.exit(1);
  });

