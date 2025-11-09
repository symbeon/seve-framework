"""
GuardFlow API - Main Application
Agiliza aí suas compras! 🚀
"""
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import time
import logging
import logging.config
import os
from contextlib import asynccontextmanager

# Imports locais
from app.config import settings, get_cors_origins, LOGGING_CONFIG, AppMessages
from app.database import init_db, close_db
from app.api import auth, scanner, cart, payment, store, health

# Configurar logging
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("guardflow")

# Rate limiter
limiter = Limiter(key_func=get_remote_address)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gerenciar ciclo de vida da aplicação"""
    # Startup
    logger.info("🚀 GuardFlow API iniciando - Agiliza aí!")
    
    # Inicializar banco de dados
    await init_db()
    
    # Criar diretórios necessários
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    
    logger.info("✅ GuardFlow API pronta para agilizar!")
    
    yield
    
    # Shutdown
    logger.info("🛑 GuardFlow API finalizando...")
    await close_db()
    logger.info("👋 GuardFlow API finalizada - Agilizou!")

# Criar aplicação FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
    openapi_url="/openapi.json" if settings.DEBUG else None,
    lifespan=lifespan
)

# Configurar rate limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=get_cors_origins(),
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
)

# Middleware de hosts confiáveis
if not settings.DEBUG:
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=settings.ALLOWED_HOSTS
    )

# Middleware de timing
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Adicionar header com tempo de processamento"""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    response.headers["X-GuardFlow-Version"] = settings.APP_VERSION
    return response

# Middleware de logging
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log de todas as requisições"""
    start_time = time.time()
    
    # Log da requisição
    logger.info(
        f"🚀 {request.method} {request.url.path} - "
        f"IP: {request.client.host if request.client else 'unknown'}"
    )
    
    try:
        response = await call_next(request)
        
        # Log da resposta
        process_time = time.time() - start_time
        logger.info(
            f"✅ {request.method} {request.url.path} - "
            f"Status: {response.status_code} - "
            f"Time: {process_time:.3f}s"
        )
        
        return response
        
    except Exception as e:
        process_time = time.time() - start_time
        logger.error(
            f"❌ {request.method} {request.url.path} - "
            f"Error: {str(e)} - "
            f"Time: {process_time:.3f}s"
        )
        raise

# Exception handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Handler para exceções HTTP com mensagens amigáveis"""
    
    # Mapear códigos de status para mensagens "agiliza aí"
    friendly_messages = {
        400: "Ops! Algo não agilizou na sua requisição. Verifica os dados aí! 😅",
        401: "Acesso não agilizou. Faz login novamente! 🔐",
        403: "Permissão não agilizou. Sem acesso a essa área! 🚫",
        404: "Não encontramos isso aí. Verifica se o caminho está certo! 🔍",
        422: "Dados não agilizaram. Verifica se tudo está preenchido certinho! 📝",
        429: "Calma aí! Muitas requisições. Aguarda um pouquinho! ⏰",
        500: "Algo deu errado aqui, mas vamos agilizar isso! Tenta de novo! ⚡"
    }
    
    message = friendly_messages.get(exc.status_code, exc.detail)
    
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": message,
            "detail": exc.detail if settings.DEBUG else None,
            "status_code": exc.status_code,
            "timestamp": time.time(),
            "path": request.url.path
        }
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Handler para exceções gerais"""
    logger.error(f"❌ Erro não tratado: {str(exc)}", exc_info=True)
    
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": AppMessages.SERVER_ERROR,
            "detail": str(exc) if settings.DEBUG else None,
            "status_code": 500,
            "timestamp": time.time(),
            "path": request.url.path
        }
    )

# Rotas principais
@app.get("/")
async def root():
    """Endpoint raiz com informações da API"""
    return {
        "message": "GuardFlow API - Agiliza aí suas compras! 🚀",
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "docs_url": "/docs" if settings.DEBUG else "Disponível apenas em desenvolvimento",
        "status": "agilizando",
        "slogan": "Agiliza aí! ⚡"
    }

@app.get("/health")
@limiter.limit("30/minute")
async def health_check(request: Request):
    """Health check da aplicação"""
    return {
        "status": "healthy",
        "message": "GuardFlow agilizando perfeitamente! ✅",
        "version": settings.APP_VERSION,
        "timestamp": time.time(),
        "environment": settings.ENVIRONMENT
    }

@app.get("/agiliza")
async def agiliza():
    """Endpoint especial com o slogan"""
    return {
        "message": "Agiliza aí! 🚀",
        "slogan": "GuardFlow - O checkout que agiliza suas compras!",
        "powered_by": "GuardPass",
        "version": settings.APP_VERSION,
        "status": "agilizando_sempre"
    }

# Incluir routers das APIs
app.include_router(
    health.router,
    prefix="/health",
    tags=["Health Check"]
)

app.include_router(
    auth.router,
    prefix=f"{settings.API_V1_PREFIX}/auth",
    tags=["Autenticação"]
)

app.include_router(
    scanner.router,
    prefix=f"{settings.API_V1_PREFIX}/scanner",
    tags=["Scanner"]
)

app.include_router(
    cart.router,
    prefix=f"{settings.API_V1_PREFIX}/cart",
    tags=["Carrinho"]
)

app.include_router(
    payment.router,
    prefix=f"{settings.API_V1_PREFIX}/payment",
    tags=["Pagamentos"]
)

app.include_router(
    store.router,
    prefix=f"{settings.API_V1_PREFIX}/stores",
    tags=["Supermercados"]
)

# Servir arquivos estáticos (uploads)
if os.path.exists("uploads"):
    app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Endpoint para testar rate limiting
@app.get("/test-rate-limit")
@limiter.limit("5/minute")
async def test_rate_limit(request: Request):
    """Testar rate limiting"""
    return {
        "message": "Rate limit funcionando! Agiliza aí com moderação! ⚡",
        "timestamp": time.time()
    }

# Informações da API para desenvolvimento
if settings.DEBUG:
    @app.get("/info")
    async def api_info():
        """Informações detalhadas da API (apenas desenvolvimento)"""
        return {
            "app_name": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "environment": settings.ENVIRONMENT,
            "debug": settings.DEBUG,
            "database_url": settings.DATABASE_URL.split("@")[0] + "@***",  # Ocultar credenciais
            "redis_url": settings.REDIS_URL.split("@")[0] + "@***" if "@" in settings.REDIS_URL else settings.REDIS_URL,
            "cors_origins": get_cors_origins(),
            "features": {
                "product_recommendations": settings.ENABLE_PRODUCT_RECOMMENDATIONS,
                "loyalty_program": settings.ENABLE_LOYALTY_PROGRAM,
                "esg_tracking": settings.ENABLE_ESG_TRACKING,
                "analytics": settings.ENABLE_ANALYTICS
            },
            "limits": {
                "max_file_size": f"{settings.MAX_FILE_SIZE / (1024*1024)}MB",
                "max_cart_items": settings.MAX_CART_ITEMS,
                "cart_expiry_hours": settings.CART_EXPIRY_HOURS,
                "rate_limit_per_minute": settings.RATE_LIMIT_PER_MINUTE
            },
            "message": "Informações disponíveis apenas em desenvolvimento! 🔧"
        }

# Startup message
@app.on_event("startup")
async def startup_message():
    """Mensagem de startup"""
    logger.info("=" * 60)
    logger.info("🚀 GUARDFLOW API - AGILIZA AÍ! 🚀")
    logger.info("=" * 60)
    logger.info(f"📱 Versão: {settings.APP_VERSION}")
    logger.info(f"🌍 Ambiente: {settings.ENVIRONMENT}")
    logger.info(f"🔧 Debug: {settings.DEBUG}")
    logger.info(f"🌐 API Base URL: {settings.API_BASE_URL}")
    logger.info(f"📊 Docs: {settings.API_BASE_URL}/docs" if settings.DEBUG else "📊 Docs: Desabilitado em produção")
    logger.info("=" * 60)
    logger.info("✅ Pronto para agilizar suas compras!")
    logger.info("=" * 60)

if __name__ == "__main__":
    import uvicorn
    
    # Configurações do servidor
    server_config = {
        "app": "app.main:app",
        "host": "0.0.0.0",
        "port": 8000,
        "reload": settings.DEBUG,
        "log_level": settings.LOG_LEVEL.lower(),
        "access_log": True,
    }
    
    print("🚀 Iniciando GuardFlow API - Agiliza aí!")
    print(f"📱 Acesse: http://localhost:8000")
    print(f"📊 Docs: http://localhost:8000/docs" if settings.DEBUG else "")
    print("=" * 50)
    
    uvicorn.run(**server_config)
