## Dia 14

### Prefácio:

Hoje avançamos na manipulação de dados em Python, focando em técnicas essenciais para trabalhar com coleções e strings de forma eficiente. Exploramos o **empacotamento e desempacotamento** de iteráveis, a utilidade das **tuplas**, como lidar com listas aninhadas, a função ``enumerate`` para iterar com índices, e métodos de string como ``split``, ``join`` e ``strip``. Além disso, abordamos a **imprecisão dos números de ponto flutuante** e a importância do módulo ``decimal``.

### Empacotamento e Desempacotamento:

O empacotamento e desempacotamento são recursos poderosos do Python que permitem atribuir múltiplos valores de um iterável a múltiplas variáveis de uma só vez.

- **Desempacotamento Básico**: Atribui cada elemento de um iterável a uma variável correspondente.

- **Operador ``*`` (Resto)**: O operador ``*`` pode ser usado para "empacotar" os elementos restantes de um iterável em uma lista. Isso é útil quando você não sabe quantos elementos sobraram ou quer ignorá-los.

- **Variável ``_`` (Ignorar)**: O underscore ``_`` é uma convenção para variáveis que não serão utilizadas, indicando que estamos desempacotando um valor, mas não precisamos dele.

````
# Exemplo 1: Desempacotamento básico
nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print(nome3) # Saída: Luiz

# Exemplo 2: Desempacotamento com o operador * (resto)
_, _, nome_util, *resto = ['Maria', 'Helena', 'Luiz', 'Marcos', 'Pedro', 'João']
print(nome_util) # Saída: Luiz
print(resto)     # Saída: ['Marcos', 'Pedro', 'João']

# Exemplo 3: Desempacotamento em chamadas de função/método
lista_nomes = ['Maria', 'Helena', 'Luiz']
print(*lista_nomes) # Saída: Maria Helena Luiz (desempacota os elementos como argumentos separados)

salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda'],
]
print(*salas, sep='\n') # Desempacota as sublistas e as imprime em linhas separadas
````

### Tuplas:

As **tuplas** são coleções ordenadas e **imutáveis** de itens, similares às listas, mas não podem ser modificadas após a criação. São definidas usando parênteses ``()`` ou simplesmente por vírgulas.

- **Criação**: Podem ser criadas com ou sem parênteses.

- **Imutabilidade**: Uma vez criada, os elementos de uma tupla não podem ser alterados, adicionados ou removidos.

- **Conversão**: É possível converter listas em tuplas usando ``tuple()`` e tuplas em listas usando ``list()``.

````
# Exemplo 4: Criação e conversão de tuplas
tupla_exemplo = 'Marcos', 'Gomes', 'Portella' # Tupla sem parênteses
print(tupla_exemplo)
print(type(tupla_exemplo)) # Saída: <class 'tuple'>

lista_convertida = list(tupla_exemplo) # Converte tupla para lista
print(lista_convertida)

tupla_convertida = tuple(lista_convertida) # Converte lista para tupla
print(tupla_convertida)
````

### Listas Aninhadas:

Python permite criar **listas de listas**, que são úteis para representar estruturas de dados bidimensionais, como matrizes ou tabelas.

- **Acesso a Elementos**: Para acessar um elemento em uma lista aninhada, você usa múltiplos índices.

````
# Exemplo 5: Listas aninhadas (lista de listas)
salas = [
    ['Maria', 'Helena'],  # Sala 0
    ['Elaine'],           # Sala 1
    ['Luiz', 'João', 'Eduarda'], # Sala 2
]

print(salas[0][1]) # Saída: Helena (elemento na sala 0, índice 1)
print(salas[2][0]) # Saída: Luiz (elemento na sala 2, índice 0)

# Iterando sobre listas aninhadas
for numero_sala, sala in enumerate(salas):
    print(f'Na sala {numero_sala + 1} temos os alunos:')
    for aluno in sala:
        print(f'- {aluno}')
````

### ``enumerate``:

A função ``enumerate()`` é uma ferramenta poderosa para iterar sobre um iterável (como uma lista ou string) e, ao mesmo tempo, obter o índice de cada elemento. Ela retorna pares de (índice, valor).

````
# Exemplo 6: Usando enumerate para obter índice e valor
lista_frutas = ['Maçã', 'Banana', 'Laranja']

for indice, fruta in enumerate(lista_frutas):
    print(f'Índice: {indice}, Fruta: {fruta}')
````

### Métodos de String: ``split``, ``join``, ``strip``:

Esses métodos são cruciais para a manipulação e limpeza de strings.

- ``split()``: Divide uma string em uma lista de substrings, usando um delimitador (padrão é espaço em branco). [cite: uploaded:split_join_strip.py]

- **``strip()`` / ``lstrip()`` / ``rstrip()``**: Remove espaços em branco (ou caracteres específicos) do início e/ou fim de uma string. ``strip()`` remove de ambos os lados, ``lstrip()`` do lado esquerdo e ``rstrip()`` do lado direito.

- ``join()``: Une os elementos de um iterável (como uma lista de strings) em uma única string, usando a string na qual o método é chamado como separador.

````
# Exemplo 7: split, strip e join
frase_suja = '   Olha só que   , coisa interessante          '
lista_crua = frase_suja.split(',') # Divide por vírgula
print(lista_crua) # Saída: ['   Olha só que   ', ' coisa interessante          ']

lista_limpa = []
for item in lista_crua:
    lista_limpa.append(item.strip()) # Remove espaços em branco de cada item
print(lista_limpa) # Saída: ['Olha só que', 'coisa interessante']

frase_unida = ', '.join(lista_limpa) # Une os itens com ', '
print(frase_unida) # Saída: Olha só que, coisa interessante
````

### Imprecisão dos Números de Ponto Flutuante (``float``) e ``decimal.Decimal``:

Números de ponto flutuante (``float``) em computadores têm uma limitação inerente de precisão devido à forma como são armazenados. Isso pode levar a resultados inesperados em cálculos com casas decimais.

- **Problema**: Operações como ``0.1 + 0.7`` podem não resultar exatamente em ``0.8``.

- **Solução**: Para cálculos financeiros ou que exigem alta precisão, o módulo ``decimal`` e o tipo ``decimal.Decimal`` devem ser usados.

````
# Exemplo 8: Imprecisão de float vs. decimal.Decimal
import decimal

numero_float_impreciso = 0.1 + 0.7
print(numero_float_impreciso) # Saída: 0.7999999999999999

numero_decimal_preciso = decimal.Decimal('0.1') + decimal.Decimal('0.7')
print(numero_decimal_preciso) # Saída: 0.8
````

### Observações Finais:

O Dia 14 expandiu significativamente nossas ferramentas para manipulação de dados em Python. O **empacotamento e desempacotamento** oferecem flexibilidade na atribuição de variáveis. As **tuplas** introduzem o conceito de coleções imutáveis, úteis para dados que não devem ser alterados. **Listas aninhadas** e a função ``enumerate`` são essenciais para trabalhar com estruturas de dados mais complexas e para iterações controladas. Por fim, os métodos de string ``split``, ``join`` e ``strip`` são indispensáveis para o pré-processamento e formatação de texto, enquanto a compreensão da **imprecisão dos floats** e o uso do módulo ``decimal`` são cruciais para garantir a precisão em cálculos sensíveis. Continue praticando esses conceitos para construir programas mais robustos e eficientes.