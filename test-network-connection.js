const hre = require("hardhat");

async function testNetworkConnection() {
  console.log("🔍 Testando conexão com redes...");
  
  const networks = ['sepolia', 'mumbai', 'bscTestnet'];
  
  for (const networkName of networks) {
    try {
      console.log(`\n📡 Testando ${networkName}...`);
      
      // Tentar obter signers
      const signers = await hre.ethers.getSigners();
      console.log(`✅ Signers obtidos: ${signers.length}`);
      
      // Tentar obter o provider
      const provider = hre.ethers.provider;
      const network = await provider.getNetwork();
      console.log(`✅ Rede conectada: ${network.name} (Chain ID: ${network.chainId})`);
      
      // Tentar obter o saldo da primeira conta
      const balance = await provider.getBalance(signers[0].address);
      console.log(`✅ Saldo da conta: ${hre.ethers.formatEther(balance)} ETH`);
      
    } catch (error) {
      console.log(`❌ Erro em ${networkName}:`, error.message);
    }
  }
}

testNetworkConnection()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Teste falhou:", error);
    process.exit(1);
  });
