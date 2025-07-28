## Dia 17

### Prefácio:

Hoje mergulhamos em duas estruturas de dados fundamentais em Python: os **dicionários** (``dict``) e os **conjuntos** (``set``). Compreendemos como armazenar e manipular dados de forma eficiente usando pares de chave-valor em dicionários e a unicidade e operações de conjuntos em sets. Além disso, aplicamos esses conhecimentos na construção de um sistema de perguntas e respostas e na resolução de um problema de detecção de duplicados.

### Dicionários (``dict``):

Dicionários são coleções de dados não ordenadas (a partir do Python 3.7, a ordem de inserção é mantida) que armazenam informações em pares de **chave-valor**. As chaves devem ser de tipos imutáveis (como strings, números, tuplas), e os valores podem ser de qualquer tipo. [cite: uploaded:introducao_dicionario.py]

- **Criação**: Podem ser criados usando chaves {} ou a função dict(). [cite: uploaded:introducao_dicionario.py]

- **Acesso e Manipulação**:

    - Acessar valores usando a chave: ``dicionario['chave']``.

    - Adicionar/Atualizar valores: ``dicionario['nova_chave'] = valor``.

    - Deletar pares chave-valor: ``del dicionario['chave']``.

    - Usar ``get()`` para acessar valores de forma segura, retornando ``None`` ou um valor padrão se a chave não existir, evitando erros. [cite: uploaded:manipulando_chaves.py]

````
# Exemplo 1: Criação e acesso a dicionários
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'endereços': [ # Dicionários podem conter listas e outros dicionários
        {'rua': 'tal tal', 'numero': 123},
    ],
}
print(pessoa['nome']) # Saída: Luiz Otávio
print(pessoa['endereços'][0]['rua']) # Acessando elementos aninhados

# Exemplo 2: Manipulando chaves e valores
pessoa['nome'] = 'Maria' # Atualiza o valor da chave 'nome'
print(pessoa['nome']) # Saída: Maria

del pessoa['sobrenome'] # Deleta a chave 'sobrenome'
print(pessoa) # Saída: {'nome': 'Maria', 'idade': 18, 'endereços': [{'rua': 'tal tal', 'numero': 123}]}

# Usando .get() para evitar KeyError
print(pessoa.get('sobrenome', 'Não existe')) # Saída: Não existe (chave 'sobrenome' foi deletada)
````

- **Métodos Úteis de Dicionários**:

    - ``len()``: Retorna o número de pares chave-valor. [cite: uploaded:metodos_uteis_dicionarios.py]

    - ``keys()``: Retorna um iterável com as chaves. [cite: uploaded:metodos_uteis_dicionarios.py]

    - ``values()``: Retorna um iterável com os valores. [cite: uploaded:metodos_uteis_dicionarios.py]

    - ``items()``: Retorna um iterável com pares (chave, valor). [cite: uploaded:metodos_uteis_dicionarios.py]

    - ``setdefault(chave, valor_padrao)``: Adiciona um valor se a chave não existir. [cite: uploaded:metodos_uteis_dicionarios.py]

    - ``copy()``: Retorna uma cópia rasa (shallow copy) do dicionário. Para cópias profundas, use copy.deepcopy(). [cite: uploaded:metodos_uteis_dicionarios.py]

    - ``pop(chave)``: Apaga um item pela chave e retorna seu valor. [cite: uploaded:metodos_uteis_dicionarios.py]

    - ``popitem()``: Apaga e retorna o último item adicionado (a partir do Python 3.7). [cite: uploaded:metodos_uteis_dicionarios.py]

    - ``update()``: Atualiza o dicionário com pares chave-valor de outro dicionário ou de um iterável de pares. [cite: uploaded:metodos_uteis_dicionarios.py]

````
# Exemplo 3: Métodos de dicionários
d1 = {'c1': 1, 'c2': 2, 'l1': [0, 1, 2]}
d2 = d1.copy() # Cópia rasa

d2['c1'] = 1000
d2['l1'][1] = 999999 # Altera também em d1 porque l1 é uma lista mutável e a cópia é rasa

print(d1) # Saída: {'c1': 1, 'c2': 2, 'l1': [0, 999999, 2]}
print(d2) # Saída: {'c1': 1000, 'c2': 2, 'l1': [0, 999999, 2]}

p1 = {'nome': 'Luiz'}
p1.update(sobrenome='Miranda', idade=30) # Atualiza/Adiciona com argumentos nomeados
print(p1) # Saída: {'nome': 'Luiz', 'sobrenome': 'Miranda', 'idade': 30}
````

### Conjuntos (``set``):

Conjuntos são coleções **mutáveis** de itens **não ordenados** e **únicos**. Eles são eficientes para remover duplicatas e realizar operações de conjunto (união, interseção, diferença). Aceitam apenas tipos imutáveis como valores internos. [cite: uploaded:introducao_ao_set.py]

- **Criação**: Podem ser criados usando ``set()`` (para um conjunto vazio) ou chaves ``{}`` com elementos. [cite: uploaded:introducao_ao_set.py]

- **Características**:

    - Não aceitam valores mutáveis (ex: listas não podem ser elementos de um set).

    - Seus valores são sempre únicos (duplicatas são automaticamente removidas).

    - Não têm índices e não garantem ordem.

    - São iteráveis (``for``, ``in``, ``not in``). [cite: uploaded:introducao_ao_set.py]

````
# Exemplo 4: Criação e características de sets
lista_com_duplicatas = [1, 2, 3, 3, 3, 1, 4]
s1 = set(lista_com_duplicatas) # Remove duplicatas automaticamente
print(s1) # Saída: {1, 2, 3, 4} (ordem pode variar)

s1.add('Luiz') # Adiciona um item
s1.update(('Olá mundo', 5)) # Adiciona múltiplos itens de um iterável
s1.discard(1) # Remove um item específico (não gera erro se o item não existir)
print(s1) # Saída: {'Olá mundo', 2, 3, 4, 5, 'Luiz'} (ordem pode variar)

# Exemplo 5: Operações de conjunto
s_a = {1, 2, 3}
s_b = {2, 3, 4}

s_uniao = s_a | s_b # União: itens em s_a OU s_b
print(s_uniao) # Saída: {1, 2, 3, 4}

s_interseccao = s_a & s_b # Interseção: itens em s_a E s_b
print(s_interseccao) # Saída: {2, 3}

s_diferenca = s_a - s_b # Diferença: itens em s_a E NÃO em s_b
print(s_diferenca) # Saída: {1}

s_diferenca_simetrica = s_a ^ s_b # Diferença simétrica: itens que NÃO estão em AMBOS
print(s_diferenca_simetrica) # Saída: {1, 4}
````

### Exercício: Encontrar o Primeiro Duplicado:

Um problema comum que pode ser eficientemente resolvido com sets é encontrar o primeiro elemento duplicado em uma lista. A lógica envolve iterar pela lista e adicionar cada número a um set de "números checados". Se um número já estiver no set, ele é o primeiro duplicado. [cite: uploaded:exercicio_encontre_duplicado.py]

````
# Exemplo 6: Função para encontrar o primeiro duplicado
def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1 # Valor padrão se não encontrar duplicado

    for numero in lista_de_inteiros:
        if numero in numeros_checados: # Se o número já foi visto, é duplicado
            primeiro_duplicado = numero
            break # Encontrou o primeiro, pode parar
        numeros_checados.add(numero) # Adiciona o número ao set de checados
    return primeiro_duplicado

listas_para_testar = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], # Sem duplicados
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8], # Primeiro duplicado é 9
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7], # Primeiro duplicado é 2
]

for lista in listas_para_testar:
    print(f'Lista: {lista}, Primeiro duplicado: {encontra_primeiro_duplicado(lista)}')
````

### Observações Finais:

Dicionários e conjuntos são estruturas de dados poderosas e flexíveis em Python, cada uma com suas particularidades e casos de uso ideais. Dicionários são perfeitos para mapeamento de chave-valor e representação de objetos complexos, enquanto conjuntos são excelentes para gerenciar coleções únicas de itens e realizar operações matemáticas de conjunto. A proficiência no uso dessas estruturas, combinada com a capacidade de aplicar loops e lógica condicional, é fundamental para resolver uma ampla gama de problemas de programação de forma eficiente e elegante. Continue explorando e praticando para solidificar seu conhecimento.