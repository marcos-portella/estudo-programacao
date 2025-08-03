## Dia 22

### Prefácio:

Hoje mergulhamos em tópicos avançados de Python que são cruciais para a programação funcional, manipulação eficiente de dados e gerenciamento de projetos. Exploramos as funções ``map``, ``filter`` e ``reduce``, as poderosas ferramentas do módulo ``itertools`` para combinações e agrupamentos, e a importância dos ambientes virtuais (``venv``) para isolar dependências de projetos.

### Funções de Ordem Superior para Manipulação de Dados: ``map``, ``filter``, ``reduce``
Essas funções são pilares da programação funcional em Python, permitindo transformar, filtrar e agregar dados de forma concisa e eficiente.

- ``map()``: Aplica uma função a cada item de um iterável e retorna um iterador com os resultados. É útil para transformar coleções de dados.

````
# Exemplo 1: Aumentando o preço dos produtos em 10% com map
from functools import partial

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
]

# Função auxiliar para aumentar porcentagem
def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

# Cria uma versão parcial da função com porcentagem fixa
aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)

# Usa map para aplicar a função a cada produto
novos_produtos = list(map(
    lambda p: {**p, 'preco': aumentar_dez_porcento(p['preco'])}, # Transforma cada dicionário
    produtos
))

print("Produtos Originais:")
print(*produtos, sep='\n')
print("\nNovos Produtos (com map):")
print(*novos_produtos, sep='\n')
````

- ``filter()``: Constrói um iterador a partir de elementos de um iterável para os quais uma função retorna ``True``. É um filtro funcional.

````
# Exemplo 2: Filtrando produtos com preço maior que 20 com filter
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
]

# Filtra produtos cujo preço é maior que 20
produtos_caros = list(filter(
    lambda p: p['preco'] > 20,
    produtos
))

print("\nProdutos Caros (com filter):")
print(*produtos_caros, sep='\n')
````

- ``reduce()``: Aplica uma função de dois argumentos cumulativamente aos itens de um iterável, da esquerda para a direita, para reduzir o iterável a um único valor.

````
# Exemplo 3: Calculando o total dos preços dos produtos com reduce
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
]

# Soma cumulativamente os preços
total_precos = reduce(
    lambda acumulador, produto: acumulador + produto['preco'],
    produtos,
    0 # Valor inicial do acumulador
)

print(f"\nTotal dos preços (com reduce): {total_precos}") # Saída: Total dos preços (com reduce): 34
````

### Funções Recursivas:

Funções recursivas são funções que se chamam de volta para resolver um problema. Elas são úteis para problemas que podem ser divididos em subproblemas menores da mesma natureza. Toda função recursiva deve ter:

- Um **caso base** que para a recursão.

- Um **caso recursivo** que resolve uma parte do problema e chama a si mesma com um problema menor.

````
# Exemplo 4: Cálculo de fatorial usando recursão
def factorial(n):
    if n <= 1: # Caso base: fatorial de 0 ou 1 é 1
        return 1
    return n * factorial(n - 1) # Caso recursivo: n * fatorial de (n-1)

print(f"\nFatorial de 5: {factorial(5)}")   # Saída: Fatorial de 5: 120
print(f"Fatorial de 10: {factorial(10)}") # Saída: Fatorial de 10: 3628800
````

### Itertools: ``combinations``, ``permutations``, ``product``, ``groupby``

O módulo ``itertools`` fornece funções para criar iteradores eficientes para loops.

- ``combinations()``: Gera todas as combinações únicas de elementos de um iterável, onde a ordem **não importa**.

- ``permutations()``: Gera todas as permutações (arranjos) de elementos de um iterável, onde a ordem **importa**.

- ``product()``: Gera o produto cartesiano de iteráveis, combinando elementos de cada iterável. É útil para gerar todas as combinações possíveis.

- ``groupby()``: Agrupa elementos consecutivos de um iterável que têm a mesma chave (definida por uma função). O iterável deve estar **ordenado** pela chave de agrupamento.

````
# Exemplo 5: Usando itertools para combinações, permutações e produtos
from itertools import combinations, permutations, product, groupby

pessoas = ['João', 'Maria', 'Pedro']
camisetas = [['preta', 'branca'], ['P', 'M']]

print("\nCombinações de 2 pessoas:")
print(*list(combinations(pessoas, 2)), sep='\n')
# Saída: ('João', 'Maria'), ('João', 'Pedro'), ('Maria', 'Pedro')

print("\nPermutações de 2 pessoas:")
print(*list(permutations(pessoas, 2)), sep='\n')
# Saída: ('João', 'Maria'), ('João', 'Pedro'), ('Maria', 'João'), ...

print("\nProduto cartesiano (camisetas):")
print(*list(product(*camisetas)), sep='\n')
# Saída: ('preta', 'P'), ('preta', 'M'), ('branca', 'P'), ('branca', 'M')
```python
# Exemplo 6: Agrupando alunos por nota com groupby
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
]

# É crucial ordenar a lista pela chave antes de usar groupby
alunos_ordenados = sorted(alunos, key=lambda aluno: aluno['nota'])

print("\nAlunos agrupados por nota:")
for chave, grupo in groupby(alunos_ordenados, key=lambda aluno: aluno['nota']):
    print(f"Nota {chave}:")
    for aluno in grupo:
        print(f"  - {aluno['nome']}")
````

### Ambientes Virtuais (``venv``):

Ambientes virtuais são essenciais para o desenvolvimento de projetos Python. Eles criam um ambiente isolado para cada projeto, onde você pode instalar pacotes e dependências sem afetar a instalação global do Python ou outros projetos.

- **Propósito**: Evitar conflitos de dependências entre diferentes projetos.

- **Criação**: ``python -m venv nome_do_ambiente`` (ex: ``python -m venv .venv``).

- **Ativação**:

    - Windows: ``.\nome_do_ambiente\Scripts\activate``

    - Linux/macOS: ``source nome_do_ambiente/bin/activate``

- **Comandos ``pip``**: Usados para gerenciar pacotes dentro do ambiente virtual (instalar, desinstalar, listar).

````
# Exemplo 7: Comandos básicos de venv e pip (executados no terminal)
# 1. Criar um ambiente virtual (no diretório do seu projeto)
# python -m venv .venv

# 2. Ativar o ambiente virtual
# No Windows: .\.venv\Scripts\activate
# No Linux/macOS: source .venv/bin/activate

# 3. Instalar um pacote (ex: requests)
# pip install requests

# 4. Listar pacotes instalados no ambiente
# pip freeze

# 5. Desativar o ambiente virtual
# deactivate
````

### Observações Finais:

O Dia 22 foi repleto de conceitos avançados que elevam a qualidade do seu código Python. As funções ``map``, ``filter`` e ``reduce`` são ferramentas poderosas para a programação funcional e manipulação de dados. Funções recursivas oferecem uma abordagem elegante para certos problemas. O módulo ``itertools`` é indispensável para gerar combinações e agrupamentos de forma eficiente. E, finalmente, o uso de **ambientes virtuais** é uma prática fundamental para gerenciar dependências de projetos de forma profissional e evitar dores de cabeça. Continue praticando esses conceitos para construir aplicações Python mais robustas, eficientes e organizadas.