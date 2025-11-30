# SEVE Framework - Dockerfile
# Base image: Python 3.9 Slim (Leve e segura)
FROM python:3.9-slim

# Metadados
LABEL maintainer="Symbeon Tech <contato@symbeon.tech>"
LABEL description="SEVE Framework - Symbiotic Ethical Vision Engine"
LABEL version="1.0.0-beta"

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    SEVE_ENV=production

# Diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema necessárias para OpenCV e build
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements primeiro (cache layer)
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fonte
COPY . .

# Instalar o pacote em modo editável
RUN pip install -e .

# Criar usuário não-root para segurança
RUN useradd -m seveuser
USER seveuser

# Comando padrão: CLI Help
ENTRYPOINT ["python", "seve_cli.py"]
CMD ["--help"]
