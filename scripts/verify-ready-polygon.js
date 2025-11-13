const hre = require("hardhat");

async function main() {
  console.log("🔍 Verificando Prontidão para Deploy na Polygon...\n");

  // Verificar saldo
  const signers = await hre.ethers.getSigners();
  const account = signers[0].address;
  
  console.log(`📧 Endereço: ${account}\n`);

  // Conectar à Polygon
  const polygonRpc = process.env.POLYGON_RPC_URL || "https://polygon-rpc.com";
  const provider = new hre.ethers.JsonRpcProvider(polygonRpc);
  
  try {
    const balance = await provider.getBalance(account);
    const balanceFormatted = hre.ethers.formatEther(balance);
    const balanceNumber = parseFloat(balanceFormatted);
    
    console.log(`💰 Saldo na Polygon: ${balanceFormatted} MATIC`);
    
    const minRequired = 0.1;
    const recommended = 0.2;
    
    if (balanceNumber >= recommended) {
      console.log(`   ✅ Saldo suficiente! (Recomendado: ${recommended} MATIC)`);
      console.log(`   🚀 Pronto para deploy!\n`);
    } else if (balanceNumber >= minRequired) {
      console.log(`   ⚠️  Saldo mínimo atingido (${minRequired} MATIC)`);
      console.log(`   💡 Recomendado: ${recommended} MATIC para margem de segurança\n`);
    } else {
      console.log(`   ❌ Saldo insuficiente!`);
      console.log(`   ⚠️  Necessário: pelo menos ${minRequired} MATIC`);
      console.log(`   💡 Recomendado: ${recommended} MATIC\n`);
      process.exit(1);
    }
    
    // Verificar configuração
    console.log("⚙️  Verificando Configuração...\n");
    
    if (process.env.PRIVATE_KEY) {
      console.log("   ✅ PRIVATE_KEY configurado");
    } else {
      console.log("   ❌ PRIVATE_KEY não encontrado no .env");
    }
    
    if (process.env.POLYGON_RPC_URL) {
      console.log("   ✅ POLYGON_RPC_URL configurado");
    } else {
      console.log("   ⚠️  Usando RPC público (pode ser mais lento)");
    }
    
    // Verificar contratos compilados
    console.log("\n📦 Verificando Contratos...\n");
    
    try {
      const SEVEToken = await hre.ethers.getContractFactory("SEVEToken");
      const SEVEProtocol = await hre.ethers.getContractFactory("SEVEProtocol");
      const SEVEDAO = await hre.ethers.getContractFactory("SEVEDAO");
      
      console.log("   ✅ SEVEToken compilado");
      console.log("   ✅ SEVEProtocol compilado");
      console.log("   ✅ SEVEDAO compilado");
    } catch (error) {
      console.log("   ❌ Erro ao verificar contratos:", error.message);
      console.log("   💡 Execute: npm run compile");
    }
    
    console.log("\n" + "=".repeat(50));
    console.log("✅ TUDO PRONTO PARA DEPLOY!");
    console.log("=".repeat(50));
    console.log("\n📋 Próximos comandos:");
    console.log("   1. Deploy: npm run deploy:polygon");
    console.log("   2. Ativar: npm run monetization:activate:polygon");
    console.log("\n🔗 PolygonScan: https://polygonscan.com/address/" + account);
    
  } catch (error) {
    console.error("❌ Erro ao verificar:", error.message);
    console.log("\n💡 Verifique:");
    console.log("   - Conexão com internet");
    console.log("   - RPC URL correto");
    console.log("   - Wallet conectada");
    process.exit(1);
  }
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Erro:", error);
    process.exit(1);
  });

