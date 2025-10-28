"""
SEVE Sense Module - Multi-Sensor Fusion
Symbiotic Ethical Vision Engine

This module implements the SEVE-Sense component, providing
multi-sensor data fusion capabilities for comprehensive
environmental perception beyond visual input.
"""

import asyncio
import logging
import time
import json
from typing import Dict, List, Any, Optional, Union, Tuple
from dataclasses import dataclass, field
from enum import Enum
import numpy as np

from .config import SEVEConfig

logger = logging.getLogger(__name__)

class SensorType(Enum):
    """Types of sensors supported"""
    TEMPERATURE = "temperature"
    HUMIDITY = "humidity"
    PRESSURE = "pressure"
    MOTION = "motion"
    PROXIMITY = "proximity"
    AUDIO = "audio"
    LIDAR = "lidar"
    RADAR = "radar"
    ACCELEROMETER = "accelerometer"
    GYROSCOPE = "gyroscope"
    MAGNETOMETER = "magnetometer"
    GPS = "gps"
    LIGHT = "light"
    AIR_QUALITY = "air_quality"

class DataQuality(Enum):
    """Quality levels for sensor data"""
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    UNRELIABLE = "unreliable"

@dataclass
class SensorReading:
    """Represents a single sensor reading"""
    sensor_type: SensorType
    value: Union[float, int, str, Dict[str, Any]]
    unit: str
    timestamp: float
    quality: DataQuality = DataQuality.GOOD
    confidence: float = 1.0
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class SensorFusionResult:
    """Result of sensor data fusion"""
    fused_data: Dict[str, Any]
    individual_readings: List[SensorReading]
    processing_time_ms: float = 0.0
    data_quality_score: float = 0.0
    anomalies_detected: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

class SEVESenseModule:
    """
    SEVE Sense Module
    
    Provides multi-sensor data fusion capabilities for comprehensive
    environmental perception and context awareness.
    """
    
    def __init__(self, config: SEVEConfig):
        self.config = config
        self.is_initialized = False
        
        # Sensor configurations
        self.sensor_configs = {}
        self.calibration_data = {}
        
        # Data fusion algorithms
        self.fusion_algorithms = {}
        
        # Quality assessment
        self.quality_thresholds = {
            SensorType.TEMPERATURE: {"min": -50, "max": 100, "std_threshold": 5.0},
            SensorType.HUMIDITY: {"min": 0, "max": 100, "std_threshold": 10.0},
            SensorType.PRESSURE: {"min": 800, "max": 1200, "std_threshold": 20.0},
            SensorType.MOTION: {"min": 0, "max": 1, "std_threshold": 0.1},
        }
        
        logger.info("SEVE Sense Module initialized")
    
    async def initialize(self) -> None:
        """Initialize sensor modules and fusion algorithms"""
        try:
            # Initialize sensor configurations
            await self._load_sensor_configs()
            
            # Initialize fusion algorithms
            await self._initialize_fusion_algorithms()
            
            # Load calibration data
            await self._load_calibration_data()
            
            self.is_initialized = True
            logger.info("SEVE Sense Module fully initialized")
            
        except Exception as e:
            logger.error(f"Error initializing SEVE Sense Module: {e}")
            raise
    
    async def _load_sensor_configs(self) -> None:
        """Load sensor configurations"""
        # Default sensor configurations
        self.sensor_configs = {
            SensorType.TEMPERATURE: {
                "enabled": True,
                "sampling_rate": 1.0,  # Hz
                "precision": 0.1,
                "range": (-50, 100)
            },
            SensorType.HUMIDITY: {
                "enabled": True,
                "sampling_rate": 1.0,
                "precision": 1.0,
                "range": (0, 100)
            },
            SensorType.MOTION: {
                "enabled": True,
                "sampling_rate": 10.0,
                "precision": 0.01,
                "range": (0, 1)
            },
            SensorType.PROXIMITY: {
                "enabled": True,
                "sampling_rate": 5.0,
                "precision": 0.1,
                "range": (0, 10)
            },
            SensorType.AUDIO: {
                "enabled": True,
                "sampling_rate": 44.1,  # kHz
                "precision": 0.001,
                "range": (0, 1)
            },
            SensorType.LIDAR: {
                "enabled": False,  # Disabled by default
                "sampling_rate": 20.0,
                "precision": 0.01,
                "range": (0, 100)
            },
            SensorType.RADAR: {
                "enabled": False,  # Disabled by default
                "sampling_rate": 10.0,
                "precision": 0.1,
                "range": (0, 200)
            }
        }
        
        logger.info(f"Loaded configurations for {len(self.sensor_configs)} sensor types")
    
    async def _initialize_fusion_algorithms(self) -> None:
        """Initialize data fusion algorithms"""
        # Simple fusion algorithms (in a real system, these would be more sophisticated)
        self.fusion_algorithms = {
            "kalman_filter": "kalman_fusion_algorithm",
            "particle_filter": "particle_fusion_algorithm",
            "weighted_average": "weighted_average_algorithm",
            "bayesian_fusion": "bayesian_fusion_algorithm"
        }
        
        logger.info("Fusion algorithms initialized")
    
    async def _load_calibration_data(self) -> None:
        """Load sensor calibration data"""
        # Default calibration data (in a real system, this would be loaded from files)
        self.calibration_data = {
            SensorType.TEMPERATURE: {"offset": 0.0, "scale": 1.0},
            SensorType.HUMIDITY: {"offset": 0.0, "scale": 1.0},
            SensorType.PRESSURE: {"offset": 0.0, "scale": 1.0},
            SensorType.MOTION: {"offset": 0.0, "scale": 1.0},
        }
        
        logger.info("Calibration data loaded")
    
    async def process_sensor_input(
        self,
        sensor_data: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> SensorFusionResult:
        """
        Process multi-sensor input and fuse data
        
        Args:
            sensor_data: Dictionary containing sensor readings
            context: Additional context information
            
        Returns:
            SensorFusionResult with fused data and analysis
        """
        start_time = time.time()
        
        if not self.is_initialized:
            await self.initialize()
        
        try:
            # Parse sensor readings
            readings = await self._parse_sensor_data(sensor_data)
            
            # Assess data quality
            quality_assessments = await self._assess_data_quality(readings)
            
            # Detect anomalies
            anomalies = await self._detect_anomalies(readings, context)
            
            # Fuse sensor data
            fused_data = await self._fuse_sensor_data(readings, context)
            
            # Calculate overall quality score
            quality_score = await self._calculate_quality_score(quality_assessments)
            
            processing_time = (time.time() - start_time) * 1000
            
            return SensorFusionResult(
                fused_data=fused_data,
                individual_readings=readings,
                processing_time_ms=processing_time,
                data_quality_score=quality_score,
                anomalies_detected=anomalies,
                metadata={
                    "sensor_count": len(readings),
                    "fusion_algorithm": "weighted_average",
                    "context": context or {}
                }
            )
            
        except Exception as e:
            logger.error(f"Error processing sensor input: {e}")
            raise
    
    async def _parse_sensor_data(self, sensor_data: Dict[str, Any]) -> List[SensorReading]:
        """Parse raw sensor data into structured readings"""
        readings = []
        current_time = time.time()
        
        for sensor_name, data in sensor_data.items():
            try:
                # Determine sensor type
                sensor_type = self._identify_sensor_type(sensor_name)
                
                # Parse sensor value
                if isinstance(data, dict):
                    value = data.get("value", 0)
                    unit = data.get("unit", "unknown")
                    quality = DataQuality(data.get("quality", "good"))
                    confidence = data.get("confidence", 1.0)
                    metadata = data.get("metadata", {})
                else:
                    value = data
                    unit = self._get_default_unit(sensor_type)
                    quality = DataQuality.GOOD
                    confidence = 1.0
                    metadata = {}
                
                # Apply calibration
                calibrated_value = await self._apply_calibration(sensor_type, value)
                
                reading = SensorReading(
                    sensor_type=sensor_type,
                    value=calibrated_value,
                    unit=unit,
                    timestamp=current_time,
                    quality=quality,
                    confidence=confidence,
                    metadata=metadata
                )
                
                readings.append(reading)
                
            except Exception as e:
                logger.warning(f"Error parsing sensor {sensor_name}: {e}")
                continue
        
        return readings
    
    def _identify_sensor_type(self, sensor_name: str) -> SensorType:
        """Identify sensor type from name"""
        sensor_name_lower = sensor_name.lower()
        
        if "temp" in sensor_name_lower:
            return SensorType.TEMPERATURE
        elif "humid" in sensor_name_lower:
            return SensorType.HUMIDITY
        elif "pressure" in sensor_name_lower:
            return SensorType.PRESSURE
        elif "motion" in sensor_name_lower:
            return SensorType.MOTION
        elif "proximity" in sensor_name_lower:
            return SensorType.PROXIMITY
        elif "audio" in sensor_name_lower or "sound" in sensor_name_lower:
            return SensorType.AUDIO
        elif "lidar" in sensor_name_lower:
            return SensorType.LIDAR
        elif "radar" in sensor_name_lower:
            return SensorType.RADAR
        elif "accel" in sensor_name_lower:
            return SensorType.ACCELEROMETER
        elif "gyro" in sensor_name_lower:
            return SensorType.GYROSCOPE
        elif "mag" in sensor_name_lower:
            return SensorType.MAGNETOMETER
        elif "gps" in sensor_name_lower:
            return SensorType.GPS
        elif "light" in sensor_name_lower:
            return SensorType.LIGHT
        elif "air" in sensor_name_lower:
            return SensorType.AIR_QUALITY
        else:
            return SensorType.TEMPERATURE  # Default fallback
    
    def _get_default_unit(self, sensor_type: SensorType) -> str:
        """Get default unit for sensor type"""
        units = {
            SensorType.TEMPERATURE: "°C",
            SensorType.HUMIDITY: "%",
            SensorType.PRESSURE: "hPa",
            SensorType.MOTION: "m/s²",
            SensorType.PROXIMITY: "m",
            SensorType.AUDIO: "dB",
            SensorType.LIDAR: "m",
            SensorType.RADAR: "m",
            SensorType.ACCELEROMETER: "m/s²",
            SensorType.GYROSCOPE: "rad/s",
            SensorType.MAGNETOMETER: "μT",
            SensorType.GPS: "degrees",
            SensorType.LIGHT: "lux",
            SensorType.AIR_QUALITY: "ppm"
        }
        return units.get(sensor_type, "unknown")
    
    async def _apply_calibration(self, sensor_type: SensorType, value: float) -> float:
        """Apply calibration to sensor value"""
        if sensor_type in self.calibration_data:
            calibration = self.calibration_data[sensor_type]
            return value * calibration["scale"] + calibration["offset"]
        return value
    
    async def _assess_data_quality(self, readings: List[SensorReading]) -> Dict[SensorType, DataQuality]:
        """Assess quality of sensor readings"""
        quality_assessments = {}
        
        for reading in readings:
            sensor_type = reading.sensor_type
            value = reading.value
            
            if sensor_type in self.quality_thresholds:
                thresholds = self.quality_thresholds[sensor_type]
                
                if isinstance(value, (int, float)):
                    if thresholds["min"] <= value <= thresholds["max"]:
                        quality = DataQuality.GOOD
                    else:
                        quality = DataQuality.POOR
                else:
                    quality = DataQuality.UNRELIABLE
            else:
                quality = DataQuality.GOOD
            
            quality_assessments[sensor_type] = quality
        
        return quality_assessments
    
    async def _detect_anomalies(
        self,
        readings: List[SensorReading],
        context: Optional[Dict[str, Any]] = None
    ) -> List[str]:
        """Detect anomalies in sensor readings"""
        anomalies = []
        
        # Simple anomaly detection (in a real system, this would be more sophisticated)
        for reading in readings:
            sensor_type = reading.sensor_type
            value = reading.value
            
            if sensor_type in self.quality_thresholds:
                thresholds = self.quality_thresholds[sensor_type]
                
                if isinstance(value, (int, float)):
                    if value < thresholds["min"] or value > thresholds["max"]:
                        anomalies.append(f"{sensor_type.value} value {value} outside normal range")
                    
                    # Check for sudden changes (simplified)
                    if hasattr(reading, 'previous_value'):
                        change = abs(value - reading.previous_value)
                        if change > thresholds.get("std_threshold", 1.0) * 3:
                            anomalies.append(f"{sensor_type.value} sudden change detected")
        
        return anomalies
    
    async def _fuse_sensor_data(
        self,
        readings: List[SensorReading],
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Fuse sensor data using appropriate algorithms"""
        fused_data = {
            "environmental": {},
            "motion": {},
            "spatial": {},
            "temporal": {},
            "quality_metrics": {}
        }
        
        # Group readings by category
        environmental_readings = []
        motion_readings = []
        spatial_readings = []
        
        for reading in readings:
            sensor_type = reading.sensor_type
            
            if sensor_type in [SensorType.TEMPERATURE, SensorType.HUMIDITY, SensorType.PRESSURE, SensorType.AIR_QUALITY]:
                environmental_readings.append(reading)
            elif sensor_type in [SensorType.MOTION, SensorType.ACCELEROMETER, SensorType.GYROSCOPE]:
                motion_readings.append(reading)
            elif sensor_type in [SensorType.PROXIMITY, SensorType.LIDAR, SensorType.RADAR, SensorType.GPS]:
                spatial_readings.append(reading)
        
        # Fuse environmental data
        if environmental_readings:
            fused_data["environmental"] = await self._fuse_environmental_data(environmental_readings)
        
        # Fuse motion data
        if motion_readings:
            fused_data["motion"] = await self._fuse_motion_data(motion_readings)
        
        # Fuse spatial data
        if spatial_readings:
            fused_data["spatial"] = await self._fuse_spatial_data(spatial_readings)
        
        # Add temporal information
        fused_data["temporal"] = {
            "timestamp": time.time(),
            "processing_time": time.time(),
            "data_freshness": min(r.timestamp for r in readings) if readings else 0
        }
        
        # Add quality metrics
        fused_data["quality_metrics"] = {
            "total_sensors": len(readings),
            "environmental_sensors": len(environmental_readings),
            "motion_sensors": len(motion_readings),
            "spatial_sensors": len(spatial_readings),
            "average_confidence": sum(r.confidence for r in readings) / len(readings) if readings else 0
        }
        
        return fused_data
    
    async def _fuse_environmental_data(self, readings: List[SensorReading]) -> Dict[str, Any]:
        """Fuse environmental sensor data"""
        environmental = {}
        
        for reading in readings:
            sensor_type = reading.sensor_type
            value = reading.value
            
            if sensor_type == SensorType.TEMPERATURE:
                environmental["temperature"] = {
                    "value": value,
                    "unit": reading.unit,
                    "confidence": reading.confidence
                }
            elif sensor_type == SensorType.HUMIDITY:
                environmental["humidity"] = {
                    "value": value,
                    "unit": reading.unit,
                    "confidence": reading.confidence
                }
            elif sensor_type == SensorType.PRESSURE:
                environmental["pressure"] = {
                    "value": value,
                    "unit": reading.unit,
                    "confidence": reading.confidence
                }
            elif sensor_type == SensorType.AIR_QUALITY:
                environmental["air_quality"] = {
                    "value": value,
                    "unit": reading.unit,
                    "confidence": reading.confidence
                }
        
        return environmental
    
    async def _fuse_motion_data(self, readings: List[SensorReading]) -> Dict[str, Any]:
        """Fuse motion sensor data"""
        motion = {}
        
        for reading in readings:
            sensor_type = reading.sensor_type
            value = reading.value
            
            if sensor_type == SensorType.MOTION:
                motion["motion_detected"] = bool(value > 0.1)
                motion["motion_intensity"] = value
            elif sensor_type == SensorType.ACCELEROMETER:
                motion["acceleration"] = {
                    "value": value,
                    "unit": reading.unit,
                    "confidence": reading.confidence
                }
            elif sensor_type == SensorType.GYROSCOPE:
                motion["rotation"] = {
                    "value": value,
                    "unit": reading.unit,
                    "confidence": reading.confidence
                }
        
        return motion
    
    async def _fuse_spatial_data(self, readings: List[SensorReading]) -> Dict[str, Any]:
        """Fuse spatial sensor data"""
        spatial = {}
        
        for reading in readings:
            sensor_type = reading.sensor_type
            value = reading.value
            
            if sensor_type == SensorType.PROXIMITY:
                spatial["proximity"] = {
                    "value": value,
                    "unit": reading.unit,
                    "confidence": reading.confidence
                }
            elif sensor_type == SensorType.LIDAR:
                spatial["lidar_distance"] = {
                    "value": value,
                    "unit": reading.unit,
                    "confidence": reading.confidence
                }
            elif sensor_type == SensorType.RADAR:
                spatial["radar_distance"] = {
                    "value": value,
                    "unit": reading.unit,
                    "confidence": reading.confidence
                }
            elif sensor_type == SensorType.GPS:
                spatial["location"] = {
                    "value": value,
                    "unit": reading.unit,
                    "confidence": reading.confidence
                }
        
        return spatial
    
    async def _calculate_quality_score(self, quality_assessments: Dict[SensorType, DataQuality]) -> float:
        """Calculate overall data quality score"""
        if not quality_assessments:
            return 0.0
        
        quality_scores = {
            DataQuality.EXCELLENT: 1.0,
            DataQuality.GOOD: 0.8,
            DataQuality.FAIR: 0.6,
            DataQuality.POOR: 0.4,
            DataQuality.UNRELIABLE: 0.2
        }
        
        total_score = sum(quality_scores[quality] for quality in quality_assessments.values())
        return total_score / len(quality_assessments)
    
    def get_status(self) -> Dict[str, Any]:
        """Get current status of the sense module"""
        return {
            "initialized": self.is_initialized,
            "sensor_types_configured": len(self.sensor_configs),
            "fusion_algorithms": len(self.fusion_algorithms),
            "calibration_data_loaded": len(self.calibration_data),
            "quality_thresholds": len(self.quality_thresholds)
        }

# Demo function
async def run_sense_demo():
    """Run SEVE Sense Module demonstration"""
    print("🔊 SEVE Sense Module Demo")
    print("=" * 40)
    
    # Create configuration
    config = SEVEConfig()
    
    # Create sense module
    sense = SEVESenseModule(config)
    await sense.initialize()
    
    print(f"✅ Sense module initialized")
    print(f"📊 Sensor types configured: {len(sense.sensor_configs)}")
    print(f"🔄 Fusion algorithms: {len(sense.fusion_algorithms)}")
    print()
    
    # Demo sensor data
    demo_sensor_data = {
        "temperature": {"value": 23.5, "unit": "°C", "confidence": 0.95},
        "humidity": {"value": 65.2, "unit": "%", "confidence": 0.90},
        "motion": {"value": 0.3, "unit": "m/s²", "confidence": 0.85},
        "proximity": {"value": 2.1, "unit": "m", "confidence": 0.80},
        "audio_level": {"value": 45.2, "unit": "dB", "confidence": 0.75}
    }
    
    print("🔄 Processing demo sensor data...")
    result = await sense.process_sensor_input(demo_sensor_data)
    
    print(f"📊 Sensor readings processed: {len(result.individual_readings)}")
    print(f"⏱️ Processing time: {result.processing_time_ms:.2f}ms")
    print(f"🎯 Data quality score: {result.data_quality_score:.2f}")
    print(f"⚠️ Anomalies detected: {len(result.anomalies_detected)}")
    
    print("\n📋 Fused Data:")
    for category, data in result.fused_data.items():
        print(f"  {category}: {data}")
    
    if result.anomalies_detected:
        print("\n⚠️ Anomalies:")
        for anomaly in result.anomalies_detected:
            print(f"  - {anomaly}")
    
    print()
    print("🌍 SEVE Sense ready for multi-sensor fusion!")

if __name__ == "__main__":
    asyncio.run(run_sense_demo())
