## Dia 55: Maturidade REST, Identificadores Únicos e Autonomia de Debug

### Prefácio:

No **Dia 55**, a API atingiu um novo patamar de maturidade técnica. O foco foi o refinamento do **Contrato de Resposta (REST)** e a implementação de fluxos de dados mais inteligentes, como a captura de identificadores gerados pelo banco de dados. Além disso, houve um avanço significativo na capacidade de **debug autônomo**, com a resolução de divergências em testes de integração e o tratamento de metadados, garantindo que a aplicação seja capaz de informar exatamente o que aconteceu com cada recurso criado.

### 1. Captura de Metadados e Respostas Estruturadas:

Uma API profissional deve informar ao cliente o identificador do recurso que acabou de ser criado. Utilizamos o atributo ``cursor.lastrowid`` do conector MySQL para recuperar o ID gerado pelo ``AUTO_INCREMENT``. Com isso, a resposta do método **POST** deixou de ser uma mensagem simples para se tornar um objeto JSON completo.

````
# Exemplo 1: Rota POST com retorno de ID e Objeto Criado
@router.post("/")
def create_customer(customer: Customer):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO customers (nome, idade) VALUES (%s, %s)"
            cursor.execute(sql, (customer.name, customer.age))
            # Captura o ID gerado pelo banco de dados
            new_id = cursor.lastrowid
            
        connection.commit()
        # Retorno estruturado seguindo padrões REST
        return {
            "id": new_id, 
            "message": "Customer created successfully", 
            "data": customer
        }
    finally:
        connection.close()
````

### 2. Consulta Individual com Dicionários (Dictionary Cursor):

Refinamos a rota de busca por ID utilizando o parâmetro ``dictionary=True`` no cursor. Isso garante que o resultado da consulta SQL seja mapeado automaticamente para um dicionário Python, facilitando a conversão para JSON e permitindo o uso de aliases no SQL para alinhar os nomes das colunas (``nome`` para ``name``).

````
# Exemplo 2: Rota GET por ID com mapeamento de dicionário
@router.get("/{customer_id}")
def get_customer(customer_id: int):
    connection = get_connection()
    try:
        # 'dictionary=True' faz o cursor retornar chaves (nome das colunas) e valores
        with connection.cursor(dictionary=True) as cursor:
            sql = "SELECT id, nome as name, idade as age FROM customers WHERE id = %s"
            cursor.execute(sql, (customer_id,))
            result = cursor.fetchone()
            
            if result is None:
                raise HTTPException(status_code=404, detail="Customer not found")
            return result
    finally:
        connection.close()
````

### 3. Testes End-to-End (E2E) e Ciclo de Vida do Recurso:

Implementamos um teste de integração que valida todo o ciclo de vida de um dado: Criar o cliente -> Capturar seu novo ID -> Consultar a rota GET com esse ID -> Deletar o registro para não deixar rastros. Esse fluxo garante que todas as engrenagens da API (MySQL, FastAPI e Pydantic) estejam girando em harmonia.

````
# Exemplo 3: Teste de Integração de fluxo completo
def test_full_customer_lifecycle():
    client = TestClient(app)
    # 1. Cria o recurso
    post_res = client.post("/customers/", json={"name": "Lifecycle Test", "age": 40})
    customer_id = post_res.json()["id"]
    
    # 2. Valida se o recurso existe via GET
    get_res = client.get(f"/customers/{customer_id}")
    assert get_res.status_code == 200
    assert get_res.json()["name"] == "Lifecycle Test"
    
    # 3. Teardown (limpeza) acontece após a validação...
````

### 4. Independência no Debug e Resolução de Erros:

O dia também foi marcado pela resolução autônoma de desafios comuns no desenvolvimento de back-end:

- **AssertionError**: Ajuste de mensagens de erro para que o teste e a API falem a mesma língua.

- **KeyError**: Prevenção de erros ao acessar chaves de resposta que podem não existir em caso de falha.

- **Privacidade**: Sanitização de logs para remover caminhos absolutos de máquinas locais, seguindo boas práticas de segurança.

````
# Exemplo 4: Tratamento de erro de validação (422) nos testes
def test_validation_error():
    client = TestClient(app)
    # Enviar dados que violam o Field do Pydantic (age < 0)
    response = client.post("/customers/", json={"name": "X", "age": -1})
    # O Pydantic deve barrar e o FastAPI retornar 422
    assert response.status_code == 422
````
### Observações Finais:

O **Dia 55** encerra com um saldo extremamente positivo: **6 testes aprovados em 0.66s**. A API agora possui uma lógica de recuperação de IDs (``lastrowid``), busca individualizada com tratamento de erro 404 e uma bateria de testes que cobre desde a criação até a validação rigorosa com Pydantic. A habilidade de identificar e corrigir erros de lógica e divergência de dados de forma independente solidifica a base necessária para projetos de maior escala.