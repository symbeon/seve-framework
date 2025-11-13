require("dotenv").config();
const { ethers } = require("ethers");

async function main() {
  console.log("🔍 Verificando MATIC com múltiplos RPCs...\n");

  if (!process.env.PRIVATE_KEY) {
    console.error("❌ PRIVATE_KEY não encontrado no .env");
    process.exit(1);
  }

  const wallet = new ethers.Wallet(process.env.PRIVATE_KEY);
  console.log(`📧 Endereço: ${wallet.address}\n`);

  const rpcs = [
    { name: "Polygon RPC (Público)", url: "https://polygon-rpc.com" },
    { name: "Ankr RPC", url: "https://rpc.ankr.com/polygon" },
    { name: "LlamaRPC", url: "https://polygon.llamarpc.com" },
    { name: "QuickNode (Público)", url: "https://polygon.quicknode.com" }
  ];

  let foundBalance = false;

  for (const rpc of rpcs) {
    try {
      console.log(`🌐 Testando: ${rpc.name}...`);
      const provider = new ethers.JsonRpcProvider(rpc.url);
      const balance = await provider.getBalance(wallet.address);
      const matic = ethers.formatEther(balance);
      const balanceNumber = parseFloat(matic);

      console.log(`   Saldo: ${matic} MATIC`);

      if (balanceNumber > 0) {
        console.log(`   ✅ MATIC ENCONTRADO!`);
        foundBalance = true;
        console.log(`\n💡 Use este RPC no .env:`);
        console.log(`   POLYGON_RPC_URL=${rpc.url}\n`);
        break;
      } else {
        console.log(`   ⚠️  Saldo: 0 MATIC\n`);
      }
    } catch (error) {
      console.log(`   ❌ Erro: ${error.message}\n`);
    }
  }

  if (!foundBalance) {
    console.log("=".repeat(50));
    console.log("❌ MATIC não encontrado em nenhum RPC da Polygon");
    console.log("=".repeat(50));
    console.log("\n💡 Possíveis causas:");
    console.log("   1. MATIC está na rede Ethereum (precisa bridge)");
    console.log("   2. Endereço diferente no .env");
    console.log("   3. MATIC ainda não chegou na Polygon");
    console.log("\n🔗 Verificar no PolygonScan:");
    console.log(`   https://polygonscan.com/address/${wallet.address}\n`);
  }
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Erro:", error);
    process.exit(1);
  });

