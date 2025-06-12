import pprint

def p(v): # Função pprint, é bom usar para deixar mais bonito o print
    pprint.pprint(v, sort_dicts=False, width=40)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} # Modificando os itens de uma lista
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(*novos_produtos, sep='\n')

print(novos_produtos)

p(novos_produtos)
lista = [n for n in range(10) if n < 5] # if é o filtro do for


novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10 # O if é o filtro do produto
]
p(novos_produtos)