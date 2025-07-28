### Dia 18: List Comprehension

### Prefácio:

Hoje aprofundamos ainda mais nas **List Comprehensions**, uma das ferramentas mais eficientes e expressivas do Python para a criação e manipulação de listas. Exploramos como aplicar mapeamento e filtragem de dados de forma concisa, como lidar com múltiplos laços ``for`` aninhados dentro de uma *list comprehension*, e a importância de manter a legibilidade mesmo em construções mais complexas.

### Mapeamento e Filtragem de Dados:

List Comprehensions são incrivelmente versáteis para transformar e selecionar dados de iteráveis.

- **Mapeamento**: Permite criar uma nova lista onde cada item é o resultado de uma expressão aplicada aos itens do iterável original.

- **Filtragem**: Permite incluir itens na nova lista apenas se eles satisfizerem uma determinada condição. A cláusula ``if`` atua como um filtro.

````
# Exemplo 1: Mapeamento de preços - Aumentando em 5% produtos acima de 20
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

# Cria uma nova lista de produtos com preços ajustados
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} # Mapeia: aumenta preço se > 20
    if produto['preco'] > 20 else {**produto}     # Caso contrário, mantém o produto original
    for produto in produtos
]

# Para uma exibição mais legível de dicionários, pprint é útil
import pprint
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

p(novos_produtos)
# Saída:
# [{'nome': 'p1', 'preco': 20},
#  {'nome': 'p2', 'preco': 10},
#  {'nome': 'p3', 'preco': 31.5}]
```python
# Exemplo 2: Filtrando números - Apenas números menores que 5
lista_numeros = [n for n in range(10) if n < 5] # O 'if' atua como filtro
print(lista_numeros) # Saída: [0, 1, 2, 3, 4]
```python
# Exemplo 3: Combinando mapeamento e filtro em um cenário mais complexo
# Ajusta o preço E filtra produtos que, após o ajuste, tenham preço maior que 10
produtos_filtrados_e_ajustados = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and (produto['preco'] * 1.05) > 10) # Filtra produtos
]
p(produtos_filtrados_e_ajustados)
# Saída:
# [{'nome': 'p1', 'preco': 20},
#  {'nome': 'p3', 'preco': 31.5}]
````

### ``for`` Aninhados em List Comprehensions:

````
List Comprehensions podem incluir múltiplos laços ``for`` aninhados, o que é útil para gerar combinações de elementos ou para achatar listas aninhadas. A ordem dos ``for`` na list comprehension segue a mesma lógica dos ``for`` aninhados tradicionais.

# Exemplo 4: Gerando pares (x, y) com for aninhado
lista_pares = []
for x in range(3):
    for y in range(3):
        lista_pares.append((x, y))
print(lista_pares)
# Saída: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# Equivalente com List Comprehension:
lista_pares_lc = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(lista_pares_lc)
# Saída: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```python
# Exemplo 5: List Comprehension aninhada para criar uma lista de listas
# Cada sublista contém pares (número, letra) para cada letra em 'Luiz'
lista_de_listas_aninhada = [
    [(x, letra) for letra in 'Luiz'] # List comprehension interna
    for x in range(3) # For externo
]
print(lista_de_listas_aninhada)
# Saída:
# [[(0, 'L'), (0, 'u'), (0, 'i'), (0, 'z')],
#  [(1, 'L'), (1, 'u'), (1, 'i'), (1, 'z')],
#  [(2, 'L'), (2, 'u'), (2, 'i'), (2, 'z')]]
````

### Observações Finais:

As List Comprehensions são uma das características mais idiomáticas e poderosas do Python. Elas permitem escrever código mais limpo, conciso e, muitas vezes, mais performático para a criação e transformação de listas. A capacidade de combinar mapeamento, filtragem e múltiplos laços ``for`` em uma única expressão as torna extremamente flexíveis. No entanto, é importante usá-las com moderação em casos muito complexos, onde a legibilidade pode ser comprometida. Para esses cenários, a abordagem tradicional com loops ``for`` pode ser mais clara. Dominar as List Comprehensions é um passo crucial para escrever código Python mais eficiente e elegante.