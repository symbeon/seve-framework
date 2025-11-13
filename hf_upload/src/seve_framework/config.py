"""
SEVE Framework - Configuration Module
Symbiotic Ethical Vision Engine

This module provides configuration management for the SEVE Framework,
supporting both Universal and v3.0 specific modes.
"""

import os
import yaml
import json
from pathlib import Path
from typing import Dict, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
import logging

logger = logging.getLogger(__name__)

class SEVEMode(Enum):
    """Operating modes for SEVE Framework"""
    UNIVERSAL = "universal"           # Multi-domain adaptive mode
    VISION_SPECIFIC = "vision_specific"  # v3.0 computer vision specific
    HYBRID = "hybrid"                # Combined mode

class PrivacyLevel(Enum):
    """Privacy protection levels"""
    MINIMAL = "minimal"              # Basic privacy protection
    STANDARD = "standard"            # Standard privacy protection
    HIGH = "high"                    # High privacy protection
    MAXIMUM = "maximum"              # Maximum privacy protection

class EthicsLevel(Enum):
    """Ethics validation levels"""
    BASIC = "basic"                  # Basic ethical validation
    STANDARD = "standard"           # Standard ethical validation
    STRICT = "strict"               # Strict ethical validation
    MAXIMUM = "maximum"             # Maximum ethical validation

@dataclass
class SEVEConfig:
    """Main configuration class for SEVE Framework"""
    
    # Core Settings
    mode: SEVEMode = SEVEMode.UNIVERSAL
    debug: bool = False
    log_level: str = "INFO"
    
    # Privacy Settings
    privacy_level: PrivacyLevel = PrivacyLevel.STANDARD
    anonymization_enabled: bool = True
    pseudonymization_enabled: bool = True
    data_retention_days: int = 30
    
    # Ethics Settings
    ethics_level: EthicsLevel = EthicsLevel.STANDARD
    ethics_validation_enabled: bool = True
    guardflow_enabled: bool = True
    audit_logging_enabled: bool = True
    
    # Performance Settings
    max_workers: int = 4
    batch_size: int = 32
    gpu_enabled: bool = True
    memory_limit_mb: int = 4096
    
    # API Settings
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_workers: int = 1
    cors_enabled: bool = True
    
    # Database Settings
    database_url: Optional[str] = None
    redis_url: Optional[str] = None
    
    # Model Settings
    model_cache_dir: str = "./models"
    model_download_enabled: bool = True
    
    # Custom Settings
    custom_settings: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Post-initialization validation"""
        self._validate_config()
    
    def _validate_config(self):
        """Validate configuration parameters"""
        if self.max_workers < 1:
            raise ValueError("max_workers must be at least 1")
        
        if self.batch_size < 1:
            raise ValueError("batch_size must be at least 1")
        
        if self.api_port < 1 or self.api_port > 65535:
            raise ValueError("api_port must be between 1 and 65535")
        
        if self.data_retention_days < 0:
            raise ValueError("data_retention_days must be non-negative")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary"""
        return {
            "mode": self.mode.value,
            "debug": self.debug,
            "log_level": self.log_level,
            "privacy_level": self.privacy_level.value,
            "anonymization_enabled": self.anonymization_enabled,
            "pseudonymization_enabled": self.pseudonymization_enabled,
            "data_retention_days": self.data_retention_days,
            "ethics_level": self.ethics_level.value,
            "ethics_validation_enabled": self.ethics_validation_enabled,
            "guardflow_enabled": self.guardflow_enabled,
            "audit_logging_enabled": self.audit_logging_enabled,
            "max_workers": self.max_workers,
            "batch_size": self.batch_size,
            "gpu_enabled": self.gpu_enabled,
            "memory_limit_mb": self.memory_limit_mb,
            "api_host": self.api_host,
            "api_port": self.api_port,
            "api_workers": self.api_workers,
            "cors_enabled": self.cors_enabled,
            "database_url": self.database_url,
            "redis_url": self.redis_url,
            "model_cache_dir": self.model_cache_dir,
            "model_download_enabled": self.model_download_enabled,
            "custom_settings": self.custom_settings
        }
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'SEVEConfig':
        """Create configuration from dictionary"""
        # Convert enum values back to enum instances
        if "mode" in config_dict:
            config_dict["mode"] = SEVEMode(config_dict["mode"])
        
        if "privacy_level" in config_dict:
            config_dict["privacy_level"] = PrivacyLevel(config_dict["privacy_level"])
        
        if "ethics_level" in config_dict:
            config_dict["ethics_level"] = EthicsLevel(config_dict["ethics_level"])
        
        return cls(**config_dict)

class ConfigManager:
    """Configuration manager for SEVE Framework"""
    
    def __init__(self, config_dir: Optional[str] = None):
        self.config_dir = Path(config_dir) if config_dir else Path("./config")
        self.config_dir.mkdir(exist_ok=True)
        
        # Default configuration files
        self.default_config_file = self.config_dir / "default.yaml"
        self.user_config_file = self.config_dir / "user.yaml"
        self.env_config_file = self.config_dir / "environment.yaml"
    
    def load_default_config(self) -> SEVEConfig:
        """Load default configuration"""
        if self.default_config_file.exists():
            return self._load_from_file(self.default_config_file)
        else:
            # Create default config file
            default_config = SEVEConfig()
            self.save_config(default_config, self.default_config_file)
            return default_config
    
    def load_user_config(self) -> Optional[SEVEConfig]:
        """Load user-specific configuration"""
        if self.user_config_file.exists():
            return self._load_from_file(self.user_config_file)
        return None
    
    def load_env_config(self) -> Optional[SEVEConfig]:
        """Load environment-specific configuration"""
        if self.env_config_file.exists():
            return self._load_from_file(self.env_config_file)
        return None
    
    def load_config(self) -> SEVEConfig:
        """Load configuration with precedence: env > user > default"""
        # Start with default config
        config = self.load_default_config()
        
        # Override with user config if exists
        user_config = self.load_user_config()
        if user_config:
            config = self._merge_configs(config, user_config)
        
        # Override with environment config if exists
        env_config = self.load_env_config()
        if env_config:
            config = self._merge_configs(config, env_config)
        
        # Override with environment variables
        config = self._apply_env_overrides(config)
        
        return config
    
    def save_config(self, config: SEVEConfig, file_path: Optional[Path] = None) -> None:
        """Save configuration to file"""
        if file_path is None:
            file_path = self.user_config_file
        
        config_dict = config.to_dict()
        
        if file_path.suffix.lower() == '.yaml':
            with open(file_path, 'w', encoding='utf-8') as f:
                yaml.dump(config_dict, f, default_flow_style=False, indent=2)
        elif file_path.suffix.lower() == '.json':
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(config_dict, f, indent=2)
        else:
            raise ValueError(f"Unsupported file format: {file_path.suffix}")
        
        logger.info(f"Configuration saved to {file_path}")
    
    def _load_from_file(self, file_path: Path) -> SEVEConfig:
        """Load configuration from file"""
        try:
            if file_path.suffix.lower() == '.yaml':
                with open(file_path, 'r', encoding='utf-8') as f:
                    config_dict = yaml.safe_load(f)
            elif file_path.suffix.lower() == '.json':
                with open(file_path, 'r', encoding='utf-8') as f:
                    config_dict = json.load(f)
            else:
                raise ValueError(f"Unsupported file format: {file_path.suffix}")
            
            return SEVEConfig.from_dict(config_dict)
        
        except Exception as e:
            logger.error(f"Error loading configuration from {file_path}: {e}")
            raise
    
    def _merge_configs(self, base: SEVEConfig, override: SEVEConfig) -> SEVEConfig:
        """Merge two configurations, with override taking precedence"""
        base_dict = base.to_dict()
        override_dict = override.to_dict()
        
        # Merge dictionaries
        merged_dict = {**base_dict, **override_dict}
        
        return SEVEConfig.from_dict(merged_dict)
    
    def _apply_env_overrides(self, config: SEVEConfig) -> SEVEConfig:
        """Apply environment variable overrides"""
        config_dict = config.to_dict()
        
        # Environment variable mappings
        env_mappings = {
            'SEVE_DEBUG': ('debug', bool),
            'SEVE_LOG_LEVEL': ('log_level', str),
            'SEVE_MODE': ('mode', str),
            'SEVE_PRIVACY_LEVEL': ('privacy_level', str),
            'SEVE_ETHICS_LEVEL': ('ethics_level', str),
            'SEVE_API_HOST': ('api_host', str),
            'SEVE_API_PORT': ('api_port', int),
            'SEVE_MAX_WORKERS': ('max_workers', int),
            'SEVE_BATCH_SIZE': ('batch_size', int),
            'SEVE_GPU_ENABLED': ('gpu_enabled', bool),
            'SEVE_DATABASE_URL': ('database_url', str),
            'SEVE_REDIS_URL': ('redis_url', str),
        }
        
        for env_var, (config_key, config_type) in env_mappings.items():
            env_value = os.getenv(env_var)
            if env_value is not None:
                try:
                    if config_type == bool:
                        config_dict[config_key] = env_value.lower() in ('true', '1', 'yes', 'on')
                    else:
                        config_dict[config_key] = config_type(env_value)
                except ValueError as e:
                    logger.warning(f"Invalid environment variable {env_var}: {e}")
        
        return SEVEConfig.from_dict(config_dict)

def setup_config(config_dir: Optional[str] = None) -> SEVEConfig:
    """Setup and return SEVE configuration"""
    config_manager = ConfigManager(config_dir)
    return config_manager.load_config()

def create_default_configs(config_dir: Optional[str] = None) -> None:
    """Create default configuration files"""
    config_manager = ConfigManager(config_dir)
    
    # Create default config
    default_config = SEVEConfig()
    config_manager.save_config(default_config, config_manager.default_config_file)
    
    # Create example user config
    user_config = SEVEConfig(
        debug=True,
        log_level="DEBUG",
        privacy_level=PrivacyLevel.HIGH,
        ethics_level=EthicsLevel.STRICT
    )
    config_manager.save_config(user_config, config_manager.user_config_file)
    
    # Create example environment config
    env_config = SEVEConfig(
        api_host="localhost",
        api_port=8080,
        gpu_enabled=False
    )
    config_manager.save_config(env_config, config_manager.env_config_file)
    
    logger.info(f"Default configuration files created in {config_manager.config_dir}")

if __name__ == "__main__":
    # Create default configurations when run directly
    create_default_configs()
    print("SEVE Framework configuration files created successfully!")
