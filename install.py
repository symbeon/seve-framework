#!/usr/bin/env python3
"""
SEVE Framework - Installation Script
Symbiotic Ethical Vision Engine

This script handles the installation and setup of the SEVE Framework.
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {sys.version}")
        return False
    
    print(f"✅ Python version: {sys.version}")
    return True

def check_system_requirements():
    """Check system requirements"""
    print("🔍 Checking system requirements...")
    
    # Check OS
    os_name = platform.system()
    print(f"   OS: {os_name}")
    
    # Check available memory
    try:
        import psutil
        memory_gb = psutil.virtual_memory().total / (1024**3)
        print(f"   Memory: {memory_gb:.1f} GB")
        
        if memory_gb < 4:
            print("⚠️  Warning: Less than 4GB RAM detected. Performance may be limited.")
    except ImportError:
        print("   Memory: Unable to check (psutil not available)")
    
    # Check disk space
    try:
        disk_usage = os.statvfs('.')
        free_gb = (disk_usage.f_bavail * disk_usage.f_frsize) / (1024**3)
        print(f"   Free disk space: {free_gb:.1f} GB")
        
        if free_gb < 2:
            print("⚠️  Warning: Less than 2GB free disk space. Installation may fail.")
    except:
        print("   Disk space: Unable to check")
    
    return True

def install_dependencies():
    """Install Python dependencies"""
    print("📦 Installing dependencies...")
    
    try:
        # Upgrade pip
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], 
                      check=True, capture_output=True)
        print("   ✅ pip upgraded")
        
        # Install requirements
        requirements_file = Path(__file__).parent / "requirements.txt"
        if requirements_file.exists():
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", str(requirements_file)], 
                          check=True, capture_output=True)
            print("   ✅ Requirements installed")
        else:
            print("   ⚠️  requirements.txt not found, installing basic dependencies")
            basic_deps = [
                "numpy>=1.21.0",
                "opencv-python>=4.5.0",
                "pillow>=8.3.0",
                "fastapi>=0.68.0",
                "uvicorn>=0.15.0",
                "pydantic>=1.8.0",
                "pyyaml>=6.0",
                "loguru>=0.6.0"
            ]
            
            for dep in basic_deps:
                subprocess.run([sys.executable, "-m", "pip", "install", dep], 
                              check=True, capture_output=True)
            print("   ✅ Basic dependencies installed")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Error installing dependencies: {e}")
        return False

def setup_configuration():
    """Setup configuration files"""
    print("⚙️  Setting up configuration...")
    
    try:
        config_dir = Path(__file__).parent / "config"
        config_dir.mkdir(exist_ok=True)
        
        # Check if config files exist
        default_config = config_dir / "default.yaml"
        if not default_config.exists():
            print("   ⚠️  Default configuration not found")
            return False
        
        print("   ✅ Configuration files ready")
        return True
        
    except Exception as e:
        print(f"   ❌ Error setting up configuration: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    print("📁 Creating directories...")
    
    try:
        base_dir = Path(__file__).parent
        
        directories = [
            "models",
            "logs",
            "data",
            "cache",
            "outputs"
        ]
        
        for dir_name in directories:
            dir_path = base_dir / dir_name
            dir_path.mkdir(exist_ok=True)
            print(f"   ✅ Created: {dir_name}/")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error creating directories: {e}")
        return False

def run_tests():
    """Run basic tests"""
    print("🧪 Running basic tests...")
    
    try:
        # Test imports
        sys.path.insert(0, str(Path(__file__).parent / "src"))
        
        from seve_framework import SEVEConfig, SEVEMode, PrivacyLevel, EthicsLevel
        print("   ✅ Core imports successful")
        
        # Test configuration
        config = SEVEConfig()
        print("   ✅ Configuration creation successful")
        
        # Test framework creation
        from seve_framework import SEVEHybridFramework
        framework = SEVEHybridFramework(config)
        print("   ✅ Framework creation successful")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error running tests: {e}")
        return False

def main():
    """Main installation function"""
    print("🚀 SEVE Framework Installation")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check system requirements
    if not check_system_requirements():
        print("❌ System requirements not met")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Dependency installation failed")
        sys.exit(1)
    
    # Setup configuration
    if not setup_configuration():
        print("❌ Configuration setup failed")
        sys.exit(1)
    
    # Create directories
    if not create_directories():
        print("❌ Directory creation failed")
        sys.exit(1)
    
    # Run tests
    if not run_tests():
        print("❌ Basic tests failed")
        sys.exit(1)
    
    print("\n🎉 Installation completed successfully!")
    print("\n📋 Next steps:")
    print("   1. Run the demo: python run_seve.py --mode basic")
    print("   2. Check configuration: python -c 'from seve_framework import setup_config; print(setup_config())'")
    print("   3. Read the documentation: docs/README.md")
    print("\n🌍 SEVE Framework is ready for ethical AI applications!")

if __name__ == "__main__":
    main()
