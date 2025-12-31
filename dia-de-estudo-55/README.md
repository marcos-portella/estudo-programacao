## Dia 54: Qualidade, Validação Rigorosa e Testes Automatizados

### Prefácio:

No **Dia 54**, o foco do projeto mudou de "construir funcionalidades" para "garantir que as funcionalidades não quebrem". Entramos na fase de **Garantia de Qualidade (QA)**, implementando testes automatizados com o framework ``pytest``. Além disso, refinamos a camada de validação de dados com o **Pydantic V2**, transformando nossa API em uma fortaleza contra dados corrompidos ou inválidos, garantindo que apenas informações que seguem as regras de negócio entrem no banco de dados.

### 1. Validação com Pydantic V2 e Regras de Negócio:

Elevamos a inteligência dos nossos modelos. Agora, o Schema ``Customer`` não apenas define os tipos de dados, mas impõe limites reais usando ``Field``. Definimos que nomes devem ter entre 3 e 50 caracteres e que a idade deve ser um valor humano biologicamente possível. O FastAPI intercepta qualquer dado fora desse padrão e retorna automaticamente um erro **422 Unprocessable Entity**.

````
from pydantic import BaseModel, Field

# Modelo com validação rigorosa (Pydantic V2)
class Customer(BaseModel):
    name: str = Field(min_length=3, max_length=50, examples=["Marcos Portella"])
    age: int = Field(gt=0, lt=120, examples=[25]) # gt = greater than | lt = less than
````

### 2. Testes de Integração com Pytest:

Introduzimos o ``TestClient`` do FastAPI para simular requisições reais sem precisar rodar o servidor manualmente. O objetivo é criar um ciclo de confiança: toda vez que o código mudar, rodamos os testes para garantir que as rotas de criação e exclusão continuam funcionando como esperado.

````
import pytest
from main import app
from fastapi.testclient import TestClient
from database import get_connection

client = TestClient(app)

def test_create_and_delete_user():
    # Simulando o envio de um JSON para a rota de criação
    payload = {"name": "Test User", "age": 30}
    response = client.post("/customers/", json=payload)
    assert response.status_code == 200 # Verificamos se o sucesso foi retornado
````

### 3. Lógica de Teardown (Limpeza de Dados):

Um princípio fundamental dos testes é não "sujar" o ambiente de produção ou desenvolvimento com dados fictícios. Implementamos um processo de **Teardown** (limpeza) manual dentro dos testes: após verificar que o usuário foi criado com sucesso, o próprio teste se encarrega de deletá-lo do banco MySQL, mantendo o ambiente hígido.

````
# Continuação da limpeza pós-teste
def teardown_test_user(name: str):
    conn = get_connection()
    if conn is not None:
        try:
            with conn.cursor() as cursor:
                # Remove o dado criado durante o teste
                cursor.execute("DELETE FROM customers WHERE nome = %s", (name,))
            conn.commit()
        finally:
            conn.close()
    else:
        pytest.fail("Falha na conexão para limpeza de ambiente")
````

### 4. Testando a Resistência do Sistema (Status 422):

Não testamos apenas o "caminho feliz". É vital testar se a API bloqueia o que deve ser bloqueado. Criamos testes específicos para enviar dados propositalmente inválidos (como idades negativas) para confirmar se o Pydantic está protegendo nossos endpoints corretamente.

````
def test_invalid_age():
    # Tenta enviar idade negativa, esperando bloqueio automático
    # O código 422 indica que o servidor entendeu a requisição, mas os dados são inválidos
    response = client.post("/customers/", json={"name": "Invalido", "age": -5})
    assert response.status_code == 422
````

### Observações Finais:

O **Dia 54** marca a maturidade do desenvolvedor: entender que código sem teste é código quebrado esperando para acontecer. A implementação do ``pytest`` e a validação profunda com Pydantic V2 dão à nossa API uma camada de profissionalismo essencial para qualquer projeto real. Além disso, lidar com retornos ``None`` de conexão para satisfazer linters como o Pylance nos ensinou a escrever códigos mais defensivos e seguros contra falhas de infraestrutura.