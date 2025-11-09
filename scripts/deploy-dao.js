const hre = require("hardhat");

async function main() {
  console.log("🚀 Deploying SEVE DAO...");
  
  // Get token address from command line, env, or deployments file
  let tokenAddress = process.env.TOKEN_ADDRESS || process.argv[2];
  
  // If not provided, try to read from deployments file
  if (!tokenAddress) {
    const fs = require('fs');
    const deploymentsFile = `deployments/${hre.network.name}_deployments.json`;
    if (fs.existsSync(deploymentsFile)) {
      const deployments = JSON.parse(fs.readFileSync(deploymentsFile, 'utf8'));
      tokenAddress = deployments.SEVEToken?.address;
    }
  }
  
  if (!tokenAddress) {
    throw new Error("Token address is required. Deploy token first or provide TOKEN_ADDRESS env var.");
  }
  
  const SEVEDAO = await hre.ethers.getContractFactory("SEVEDAO");
  const seveDAO = await SEVEDAO.deploy(tokenAddress);
  
  await seveDAO.waitForDeployment();
  
  const seveDAOAddress = await seveDAO.getAddress();
  const deployTx = seveDAO.deploymentTransaction();
  
  console.log("✅ SEVE DAO deployed to:", seveDAOAddress);
  console.log("📊 Transaction hash:", deployTx?.hash || "N/A");
  console.log("🔗 Token address:", tokenAddress);
  
  // Save deployment info
  const deploymentInfo = {
    contract: "SEVEDAO",
    address: seveDAOAddress,
    transactionHash: deployTx?.hash || "N/A",
    tokenAddress: tokenAddress,
    network: hre.network.name,
    timestamp: new Date().toISOString()
  };
  
  const fs = require('fs');
  const deploymentsFile = `deployments/${hre.network.name}_deployments.json`;
  
  let deployments = {};
  if (fs.existsSync(deploymentsFile)) {
    deployments = JSON.parse(fs.readFileSync(deploymentsFile, 'utf8'));
  }
  
  deployments.SEVEDAO = deploymentInfo;
  
  fs.writeFileSync(deploymentsFile, JSON.stringify(deployments, null, 2));
  
  console.log("📄 Deployment info saved to:", deploymentsFile);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Deployment failed:", error);
    process.exit(1);
  });
