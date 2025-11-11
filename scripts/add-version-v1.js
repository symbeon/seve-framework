const hre = require("hardhat");
const fs = require("fs");
const path = require("path");

/**
 * Script para adicionar versão v1.0.0 ao SEVE Protocol
 * Ativa monetização imediata do framework
 */

async function main() {
  console.log("🚀 Adicionando SEVE Framework v1.0.0 ao Protocolo...\n");

  // Carregar deployments
  const deploymentsPath = path.join(__dirname, "../deployments/sepolia_deployments.json");
  
  if (!fs.existsSync(deploymentsPath)) {
    console.error("❌ Arquivo de deployments não encontrado!");
    console.error("   Execute o deploy primeiro: npm run deploy:sepolia");
    process.exit(1);
  }

  const deployments = JSON.parse(fs.readFileSync(deploymentsPath, "utf8"));
  
  if (!deployments.SEVEProtocol) {
    console.error("❌ SEVE Protocol não encontrado nos deployments!");
    process.exit(1);
  }

  const protocolAddress = deployments.SEVEProtocol.address;
  const [owner] = await hre.ethers.getSigners();

  console.log("📧 Endereço do Owner:", owner.address);
  console.log("🔗 Protocol Address:", protocolAddress);
  console.log("🌐 Network:", hre.network.name);
  console.log("\n");

  // Conectar ao contrato
  const SEVEProtocol = await hre.ethers.getContractFactory("SEVEProtocol");
  const protocol = SEVEProtocol.attach(protocolAddress);

  // Parâmetros da versão
  const version = "v1.0.0";
  const price = hre.ethers.parseEther("1000"); // 1000 SEVE tokens por ano
  const codeHash = hre.ethers.keccak256(
    hre.ethers.toUtf8Bytes("SEVE_FRAMEWORK_v1.0.0_PRODUCTION")
  );
  const description = "SEVE Framework v1.0.0 - Production Ready Release with Ethical Validation, Privacy by Design, and Universal Domain Adaptation";

  console.log("📋 Parâmetros da Versão:");
  console.log("   Versão:", version);
  console.log("   Preço Anual:", hre.ethers.formatEther(price), "SEVE");
  console.log("   Code Hash:", codeHash);
  console.log("   Descrição:", description);
  console.log("\n");

  try {
    // Verificar se versão já existe
    const versionInfo = await protocol.versionPricing(version);
    if (versionInfo.available) {
      console.log("⚠️  Versão já existe e está disponível!");
      console.log("   Preço atual:", hre.ethers.formatEther(versionInfo.price), "SEVE");
      return;
    }
  } catch (error) {
    // Versão não existe, continuar
  }

  // Adicionar versão
  console.log("⏳ Adicionando versão ao protocolo...");
  const tx = await protocol.addVersion(version, price, codeHash, description);
  console.log("📤 Transaction enviada:", tx.hash);
  
  console.log("⏳ Aguardando confirmação...");
  const receipt = await tx.wait();
  
  console.log("✅ Versão v1.0.0 adicionada com sucesso!");
  console.log("📊 Block Number:", receipt.blockNumber);
  console.log("⛽ Gas Used:", receipt.gasUsed.toString());
  
  // Verificar versão adicionada
  const versionInfo = await protocol.versionPricing(version);
  console.log("\n📋 Versão Verificada:");
  console.log("   Disponível:", versionInfo.available);
  console.log("   Preço:", hre.ethers.formatEther(versionInfo.price), "SEVE");
  console.log("   Descrição:", versionInfo.description);
  
  console.log("\n🎉 Monetização ativada! Versão v1.0.0 está disponível para licenciamento.");
  console.log("\n📚 Próximos passos:");
  console.log("   1. Criar proposta no DAO: npm run dao:proposal");
  console.log("   2. Registrar primeiro agente: npm run agent:register");
  console.log("   3. Testar compra de licença: npm run license:purchase");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Erro:", error);
    process.exit(1);
  });

