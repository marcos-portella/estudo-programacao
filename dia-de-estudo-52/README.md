## Dia 52: O Ciclo Completo do CRUD e a Inteligência das Rotas

### Prefácio:

No **Dia 52**, consolidamos o domínio sobre as operações de um sistema profissional ao completar o ciclo **CRUD** (Create, Read, Update, Delete). O foco principal foi a implementação da busca individualizada e da atualização de registros, explorando a fundo a diferença entre dados enviados pela URL (**Path Parameters**) e dados enviados no corpo da requisição (**Request Body**). Além disso, refinamos a experiência do usuário com tratamentos de erros específicos para registros inexistentes.

### 1. Dinamismo com Path Parameters e Busca Individual:

Aprendemos que as chaves na URL (``{id}``) criam variáveis dinâmicas que o FastAPI injeta automaticamente em nossas funções. Para otimizar a performance e o uso de memória, introduzimos o método ``cursor.fetchone()``, ideal para consultas que retornam apenas um único registro (como buscas por ID).

````
# Exemplo 1: Busca Refinada com Tratamento de Erro 404
@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # Buscamos um ID específico vindo da URL (Path Parameter)
            sql = "SELECT * FROM customers WHERE id = %s"
            cursor.execute(sql, (customer_id,))
            result = cursor.fetchone() 
            
            # Validação: se o banco retornar None, lançamos o erro 404
            if result is None:
                raise HTTPException(status_code=404, detail="Customer not found in database")
            
            return result # Retorna o dicionário com os dados
    finally:
        connection.close()
````

### 2. Atualização Completa (PUT) e Validação Dupla:

O método **PUT** foi o nosso maior desafio técnico hoje. Ele exige a combinação de dois conceitos: o **Path Parameter** para identificar quem será atualizado e o **Request Body** (via Pydantic) para definir o que será alterado. Esta estrutura garante que a atualização seja precisa e que os novos dados sigam todas as regras de negócio.

````
# Exemplo 2: Atualização Completa (PUT) validada pelo Pydantic
@app.put("/customers/{customer_id}")
def update_customer(customer_id: int, customer: Customer):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # Atualizamos nome e idade, filtrando pelo ID da rota
            sql = "UPDATE customers SET name = %s, age = %s WHERE id = %s"
            cursor.execute(sql, (customer.name, customer.age, customer_id))
            
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Update failed: ID not found")
                
        connection.commit()
        return {"message": f"Customer {customer_id} updated successfully"}
    finally:
        connection.close()
````

### 3. Anatomia de uma Requisição Profissional:

Durante a implementação, ficou clara a divisão de responsabilidades. O **Path Parameter** identifica o alvo, enquanto o **Body** transporta o pacote de dados. No exemplo abaixo, vemos como a tipagem do Python ajuda o FastAPI a distinguir automaticamente de onde cada informação deve vir.

````
# Exemplo 3: Diferenciação de fluxos (Body vs Path)
# 'customer_id' vem da URL, 'customer' vem do JSON no corpo da mensagem
@app.patch("/customers-partial/{customer_id}") # Exemplo conceitual de PATCH
def update_partial(customer_id: int, customer: Customer):
    # Lógica de atualização parcial aqui...
    pass
````

### 4. Resolução de Conflitos e Sintaxe:

Enfrentamos erros comuns de desenvolvimento, como o ``Non-default argument follows default argument``. Aprendemos que no Python, parâmetros obrigatórios (com tipagem ``:``) devem vir antes de parâmetros com valores padrão (com ``=``). Também resolvemos o "Mistério do null", onde a ausência da palavra ``return`` causava respostas vazias na API.

````
# Exemplo 4: Sintaxe correta e uso de CursorContext
# O uso de 'with' garante que o cursor seja fechado mesmo se houver erro
with connection.cursor() as cursor:
    cursor.execute("SELECT 1")
    # Lembre-se sempre de retornar o valor desejado!
    # return cursor.fetchone() 
````

### Observações Finais:

O **Dia 52** encerra a lógica básica de manipulação de dados. Agora possuímos uma API que não apenas "funciona", mas que é inteligente o suficiente para validar entradas, diferenciar métodos de envio e comunicar estados de erro de forma técnica. O domínio sobre o ``cursor.rowcount`` e o ``cursor.fetchone()`` nos dá um controle granular sobre o que acontece dentro do banco de dados MySQL a cada requisição.