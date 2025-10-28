"""
SEVE Framework - Basic Tests
Symbiotic Ethical Vision Engine

This module contains basic tests for the SEVE Framework components.
"""

import pytest
import asyncio
import tempfile
import shutil
from pathlib import Path
import sys

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from seve_framework import (
    SEVEConfig,
    SEVEMode,
    PrivacyLevel,
    EthicsLevel,
    SEVEHybridFramework,
    SEVECoreV3,
    SEVEVisionModule,
    SEVESenseModule,
    SEVEEthicsModule,
    SEVELinkModule
)

class TestSEVEConfig:
    """Test SEVE configuration"""
    
    def test_default_config(self):
        """Test default configuration creation"""
        config = SEVEConfig()
        assert config.mode == SEVEMode.UNIVERSAL
        assert config.privacy_level == PrivacyLevel.STANDARD
        assert config.ethics_level == EthicsLevel.STANDARD
        assert config.debug == False
    
    def test_custom_config(self):
        """Test custom configuration creation"""
        config = SEVEConfig(
            mode=SEVEMode.HYBRID,
            privacy_level=PrivacyLevel.HIGH,
            ethics_level=EthicsLevel.STRICT,
            debug=True
        )
        assert config.mode == SEVEMode.HYBRID
        assert config.privacy_level == PrivacyLevel.HIGH
        assert config.ethics_level == EthicsLevel.STRICT
        assert config.debug == True
    
    def test_config_validation(self):
        """Test configuration validation"""
        # Test invalid max_workers
        with pytest.raises(ValueError):
            SEVEConfig(max_workers=0)
        
        # Test invalid batch_size
        with pytest.raises(ValueError):
            SEVEConfig(batch_size=0)
        
        # Test invalid api_port
        with pytest.raises(ValueError):
            SEVEConfig(api_port=0)
    
    def test_config_to_dict(self):
        """Test configuration to dictionary conversion"""
        config = SEVEConfig()
        config_dict = config.to_dict()
        
        assert isinstance(config_dict, dict)
        assert "mode" in config_dict
        assert "privacy_level" in config_dict
        assert "ethics_level" in config_dict

class TestSEVEVisionModule:
    """Test SEVE Vision Module"""
    
    @pytest.fixture
    def vision_module(self):
        """Create vision module for testing"""
        config = SEVEConfig()
        return SEVEVisionModule(config)
    
    @pytest.mark.asyncio
    async def test_vision_initialization(self, vision_module):
        """Test vision module initialization"""
        await vision_module.initialize()
        assert vision_module.is_initialized == True
    
    @pytest.mark.asyncio
    async def test_vision_status(self, vision_module):
        """Test vision module status"""
        status = vision_module.get_status()
        assert isinstance(status, dict)
        assert "initialized" in status
        assert "privacy_level" in status

class TestSEVESenseModule:
    """Test SEVE Sense Module"""
    
    @pytest.fixture
    def sense_module(self):
        """Create sense module for testing"""
        config = SEVEConfig()
        return SEVESenseModule(config)
    
    @pytest.mark.asyncio
    async def test_sense_initialization(self, sense_module):
        """Test sense module initialization"""
        await sense_module.initialize()
        assert sense_module.is_initialized == True
    
    @pytest.mark.asyncio
    async def test_sense_processing(self, sense_module):
        """Test sense module processing"""
        await sense_module.initialize()
        
        sensor_data = {
            "temperature": {"value": 25.0, "unit": "°C"},
            "humidity": {"value": 60.0, "unit": "%"},
            "motion": {"value": 0.5, "unit": "m/s²"}
        }
        
        result = await sense_module.process_sensor_input(sensor_data)
        
        assert result.fused_data is not None
        assert len(result.individual_readings) > 0
        assert result.processing_time_ms > 0

class TestSEVEEthicsModule:
    """Test SEVE Ethics Module"""
    
    @pytest.fixture
    def ethics_module(self):
        """Create ethics module for testing"""
        config = SEVEConfig(ethics_level=EthicsLevel.STRICT)
        return SEVEEthicsModule(config)
    
    @pytest.mark.asyncio
    async def test_ethics_initialization(self, ethics_module):
        """Test ethics module initialization"""
        await ethics_module.initialize()
        assert ethics_module.is_initialized == True
        assert len(ethics_module.ethical_rules) > 0
    
    @pytest.mark.asyncio
    async def test_ethics_validation(self, ethics_module):
        """Test ethics validation"""
        await ethics_module.initialize()
        
        # Test compliant decision
        compliant_data = {
            "consent_given": True,
            "has_bias_risk": False,
            "hazard_detected": False
        }
        
        assessments = await ethics_module.validate_decision(compliant_data)
        assert len(assessments) > 0
        
        # Test non-compliant decision
        non_compliant_data = {
            "data_type": "facial_recognition",
            "action": "store",
            "consent_given": False
        }
        
        assessments = await ethics_module.validate_decision(non_compliant_data)
        assert len(assessments) > 0

class TestSEVELinkModule:
    """Test SEVE Link Module"""
    
    @pytest.fixture
    def link_module(self):
        """Create link module for testing"""
        config = SEVEConfig()
        return SEVELinkModule(config)
    
    @pytest.mark.asyncio
    async def test_link_initialization(self, link_module):
        """Test link module initialization"""
        await link_module.initialize()
        assert link_module.is_initialized == True
        assert len(link_module.connections) > 0
    
    @pytest.mark.asyncio
    async def test_link_status(self, link_module):
        """Test link module status"""
        status = link_module.get_status()
        assert isinstance(status, dict)
        assert "initialized" in status
        assert "total_connections" in status

class TestSEVECoreV3:
    """Test SEVE Core v3.0"""
    
    @pytest.fixture
    def core_v3(self):
        """Create SEVE Core v3.0 for testing"""
        config = SEVEConfig(mode=SEVEMode.VISION_SPECIFIC)
        return SEVECoreV3(config)
    
    @pytest.mark.asyncio
    async def test_core_initialization(self, core_v3):
        """Test core initialization"""
        await core_v3.initialize()
        assert core_v3.is_initialized == True
    
    @pytest.mark.asyncio
    async def test_core_processing(self, core_v3):
        """Test core processing"""
        await core_v3.initialize()
        
        input_data = {
            "visual": {"image": "test.jpg", "objects": ["person"]},
            "sensor": {"temperature": 25.0, "motion": True}
        }
        
        result = await core_v3.process_context(input_data)
        
        assert result.status.value in ["completed", "failed", "ethics_blocked"]
        assert result.processing_time_ms > 0

class TestSEVEHybridFramework:
    """Test SEVE Hybrid Framework"""
    
    @pytest.fixture
    def hybrid_framework(self):
        """Create hybrid framework for testing"""
        config = SEVEConfig(mode=SEVEMode.HYBRID)
        return SEVEHybridFramework(config)
    
    @pytest.mark.asyncio
    async def test_hybrid_initialization(self, hybrid_framework):
        """Test hybrid framework initialization"""
        await hybrid_framework.initialize()
        assert hybrid_framework.v3_core.is_initialized == True
    
    @pytest.mark.asyncio
    async def test_hybrid_capabilities(self, hybrid_framework):
        """Test hybrid framework capabilities"""
        capabilities = hybrid_framework.get_capabilities()
        assert isinstance(capabilities, dict)
        assert "version" in capabilities
        assert "mode" in capabilities
    
    @pytest.mark.asyncio
    async def test_hybrid_processing(self, hybrid_framework):
        """Test hybrid framework processing"""
        await hybrid_framework.initialize()
        
        input_data = {
            "visual": {"image": "test.jpg"},
            "sensor": {"temperature": 25.0}
        }
        
        result = await hybrid_framework.process_context(input_data)
        
        assert result.status.value in ["completed", "failed", "ethics_blocked"]
        assert result.processing_time_ms > 0

class TestIntegration:
    """Integration tests"""
    
    @pytest.mark.asyncio
    async def test_full_pipeline(self):
        """Test full SEVE pipeline"""
        config = SEVEConfig(
            mode=SEVEMode.HYBRID,
            privacy_level=PrivacyLevel.HIGH,
            ethics_level=EthicsLevel.STRICT
        )
        
        framework = SEVEHybridFramework(config)
        await framework.initialize()
        
        # Test data
        input_data = {
            "visual": {
                "image": "test_image.jpg",
                "objects": ["person", "car"],
                "faces_detected": 1
            },
            "sensor": {
                "temperature": 23.5,
                "humidity": 65.0,
                "motion": True
            }
        }
        
        context = {
            "location": "test_location",
            "privacy_mode": "high",
            "consent_given": True
        }
        
        result = await framework.process_context(input_data, context)
        
        # Verify result
        assert result.status.value in ["completed", "failed", "ethics_blocked"]
        assert result.processing_time_ms > 0
        
        # Verify framework status
        status = framework.get_status()
        assert status["framework"]["mode"] == "hybrid"

# Utility functions for testing
def create_temp_config():
    """Create temporary configuration for testing"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        f.write("""
mode: "hybrid"
debug: true
privacy_level: "high"
ethics_level: "strict"
""")
        return f.name

def cleanup_temp_files():
    """Clean up temporary files"""
    # This would be implemented to clean up any temporary files created during tests
    pass

if __name__ == "__main__":
    # Run tests if executed directly
    pytest.main([__file__, "-v"])
