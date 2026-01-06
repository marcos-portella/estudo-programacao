## JOURNAL - 05/01/2026 (Tarde/noite)

**Status**: Arquitetura Refatorada e Estável (8/8 testes passados)

### Objetivo da Sessão:

Transição da arquitetura "Monolítica Simples" para uma **Arquitetura em Camadas (Service Layer Pattern)**, visando o desacoplamento da lógica de negócio das rotas da API e a melhoria da testabilidade do sistema.

### Evoluções Técnicas Implementadas:

**1. Implementação da Service Layer (Camada de Serviço)**:

- **Centralização de Lógica**: Criação dos módulos ``app/services/order_service.py`` e ``app/services/customer_service.py``.

- **Desacoplamento de Framework**: Foram removidas todas as dependências do FastAPI (como ``Depends``) de dentro da lógica de negócio. Os serviços agora operam de forma independente, recebendo a conexão do banco como um parâmetro comum.

- **Vantagem**: O código agora é reutilizável fora do contexto da API (scripts, automações) e muito mais fácil de testar isoladamente.

**2. Refatoração de Rotas (Controllers)**:

- **Skinny Controllers**: As rotas em ``app/routers/`` foram simplificadas para atuar apenas como "gateways". Elas recebem o tráfego, injetam as dependências e delegam a execução para o Service correspondente.

- **Clean Code**: Redução drástica na complexidade visual dos arquivos de rotas, melhorando a manutenibilidade.

**3. Tipagem Estrita e Segurança de Dados**:

- **Uso de ``typing.cast``**: Aplicado para garantir que os retornos complexos do driver MySQL sejam interpretados corretamente pelo Mypy e Pylance como ``List[Dict[str, Any]]`` ou ``Optional[Dict]``.

- **Context Managers (``with``)**: Adotada a prática de utilizar ``with db.cursor() as cursor:`` nos métodos de escrita (Update/Delete), garantindo que o cursor seja fechado automaticamente e prevenindo vazamentos de memória (Memory Leaks).

- **Consistência de Tipagem**: Padronização absoluta do uso da interface ``MySQLConnectionAbstract`` em todas as assinaturas de métodos.

### Exemplo do Padrão Implementado:

````
# app/services/customer_service.py
@staticmethod
def delete_customer(customer_id: int, db: MySQLConnectionAbstract):
    with db.cursor() as cursor:
        sql = "DELETE FROM customers WHERE id = %s"
        cursor.execute(sql, (customer_id,))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Customer not found")
        db.commit()
        return {"message": "Customer deleted successfully", "id": customer_id}

# app/routers/customers.py
@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: MySQLConnectionAbstract = Depends(get_db)):
    return CustomerServices.delete_customer(customer_id, db)
````

### Insights e Próximos Passos:

- **Maturidade**: A refatoração provou que o uso de testes automatizados (Pytest) é fundamental. A confiança em mudar a estrutura do projeto veio do fato de os 8 testes continuarem "verdes" após o transplante de código.

- **Próximo Desafio (Sprint 30 Dias)**: Iniciar a Semana 1 focada em **Segurança (JWT)** para substituir a autenticação por API Key por um sistema de tokens assinados e expiráveis.

## JOURNAL - 05/01/2026 (Manhã)

Status do Projeto: Estável (8 testes aprovados, 0 warnings)

### Visão Geral
A sessão de hoje focou na estabilização da infraestrutura do projeto, correção de dívidas técnicas de tipagem e padronização do ambiente de testes integrados. O objetivo central foi alcançar um estado de "Zero Warnings" no terminal e garantir a integridade dos dados no MySQL durante o ciclo de vida dos testes.

### Implementações e Resoluções Técnicas
**1. Refatoração de Modelos (Pydantic V2)**
Migração da configuração dos esquemas de validação para os padrões da versão 2.12 do Pydantic.

- **Problema**: O terminal exibia avisos de depreciação (``PydanticDeprecatedSince20``) devido ao uso da antiga ``class Config``.

- **Solução**: Implementação do ``model_config`` utilizando ``ConfigDict``.

- **Impacto**: Eliminação total de avisos de sistema e garantia de compatibilidade com versões futuras da biblioteca.

**2. Estabilização do Ambiente de Testes (Pytest)**

Aprimoramento do rigor técnico nos testes de integração.

- **Gestão de Estado**: Implementação de lógica de teardown robusta com blocos ``try/finally`` para garantir que, independentemente do sucesso ou falha do teste, a conexão com o banco seja encerrada e o registro criado seja removido.

- **Segurança**: Inclusão de cabeçalhos ``X-API-KEY`` em todas as requisições de teste para refletir o middleware de produção.

**3. Resolução de Importação e Namespacing**
Correção de erros de análise estática que persistiam mesmo com o código funcional.

- **Package Initialization**: Criação do arquivo ``tests/__init__.py``, permitindo que o Mypy e o Pylance resolvam corretamente os caminhos entre pacotes irmãos (``app`` e ``tests``).

- **Linting Control**: Uso estratégico de ``# noqa: E402`` e ``# type: ignore`` para gerenciar a ordem de carregamento do ``load_dotenv()`` sem violar as regras da PEP 8.

### Fragmentos de Código Relevantes

````
# Modernização do modelo OrderResponse
from pydantic import ConfigDict

class OrderResponse(Order):
    model_config = ConfigDict(from_attributes=True)

# Padrão de limpeza de banco em Testes de Integração
conn = get_db_connection()
try:
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM customers WHERE id = %s", (new_id,))
    conn.commit()
finally:
    conn.close()
````

### Insights e Próximos Passos

- **Aprendizado**: A resolução independente de erros de configuração de IDE (Pylance/Mypy) demonstrou a importância da estrutura de diretórios (``__init__.py``) para ferramentas de análise estática.

- **Próximo Passo**: Avaliar a transição para uma arquitetura de camadas (Services/Repositories) para desacoplar a lógica de negócio das rotas da API.


## JOURNAL - 04/01/2026
**Módulo: Expansão de Negócio e Relacionalidade**

Nesta data, o desenvolvedor **Marcos** consolidou a arquitetura do sistema ao implementar o módulo de pedidos (**Orders**), estabelecendo a primeira relação complexa entre entidades e garantindo a integridade dos dados no banco MySQL.

**1. Desenvolvimento Técnico**:
- **Arquitetura de Software**: O desenvolvedor estruturou o projeto seguindo o padrão de separação de responsabilidades, distinguindo claramente os modelos de validação (Pydantic) em ``app/models/orders.py`` da lógica de rotas e persistência em ``app/routers/orders.py``.

- **Persistência e Relacionamentos**: Foi estabelecida uma relação 1:N entre clientes e pedidos. Marcos configurou a restrição ``ON DELETE CASCADE``, garantindo que o sistema mantenha a higienização automática do banco de dados ao remover registros pai.

- **Inteligência de Negócio (BI)**: Implementou uma rota de estatísticas que utiliza funções de agregação SQL (``COUNT``, ``SUM``, ``AVG``), transformando dados brutos em métricas de faturamento e volume de vendas.

- **Engenharia de Tipos**: O desenvolvedor refinou a qualidade do código utilizando técnicas de **Type Hinting** avançadas. Através do uso de ``typing.cast`` e ``Dict[str, Any]``, eliminou inconsistências de análise estática entre a biblioteca ``mysql-connector`` e o servidor de linguagem Pylance.

**2. Resolução de Problemas (Troubleshooting)**:

- **Sintaxe SQL**: Corrigiu falhas de concatenação em comandos ``INSERT`` multilinhas através da padronização com aspas triplas.

- **Gerenciamento de Cursores**: Solucionou o erro crítico ``InternalError: Unread result found``, estruturando o ciclo de vida do comando SQL para garantir que todos os dados sejam consumidos antes do encerramento da conexão.

**3. Destaques de Código**:

````
# Exemplo de consulta enriquecida com INNER JOIN implementada pelo desenvolvedor:
sql = """
    SELECT o.*, c.nome as customer_name 
    FROM orders o 
    INNER JOIN customers c ON o.customer_id = c.id
"""
````

````
# Aplicação de casting para garantir estabilidade de tipos:
stats = cast(Optional[Dict[str, Any]], cursor.fetchone())
````

### Status da Entrega:

**Desenvolvedor**: Marcos

**Conclusão**: 100% (Módulo de Pedidos e Estatísticas)

**Próximo Objetivo**: Implementação de camadas de segurança e autenticação.


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







