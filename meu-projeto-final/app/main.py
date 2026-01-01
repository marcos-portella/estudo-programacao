from fastapi import FastAPI
from app.routers import customers  # Adicionamos o 'app.' na frente

app = FastAPI()

app.include_router(customers.router, prefix="/customers", tags=["customers"])


@app.get("/")
def root():
    return {"message": "API Online - Estrutura Modularizada!"}

#  uvicorn app.main:app --reload
#  http://127.0.0.1:8000/docs
