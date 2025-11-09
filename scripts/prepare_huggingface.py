#!/usr/bin/env python3
"""
Script para preparar SEVE Framework para publicação no Hugging Face
"""

import os
import shutil
import subprocess
from pathlib import Path

def create_requirements_txt():
    """Cria requirements.txt a partir do pyproject.toml"""
    print("📦 Criando requirements.txt...")
    
    requirements = [
        "numpy>=1.21.0",
        "opencv-python>=4.5.0",
        "pillow>=8.3.0",
        "torch>=1.9.0",
        "torchvision>=0.10.0",
        "transformers>=4.20.0",
        "scikit-learn>=1.0.0",
        "pandas>=1.3.0",
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "pydantic>=1.8.0",
        "aiofiles>=0.7.0",
        "python-multipart>=0.0.5",
        "httpx>=0.24.0",
        "cryptography>=3.4.0",
        "pyyaml>=6.0",
        "loguru>=0.6.0",
        "asyncio-mqtt>=0.11.0",
        "redis>=4.0.0",
        "sqlalchemy>=1.4.0",
        "alembic>=1.7.0",
    ]
    
    with open("requirements.txt", "w") as f:
        f.write("\n".join(requirements) + "\n")
    
    print("✅ requirements.txt criado!")

def create_gitignore():
    """Cria .gitignore para Hugging Face"""
    print("📝 Criando .gitignore...")
    
    gitignore_content = """__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.so
*.egg
*.egg-info/
dist/
build/
.venv/
venv/
.env
*.log
.DS_Store
*.swp
*.swo
*~
"""
    
    with open(".gitignore", "w") as f:
        f.write(gitignore_content)
    
    print("✅ .gitignore criado!")

def check_files():
    """Verifica se arquivos necessários existem"""
    print("🔍 Verificando arquivos necessários...")
    
    required_files = [
        "README.md",
        "LICENSE_Symbeon_Vault.md",
        "model_card.md",
        "pyproject.toml",
        "requirements.txt",
        "src/seve_framework/__init__.py",
    ]
    
    missing = []
    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)
        else:
            print(f"  ✅ {file}")
    
    if missing:
        print(f"\n⚠️  Arquivos faltando: {', '.join(missing)}")
        return False
    
    print("✅ Todos os arquivos necessários estão presentes!")
    return True

def create_upload_structure():
    """Cria estrutura para upload"""
    print("📁 Criando estrutura para upload...")
    
    upload_dir = Path("hf_upload")
    if upload_dir.exists():
        shutil.rmtree(upload_dir)
    upload_dir.mkdir()
    
    # Copiar arquivos necessários
    files_to_copy = [
        ("src", "src"),
        ("examples", "examples"),
        ("README.md", "README.md"),
        ("LICENSE_Symbeon_Vault.md", "LICENSE_Symbeon_Vault.md"),
        ("model_card.md", "model_card.md"),
        ("requirements.txt", "requirements.txt"),
        ("pyproject.toml", "pyproject.toml"),
    ]
    
    for src, dst in files_to_copy:
        src_path = Path(src)
        if src_path.exists():
            if src_path.is_dir():
                shutil.copytree(src_path, upload_dir / dst)
            else:
                shutil.copy2(src_path, upload_dir / dst)
            print(f"  ✅ Copiado: {src}")
    
    # Criar .gitignore no upload_dir
    create_gitignore()
    shutil.copy2(".gitignore", upload_dir / ".gitignore")
    
    print(f"✅ Estrutura criada em: {upload_dir}")
    return upload_dir

def main():
    """Função principal"""
    print("🚀 Preparando SEVE Framework para Hugging Face\n")
    
    # Verificar se estamos no diretório correto
    if not os.path.exists("src/seve_framework"):
        print("❌ Erro: Execute este script na raiz do projeto SEVE-FRAMEWORK")
        return
    
    # Criar requirements.txt se não existir
    if not os.path.exists("requirements.txt"):
        create_requirements_txt()
    
    # Criar .gitignore se não existir
    if not os.path.exists(".gitignore"):
        create_gitignore()
    
    # Verificar arquivos
    if not check_files():
        print("\n❌ Alguns arquivos estão faltando. Por favor, crie-os antes de continuar.")
        return
    
    # Criar estrutura de upload
    upload_dir = create_upload_structure()
    
    print("\n✅ Preparação concluída!")
    print("\n📋 Próximos passos:")
    print("  1. Instalar huggingface_hub: pip install huggingface_hub")
    print("  2. Login: huggingface-cli login")
    print("  3. Upload: cd hf_upload && huggingface-cli upload symbeon/seve-framework . --repo-type model")
    print("\n📚 Veja o guia completo em: docs/GUIA_PUBLICACAO_HUGGING_FACE.md")

if __name__ == "__main__":
    main()

