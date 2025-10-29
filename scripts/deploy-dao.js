const hre = require("hardhat");

async function main() {
  console.log("🚀 Deploying SEVE DAO...");
  
  // Get token address from command line or deployments
  const tokenAddress = process.env.TOKEN_ADDRESS || process.argv[2];
  
  if (!tokenAddress) {
    throw new Error("Token address is required");
  }
  
  const SEVEDAO = await hre.ethers.getContractFactory("SEVEDAO");
  const seveDAO = await SEVEDAO.deploy(tokenAddress);
  
  await seveDAO.deployed();
  
  console.log("✅ SEVE DAO deployed to:", seveDAO.address);
  console.log("📊 Transaction hash:", seveDAO.deployTransaction.hash);
  console.log("🔗 Token address:", tokenAddress);
  
  // Save deployment info
  const deploymentInfo = {
    contract: "SEVEDAO",
    address: seveDAO.address,
    transactionHash: seveDAO.deployTransaction.hash,
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
