const hre = require("hardhat");
const fs = require("fs");
const path = require("path");

/**
 * Script para registrar primeiro agente de IA ética no SEVE Protocol
 * Demonstra funcionalidade de registro de agentes
 */

async function main() {
  console.log("🤖 Registrando Primeiro Agente de IA Ética...\n");

  // Carregar deployments
  const deploymentsPath = path.join(__dirname, "../deployments/sepolia_deployments.json");
  
  if (!fs.existsSync(deploymentsPath)) {
    console.error("❌ Arquivo de deployments não encontrado!");
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

  // Parâmetros do agente
  const capabilities = "Ethical AI Validation, LGPD/GDPR Compliance, Bias Detection, Privacy by Design, Cultural Adaptation";
  const agentHash = hre.ethers.keccak256(
    hre.ethers.toUtf8Bytes("SEVE_ETHICS_AGENT_v1.0.0_PRODUCTION")
  );
  const metadata = JSON.stringify({
    name: "SEVE-Ethics Module",
    version: "1.0.0",
    description: "Automated Ethical Validation Agent for SEVE Framework",
    capabilities: [
      "Real-time ethical validation (<120ms)",
      "LGPD/GDPR/AI Act compliance (98% automated)",
      "Bias detection and mitigation",
      "Privacy by Design enforcement",
      "Blockchain audit trail"
    ],
    performance: {
      latency: "78ms average",
      compliance_coverage: "98%",
      accuracy: "95%+"
    }
  });

  console.log("📋 Parâmetros do Agente:");
  console.log("   Capabilities:", capabilities);
  console.log("   Agent Hash:", agentHash);
  console.log("   Metadata:", metadata.substring(0, 100) + "...");
  console.log("\n");

  try {
    // Verificar se agente já está registrado
    const existingAgent = await protocol.agents(owner.address);
    if (existingAgent.agentHash !== "0x0000000000000000000000000000000000000000000000000000000000000000") {
      console.log("⚠️  Agente já está registrado para este endereço!");
      console.log("   Agent Hash:", existingAgent.agentHash);
      console.log("   Capabilities:", existingAgent.capabilities);
      return;
    }
  } catch (error) {
    // Agente não existe, continuar
  }

  // Registrar agente
  console.log("⏳ Registrando agente no protocolo...");
  const tx = await protocol.registerAgent(capabilities, agentHash, metadata);
  console.log("📤 Transaction enviada:", tx.hash);
  
  console.log("⏳ Aguardando confirmação...");
  const receipt = await tx.wait();
  
  console.log("✅ Agente registrado com sucesso!");
  console.log("📊 Block Number:", receipt.blockNumber);
  console.log("⛽ Gas Used:", receipt.gasUsed.toString());
  
  // Verificar agente registrado
  const agent = await protocol.agents(owner.address);
  console.log("\n📋 Agente Verificado:");
  console.log("   Endereço:", owner.address);
  console.log("   Capabilities:", agent.capabilities);
  console.log("   Agent Hash:", agent.agentHash);
  console.log("   Verificado:", agent.verified);
  console.log("   Performance Score:", agent.performanceScore.toString());
  
  console.log("\n🎉 Primeiro agente de IA ética registrado!");
  console.log("\n📚 Próximos passos:");
  console.log("   1. Verificar agente: npm run agent:verify");
  console.log("   2. Atualizar performance: npm run agent:update-performance");
  console.log("   3. Listar todos os agentes: npm run agent:list");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Erro:", error);
    process.exit(1);
  });

