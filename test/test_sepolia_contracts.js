const { expect } = require("chai");
const { ethers } = require("hardhat");
const fs = require("fs");
const path = require("path");

/**
 * Testes de Integração para Contratos Deployados na Sepolia
 * 
 * Estes testes validam os contratos já deployados na testnet Sepolia
 * e testam funcionalidades básicas de cada contrato.
 */

describe("SEVE Contracts - Sepolia Integration Tests", function () {
  let deployments;
  let seveToken;
  let seveProtocol;
  let seveDAO;
  let owner;
  let addr1;
  let addr2;

  // Carregar deployments
  before(async function () {
    const deploymentsPath = path.join(__dirname, "../deployments/sepolia_deployments.json");
    
    if (!fs.existsSync(deploymentsPath)) {
      this.skip(); // Pula testes se não houver deployments
    }

    deployments = JSON.parse(fs.readFileSync(deploymentsPath, "utf8"));
    
    [owner, addr1, addr2] = await ethers.getSigners();

    // Conectar aos contratos deployados
    const SEVEToken = await ethers.getContractFactory("SEVEToken");
    const SEVEProtocol = await ethers.getContractFactory("SEVEProtocol");
    const SEVEDAO = await ethers.getContractFactory("SEVEDAO");

    seveToken = SEVEToken.attach(deployments.SEVEToken.address);
    seveProtocol = SEVEProtocol.attach(deployments.SEVEProtocol.address);
    seveDAO = SEVEDAO.attach(deployments.SVEDAO.address);
  });

  describe("SEVE Token", function () {
    it("Should have correct name and symbol", async function () {
      expect(await seveToken.name()).to.equal("SEVE Token");
      expect(await seveToken.symbol()).to.equal("SEVE");
    });

    it("Should have correct total supply", async function () {
      const totalSupply = await seveToken.totalSupply();
      expect(totalSupply).to.equal(ethers.parseEther("1000000000")); // 1 bilhão
    });

    it("Should allow token transfer", async function () {
      const amount = ethers.parseEther("1000");
      await seveToken.transfer(addr1.address, amount);
      
      const balance = await seveToken.balanceOf(addr1.address);
      expect(balance).to.equal(amount);
    });

    it("Should allow staking", async function () {
      const amount = ethers.parseEther("100");
      await seveToken.approve(seveToken.target, amount);
      await seveToken.stake(amount);
      
      const stakedAmount = await seveToken.stakedAmount(owner.address);
      expect(stakedAmount).to.equal(amount);
    });

    it("Should calculate voting power", async function () {
      const votingPower = await seveToken.getVotingPower(owner.address);
      expect(votingPower).to.be.gt(0);
    });
  });

  describe("SEVE Protocol", function () {
    it("Should have correct token address", async function () {
      const tokenAddress = await seveProtocol.seveToken();
      expect(tokenAddress.toLowerCase()).to.equal(
        deployments.SEVEToken.address.toLowerCase()
      );
    });

    it("Should allow adding a version", async function () {
      const version = "1.0.0";
      const price = ethers.parseEther("1000");
      const codeHash = ethers.id("test-code-hash");
      
      await seveProtocol.addVersion(
        version,
        price,
        codeHash,
        "Initial version"
      );
      
      const versionInfo = await seveProtocol.getVersionInfo(version);
      expect(versionInfo.price).to.equal(price);
      expect(versionInfo.available).to.be.true;
    });

    it("Should allow registering an agent", async function () {
      const capabilities = "test-capabilities";
      const agentHash = ethers.id("test-agent-hash");
      const metadata = "test-metadata";
      
      await seveProtocol.connect(addr1).registerAgent(
        capabilities,
        agentHash,
        metadata
      );
      
      const agentInfo = await seveProtocol.getAgentInfo(addr1.address);
      expect(agentInfo.capabilities).to.equal(capabilities);
      expect(agentInfo.agentHash).to.equal(agentHash);
    });
  });

  describe("SEVE DAO", function () {
    it("Should have correct token address", async function () {
      const tokenAddress = await seveDAO.seveToken();
      expect(tokenAddress.toLowerCase()).to.equal(
        deployments.SEVEToken.address.toLowerCase()
      );
    });

    it("Should allow creating a proposal", async function () {
      const title = "Test Proposal";
      const description = "This is a test proposal";
      const proposalType = 0; // TECHNICAL
      
      await seveDAO.createProposal(
        title,
        description,
        proposalType,
        "0x"
      );
      
      const proposal = await seveDAO.getProposal(0);
      expect(proposal.title).to.equal(title);
      expect(proposal.description).to.equal(description);
    });

    it("Should allow voting on a proposal", async function () {
      // Primeiro precisa ter tokens staked para ter voting power
      const amount = ethers.parseEther("1000");
      await seveToken.approve(seveToken.target, amount);
      await seveToken.stakeForGovernance(amount);
      
      // Criar proposta
      await seveDAO.createProposal(
        "Vote Test",
        "Testing voting",
        0,
        "0x"
      );
      
      // Votar
      await seveDAO.vote(0, true);
      
      const vote = await seveDAO.getUserVote(0, owner.address);
      expect(vote.hasVoted).to.be.true;
      expect(vote.support).to.be.true;
    });
  });

  describe("Integration Tests", function () {
    it("Should allow full license purchase flow", async function () {
      // 1. Adicionar versão
      const version = "1.0.0-test";
      const price = ethers.parseEther("100");
      const codeHash = ethers.id("test-hash");
      
      await seveProtocol.addVersion(
        version,
        price,
        codeHash,
        "Test version"
      );
      
      // 2. Aprovar tokens para protocolo
      await seveToken.connect(addr1).approve(seveProtocol.target, price);
      
      // 3. Comprar licença
      await seveProtocol.connect(addr1).purchaseLicense(
        version,
        365, // 1 ano
        "test-capabilities"
      );
      
      // 4. Verificar licença
      const hasLicense = await seveProtocol.hasValidLicense(
        addr1.address,
        version
      );
      expect(hasLicense).to.be.true;
    });
  });
});

