## Dia 3

### Prefácio:

Este dia foi crucial para solidificar a compreensão sobre como o Python lida com dados, introduzindo o conceito de variáveis para armazenar informações e explorando os tipos de dados primitivos mais comuns: números inteiros (``int``), números de ponto flutuante (``float``) e valores booleanos (``bool``). Além disso, aprendemos sobre a conversão de tipos, uma habilidade essencial para manipular dados de diferentes naturezas.

### Variáveis: Armazenando Informações:

Variáveis são nomes simbólicos que usamos para armazenar valores na memória do computador. Elas nos permitem referenciar e manipular dados de forma organizada e flexível em nossos programas.

#### Definição e Boas Práticas:

- **Atribuição**: O sinal de igual (=) é o operador de atribuição, utilizado para vincular um valor a um nome de variável.

- **PEP8**: A convenção de estilo oficial do Python (PEP8) recomenda que nomes de variáveis sejam iniciados com letras minúsculas e usem ``_`` (underscore) para separar palavras (snake_case).

````
nome = 'Luiz'         # String
idade = 30            # Inteiro
altura_metros = 1.80  # Float
e_maior_de_idade = idade >= 18 # Booleano

print('Nome:', nome)
print('Idade:', idade)
print('É maior de idade?', e_maior_de_idade)
print('Altura em metros:', altura_metros) 
````

### Tipos de Dados Primitivos:

Python é uma linguagem de tipagem dinâmica e forte, o que significa que os tipos das variáveis são inferidos em tempo de execução, e as operações entre tipos incompatíveis geralmente levantam erros, prevenindo surpresas.

#### Inteiros (``int``) e Floats (``float``):

- **Inteiros** (``int``): Representam números inteiros, positivos, negativos ou zero.

````
print(11)  # int
print(-11) # int
print(0)   # int
````

- **Floats** (``float``): Representam números com ponto flutuante (decimais), positivos ou negativos.

````
print(1.1, 10.11) # float
````

#### Booleanos (``bool``):
O tipo ``bool`` (booleano) representa valores lógicos, que só podem ser ``True`` (verdadeiro) ou ``False`` (falso). Eles são o resultado de operações de comparação ou lógicas.

- **Operador de Comparação** ``==``: Um dos operadores lógicos que questiona se um valor é igual a outro, retornando ``True`` ou ``False``.

````
print(10 == 10) # Saída: True (verdadeiro)
print(10 == 11) # Saída: False (falso)
````

#### A Função ``type()``:

A função ``type()`` é uma ferramenta útil para verificar o tipo de dado que o Python inferiu para um valor ou uma variável.

````
print(type('Marcos'))  # Saída: <class 'str'>
print(type(1))         # Saída: <class 'int'>
print(type(1.1))       # Saída: <class 'float'>
print(type(10 == 10))  # Saída: <class 'bool'>
````

### Conversão de Tipos (Coerção):

A conversão de tipos (ou coerção, type casting) é o processo de transformar um valor de um tipo de dado para outro. Em Python, isso é feito explicitamente usando funções como ``int()``, ``float()``, ``str()`` e ``bool()``.

- ``int()``: Converte para inteiro.

- ``float()``: Converte para float.

- ``str()``: Converte para string.

- ``bool()``: Converte para booleano (valores vazios ou zero geralmente são ``False``, outros são ``True``).

````
print(int('1') + 1)      # Converte '1' (string) para 1 (int), resultando em 2
print(float('1') + 1)    # Converte '1' (string) para 1.0 (float), resultando em 2.0
print(str(11) + 'b')     # Converte 11 (int) para '11' (str), resultando em '11b'
print(bool(''))          # Saída: False (string vazia é False)
print(bool(' '))         # Saída: True (string com espaço é True)
````

É importante notar que nem todas as conversões são válidas (ex: não é possível converter ``'abc'`` para ``int`` diretamente).

### Observações Finais:

A habilidade de definir e manipular variáveis é o cerne da criação de programas dinâmicos. A compreensão dos tipos de dados numéricos e booleanos, juntamente com a prática da conversão de tipos, equipa o programador para lidar com uma variedade maior de informações e realizar operações matemáticas e lógicas essenciais. Com esses conceitos, estamos prontos para construir lógicas mais complexas e interativas em nossos próximos passos.