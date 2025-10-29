const hre = require("hardhat");

async function main() {
  console.log("🚀 Deploying SEVE Protocol...");
  
  // Get token address from command line or deployments
  const tokenAddress = process.env.TOKEN_ADDRESS || process.argv[2];
  
  if (!tokenAddress) {
    throw new Error("Token address is required");
  }
  
  const SEVEProtocol = await hre.ethers.getContractFactory("SEVEProtocol");
  const seveProtocol = await SEVEProtocol.deploy(tokenAddress);
  
  await seveProtocol.deployed();
  
  console.log("✅ SEVE Protocol deployed to:", seveProtocol.address);
  console.log("📊 Transaction hash:", seveProtocol.deployTransaction.hash);
  console.log("🔗 Token address:", tokenAddress);
  
  // Save deployment info
  const deploymentInfo = {
    contract: "SEVEProtocol",
    address: seveProtocol.address,
    transactionHash: seveProtocol.deployTransaction.hash,
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
  
  deployments.SEVEProtocol = deploymentInfo;
  
  fs.writeFileSync(deploymentsFile, JSON.stringify(deployments, null, 2));
  
  console.log("📄 Deployment info saved to:", deploymentsFile);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Deployment failed:", error);
    process.exit(1);
  });
