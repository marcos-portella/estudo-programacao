## Dia 21: Exercícios Práticos

### Prefácio:

Hoje consolidamos os conhecimentos adquiridos sobre funções de ordem superior, *closures*, manipulação de listas e o uso de ``zip`` através de exercícios práticos. A resolução desses problemas reforça a compreensão de como aplicar esses conceitos para criar código mais flexível e eficiente.

### Exercício 1: Adiando a Execução de Funções (Closures)

Este exercício explora o conceito de *closures* e funções de ordem superior, onde uma função pode "lembrar" o ambiente em que foi criada e retornar outra função. A ideia é criar uma função que "adianta" a execução de outra função, fixando um de seus argumentos.

- **Objetivo**: Criar uma função ``criar_funcao`` que recebe uma função (``funcao``) e um valor ``x``. Ela deve retornar uma nova função que, quando chamada com um valor ``y``, executa a ``funcao`` original com ``x`` e ``y``.

````
# Exemplo 1: Função para adiar a execução
def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_funcao(funcao, x): # Recebe a função a ser adiada e o primeiro argumento
    def interna(y): # Retorna uma nova função que espera o segundo argumento
        return funcao(x, y) # A função interna "lembra" o 'x' do escopo externo
    return interna

# Criando funções com um argumento fixo
soma_com_cinco = criar_funcao(soma, 5) # 'soma_com_cinco' agora é uma função que soma 5 a qualquer número
multiplica_por_dez = criar_funcao(multiplica, 10) # 'multiplica_por_dez' agora multiplica por 10

print(soma_com_cinco(10))     # Saída: 15 (5 + 10)
print(multiplica_por_dez(10)) # Saída: 100 (10 * 10)
````

### Exercício 2: Somando Listas com ``zip`` e List Comprehension

Este exercício foca na combinação de elementos de duas listas, somando-os e criando uma nova lista com os resultados. A função ``zip()`` é ideal para iterar sobre múltiplos iteráveis em paralelo, e a *list comprehension* oferece uma sintaxe concisa para a criação da nova lista.

- **Objetivo**: Dadas duas listas de números, criar uma nova lista onde cada elemento é a soma dos elementos correspondentes das listas originais. Se as listas tiverem tamanhos diferentes, a soma deve considerar o tamanho da menor lista.

````
# Exemplo 2: Somando listas com zip e list comprehension
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

# zip() combina os elementos correspondentes até o fim da menor lista
# list comprehension cria a nova lista com as somas
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma) # Saída: [2, 4, 6, 8]
````

### Exercício 3: Manipulação e Ordenação de Produtos (List Comprehension, Lambda, ``sorted``, ``copy.deepcopy``)
Este exercício integra diversos conceitos importantes para manipulação de coleções de dicionários, como ajuste de valores, ordenação e a importância de cópias profundas para evitar efeitos colaterais.

- **Objetivos**:

    1. Aumentar o preço de todos os produtos em 10%.

    2. Gerar uma nova lista de produtos com os preços aumentados, garantindo uma **cópia profunda** para não modificar a lista original.

    3. Ordenar os produtos por nome em ordem decrescente.

    4. Ordenar os produtos por preço em ordem crescente.

````
# Exemplo 3: Dados iniciais
import copy # Importa o módulo copy para deepcopy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

print("Produtos Originais:")
print(*produtos, sep='\n')
```python
# Exemplo 4: Aumentando preços e gerando nova lista com deep copy
# {**p, 'preco': round(p['preco'] * 1.1, 2)} cria um novo dicionário
# com todos os itens de 'p' e sobrescreve 'preco' com o novo valor.
# copy.deepcopy(produtos) garante que a lista original e seus dicionários internos não sejam alterados.
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]
print("\nNovos Produtos (preços +10%):")
print(*novos_produtos, sep='\n')
```python
# Exemplo 5: Ordenando produtos por nome (decrescente) e preço (crescente)
# sorted() retorna uma nova lista ordenada.
# key=lambda p: p['nome'] define a chave de ordenação como o valor da chave 'nome'.
# reverse=True para ordem decrescente.
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos), # Cópia profunda para não alterar a lista original
    key=lambda p: p['nome'],
    reverse=True
)
print("\nProdutos Ordenados por Nome (Decrescente):")
print(*produtos_ordenados_por_nome, sep='\n')

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos), # Cópia profunda
    key=lambda p: p['preco']
)
print("\nProdutos Ordenados por Preço (Crescente):")
print(*produtos_ordenados_por_preco, sep='\n')
````

### Observações Finais:

A resolução desses exercícios práticos é fundamental para solidificar o aprendizado de conceitos como closures, funções de ordem superior, manipulação de listas com ``zip`` e *list comprehensions*, e a importância de ``copy.deepcopy`` ao trabalhar com dados mutáveis. A capacidade de aplicar ``lambda`` para ordenação personalizada e transformações concisas demonstra uma proficiência crescente em Python. Continue praticando esses tipos de problemas para aprimorar suas habilidades de programação e desenvolver soluções mais elegantes e eficientes.