require("dotenv").config();
const { ethers } = require("ethers");
const https = require("https");

/**
 * Bridge usando Socket.xyz API
 * Mais simples e confiável que usar contratos diretamente
 */

const SOCKET_API_URL = "https://api.socket.tech/v2";

async function getQuote(fromChain, toChain, tokenAddress, amount) {
  return new Promise((resolve, reject) => {
    const url = `${SOCKET_API_URL}/quote?fromChainId=${fromChain}&toChainId=${toChain}&fromTokenAddress=${tokenAddress}&toTokenAddress=${tokenAddress}&fromAmount=${amount}&userAddress=${process.env.PRIVATE_KEY ? new ethers.Wallet(process.env.PRIVATE_KEY).address : ""}`;
    
    https.get(url, (res) => {
      let data = "";
      res.on("data", (chunk) => { data += chunk; });
      res.on("end", () => {
        try {
          resolve(JSON.parse(data));
        } catch (e) {
          reject(e);
        }
      });
    }).on("error", reject);
  });
}

async function main() {
  console.log("🌉 Bridge via Socket.xyz API\n");

  if (!process.env.PRIVATE_KEY) {
    console.error("❌ PRIVATE_KEY não encontrado no .env");
    process.exit(1);
  }

  const wallet = new ethers.Wallet(process.env.PRIVATE_KEY);
  console.log(`📧 Endereço: ${wallet.address}\n`);

  // Chain IDs
  const ETHEREUM_CHAIN_ID = 1;
  const POLYGON_CHAIN_ID = 137;
  
  // MATIC token addresses
  const MATIC_ETH = "0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0";
  const MATIC_POLYGON = "0x0000000000000000000000000000000000001010"; // Native MATIC

  // Quantidade para bridge (0.2 MATIC)
  const amount = ethers.parseEther("0.2");

  console.log("🔍 Buscando quote do bridge...\n");

  try {
    const quote = await getQuote(
      ETHEREUM_CHAIN_ID,
      POLYGON_CHAIN_ID,
      MATIC_ETH,
      amount.toString()
    );

    if (quote.success) {
      console.log("✅ Quote obtido!");
      console.log(`   De: ${quote.result.fromAmount} MATIC (Ethereum)`);
      console.log(`   Para: ${quote.result.toAmount} MATIC (Polygon)`);
      console.log(`   Taxa: ${quote.result.totalGasFees || "N/A"}\n`);
      
      console.log("📋 Para completar o bridge:");
      console.log("   1. Acesse: https://socket.tech/");
      console.log("   2. Conecte sua wallet");
      console.log("   3. Selecione: Ethereum → Polygon");
      console.log("   4. Token: MATIC");
      console.log("   5. Quantidade: 0.2 MATIC");
      console.log("   6. Confirme transação\n");
    } else {
      console.error("❌ Erro ao obter quote:", quote.message);
    }
  } catch (error) {
    console.error("❌ Erro:", error.message);
    console.log("\n💡 Alternativa: Usar bridge direto via portal");
    console.log("   https://portal.polygon.technology/\n");
  }
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Erro:", error);
    process.exit(1);
  });

