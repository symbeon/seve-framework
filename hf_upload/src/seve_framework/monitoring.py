#!/usr/bin/env python3
"""
SEVE Framework - Sistema de Monitoramento em Tempo Real
Symbiotic Ethical Vision Engine
Developed by EON Team - Symbeon Tech

Este módulo implementa monitoramento em tempo real com métricas,
alertas e dashboards para o SEVE Framework.
"""

import asyncio
import time
import json
import logging
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime, timedelta
import psutil
import threading
from collections import defaultdict, deque
import websockets
import aiohttp

logger = logging.getLogger(__name__)

class MetricType(Enum):
    """Tipos de métricas"""
    COUNTER = "counter"
    GAUGE = "gauge"
    HISTOGRAM = "histogram"
    TIMER = "timer"

class AlertLevel(Enum):
    """Níveis de alerta"""
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"
    EMERGENCY = "emergency"

@dataclass
class Metric:
    """Representa uma métrica"""
    name: str
    value: float
    metric_type: MetricType
    timestamp: datetime = field(default_factory=datetime.now)
    tags: Dict[str, str] = field(default_factory=dict)
    unit: Optional[str] = None

@dataclass
class Alert:
    """Representa um alerta"""
    id: str
    level: AlertLevel
    message: str
    timestamp: datetime = field(default_factory=datetime.now)
    source: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    resolved: bool = False

@dataclass
class HealthStatus:
    """Status de saúde do sistema"""
    component: str
    status: str  # healthy, degraded, unhealthy
    last_check: datetime = field(default_factory=datetime.now)
    metrics: Dict[str, Any] = field(default_factory=dict)
    issues: List[str] = field(default_factory=list)

class MetricsCollector:
    """Coletor de métricas em tempo real"""
    
    def __init__(self):
        self.metrics: Dict[str, deque] = defaultdict(lambda: deque(maxlen=1000))
        self.counters: Dict[str, int] = defaultdict(int)
        self.gauges: Dict[str, float] = {}
        self.histograms: Dict[str, List[float]] = defaultdict(list)
        self.timers: Dict[str, List[float]] = defaultdict(list)
        
    def increment_counter(self, name: str, value: int = 1, tags: Dict[str, str] = None):
        """Incrementa um contador"""
        self.counters[name] += value
        metric = Metric(
            name=name,
            value=self.counters[name],
            metric_type=MetricType.COUNTER,
            tags=tags or {}
        )
        self.metrics[name].append(metric)
    
    def set_gauge(self, name: str, value: float, tags: Dict[str, str] = None):
        """Define um gauge"""
        self.gauges[name] = value
        metric = Metric(
            name=name,
            value=value,
            metric_type=MetricType.GAUGE,
            tags=tags or {}
        )
        self.metrics[name].append(metric)
    
    def record_histogram(self, name: str, value: float, tags: Dict[str, str] = None):
        """Registra um valor em histograma"""
        self.histograms[name].append(value)
        # Manter apenas os últimos 1000 valores
        if len(self.histograms[name]) > 1000:
            self.histograms[name] = self.histograms[name][-1000:]
        
        metric = Metric(
            name=name,
            value=value,
            metric_type=MetricType.HISTOGRAM,
            tags=tags or {}
        )
        self.metrics[name].append(metric)
    
    def record_timer(self, name: str, duration_ms: float, tags: Dict[str, str] = None):
        """Registra tempo de execução"""
        self.timers[name].append(duration_ms)
        # Manter apenas os últimos 1000 valores
        if len(self.timers[name]) > 1000:
            self.timers[name] = self.timers[name][-1000:]
        
        metric = Metric(
            name=name,
            value=duration_ms,
            metric_type=MetricType.TIMER,
            tags=tags or {},
            unit="ms"
        )
        self.metrics[name].append(metric)
    
    def get_metrics_summary(self) -> Dict[str, Any]:
        """Retorna resumo das métricas"""
        summary = {
            "counters": dict(self.counters),
            "gauges": dict(self.gauges),
            "histograms": {},
            "timers": {}
        }
        
        # Calcular estatísticas dos histogramas
        for name, values in self.histograms.items():
            if values:
                summary["histograms"][name] = {
                    "count": len(values),
                    "min": min(values),
                    "max": max(values),
                    "avg": sum(values) / len(values),
                    "p95": sorted(values)[int(len(values) * 0.95)] if values else 0,
                    "p99": sorted(values)[int(len(values) * 0.99)] if values else 0
                }
        
        # Calcular estatísticas dos timers
        for name, values in self.timers.items():
            if values:
                summary["timers"][name] = {
                    "count": len(values),
                    "min_ms": min(values),
                    "max_ms": max(values),
                    "avg_ms": sum(values) / len(values),
                    "p95_ms": sorted(values)[int(len(values) * 0.95)] if values else 0,
                    "p99_ms": sorted(values)[int(len(values) * 0.99)] if values else 0
                }
        
        return summary

class AlertManager:
    """Gerenciador de alertas"""
    
    def __init__(self):
        self.alerts: List[Alert] = []
        self.alert_rules: Dict[str, Callable] = {}
        self.alert_handlers: List[Callable] = []
        
    def add_alert_rule(self, name: str, rule_func: Callable):
        """Adiciona regra de alerta"""
        self.alert_rules[name] = rule_func
    
    def add_alert_handler(self, handler: Callable):
        """Adiciona handler de alerta"""
        self.alert_handlers.append(handler)
    
    def create_alert(self, level: AlertLevel, message: str, source: str = "", metadata: Dict[str, Any] = None):
        """Cria um novo alerta"""
        alert_id = f"{source}_{int(time.time())}" if source else f"alert_{int(time.time())}"
        alert = Alert(
            id=alert_id,
            level=level,
            message=message,
            source=source,
            metadata=metadata or {}
        )
        
        self.alerts.append(alert)
        
        # Notificar handlers
        for handler in self.alert_handlers:
            try:
                handler(alert)
            except Exception as e:
                logger.error(f"Erro no handler de alerta: {e}")
        
        logger.warning(f"Alerta criado: {alert.level.value} - {alert.message}")
        return alert
    
    def resolve_alert(self, alert_id: str):
        """Resolve um alerta"""
        for alert in self.alerts:
            if alert.id == alert_id:
                alert.resolved = True
                logger.info(f"Alerta resolvido: {alert_id}")
                break
    
    def get_active_alerts(self) -> List[Alert]:
        """Retorna alertas ativos"""
        return [alert for alert in self.alerts if not alert.resolved]
    
    def check_alert_rules(self, metrics: Dict[str, Any]):
        """Verifica regras de alerta"""
        for rule_name, rule_func in self.alert_rules.items():
            try:
                result = rule_func(metrics)
                if result:
                    level, message, metadata = result
                    self.create_alert(level, message, rule_name, metadata)
            except Exception as e:
                logger.error(f"Erro na regra de alerta {rule_name}: {e}")

class HealthChecker:
    """Verificador de saúde do sistema"""
    
    def __init__(self):
        self.components: Dict[str, HealthStatus] = {}
        self.check_interval = 30  # segundos
        
    def register_component(self, name: str, check_func: Callable):
        """Registra componente para verificação de saúde"""
        self.components[name] = HealthStatus(
            component=name,
            status="unknown"
        )
        self.components[name].check_func = check_func
    
    async def check_component_health(self, component_name: str) -> HealthStatus:
        """Verifica saúde de um componente"""
        if component_name not in self.components:
            return HealthStatus(component=component_name, status="unknown")
        
        component = self.components[component_name]
        
        try:
            # Executar função de verificação
            result = await component.check_func()
            
            if isinstance(result, dict):
                component.status = result.get("status", "healthy")
                component.metrics = result.get("metrics", {})
                component.issues = result.get("issues", [])
            else:
                component.status = "healthy" if result else "unhealthy"
            
            component.last_check = datetime.now()
            
        except Exception as e:
            component.status = "unhealthy"
            component.issues = [f"Erro na verificação: {str(e)}"]
            component.last_check = datetime.now()
            logger.error(f"Erro ao verificar saúde do componente {component_name}: {e}")
        
        return component
    
    async def check_all_components(self) -> Dict[str, HealthStatus]:
        """Verifica saúde de todos os componentes"""
        results = {}
        
        for component_name in self.components:
            results[component_name] = await self.check_component_health(component_name)
        
        return results

class RealTimeMonitor:
    """Monitor em tempo real do SEVE Framework"""
    
    def __init__(self):
        self.metrics_collector = MetricsCollector()
        self.alert_manager = AlertManager()
        self.health_checker = HealthChecker()
        self.is_running = False
        self.monitoring_task = None
        
        # Configurar regras de alerta padrão
        self._setup_default_alert_rules()
        
        # Configurar handlers de alerta padrão
        self._setup_default_alert_handlers()
    
    def _setup_default_alert_rules(self):
        """Configura regras de alerta padrão"""
        
        def high_error_rate_rule(metrics):
            """Regra para alta taxa de erro"""
            error_rate = metrics.get("gauges", {}).get("error_rate", 0)
            if error_rate > 0.1:  # 10%
                return (
                    AlertLevel.CRITICAL,
                    f"Taxa de erro alta: {error_rate:.2%}",
                    {"error_rate": error_rate}
                )
            elif error_rate > 0.05:  # 5%
                return (
                    AlertLevel.WARNING,
                    f"Taxa de erro elevada: {error_rate:.2%}",
                    {"error_rate": error_rate}
                )
            return None
        
        def low_ethics_compliance_rule(metrics):
            """Regra para baixa conformidade ética"""
            compliance_rate = metrics.get("gauges", {}).get("ethics_compliance_rate", 1.0)
            if compliance_rate < 0.8:  # 80%
                return (
                    AlertLevel.CRITICAL,
                    f"Conformidade ética baixa: {compliance_rate:.2%}",
                    {"compliance_rate": compliance_rate}
                )
            elif compliance_rate < 0.9:  # 90%
                return (
                    AlertLevel.WARNING,
                    f"Conformidade ética reduzida: {compliance_rate:.2%}",
                    {"compliance_rate": compliance_rate}
                )
            return None
        
        def high_processing_time_rule(metrics):
            """Regra para tempo de processamento alto"""
            avg_time = metrics.get("timers", {}).get("processing_time", {}).get("avg_ms", 0)
            if avg_time > 5000:  # 5 segundos
                return (
                    AlertLevel.WARNING,
                    f"Tempo de processamento alto: {avg_time:.0f}ms",
                    {"avg_processing_time_ms": avg_time}
                )
            return None
        
        def memory_usage_rule(metrics):
            """Regra para uso de memória"""
            memory_usage = metrics.get("gauges", {}).get("memory_usage_percent", 0)
            if memory_usage > 90:  # 90%
                return (
                    AlertLevel.CRITICAL,
                    f"Uso de memória crítico: {memory_usage:.1f}%",
                    {"memory_usage_percent": memory_usage}
                )
            elif memory_usage > 80:  # 80%
                return (
                    AlertLevel.WARNING,
                    f"Uso de memória elevado: {memory_usage:.1f}%",
                    {"memory_usage_percent": memory_usage}
                )
            return None
        
        # Registrar regras
        self.alert_manager.add_alert_rule("high_error_rate", high_error_rate_rule)
        self.alert_manager.add_alert_rule("low_ethics_compliance", low_ethics_compliance_rule)
        self.alert_manager.add_alert_rule("high_processing_time", high_processing_time_rule)
        self.alert_manager.add_alert_rule("memory_usage", memory_usage_rule)
    
    def _setup_default_alert_handlers(self):
        """Configura handlers de alerta padrão"""
        
        def log_alert_handler(alert: Alert):
            """Handler que registra alertas no log"""
            if alert.level == AlertLevel.CRITICAL:
                logger.critical(f"ALERTA CRÍTICO: {alert.message}")
            elif alert.level == AlertLevel.WARNING:
                logger.warning(f"ALERTA: {alert.message}")
            else:
                logger.info(f"INFO: {alert.message}")
        
        def webhook_alert_handler(alert: Alert):
            """Handler que envia alertas via webhook"""
            # Implementar envio via webhook se necessário
            pass
        
        # Registrar handlers
        self.alert_manager.add_alert_handler(log_alert_handler)
        self.alert_manager.add_alert_handler(webhook_alert_handler)
    
    async def start_monitoring(self):
        """Inicia monitoramento em tempo real"""
        if self.is_running:
            return
        
        self.is_running = True
        self.monitoring_task = asyncio.create_task(self._monitoring_loop())
        logger.info("Monitoramento em tempo real iniciado")
    
    async def stop_monitoring(self):
        """Para monitoramento"""
        if not self.is_running:
            return
        
        self.is_running = False
        if self.monitoring_task:
            self.monitoring_task.cancel()
            try:
                await self.monitoring_task
            except asyncio.CancelledError:
                pass
        
        logger.info("Monitoramento em tempo real parado")
    
    async def _monitoring_loop(self):
        """Loop principal de monitoramento"""
        while self.is_running:
            try:
                # Coletar métricas do sistema
                await self._collect_system_metrics()
                
                # Verificar saúde dos componentes
                await self._check_components_health()
                
                # Verificar regras de alerta
                metrics_summary = self.metrics_collector.get_metrics_summary()
                self.alert_manager.check_alert_rules(metrics_summary)
                
                # Aguardar próxima iteração
                await asyncio.sleep(10)  # Verificar a cada 10 segundos
                
            except Exception as e:
                logger.error(f"Erro no loop de monitoramento: {e}")
                await asyncio.sleep(5)  # Aguardar antes de tentar novamente
    
    async def _collect_system_metrics(self):
        """Coleta métricas do sistema"""
        # Métricas de CPU
        cpu_percent = psutil.cpu_percent(interval=1)
        self.metrics_collector.set_gauge("cpu_usage_percent", cpu_percent)
        
        # Métricas de memória
        memory = psutil.virtual_memory()
        self.metrics_collector.set_gauge("memory_usage_percent", memory.percent)
        self.metrics_collector.set_gauge("memory_available_mb", memory.available / 1024 / 1024)
        
        # Métricas de disco
        disk = psutil.disk_usage('/')
        self.metrics_collector.set_gauge("disk_usage_percent", disk.percent)
        
        # Métricas de rede
        network = psutil.net_io_counters()
        self.metrics_collector.set_gauge("network_bytes_sent", network.bytes_sent)
        self.metrics_collector.set_gauge("network_bytes_recv", network.bytes_recv)
    
    async def _check_components_health(self):
        """Verifica saúde dos componentes"""
        health_status = await self.health_checker.check_all_components()
        
        # Atualizar métricas de saúde
        healthy_components = sum(1 for status in health_status.values() if status.status == "healthy")
        total_components = len(health_status)
        
        self.metrics_collector.set_gauge(
            "healthy_components_ratio",
            healthy_components / total_components if total_components > 0 else 1.0
        )
    
    def record_processing_metrics(self, processing_time_ms: float, success: bool, ethics_compliant: bool):
        """Registra métricas de processamento"""
        # Tempo de processamento
        self.metrics_collector.record_timer("processing_time", processing_time_ms)
        
        # Contadores
        self.metrics_collector.increment_counter("total_requests")
        if success:
            self.metrics_collector.increment_counter("successful_requests")
        else:
            self.metrics_collector.increment_counter("failed_requests")
        
        if ethics_compliant:
            self.metrics_collector.increment_counter("ethics_compliant_requests")
        else:
            self.metrics_collector.increment_counter("ethics_violations")
        
        # Calcular taxas
        total_requests = self.metrics_collector.counters["total_requests"]
        if total_requests > 0:
            error_rate = self.metrics_collector.counters["failed_requests"] / total_requests
            compliance_rate = self.metrics_collector.counters["ethics_compliant_requests"] / total_requests
            
            self.metrics_collector.set_gauge("error_rate", error_rate)
            self.metrics_collector.set_gauge("ethics_compliance_rate", compliance_rate)
    
    def get_dashboard_data(self) -> Dict[str, Any]:
        """Retorna dados para dashboard"""
        metrics_summary = self.metrics_collector.get_metrics_summary()
        active_alerts = self.alert_manager.get_active_alerts()
        
        return {
            "timestamp": datetime.now().isoformat(),
            "metrics": metrics_summary,
            "alerts": [
                {
                    "id": alert.id,
                    "level": alert.level.value,
                    "message": alert.message,
                    "timestamp": alert.timestamp.isoformat(),
                    "source": alert.source,
                    "resolved": alert.resolved
                }
                for alert in active_alerts
            ],
            "health": {
                component: {
                    "status": status.status,
                    "last_check": status.last_check.isoformat(),
                    "issues": status.issues
                }
                for component, status in self.health_checker.components.items()
            }
        }

# Instância global do monitor
monitor = RealTimeMonitor()

async def start_monitoring():
    """Inicia monitoramento global"""
    await monitor.start_monitoring()

async def stop_monitoring():
    """Para monitoramento global"""
    await monitor.stop_monitoring()

def get_monitor() -> RealTimeMonitor:
    """Retorna instância do monitor"""
    return monitor
