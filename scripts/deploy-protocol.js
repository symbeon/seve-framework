const hre = require("hardhat");

async function main() {
  console.log("🚀 Deploying SEVE Protocol...");
  
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
  
  const SEVEProtocol = await hre.ethers.getContractFactory("SEVEProtocol");
  const seveProtocol = await SEVEProtocol.deploy(tokenAddress);
  
  await seveProtocol.waitForDeployment();
  
  const seveProtocolAddress = await seveProtocol.getAddress();
  const deployTx = seveProtocol.deploymentTransaction();
  
  console.log("✅ SEVE Protocol deployed to:", seveProtocolAddress);
  console.log("📊 Transaction hash:", deployTx?.hash || "N/A");
  console.log("🔗 Token address:", tokenAddress);
  
  // Save deployment info
  const deploymentInfo = {
    contract: "SEVEProtocol",
    address: seveProtocolAddress,
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
