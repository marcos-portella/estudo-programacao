import time
import logging
from fastapi import FastAPI, Request
from app.routers import customers, orders, auth

# 1. Configuração do Log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("API-Auditoria")

app = FastAPI()


# 2. O Middleware (O "Porteiro" que registra tudo)
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    # Informações da requisição
    logger.info(f" {request.method} {request.url.path} - Iniciado")

    response = await call_next(request)

    # Cálculo de tempo
    process_time = (time.time() - start_time) * 1000
    formatted_time = f"{process_time:.2f}ms"

    logger.info(f"✅ Status: {response.status_code} | Tempo: {formatted_time}")

    response.headers["X-Process-Time"] = formatted_time
    return response

# 3. Inclusão das Rotas
app.include_router(customers.router)  # Se o prefixo já estiver no router.py
app.include_router(orders.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "API Online - Monitoramento Ativo!"}
#  uvicorn app.main:app --reload
#  http://127.0.0.1:8000/docs
