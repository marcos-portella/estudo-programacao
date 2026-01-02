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


## Diário de Bordo: Evolução da API de Clientes
### Desenvolvedor: Marcos Portella

**Status Atual**: Estrutura Modular com Injeção de Dependência

## Dia 58: Refatoração com Dependency Injection (Depends)

### Objetivo:
Eliminar a redundância de código (boilerplate) na gestão de conexões com o banco de dados e garantir o fechamento automático de recursos, utilizando os recursos nativos do FastAPI.

**Evolução da Arquitetura**:

Saímos de um modelo onde cada rota gerenciava sua própria conexão (abrir, cometer, fechar) para um modelo de **Injeção de Dependência**.

### Principais Mudanças:

**1. Criação do ``app/dependencies.py``**: Centralização da lógica de conexão usando o gerador ``yield``.

**2. Uso do ``Depends``**: As rotas agora recebem o objeto ``db`` pronto para uso como parâmetro, aumentando a testabilidade.

**3. Lógica de Escrita Otimizada**: Implementação do ``cursor.rowcount`` no ``PUT`` e ``DELETE`` para validar a existência do registro sem a necessidade de um ``SELECT`` prévio.

### Códigos de Destaque:

**1. Gerenciador de Ciclo de Vida do Banco (get_db)**:

````
def get_db() -> Generator:
    connection = get_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    try:
        yield connection  # Fornece a conexão para a rota
    finally:
        connection.close() # Executado automaticamente após a resposta HTTP
        print("Conexão encerrada com segurança.")
````

**2. Rota de Deleção Profissional (Clean Code)**:

````
@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: MySQLConnectionAbstract = Depends(get_db)):
    with db.cursor() as cursor:
        cursor.execute("DELETE FROM customers WHERE id = %s", (customer_id,))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Customer not found")
        db.commit()
        return {"message": "Customer deleted successfully", "id": customer_id}
````

### Resultados e Métricas:

- **Testes Automatizados**: 8 testes de integração executados com sucesso (8 PASSED).

- **Tempo de Execução**: ~0.66s.

- **Qualidade**: Remoção de blocos try/finally repetitivos em todas as rotas de clientes.

### Lições Aprendidas:

- O ``yield`` no FastAPI é uma ferramenta poderosa para gerenciar recursos que precisam de setup e teardown.

- A injeção de dependência desacopla a lógica de negócio da infraestrutura.

- Trabalhar com a suite de testes verde durante a refatoração dá a segurança necessária para grandes mudanças.