## Dia 51: Evoluindo para uma API Profissional (Pydantic e HTTP Status)

### Prefácio:

O **Dia 51** foi focado em elevar o nível de maturidade da nossa aplicação. Saímos de scripts funcionais para implementar padrões de mercado utilizados em arquiteturas profissionais. O objetivo central foi garantir a **integridade dos dados** através do Pydantic, implementar um **tratamento de erros** robusto com códigos de status HTTP reais e alinhar o projeto aos padrões internacionais de nomenclatura em inglês.

### 1. Validação com Schemas (Pydantic):

Em vez de receber parâmetros soltos nas rotas, passamos a utilizar o ``BaseModel`` do Pydantic para criar "moldes" (Schemas). Com o uso do ``Field``, aplicamos regras de negócio diretamente na entrada dos dados, como tamanho mínimo de nomes e limites de idade, impedindo que dados inválidos cheguem ao banco de dados.

````
from pydantic import BaseModel, Field

# Schema para validação de entrada de dados
class Customer(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=0, le=120)

# O FastAPI agora espera um JSON que siga exatamente este molde
````

### 2. Rotas de Cadastro (POST) e Nomenclatura Internacional:

Refatoramos o código para o inglês, seguindo o padrão global de desenvolvimento (``Customer`` em vez de ``Cliente``). Ao receber o objeto ``Customer``, o FastAPI valida automaticamente o JSON enviado pelo cliente.

````
@app.post("/customers")
def create_customer(customer: Customer):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO customers (name, age) VALUES (%s, %s)"
            cursor.execute(sql, (customer.name, customer.age))
        conn.commit()
        return {"message": "Customer created successfully"}
    finally:
        conn.close()
````

### 3. Tratamento de Erros com HTTPException (DELETE):

Implementamos o uso de ``HTTPException``. Agora, se tentarmos deletar um usuário que não existe, a API não retorna apenas uma mensagem comum, mas sim um **Status Code 404 (Not Found)**, permitindo que o front-end ou outros sistemas tratem o erro de forma técnica e padronizada.

````
from fastapi import HTTPException

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Verifica se o registro existe
            cursor.execute("DELETE FROM customers WHERE id = %s", (customer_id,))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Customer not found")
        conn.commit()
        return {"message": f"Customer {customer_id} deleted"}
    finally:
        conn.close()
````

### 4. Gerenciadores de Contexto e Tipagem:

Reforçamos o uso do ``with`` (context manager) para garantir que o cursor do banco de dados seja fechado corretamente, mesmo em caso de falhas. Além disso, a tipagem forte (``customer_id: int``) auxilia o editor de código a prevenir bugs de lógica durante o desenvolvimento.

````
# Exemplo de leitura garantindo tipagem e fechamento de cursor
@app.get("/customers")
def get_customers():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM customers")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()
````

### Observações Finais:

O progresso do Dia 51 demonstra uma preocupação com a **robustez e manutenibilidade**. A transição para o inglês e a adoção do Pydantic preparam o sistema para ser consumido por qualquer desenvolvedor no mundo. Aprendemos que uma API de qualidade não é apenas aquela que salva dados, mas aquela que protege o banco de dados contra entradas inválidas e comunica seus erros de forma clara através dos protocolos HTTP.