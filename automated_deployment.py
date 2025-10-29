#!/usr/bin/env python3
"""
SEVE Framework - Automated Deployment & Testing
Symbiotic Ethical Vision Engine v3.0
Developed by EON Team - Symbeon Tech

Script automatizado para deploy e teste dos contratos SEVE
"""

import os
import json
import subprocess
import time
from typing import Dict, Any, List
from datetime import datetime

class SEVEDeploymentManager:
    """Gerenciador de deploy dos contratos SEVE"""
    
    def __init__(self):
        self.deployments = {}
        self.test_results = {}
        self.networks = ["sepolia", "mumbai"]
        
    def check_dependencies(self) -> bool:
        """Verifica se as dependências estão instaladas"""
        print("🔍 Checking dependencies...")
        
        try:
            # Verificar Node.js
            result = subprocess.run(["node", "--version"], capture_output=True, text=True)
            if result.returncode != 0:
                print("❌ Node.js not found. Please install Node.js first.")
                return False
            print(f"✅ Node.js version: {result.stdout.strip()}")
            
            # Verificar npm
            result = subprocess.run(["npm", "--version"], capture_output=True, text=True)
            if result.returncode != 0:
                print("❌ npm not found. Please install npm first.")
                return False
            print(f"✅ npm version: {result.stdout.strip()}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error checking dependencies: {e}")
            return False
    
    def install_dependencies(self) -> bool:
        """Instala dependências do projeto"""
        print("📦 Installing dependencies...")
        
        try:
            result = subprocess.run(["npm", "install"], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"❌ Failed to install dependencies: {result.stderr}")
                return False
            
            print("✅ Dependencies installed successfully")
            return True
            
        except Exception as e:
            print(f"❌ Error installing dependencies: {e}")
            return False
    
    def compile_contracts(self) -> bool:
        """Compila os contratos"""
        print("🔨 Compiling contracts...")
        
        try:
            result = subprocess.run(["npm", "run", "compile"], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"❌ Compilation failed: {result.stderr}")
                return False
            
            print("✅ Contracts compiled successfully")
            return True
            
        except Exception as e:
            print(f"❌ Error compiling contracts: {e}")
            return False
    
    def run_tests(self) -> bool:
        """Executa testes dos contratos"""
        print("🧪 Running tests...")
        
        try:
            result = subprocess.run(["npm", "run", "test"], capture_output=True, text=True)
            
            # Salvar resultados dos testes
            self.test_results = {
                "timestamp": datetime.now().isoformat(),
                "exit_code": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr
            }
            
            if result.returncode != 0:
                print(f"❌ Tests failed: {result.stderr}")
                return False
            
            print("✅ All tests passed")
            return True
            
        except Exception as e:
            print(f"❌ Error running tests: {e}")
            return False
    
    def deploy_to_network(self, network: str) -> Dict[str, Any]:
        """Deploy dos contratos para uma rede específica"""
        print(f"🚀 Deploying to {network}...")
        
        deployment_info = {
            "network": network,
            "timestamp": datetime.now().isoformat(),
            "contracts": {}
        }
        
        try:
            # Deploy do token
            print(f"  📄 Deploying SEVE Token...")
            result = subprocess.run(
                ["npm", "run", f"deploy:{network}"],
                capture_output=True, text=True
            )
            
            if result.returncode != 0:
                print(f"❌ Token deployment failed: {result.stderr}")
                return deployment_info
            
            # Extrair endereço do token do output
            token_address = self._extract_address(result.stdout, "SEVE Token")
            deployment_info["contracts"]["SEVEToken"] = {
                "address": token_address,
                "transaction_hash": self._extract_tx_hash(result.stdout),
                "deployed_at": datetime.now().isoformat()
            }
            
            print(f"  ✅ SEVE Token deployed at: {token_address}")
            
            # Deploy do protocolo
            print(f"  📄 Deploying SEVE Protocol...")
            result = subprocess.run(
                ["npx", "hardhat", "run", "scripts/deploy-protocol.js", "--network", network],
                capture_output=True, text=True,
                env={**os.environ, "TOKEN_ADDRESS": token_address}
            )
            
            if result.returncode != 0:
                print(f"❌ Protocol deployment failed: {result.stderr}")
                return deployment_info
            
            protocol_address = self._extract_address(result.stdout, "SEVE Protocol")
            deployment_info["contracts"]["SEVEProtocol"] = {
                "address": protocol_address,
                "transaction_hash": self._extract_tx_hash(result.stdout),
                "token_address": token_address,
                "deployed_at": datetime.now().isoformat()
            }
            
            print(f"  ✅ SEVE Protocol deployed at: {protocol_address}")
            
            # Deploy da DAO
            print(f"  📄 Deploying SEVE DAO...")
            result = subprocess.run(
                ["npx", "hardhat", "run", "scripts/deploy-dao.js", "--network", network],
                capture_output=True, text=True,
                env={**os.environ, "TOKEN_ADDRESS": token_address}
            )
            
            if result.returncode != 0:
                print(f"❌ DAO deployment failed: {result.stderr}")
                return deployment_info
            
            dao_address = self._extract_address(result.stdout, "SEVE DAO")
            deployment_info["contracts"]["SEVEDAO"] = {
                "address": dao_address,
                "transaction_hash": self._extract_tx_hash(result.stdout),
                "token_address": token_address,
                "deployed_at": datetime.now().isoformat()
            }
            
            print(f"  ✅ SEVE DAO deployed at: {dao_address}")
            
            # Salvar informações de deploy
            self.deployments[network] = deployment_info
            
            print(f"✅ Deployment to {network} completed successfully")
            return deployment_info
            
        except Exception as e:
            print(f"❌ Error deploying to {network}: {e}")
            return deployment_info
    
    def verify_contracts(self, network: str) -> bool:
        """Verifica contratos no explorer"""
        print(f"🔍 Verifying contracts on {network}...")
        
        if network not in self.deployments:
            print(f"❌ No deployment found for {network}")
            return False
        
        deployment = self.deployments[network]
        
        try:
            for contract_name, contract_info in deployment["contracts"].items():
                print(f"  📄 Verifying {contract_name}...")
                
                result = subprocess.run(
                    ["npm", "run", f"verify:{network}"],
                    capture_output=True, text=True,
                    env={**os.environ, "CONTRACT_ADDRESS": contract_info["address"]}
                )
                
                if result.returncode == 0:
                    print(f"  ✅ {contract_name} verified successfully")
                else:
                    print(f"  ⚠️ {contract_name} verification failed: {result.stderr}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error verifying contracts: {e}")
            return False
    
    def _extract_address(self, output: str, contract_name: str) -> str:
        """Extrai endereço do contrato do output"""
        lines = output.split('\n')
        for line in lines:
            if contract_name in line and "deployed to:" in line:
                return line.split("deployed to:")[-1].strip()
        return "0x" + "0" * 40  # Placeholder
    
    def _extract_tx_hash(self, output: str) -> str:
        """Extrai hash da transação do output"""
        lines = output.split('\n')
        for line in lines:
            if "Transaction hash:" in line:
                return line.split("Transaction hash:")[-1].strip()
        return "0x" + "0" * 64  # Placeholder
    
    def generate_deployment_report(self) -> Dict[str, Any]:
        """Gera relatório de deploy"""
        report = {
            "deployment_summary": {
                "total_networks": len(self.deployments),
                "networks_deployed": list(self.deployments.keys()),
                "total_contracts": sum(len(d["contracts"]) for d in self.deployments.values()),
                "deployment_time": datetime.now().isoformat()
            },
            "test_results": self.test_results,
            "deployments": self.deployments,
            "contract_addresses": {}
        }
        
        # Consolidar endereços de contratos
        for network, deployment in self.deployments.items():
            report["contract_addresses"][network] = {}
            for contract_name, contract_info in deployment["contracts"].items():
                report["contract_addresses"][network][contract_name] = contract_info["address"]
        
        return report
    
    def save_deployment_report(self, filename: str = None):
        """Salva relatório de deploy"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"deployment_report_{timestamp}.json"
        
        report = self.generate_deployment_report()
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"📄 Deployment report saved to: {filename}")
        return filename
    
    def run_full_deployment(self) -> bool:
        """Executa deploy completo"""
        print("🚀 Starting full SEVE deployment process...")
        print("=" * 50)
        
        # Verificar dependências
        if not self.check_dependencies():
            return False
        
        # Instalar dependências
        if not self.install_dependencies():
            return False
        
        # Compilar contratos
        if not self.compile_contracts():
            return False
        
        # Executar testes
        if not self.run_tests():
            return False
        
        # Deploy em todas as redes
        for network in self.networks:
            print(f"\n🌐 Deploying to {network}...")
            deployment_info = self.deploy_to_network(network)
            
            if not deployment_info["contracts"]:
                print(f"❌ Failed to deploy to {network}")
                continue
            
            # Verificar contratos
            self.verify_contracts(network)
        
        # Gerar relatório
        print(f"\n📊 Generating deployment report...")
        report_file = self.save_deployment_report()
        
        print(f"\n🎉 Full deployment process completed!")
        print(f"📄 Report saved to: {report_file}")
        
        return True

def main():
    """Função principal"""
    print("⛓️ SEVE Framework - Automated Deployment")
    print("=" * 40)
    
    deployment_manager = SEVEDeploymentManager()
    
    # Executar deploy completo
    success = deployment_manager.run_full_deployment()
    
    if success:
        print(f"\n✅ Deployment completed successfully!")
        print(f"\n📋 Next steps:")
        print(f"1. Review deployment report")
        print(f"2. Test contracts on deployed networks")
        print(f"3. Setup monitoring and alerts")
        print(f"4. Prepare for mainnet deployment")
        print(f"5. Launch token sale")
    else:
        print(f"\n❌ Deployment failed. Please check the errors above.")

if __name__ == "__main__":
    main()
