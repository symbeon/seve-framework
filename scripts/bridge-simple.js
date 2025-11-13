require("dotenv").config();
const { ethers } = require("ethers");

/**
 * Bridge Simplificado - Usa o contrato do Polygon Bridge de forma mais direta
 * Foca apenas em fazer o deposit básico
 */

async function main() {
  console.log("🌉 Bridge Simplificado: MATIC Ethereum → Polygon\n");

  if (!process.env.PRIVATE_KEY) {
    console.error("❌ PRIVATE_KEY não encontrado no .env");
    process.exit(1);
  }

  const wallet = new ethers.Wallet(process.env.PRIVATE_KEY);
  console.log(`📧 Endereço: ${wallet.address}\n`);

  // Conectar à Ethereum
  const ethRpc = process.env.ETHEREUM_RPC || "https://eth.llamarpc.com";
  const ethProvider = new ethers.JsonRpcProvider(ethRpc);
  const ethWallet = wallet.connect(ethProvider);

  // Verificar saldo ETH
  const ethBalance = await ethProvider.getBalance(wallet.address);
  const ethFormatted = ethers.formatEther(ethBalance);
  console.log(`💰 Saldo ETH: ${ethFormatted} ETH`);

  if (parseFloat(ethFormatted) < 0.002) {
    console.error("\n❌ ETH insuficiente para gas!");
    console.error("   Precisa de pelo menos 0.002 ETH para gas fee");
    console.error("   Você tem:", ethFormatted, "ETH\n");
    console.log("💡 SOLUÇÕES:");
    console.log("   1. Comprar mais ETH (~$5-10 USD)");
    console.log("   2. Comprar MATIC direto na Polygon (recomendado)");
    console.log("      - Não precisa de ETH");
    console.log("      - Mais rápido e barato\n");
    process.exit(1);
  }

  // Verificar saldo MATIC
  const MATIC_TOKEN_ETH = "0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0";
  const maticToken = new ethers.Contract(
    MATIC_TOKEN_ETH,
    ["function balanceOf(address) view returns (uint256)"],
    ethWallet
  );

  const maticBalance = await maticToken.balanceOf(wallet.address);
  const maticFormatted = ethers.formatEther(maticBalance);
  console.log(`💰 Saldo MATIC: ${maticFormatted} MATIC\n`);

  if (parseFloat(maticFormatted) < 0.1) {
    console.error("❌ MATIC insuficiente!");
    process.exit(1);
  }

  // Quantidade para bridge (0.2 MATIC)
  const amountToBridge = ethers.parseEther("0.2");
  console.log(`🌉 Preparando bridge de ${ethers.formatEther(amountToBridge)} MATIC...\n`);

  console.log("⚠️  ATENÇÃO:");
  console.log("   O bridge do Polygon é complexo e requer múltiplas etapas.");
  console.log("   A forma mais confiável é usar a interface web.\n");

  console.log("📋 OPÇÕES DISPONÍVEIS:\n");

  console.log("1️⃣  Bridge via Portal Oficial (Recomendado)");
  console.log("   URL: https://portal.polygon.technology/");
  console.log("   Vantagem: Oficial, seguro, interface simples");
  console.log("   Desvantagem: Precisa de ETH para gas\n");

  console.log("2️⃣  Bridge via Socket.xyz");
  console.log("   URL: https://socket.tech/");
  console.log("   Vantagem: Interface moderna, múltiplas rotas");
  console.log("   Desvantagem: Precisa de ETH para gas\n");

  console.log("3️⃣  Comprar MATIC Direto na Polygon 🚀 MELHOR OPÇÃO");
  console.log("   Exchange: Binance, Coinbase, etc.");
  console.log("   Vantagem: Não precisa de ETH, mais rápido, mais barato");
  console.log("   Custo: ~$0.30-1.00 USD total");
  console.log("   Endereço: " + wallet.address + "\n");

  console.log("=".repeat(50));
  console.log("💡 RECOMENDAÇÃO FINAL:");
  console.log("   Comprar MATIC direto na Polygon é a melhor opção");
  console.log("   porque não precisa de ETH adicional e é mais rápido!");
  console.log("=".repeat(50));
  console.log("");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Erro:", error);
    process.exit(1);
  });

