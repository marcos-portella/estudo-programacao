## Diário de Bordo: Evolução API Clientes
### Desenvolvedor: Marcos Portella

### Objetivo: Registro diário de desafios técnicos, soluções de arquitetura e progresso em FastAPI e MySQL.


## Dia 57: A Grande Refatoração (Arquitetura Modular)

### Objetivo do Dia:

Transição da estrutura monolítica (arquivo único) para uma arquitetura profissional baseada em pacotes, separando responsabilidades em pastas específicas.

### Desafios Superados:

- **Inferno dos Imports**: Resolvido o erro ``ModuleNotFoundError`` configurando o ``PYTHONPATH`` e usando a execução via módulo (``python -m``).

- **Sincronia do VS Code**: Ajustado o ``settings.json`` para eliminar falsos positivos de erro (vermelhos) do Pylance/Mypy.

- **Roteamento**: Configuração de prefixos no ``main.py`` para evitar URLs duplicadas ou erros ``404 Not Found``.

### Códigos de Destaque:

**1. Estrutura de Modelos Isolada (``app/models/customer.py``)**

````
from pydantic import BaseModel, Field

class Customer(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=0, le=120)
````

### 2. Orquestração de Rotas (``app/main.py``):

````
from fastapi import FastAPI
from app.routers import customers

app = FastAPI()

# Registro modular das rotas de clientes
app.include_router(customers.router, prefix="/customers", tags=["Customers"])

@app.get("/")
def root():
    return {"message": "API Online - Estrutura Modularizada!"}
````

### Status Final:

- **Servidor**: Rodando via uvicorn app.main:app --reload.

- **Testes**: 8 testes de integração passando (PASSED).

- **Arquitetura**: Padrão de mercado com pastas app/, routers/, models/ e tests/.