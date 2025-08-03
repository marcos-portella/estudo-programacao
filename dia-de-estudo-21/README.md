## Dia 21: Iteradores, Funções Avançadas e Manipulação de Dados

### Prefácio:

Hoje consolidamos uma série de conceitos avançados em Python que são cruciais para escrever código mais eficiente, flexível e compreensível. Exploramos a fundo os **iteradores** e geradores de sequências, como combinar múltiplos iteráveis de forma inteligente usando ``zip`` e ``zip_longest``, e aprofundamos no entendimento do **escopo de variáveis** com foco em variáveis livres e na palavra-chave ``nonlocal``.

### Iteradores e Geração de Sequências:

Em Python, muitos objetos são **iteráveis**, o que significa que podem ser percorridos (iterados) elemento por elemento. Um **iterador** é um objeto que sabe como acessar os elementos de um iterável um por um.

- **``range()`` vs. ``itertools.count``**:

    - ``range()``: Gera uma sequência de números, mas não é um iterador no sentido estrito de gerar valores infinitamente. Ele é um iterável que produz uma sequência finita.

    - ``itertools.count``: É um iterador que gera números infinitamente a partir de um início e com um passo definidos. É útil para contadores contínuos.

````
# Exemplo 1: Comparando range() e itertools.count
from itertools import count

c1 = count(step=8, start=8) # Um contador infinito que começa em 8 e incrementa de 8 em 8
r1 = range(8, 100, 8) # Uma sequência finita de 8 a 96 (pulando de 8 em 8)

print('itertools.count (c1):')
for i in c1:
    if i >= 100: # Precisamos de uma condição de parada para loops infinitos
        break
    print(i) # Saída: 8, 16, 24, ..., 96

print('\nrange (r1):')
for i in r1:
    print(i) # Saída: 8, 16, 24, ..., 96
````

### Combinando Iteráveis com ``zip`` e ``zip_longest``:

A função ``zip()`` é uma ferramenta poderosa para combinar elementos de múltiplos iteráveis.

- ``zip()``: Agrupa os elementos correspondentes de dois ou mais iteráveis em tuplas. A iteração para quando o iterável mais curto se esgota.

- ``itertools.zip_longest``: Similar ao ``zip()``, mas continua a agrupar elementos até que o iterável mais longo se esgote, preenchendo os valores ausentes com ``None`` por padrão (ou um ``fillvalue`` especificado).

````
# Exemplo 2: Usando zip para combinar listas
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ'] # 'RJ' será ignorado por zip

cidades_estados_zip = list(zip(cidades, estados))
print(cidades_estados_zip)
# Saída: [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
```python
# Exemplo 3: Usando itertools.zip_longest para incluir todos os elementos
from itertools import zip_longest

cidades_estados_longest = list(zip_longest(cidades, estados, fillvalue='SEM CIDADE'))
print(cidades_estados_longest)
# Saída: [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG'), ('SEM CIDADE', 'RJ')]
````

### Funções Avançadas e Escopo de Variáveis:

Revisitamos o conceito de **variáveis livres** e a palavra-chave ``nonlocal``, que são cruciais para entender como funções aninhadas interagem com variáveis em seus escopos externos.

- **Variáveis Livres**: São variáveis de um escopo externo que são referenciadas por uma função aninhada. A função aninhada "fecha" sobre essas variáveis (closure).

- ``nonlocal``: Usada dentro de uma função aninhada para indicar que uma variável não é local à função aninhada, nem global, mas sim uma variável no escopo da função externa mais próxima. Isso permite modificar uma variável livre.

- **``locals()`` e ``globals()``**: Funções built-in que retornam dicionários contendo as variáveis no escopo local e global, respectivamente.

````
# Exemplo 4: Variáveis livres (closure)
def fora(x):
    a = x # 'a' é uma variável livre para a função 'dentro'

    def dentro():
        return a # 'dentro' acessa 'a' mesmo depois que 'fora' terminou
    return dentro

dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1()) # Saída: 10
print(dentro2()) # Saída: 20
```python
# Exemplo 5: Usando 'nonlocal' para modificar uma variável livre
def concatenar(string_inicial):
    valor_final = string_inicial # 'valor_final' é uma variável livre

    def interna(valor_a_concatenar=''):
        nonlocal valor_final # Declara que 'valor_final' não é local a 'interna'
        valor_final += valor_a_concatenar # Modifica a variável livre
        return valor_final
    return interna

c = concatenar('a')
print(c('b')) # Saída: ab
print(c('c')) # Saída: abc
print(c('d')) # Saída: abcd
final = c()
print(final) # Saída: abcd
````

### Observações Finais:

Esta última parte do Dia 21 consolidou conceitos importantes sobre a manipulação de dados e o controle de fluxo em Python. A compreensão de **iteradores** e a utilização de ferramentas como ``itertools.count`` e as funções ``zip`` e ``zip_longest`` são cruciais para processar coleções de forma eficiente. Além disso, o aprofundamento no **escopo de variáveis**, com destaque para variáveis livres e o uso de ``nonlocal``, é fundamental para escrever funções mais complexas e flexíveis, especialmente no contexto de *closures*. A prática desses conceitos avançados é essencial para construir aplicações Python mais robustas e performáticas.