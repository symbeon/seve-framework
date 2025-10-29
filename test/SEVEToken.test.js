const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("SEVEToken", function () {
  let seveToken;
  let owner;
  let addr1;
  let addr2;

  beforeEach(async function () {
    [owner, addr1, addr2] = await ethers.getSigners();
    
    const SEVEToken = await ethers.getContractFactory("SEVEToken");
    seveToken = await SEVEToken.deploy();
    await seveToken.waitForDeployment();
  });

  describe("Deployment", function () {
    it("Should set the correct total supply", async function () {
      const totalSupply = await seveToken.totalSupply();
      expect(totalSupply).to.equal(ethers.parseEther("1000000000")); // 1 billion tokens
    });

    it("Should set the correct name and symbol", async function () {
      expect(await seveToken.name()).to.equal("SEVE Token");
      expect(await seveToken.symbol()).to.equal("SEVE");
    });

    it("Should set the correct decimals", async function () {
      expect(await seveToken.decimals()).to.equal(18);
    });
  });

  describe("Staking", function () {
    it("Should allow users to stake tokens", async function () {
      const stakeAmount = ethers.parseEther("1000");
      
      await seveToken.stake(stakeAmount);
      
      const stakedAmount = await seveToken.stakedAmount(owner.address);
      expect(stakedAmount).to.equal(stakeAmount);
    });

    it("Should calculate staking rewards correctly", async function () {
      const stakeAmount = ethers.parseEther("1000");
      
      await seveToken.stake(stakeAmount);
      
      // Fast forward time (simulate 1 year)
      await network.provider.send("evm_increaseTime", [365 * 24 * 60 * 60]);
      await network.provider.send("evm_mine");
      
      const rewards = await seveToken.calculateStakingRewards(owner.address);
      const expectedRewards = (stakeAmount * 10n) / 100n; // 10% APY
      
      expect(rewards).to.be.closeTo(expectedRewards, ethers.parseEther("1"));
    });
  });

  describe("Governance Staking", function () {
    it("Should allow users to stake for governance", async function () {
      const stakeAmount = ethers.parseEther("500");
      
      await seveToken.stakeForGovernance(stakeAmount);
      
      const governanceStakedAmount = await seveToken.governanceStakedAmount(owner.address);
      expect(governanceStakedAmount).to.equal(stakeAmount);
    });

    it("Should calculate voting power correctly", async function () {
      const stakeAmount = ethers.parseEther("1000");
      const governanceAmount = ethers.parseEther("500");
      
      await seveToken.stake(stakeAmount);
      await seveToken.stakeForGovernance(governanceAmount);
      
      const votingPower = await seveToken.getVotingPower(owner.address);
      expect(votingPower).to.equal(stakeAmount + governanceAmount);
    });
  });
});
