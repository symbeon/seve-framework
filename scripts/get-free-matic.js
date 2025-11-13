require("dotenv").config();

/**
 * Script para ajudar a obter MATIC grátis via faucets
 * Lista faucets disponíveis e instruções
 */

console.log("🚰 Faucets de MATIC para Polygon\n");
console.log("=".repeat(50));
console.log("📋 FAUCETS DISPONÍVEIS:\n");

console.log("1️⃣  Alchemy Faucet");
console.log("   URL: https://www.alchemy.com/faucets/ethereum-goerli");
console.log("   Requer: Conta Alchemy (grátis)");
console.log("   Dá: Varia (pode ter Polygon)\n");

console.log("2️⃣  QuickNode Faucet");
console.log("   URL: https://faucet.quicknode.com/");
console.log("   Requer: Conta QuickNode (grátis)");
console.log("   Dá: Varia (pode ter Polygon)\n");

console.log("3️⃣  Polygon Faucet Oficial");
console.log("   URL: https://faucet.polygon.technology/");
console.log("   Requer: Pode ter limitações");
console.log("   Dá: 0.1-0.5 MATIC\n");

console.log("4️⃣  Comunidade");
console.log("   Discord: https://discord.gg/polygon");
console.log("   Reddit: r/polygonnetwork");
console.log("   Twitter: @0xPolygon");
console.log("   Dá: Varia (pedir ajuda)\n");

console.log("=".repeat(50));
console.log("💡 DICA:");
console.log("   Tente múltiplos faucets para acumular MATIC");
console.log("   Pode levar alguns dias, mas é grátis!\n");

console.log("📧 Seu endereço:");
if (process.env.PRIVATE_KEY) {
  const { ethers } = require("ethers");
  const wallet = new ethers.Wallet(process.env.PRIVATE_KEY);
  console.log(`   ${wallet.address}\n`);
  console.log("   Use este endereço nos faucets!\n");
} else {
  console.log("   Configure PRIVATE_KEY no .env\n");
}

console.log("✅ Alternativa: Continuar usando Sepolia");
console.log("   Você já tem tudo funcionando lá!");
console.log("   Pode usar até conseguir MATIC para Polygon\n");

