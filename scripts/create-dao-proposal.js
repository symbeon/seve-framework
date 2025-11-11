const hre = require("hardhat");
const fs = require("fs");
const path = require("path");

/**
 * Script para criar primeira proposta no SEVE DAO
 * Estabelece governança ativa do protocolo
 */

async function main() {
  console.log("🗳️  Criando Proposta no SEVE DAO...\n");

  // Carregar deployments
  const deploymentsPath = path.join(__dirname, "../deployments/sepolia_deployments.json");
  
  if (!fs.existsSync(deploymentsPath)) {
    console.error("❌ Arquivo de deployments não encontrado!");
    process.exit(1);
  }

  const deployments = JSON.parse(fs.readFileSync(deploymentsPath, "utf8"));
  
  if (!deployments.SEVEDAO) {
    console.error("❌ SEVE DAO não encontrado nos deployments!");
    process.exit(1);
  }

  const daoAddress = deployments.SEVEDAO.address;
  const [owner] = await hre.ethers.getSigners();

  console.log("📧 Endereço do Owner:", owner.address);
  console.log("🔗 DAO Address:", daoAddress);
  console.log("🌐 Network:", hre.network.name);
  console.log("\n");

  // Conectar ao contrato
  const SEVEDAO = await hre.ethers.getContractFactory("SEVEDAO");
  const dao = SEVEDAO.attach(daoAddress);

  // Parâmetros da proposta
  const title = "Aprovar Licenciamento Comercial de SEVE Framework v1.0.0";
  const description = `Proposta para aprovar o licenciamento comercial do SEVE Framework v1.0.0 através do protocolo blockchain.

Esta proposta estabelece:
- Preço de licenciamento: 1000 SEVE tokens/ano
- Versão disponível: v1.0.0 (Production Ready)
- Modelo de licenciamento: Baseado em duração (mensal, trimestral, anual)
- Receita será utilizada para desenvolvimento contínuo do framework

A aprovação desta proposta ativa a linha de monetização do SEVE Framework, permitindo que empresas e desenvolvedores licenciem o framework para uso em produção.`;
  
  const proposalType = 0; // TECHNICAL
  const data = "0x"; // Sem dados adicionais

  console.log("📋 Parâmetros da Proposta:");
  console.log("   Título:", title);
  console.log("   Tipo:", proposalType === 0 ? "TECHNICAL" : proposalType === 1 ? "FINANCIAL" : "GOVERNANCE");
  console.log("\n");

  try {
    // Criar proposta
    console.log("⏳ Criando proposta no DAO...");
    const tx = await dao.createProposal(title, description, proposalType, data);
    console.log("📤 Transaction enviada:", tx.hash);
    
    console.log("⏳ Aguardando confirmação...");
    const receipt = await tx.wait();
    
    // Obter ID da proposta (será o próximo proposalCount)
    const proposalCount = await dao.proposalCount();
    const proposalId = proposalCount - 1n;
    
    console.log("✅ Proposta criada com sucesso!");
    console.log("📊 Proposal ID:", proposalId.toString());
    console.log("📊 Block Number:", receipt.blockNumber);
    console.log("⛽ Gas Used:", receipt.gasUsed.toString());
    
    // Verificar proposta
    const proposal = await dao.proposals(proposalId);
    console.log("\n📋 Proposta Verificada:");
    console.log("   Título:", proposal.title);
    console.log("   Tipo:", proposal.proposalType === 0 ? "TECHNICAL" : proposal.proposalType === 1 ? "FINANCIAL" : "GOVERNANCE");
    console.log("   Status:", proposal.executed ? "Executada" : "Ativa");
    console.log("   Votos a Favor:", hre.ethers.formatEther(proposal.votesFor), "SEVE");
    console.log("   Votos Contra:", hre.ethers.formatEther(proposal.votesAgainst), "SEVE");
    
    console.log("\n🎉 Governança ativada! Proposta criada e pronta para votação.");
    console.log("\n📚 Próximos passos:");
    console.log("   1. Fazer stake de tokens para votar: npm run token:stake-governance");
    console.log("   2. Votar na proposta: npm run dao:vote");
    console.log("   3. Executar proposta após aprovação: npm run dao:execute");
  } catch (error) {
    console.error("❌ Erro ao criar proposta:", error.message);
    if (error.data) {
      console.error("   Data:", error.data);
    }
    throw error;
  }
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Erro:", error);
    process.exit(1);
  });

