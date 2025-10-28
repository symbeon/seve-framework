#!/usr/bin/env python3
"""
SEVE Framework - Modelo Financeiro Blockchain
Symbiotic Ethical Vision Engine v3.0
Developed by EON Team - Symbeon Tech

Este script calcula projeções financeiras detalhadas para o SEVE Protocol
incluindo tokenomics, receitas e valuation.
"""

import json
import pandas as pd
import numpy as np
from typing import Dict, List, Any
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns

@dataclass
class Tokenomics:
    """Estrutura de tokenomics"""
    total_supply: int = 1_000_000_000  # 1 billion tokens
    team_allocation: int = 200_000_000  # 20%
    development_allocation: int = 300_000_000  # 30%
    community_allocation: int = 250_000_000  # 25%
    partnership_allocation: int = 150_000_000  # 15%
    reserve_allocation: int = 100_000_000  # 10%
    
    # Vesting schedules
    team_vesting_months: int = 24
    development_vesting_months: int = 36
    community_vesting_months: int = 12
    partnership_vesting_months: int = 18
    reserve_vesting_months: int = 60

@dataclass
class RevenueStream:
    """Estrutura de fonte de receita"""
    name: str
    year_1: float
    year_2: float
    year_3: float
    year_4: float
    year_5: float
    growth_rate: float = 0.0

@dataclass
class FinancialProjection:
    """Projeção financeira"""
    year: int
    total_revenue: float
    total_costs: float
    net_profit: float
    token_price: float
    market_cap: float
    circulating_supply: int

class SEVEFinancialModel:
    """Modelo financeiro para SEVE Protocol"""
    
    def __init__(self):
        self.tokenomics = Tokenomics()
        self.revenue_streams = self._setup_revenue_streams()
        self.cost_structure = self._setup_cost_structure()
        self.projections = []
        
    def _setup_revenue_streams(self) -> List[RevenueStream]:
        """Configura fontes de receita"""
        return [
            RevenueStream(
                name="Token Sale (ICO/IDO)",
                year_1=15_000_000,  # $15M
                year_2=0,  # One-time
                year_3=0,
                year_4=0,
                year_5=0,
                growth_rate=0.0
            ),
            RevenueStream(
                name="Licensing Revenue",
                year_1=2_000_000,  # $2M
                year_2=10_000_000,  # $10M
                year_3=25_000_000,  # $25M
                year_4=50_000_000,  # $50M
                year_5=100_000_000,  # $100M
                growth_rate=0.5  # 50% growth
            ),
            RevenueStream(
                name="Protocol Fees",
                year_1=500_000,  # $500K
                year_2=5_000_000,  # $5M
                year_3=15_000_000,  # $15M
                year_4=30_000_000,  # $30M
                year_5=60_000_000,  # $60M
                growth_rate=0.4  # 40% growth
            ),
            RevenueStream(
                name="Services Revenue",
                year_1=3_000_000,  # $3M
                year_2=15_000_000,  # $15M
                year_3=30_000_000,  # $30M
                year_4=60_000_000,  # $60M
                year_5=120_000_000,  # $120M
                growth_rate=0.6  # 60% growth
            ),
            RevenueStream(
                name="DeFi Revenue",
                year_1=0,  # Not active in year 1
                year_2=2_000_000,  # $2M
                year_3=10_000_000,  # $10M
                year_4=25_000_000,  # $25M
                year_5=50_000_000,  # $50M
                growth_rate=0.8  # 80% growth
            ),
            RevenueStream(
                name="Venture Capital",
                year_1=0,  # Series A in year 2
                year_2=20_000_000,  # $20M Series A
                year_3=0,
                year_4=50_000_000,  # $50M Series B
                year_5=0,
                growth_rate=0.0
            )
        ]
    
    def _setup_cost_structure(self) -> Dict[str, List[float]]:
        """Configura estrutura de custos"""
        return {
            "Development": [5_000_000, 8_000_000, 12_000_000, 18_000_000, 25_000_000],
            "Marketing": [2_000_000, 5_000_000, 10_000_000, 15_000_000, 20_000_000],
            "Operations": [1_000_000, 2_000_000, 3_000_000, 5_000_000, 8_000_000],
            "Legal & Compliance": [500_000, 1_000_000, 1_500_000, 2_000_000, 3_000_000],
            "Infrastructure": [1_000_000, 2_000_000, 4_000_000, 6_000_000, 10_000_000],
            "Personnel": [3_000_000, 6_000_000, 10_000_000, 15_000_000, 20_000_000],
            "Other": [500_000, 1_000_000, 1_500_000, 2_000_000, 3_000_000]
        }
    
    def calculate_token_price_projection(self) -> Dict[int, float]:
        """Calcula projeção de preço do token"""
        # Baseado em múltiplos de receita e market cap
        price_projections = {
            1: 0.05,   # $0.05 - Market cap $50M
            2: 0.20,   # $0.20 - Market cap $200M
            3: 1.00,   # $1.00 - Market cap $1B
            4: 2.50,   # $2.50 - Market cap $2.5B
            5: 5.00    # $5.00 - Market cap $5B
        }
        return price_projections
    
    def calculate_circulating_supply(self, year: int) -> int:
        """Calcula supply em circulação por ano"""
        # Baseado no vesting schedule
        circulating_percentages = {
            1: 0.15,  # 15% em circulação no ano 1
            2: 0.35,  # 35% em circulação no ano 2
            3: 0.55,  # 55% em circulação no ano 3
            4: 0.75,  # 75% em circulação no ano 4
            5: 0.90   # 90% em circulação no ano 5
        }
        
        percentage = circulating_percentages.get(year, 0.90)
        return int(self.tokenomics.total_supply * percentage)
    
    def generate_financial_projections(self) -> List[FinancialProjection]:
        """Gera projeções financeiras para 5 anos"""
        projections = []
        token_prices = self.calculate_token_price_projection()
        
        for year in range(1, 6):
            # Calcular receita total
            total_revenue = sum(
                getattr(stream, f"year_{year}") for stream in self.revenue_streams
            )
            
            # Calcular custos totais
            total_costs = sum(
                costs[year - 1] for costs in self.cost_structure.values()
            )
            
            # Calcular lucro líquido
            net_profit = total_revenue - total_costs
            
            # Calcular métricas do token
            token_price = token_prices[year]
            circulating_supply = self.calculate_circulating_supply(year)
            market_cap = token_price * circulating_supply
            
            projection = FinancialProjection(
                year=year,
                total_revenue=total_revenue,
                total_costs=total_costs,
                net_profit=net_profit,
                token_price=token_price,
                market_cap=market_cap,
                circulating_supply=circulating_supply
            )
            
            projections.append(projection)
        
        self.projections = projections
        return projections
    
    def calculate_roi_scenarios(self) -> Dict[str, Dict[str, float]]:
        """Calcula cenários de ROI para investidores"""
        scenarios = {
            "Conservative": {
                "year_1_price": 0.03,
                "year_3_price": 0.50,
                "year_5_price": 2.00,
                "roi_3_year": 1567,  # 1567% ROI
                "roi_5_year": 6567   # 6567% ROI
            },
            "Moderate": {
                "year_1_price": 0.05,
                "year_3_price": 1.00,
                "year_5_price": 5.00,
                "roi_3_year": 1900,  # 1900% ROI
                "roi_5_year": 9900   # 9900% ROI
            },
            "Optimistic": {
                "year_1_price": 0.08,
                "year_3_price": 2.00,
                "year_5_price": 10.00,
                "roi_3_year": 2400,  # 2400% ROI
                "roi_5_year": 12400  # 12400% ROI
            }
        }
        return scenarios
    
    def calculate_token_distribution(self) -> Dict[str, Any]:
        """Calcula distribuição de tokens por ano"""
        distribution = {}
        
        for year in range(1, 6):
            year_dist = {
                "team": self._calculate_vested_amount(
                    self.tokenomics.team_allocation,
                    self.tokenomics.team_vesting_months,
                    year
                ),
                "development": self._calculate_vested_amount(
                    self.tokenomics.development_allocation,
                    self.tokenomics.development_vesting_months,
                    year
                ),
                "community": self._calculate_vested_amount(
                    self.tokenomics.community_allocation,
                    self.tokenomics.community_vesting_months,
                    year
                ),
                "partnership": self._calculate_vested_amount(
                    self.tokenomics.partnership_allocation,
                    self.tokenomics.partnership_vesting_months,
                    year
                ),
                "reserve": self._calculate_vested_amount(
                    self.tokenomics.reserve_allocation,
                    self.tokenomics.reserve_vesting_months,
                    year
                )
            }
            
            year_dist["total_circulating"] = sum(year_dist.values())
            distribution[f"year_{year}"] = year_dist
        
        return distribution
    
    def _calculate_vested_amount(self, total_allocation: int, vesting_months: int, year: int) -> int:
        """Calcula quantidade de tokens liberados por ano"""
        months_passed = min(year * 12, vesting_months)
        vested_percentage = months_passed / vesting_months
        return int(total_allocation * vested_percentage)
    
    def generate_funding_roadmap(self) -> Dict[str, Any]:
        """Gera roadmap de financiamento"""
        return {
            "phase_1": {
                "name": "Seed Round",
                "target": "$2M",
                "valuation": "$20M",
                "duration": "3 months",
                "use_of_funds": [
                    "Smart contract development",
                    "Initial team expansion",
                    "Legal and compliance setup",
                    "Marketing and community building"
                ]
            },
            "phase_2": {
                "name": "Private Sale",
                "target": "$5M",
                "valuation": "$50M",
                "duration": "2 months",
                "use_of_funds": [
                    "Protocol development",
                    "Security audits",
                    "Testnet launch",
                    "Partnership development"
                ]
            },
            "phase_3": {
                "name": "Public Sale (IDO)",
                "target": "$10M",
                "valuation": "$100M",
                "duration": "1 month",
                "use_of_funds": [
                    "Mainnet launch",
                    "Exchange listings",
                    "Global marketing",
                    "Team expansion"
                ]
            },
            "phase_4": {
                "name": "Series A",
                "target": "$20M",
                "valuation": "$500M",
                "duration": "6 months",
                "use_of_funds": [
                    "International expansion",
                    "Enterprise partnerships",
                    "R&D investment",
                    "Acquisition opportunities"
                ]
            },
            "phase_5": {
                "name": "Series B",
                "target": "$50M",
                "valuation": "$2B",
                "duration": "12 months",
                "use_of_funds": [
                    "Global market penetration",
                    "Strategic acquisitions",
                    "Advanced R&D",
                    "IPO preparation"
                ]
            }
        }
    
    def create_financial_charts(self):
        """Cria gráficos financeiros"""
        # Configurar estilo
        plt.style.use('seaborn-v0_8')
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('SEVE Protocol - Financial Projections', fontsize=16, fontweight='bold')
        
        # Dados para gráficos
        years = [p.year for p in self.projections]
        revenue = [p.total_revenue / 1_000_000 for p in self.projections]  # Em milhões
        costs = [p.total_costs / 1_000_000 for p in self.projections]
        profit = [p.net_profit / 1_000_000 for p in self.projections]
        token_price = [p.token_price for p in self.projections]
        market_cap = [p.market_cap / 1_000_000_000 for p in self.projections]  # Em bilhões
        
        # Gráfico 1: Receita vs Custos
        axes[0, 0].plot(years, revenue, 'g-', linewidth=2, label='Revenue', marker='o')
        axes[0, 0].plot(years, costs, 'r-', linewidth=2, label='Costs', marker='s')
        axes[0, 0].plot(years, profit, 'b-', linewidth=2, label='Net Profit', marker='^')
        axes[0, 0].set_title('Revenue vs Costs (Millions USD)')
        axes[0, 0].set_xlabel('Year')
        axes[0, 0].set_ylabel('Amount (M USD)')
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        
        # Gráfico 2: Preço do Token
        axes[0, 1].plot(years, token_price, 'purple', linewidth=3, marker='o', markersize=8)
        axes[0, 1].set_title('SEVE Token Price Projection')
        axes[0, 1].set_xlabel('Year')
        axes[0, 1].set_ylabel('Price (USD)')
        axes[0, 1].grid(True, alpha=0.3)
        
        # Gráfico 3: Market Cap
        axes[1, 0].plot(years, market_cap, 'orange', linewidth=3, marker='s', markersize=8)
        axes[1, 0].set_title('Market Capitalization (Billions USD)')
        axes[1, 0].set_xlabel('Year')
        axes[1, 0].set_ylabel('Market Cap (B USD)')
        axes[1, 0].grid(True, alpha=0.3)
        
        # Gráfico 4: Fontes de Receita (Ano 3)
        revenue_streams_year_3 = [
            stream.name for stream in self.revenue_streams
            if getattr(stream, 'year_3', 0) > 0
        ]
        revenue_amounts_year_3 = [
            getattr(stream, 'year_3', 0) / 1_000_000
            for stream in self.revenue_streams
            if getattr(stream, 'year_3', 0) > 0
        ]
        
        axes[1, 1].pie(revenue_amounts_year_3, labels=revenue_streams_year_3, autopct='%1.1f%%')
        axes[1, 1].set_title('Revenue Sources - Year 3 (Millions USD)')
        
        plt.tight_layout()
        plt.savefig('seve_financial_projections.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def generate_financial_report(self) -> Dict[str, Any]:
        """Gera relatório financeiro completo"""
        projections = self.generate_financial_projections()
        token_distribution = self.calculate_token_distribution()
        roi_scenarios = self.calculate_roi_scenarios()
        funding_roadmap = self.generate_funding_roadmap()
        
        report = {
            "executive_summary": {
                "total_revenue_5_years": sum(p.total_revenue for p in projections),
                "total_profit_5_years": sum(p.net_profit for p in projections),
                "peak_market_cap": max(p.market_cap for p in projections),
                "peak_token_price": max(p.token_price for p in projections),
                "total_funding_needed": 87_000_000  # Sum of all funding phases
            },
            "financial_projections": [
                {
                    "year": p.year,
                    "revenue": p.total_revenue,
                    "costs": p.total_costs,
                    "net_profit": p.net_profit,
                    "token_price": p.token_price,
                    "market_cap": p.market_cap,
                    "circulating_supply": p.circulating_supply
                }
                for p in projections
            ],
            "tokenomics": {
                "total_supply": self.tokenomics.total_supply,
                "distribution": token_distribution,
                "vesting_schedules": {
                    "team": f"{self.tokenomics.team_vesting_months} months",
                    "development": f"{self.tokenomics.development_vesting_months} months",
                    "community": f"{self.tokenomics.community_vesting_months} months",
                    "partnership": f"{self.tokenomics.partnership_vesting_months} months",
                    "reserve": f"{self.tokenomics.reserve_vesting_months} months"
                }
            },
            "roi_scenarios": roi_scenarios,
            "funding_roadmap": funding_roadmap,
            "revenue_streams": [
                {
                    "name": stream.name,
                    "year_1": stream.year_1,
                    "year_2": stream.year_2,
                    "year_3": stream.year_3,
                    "year_4": stream.year_4,
                    "year_5": stream.year_5,
                    "growth_rate": stream.growth_rate
                }
                for stream in self.revenue_streams
            ],
            "cost_structure": self.cost_structure,
            "generated_at": datetime.now().isoformat()
        }
        
        return report
    
    def save_financial_report(self, filename: str = None):
        """Salva relatório financeiro"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"seve_financial_report_{timestamp}.json"
        
        report = self.generate_financial_report()
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"📊 Financial report saved to: {filename}")
        return filename

def main():
    """Função principal"""
    print("💰 SEVE Framework - Financial Model")
    print("=" * 40)
    
    # Inicializar modelo financeiro
    financial_model = SEVEFinancialModel()
    
    # Gerar projeções
    print("📈 Generating financial projections...")
    projections = financial_model.generate_financial_projections()
    
    # Mostrar resumo executivo
    print("\n📊 EXECUTIVE SUMMARY")
    print("-" * 30)
    print(f"Total Revenue (5 years): ${sum(p.total_revenue for p in projections):,.0f}")
    print(f"Total Profit (5 years): ${sum(p.net_profit for p in projections):,.0f}")
    print(f"Peak Market Cap: ${max(p.market_cap for p in projections):,.0f}")
    print(f"Peak Token Price: ${max(p.token_price for p in projections):.2f}")
    
    # Mostrar projeções por ano
    print("\n📅 YEARLY PROJECTIONS")
    print("-" * 30)
    for projection in projections:
        print(f"Year {projection.year}:")
        print(f"  Revenue: ${projection.total_revenue:,.0f}")
        print(f"  Costs: ${projection.total_costs:,.0f}")
        print(f"  Profit: ${projection.net_profit:,.0f}")
        print(f"  Token Price: ${projection.token_price:.2f}")
        print(f"  Market Cap: ${projection.market_cap:,.0f}")
        print()
    
    # Mostrar cenários de ROI
    print("🎯 ROI SCENARIOS")
    print("-" * 30)
    roi_scenarios = financial_model.calculate_roi_scenarios()
    for scenario, data in roi_scenarios.items():
        print(f"{scenario}:")
        print(f"  3-Year ROI: {data['roi_3_year']}%")
        print(f"  5-Year ROI: {data['roi_5_year']}%")
        print()
    
    # Salvar relatório
    print("💾 Saving financial report...")
    report_file = financial_model.save_financial_report()
    
    # Criar gráficos
    print("📊 Creating financial charts...")
    financial_model.create_financial_charts()
    
    print(f"\n✅ Financial model completed!")
    print(f"📄 Report saved to: {report_file}")
    print(f"📊 Charts saved as: seve_financial_projections.png")

if __name__ == "__main__":
    main()
