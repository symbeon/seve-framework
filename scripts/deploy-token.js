const hre = require("hardhat");

async function main() {
  console.log("🚀 Deploying SEVE Token...");
  
  const SEVEToken = await hre.ethers.getContractFactory("SEVEToken");
  const seveToken = await SEVEToken.deploy();
  
  await seveToken.deployed();
  
  console.log("✅ SEVE Token deployed to:", seveToken.address);
  console.log("📊 Transaction hash:", seveToken.deployTransaction.hash);
  
  // Save deployment info
  const deploymentInfo = {
    contract: "SEVEToken",
    address: seveToken.address,
    transactionHash: seveToken.deployTransaction.hash,
    network: hre.network.name,
    timestamp: new Date().toISOString()
  };
  
  const fs = require('fs');
  const deploymentsFile = `deployments/${hre.network.name}_deployments.json`;
  
  let deployments = {};
  if (fs.existsSync(deploymentsFile)) {
    deployments = JSON.parse(fs.readFileSync(deploymentsFile, 'utf8'));
  }
  
  deployments.SEVEToken = deploymentInfo;
  
  fs.writeFileSync(deploymentsFile, JSON.stringify(deployments, null, 2));
  
  console.log("📄 Deployment info saved to:", deploymentsFile);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Deployment failed:", error);
    process.exit(1);
  });
