from fastapi import FastAPI
from routers import customers

app = FastAPI()

app.include_router(customers.router)


@app.get("/")
def root():
    return {"message": "API Online - Estrutura Modularizada!"}

#  uvicorn main:app --reload
#  http://127.0.0.1:8000/docs
