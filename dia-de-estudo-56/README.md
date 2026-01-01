## Dia 56: Fechamento do Ciclo CRUD, Transações e Performance

### Prefácio:

No **Dia 56**, avançamos para a etapa de refinamento e estabilização da API. O foco não foi apenas fazer as funcionalidades funcionarem, mas garantir que operem com **performance otimizada** e **consistência de dados**. Enfrentamos desafios reais de backend, como o gerenciamento de estados de conexão (evitando o erro de unread results) e o uso estratégico de atributos do cursor para reduzir a latência das operações no banco de dados MySQL.

### 1. Performance no DELETE com rowcount:

Uma técnica comum, porém menos eficiente, é realizar um ``SELECT`` para verificar a existência de um registro antes de deletá-lo. No Dia 56, otimizamos este fluxo utilizando o atributo ``cursor.rowcount``. Com apenas um comando SQL enviado ao banco, conseguimos deletar o registro e, simultaneamente, verificar se ele realmente existia, reduzindo o tráfego de rede e a carga no servidor.

````
# Exemplo 1: Rota DELETE otimizada (routers/customers.py)
@router.delete("/{customer_id}")
def delete_customer(customer_id: int):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM customers WHERE id = %s"
            cursor.execute(sql, (customer_id,))
            
            # Se rowcount é 0, o ID não existia no banco.
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Customer not found")
        
        connection.commit()
        return {"message": "Customer deleted successfully", "id": customer_id}
    finally:
        connection.close()
````

### 2. Consistência e Proteção de Estado (UPDATE):

Aprendemos que o protocolo do MySQL exige que qualquer resultado de uma consulta seja "consumido" antes que um novo comando seja enviado na mesma conexão. Ao refinar o método **PUT**, garantimos que o cursor seja limpo após a verificação de existência, evitando travamentos e garantindo que o ``UPDATE`` subsequente ocorra de forma segura e atômica.

````
# Exemplo 2: Rota PUT com proteção de estado (consumo de resultados)
@router.put("/{customer_id}")
def update_customer(customer_id: int, updated_data: Customer):
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            # Passo 1: Verifica existência e limpa o cursor com fetchone()
            cursor.execute("SELECT id FROM customers WHERE id = %s", (customer_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Customer not found")
            
            # Passo 2: O canal está livre para a atualização
            sql = "UPDATE customers SET nome = %s, idade = %s WHERE id = %s"
            cursor.execute(sql, (updated_data.name, updated_data.age, customer_id))
        
        connection.commit()
        return {"message": "Update successful"}
    finally:
        connection.close()
````

### 3. Testes End-to-End (E2E) e Estabilidade:

A bateria de testes com ``pytest`` evoluiu para simular o comportamento completo de um usuário final. O teste de "Ciclo Completo" é a prova definitiva da estabilidade da API: ele cria um dado dinâmico, atualiza suas informações, valida a persistência e, por fim, utiliza a própria rota de deleção para limpar o rastro no banco de dados.

````
# Exemplo 3: Teste de Ciclo CRUD Completo (test_api.py)
def test_full_crud_cycle():
    # 1. POST: Criação e captura do ID real gerado pelo MySQL
    res_post = client.post("/customers/", json={"name": "Teste Final", "age": 20})
    new_id = res_post.json()["id"]

    # 2. PUT: Atualização dos dados do cliente recém-criado
    res_put = client.put(f"/customers/{new_id}", json={"name": "Teste OK", "age": 21})
    assert res_put.status_code == 200

    # 3. GET: Prova real de que o banco salvou a alteração
    res_get = client.get(f"/customers/{new_id}")
    assert res_get.json()["name"] == "Teste OK"
````

### 4. Gestão de Limpeza e Resiliência:

Para manter o ambiente de testes sempre limpo e evitar erros de "ID duplicado" ou acúmulo de lixo eletrônico, o passo final do teste utiliza o método ``DELETE``. Isso garante que cada execução do teste comece e termine com o banco de dados em um estado previsível.

````
# Exemplo 4: Finalização do teste com limpeza automática
def test_cleanup_step(new_id):
    # DELETE: Limpeza usando a própria lógica da API
    res_del = client.delete(f"/customers/{new_id}")
    assert res_del.status_code == 200
    
    # Validação extra: Garantir que o dado realmente sumiu
    res_verify = client.get(f"/customers/{new_id}")
    assert res_verify.status_code == 404
````

### Observações Finais:

O **Dia 56** conclui a integração entre FastAPI e MySQL com um alto nível de maturidade técnica. A transição de scripts isolados para uma API integrada e testada foi concluída com sucesso. Agora, além de saber manipular o banco de dados, você domina o controle de transações, a otimização de rotas e a importância de consumir resultados para manter a saúde da conexão. O projeto está pronto para crescer em complexidade ou escala.