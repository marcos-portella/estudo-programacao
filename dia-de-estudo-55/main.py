from fastapi import FastAPI
from routers import customers  # Importamos o nosso novo ficheiro

app = FastAPI()

# "Incluímos" as rotas de clientes na nossa aplicação principal
app.include_router(customers.router)


@app.get("/")
def root():
    return {"message": "API Online - Estrutura Modularizada!"}

#  uvicorn main:app --reload
#  http://127.0.0.1:8000/docs
