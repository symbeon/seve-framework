#!/usr/bin/env python3
"""
SEVE Framework - Setup Script
Symbiotic Ethical Vision Engine

This script handles the setup and installation of the SEVE Framework.
"""

from setuptools import setup, find_packages
import os
import sys
from pathlib import Path

# Read the README file
def read_readme():
    readme_path = Path(__file__).parent / "README.md"
    if readme_path.exists():
        return read_readme().read_text(encoding="utf-8")
    return "SEVE Framework - Symbiotic Ethical Vision Engine"

# Read requirements
def read_requirements():
    requirements_path = Path(__file__).parent / "requirements.txt"
    if requirements_path.exists():
        with open(requirements_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

# Read version
def read_version():
    version_path = Path(__file__).parent / "src" / "seve_framework" / "__init__.py"
    if version_path.exists():
        with open(version_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('__version__'):
                    return line.split('=')[1].strip().strip('"\'')
    return "3.0.0"

# Setup configuration
setup(
    name="seve-framework",
    version=read_version(),
    author="Symbeon Tech - EON Team",
    author_email="research@symbeon-tech.com",
    description="Symbiotic Ethical Vision Engine - Universal Adaptive Intelligence Framework",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/symbeon-tech/seve-framework",
    project_urls={
        "Homepage": "https://symbeon-tech.com",
        "Documentation": "https://docs.seve-framework.ai",
        "Repository": "https://github.com/symbeon-tech/seve-framework",
        "Bug Tracker": "https://github.com/symbeon-tech/seve-framework/issues",
        "Source Code": "https://github.com/symbeon-tech/seve-framework",
        "Download": "https://github.com/symbeon-tech/seve-framework/releases",
        "Changelog": "https://github.com/symbeon-tech/seve-framework/blob/main/CHANGELOG.md",
        "License": "https://github.com/symbeon-tech/seve-framework/blob/main/LICENSE_Symbeon_Vault.md"
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Education",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: GPU",
        "Environment :: Console",
        "Environment :: Web Environment",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "gpu": [
            "cupy-cuda11x>=9.0.0",
            "nvidia-ml-py3>=7.352.0",
        ],
        "dev": [
            "pytest>=6.2.0",
            "pytest-asyncio>=0.18.0",
            "pytest-cov>=2.12.0",
            "black>=21.0.0",
            "isort>=5.9.0",
            "flake8>=3.9.0",
            "mypy>=0.910",
            "pre-commit>=2.15.0",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "myst-parser>=0.15.0",
            "sphinxcontrib-mermaid>=0.7.0",
        ],
        "all": [
            "seve-framework[gpu,dev,docs]"
        ]
    },
    entry_points={
        "console_scripts": [
            "seve=seve_framework.cli:main",
            "seve-demo=seve_framework.demo:run_demo",
            "seve-config=seve_framework.config:setup_config",
            "seve-test=seve_framework.test:run_tests",
        ],
        "gui_scripts": [
            "seve-gui=seve_framework.gui:main",
        ],
    },
    package_data={
        "seve_framework": [
            "config/*.yaml",
            "config/*.json", 
            "models/*.pth",
            "models/*.onnx",
            "data/*.json",
            "data/*.csv",
            "templates/*.html",
            "static/*.css",
            "static/*.js",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "artificial-intelligence",
        "computer-vision", 
        "ethical-ai",
        "privacy-by-design",
        "adaptive-intelligence",
        "symbiotic-ai",
        "universal-framework",
        "machine-learning",
        "deep-learning",
        "neural-networks",
        "computer-vision",
        "image-processing",
        "object-detection",
        "facial-recognition",
        "privacy-protection",
        "data-anonymization",
        "ethical-validation",
        "guardflow",
        "symbeon-vault",
        "symbeon-tech",
        "eon-team"
    ],
    license="Symbeon-Vault",
    platforms=["any"],
    test_suite="tests",
    tests_require=[
        "pytest>=6.2.0",
        "pytest-asyncio>=0.18.0",
        "pytest-cov>=2.12.0",
    ],
)

if __name__ == "__main__":
    print("🚀 SEVE Framework Setup")
    print("=" * 50)
    print("Installing SEVE Framework...")
    print("This may take a few minutes.")
    print()
    print("For more information, visit:")
    print("https://github.com/symbeon-tech/seve-framework")
    print()
    print("🌍 Building Ethical AI Together!")
