require("dotenv").config();
const { ethers } = require("ethers");

/**
 * Script alternativo usando API de bridge (Socket, LiFi, etc.)
 * Mais simples e rápido que usar contratos diretamente
 */

async function main() {
  console.log("🌉 Bridge via API: Ethereum → Polygon\n");
  console.log("⚠️  Este script usa APIs de bridge de terceiros");
  console.log("💡 Recomendado: Usar bridge oficial ou comprar direto na Polygon\n");

  console.log("📋 OPÇÕES DISPONÍVEIS:\n");

  console.log("1️⃣  Bridge Oficial Polygon (Portal)");
  console.log("   URL: https://portal.polygon.technology/");
  console.log("   Vantagem: Oficial, seguro");
  console.log("   Desvantagem: Demora 10-30 minutos\n");

  console.log("2️⃣  Socket.xyz (API de Bridge)");
  console.log("   URL: https://socket.tech/");
  console.log("   Vantagem: Rápido, múltiplas rotas");
  console.log("   Desvantagem: Requer integração com API\n");

  console.log("3️⃣  LiFi (API de Bridge)");
  console.log("   URL: https://li.fi/");
  console.log("   Vantagem: Agrega múltiplos bridges");
  console.log("   Desvantagem: Requer integração com API\n");

  console.log("4️⃣  Comprar MATIC Direto na Polygon");
  console.log("   Exchange: Binance, Coinbase, etc.");
  console.log("   Vantagem: Mais rápido (sem esperar bridge)");
  console.log("   Desvantagem: Precisa comprar\n");

  console.log("=".repeat(50));
  console.log("💡 RECOMENDAÇÃO:");
  console.log("   Para deploy rápido: Comprar MATIC direto na Polygon");
  console.log("   Para economizar: Fazer bridge via portal oficial");
  console.log("=".repeat(50));
  console.log("");

  console.log("📚 Guias disponíveis:");
  console.log("   - docs/BRIDGE_RAPIDO_MATIC.md");
  console.log("   - docs/BRIDGE_MATIC_POLYGON.md");
  console.log("");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Erro:", error);
    process.exit(1);
  });

