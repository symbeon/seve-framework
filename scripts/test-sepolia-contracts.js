const hre = require("hardhat");
const fs = require("fs");
const path = require("path");

/**
 * Script para testar contratos deployados na Sepolia
 * Valida funcionalidades básicas sem usar framework de testes
 */

async function main() {
  console.log("🧪 Testando Contratos Deployados na Sepolia...\n");

  // Carregar deployments
  const deploymentsPath = path.join(__dirname, "../deployments/sepolia_deployments.json");
  
  if (!fs.existsSync(deploymentsPath)) {
    console.error("❌ Arquivo de deployments não encontrado!");
    console.error("   Execute o deploy primeiro: npm run deploy:sepolia");
    process.exit(1);
  }

  const deployments = JSON.parse(fs.readFileSync(deploymentsPath, "utf8"));
  const [owner] = await hre.ethers.getSigners();

  console.log("📧 Endereço do Owner:", owner.address);
  console.log("📊 Deployments encontrados:\n");

  // Conectar aos contratos
  const SEVEToken = await hre.ethers.getContractFactory("SEVEToken");
  const SEVEProtocol = await hre.ethers.getContractFactory("SEVEProtocol");
  const SEVEDAO = await hre.ethers.getContractFactory("SEVEDAO");

  console.log("1️⃣  SEVE Token:", deployments.SEVEToken.address);
  console.log("2️⃣  SEVE Protocol:", deployments.SEVEProtocol.address);
  console.log("3️⃣  SEVE DAO:", deployments.SVEDAO.address);
  console.log("\n");

  const seveToken = SEVEToken.attach(deployments.SEVEToken.address);
  const seveProtocol = SEVEProtocol.attach(deployments.SEVEProtocol.address);
  const seveDAO = SEVEDAO.attach(deployments.SVEDAO.address);

  // Testes do Token
  console.log("🔍 Testando SEVE Token...");
  try {
    const name = await seveToken.name();
    const symbol = await seveToken.symbol();
    const totalSupply = await seveToken.totalSupply();
    const ownerBalance = await seveToken.balanceOf(owner.address);

    console.log("   ✅ Nome:", name);
    console.log("   ✅ Símbolo:", symbol);
    console.log("   ✅ Total Supply:", hre.ethers.formatEther(totalSupply), "SEVE");
    console.log("   ✅ Saldo do Owner:", hre.ethers.formatEther(ownerBalance), "SEVE");
  } catch (error) {
    console.error("   ❌ Erro ao testar Token:", error.message);
  }

  // Testes do Protocol
  console.log("\n🔍 Testando SEVE Protocol...");
  try {
    const tokenAddress = await seveProtocol.seveToken();
    const totalLicenses = await seveProtocol.totalLicensesSold();
    const totalRevenue = await seveProtocol.totalRevenue();

    console.log("   ✅ Token Address:", tokenAddress);
    console.log("   ✅ Licenças Vendidas:", totalLicenses.toString());
    console.log("   ✅ Receita Total:", hre.ethers.formatEther(totalRevenue), "SEVE");
  } catch (error) {
    console.error("   ❌ Erro ao testar Protocol:", error.message);
  }

  // Testes do DAO
  console.log("\n🔍 Testando SEVE DAO...");
  try {
    const tokenAddress = await seveDAO.seveToken();
    const proposalCount = await seveDAO.proposalCount();
    const votingPeriod = await seveDAO.votingPeriod();

    console.log("   ✅ Token Address:", tokenAddress);
    console.log("   ✅ Propostas Criadas:", proposalCount.toString());
    console.log("   ✅ Período de Votação:", votingPeriod.toString(), "segundos");
  } catch (error) {
    console.error("   ❌ Erro ao testar DAO:", error.message);
  }

  // Teste de Transferência
  console.log("\n🔍 Testando Transferência de Tokens...");
  try {
    const testAmount = hre.ethers.parseEther("100");
    const [owner, addr1] = await hre.ethers.getSigners();
    
    const balanceBefore = await seveToken.balanceOf(addr1.address);
    await seveToken.transfer(addr1.address, testAmount);
    const balanceAfter = await seveToken.balanceOf(addr1.address);

    console.log("   ✅ Transferência realizada!");
    console.log("   ✅ Saldo antes:", hre.ethers.formatEther(balanceBefore), "SEVE");
    console.log("   ✅ Saldo depois:", hre.ethers.formatEther(balanceAfter), "SEVE");
  } catch (error) {
    console.error("   ❌ Erro ao transferir:", error.message);
  }

  console.log("\n✅ Testes concluídos!");
  console.log("\n📚 Verifique os contratos no explorer:");
  console.log("   Token: https://sepolia.etherscan.io/address/" + deployments.SEVEToken.address);
  console.log("   Protocol: https://sepolia.etherscan.io/address/" + deployments.SEVEProtocol.address);
  console.log("   DAO: https://sepolia.etherscan.io/address/" + deployments.SVEDAO.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Erro:", error);
    process.exit(1);
  });
