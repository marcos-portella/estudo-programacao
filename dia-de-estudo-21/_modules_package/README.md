### Dia 21: Estrutura de Pacotes e Decoradores Simples

### Prefácio:

Hoje revisitamos e aprofundamos na organização de código em Python, explorando a estrutura de pacotes e o papel do arquivo ``__init__.py`` para expor funcionalidades. Além disso, reforçamos o conceito de **decoradores**, uma forma poderosa de modificar ou estender o comportamento de funções sem alterar seu código diretamente, focando em um exemplo prático de validação de tipos.

### Estrutura de Pacotes e ``__init__.py``:

Para organizar projetos Python maiores, utilizamos **pacotes**. Um pacote é essencialmente um diretório que contém um ou mais módulos e um arquivo especial chamado ``__init__.py``. A presença de ``__init__.py`` (mesmo que vazio) indica ao Python que o diretório deve ser tratado como um pacote.

- ``__init__.py``: Este arquivo pode ser usado para inicializações do pacote ou, mais comumente, para definir quais módulos ou funções devem ser expostos quando o pacote é importado. Isso permite uma importação mais limpa e direta das funcionalidades. [cite: uploaded:init.py]

- **Módulos Internos**: Módulos dentro de um pacote (como ``_modules.py``) contêm o código principal.

Exemplo de estrutura:

````
meu_projeto/
├── main.py
└── _modules_package/
    ├── __init__.py
    └── _modules.py
````

Conteúdo de ``_modules_package/_modules.py``:

````
# _modules_package/_modules.py

# Função para verificar se um parâmetro é int ou float
def e_int_float(param):
    if not isinstance(param, (int, float)):
        raise TypeError('Adicione um int ou float')

# Função de adição, decorada para validação de tipo
@type_int_float
def _add(x, y):
    return x + y

# Função para criar novas funções (ex: multiplicadores)
def create_functions(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

# Função de multiplicação, decorada para validação de tipo
@type_int_float
def _mult(x, y):
    return x * y
````

Conteúdo de ``_modules_package/__init__.py``:

````
# _modules_package/__init__.py

# Expondo a função _add diretamente do pacote para facilitar a importação
def _add(x, y):
    return x + y
````

### Decoradores Simples para Validação de Tipo:

Um **decorador** é uma função que recebe outra função como argumento, adiciona alguma funcionalidade e retorna uma nova função (ou a função modificada). Eles são uma forma elegante de reutilizar código e aplicar lógica transversal, como validação, log ou medição de tempo de execução.

No exemplo fornecido, um decorador chamado ``type_int_float`` é usado para validar se os argumentos de uma função são do tipo ``int`` ou ``float``.

- **Função ``type_int_float`` (o decorador)**:

    - Recebe uma função (``func``) como argumento.

    - Define uma função interna (``iner``) que será a "nova" versão da função original.

     -Dentro de ``iner``, ela itera sobre os ``*args`` (argumentos não nomeados) e chama ``e_int_float`` para validar o tipo de cada um.

    - Após a validação, ela executa a função original (``func``) com os argumentos e retorna o resultado.

    - Retorna a função ``iner``. [cite: uploaded:_modules.py]

- **Função ``e_int_float`` (a lógica de validação)**:

    - Verifica se o ``param`` é uma instância de ``int`` ou ``float``.

    - Se não for, levanta um ``TypeError`` com uma mensagem descritiva. [cite: uploaded:_modules.py]

- **Sintaxe ``@decorador``**: O ``@`` é um "açúcar sintático" que facilita a aplicação de um decorador a uma função. É equivalente a ``funcao = decorador(funcao)``.

Exemplos:

````
# Exemplo 1: Definição do decorador e da função de validação (do _modules.py)
def type_int_float(func):
    def iner(*args, **kwargs):
        for arg in args:
            e_int_float(arg) # Chama a função de validação para cada argumento
        resultado = func(*args, **kwargs)
        return resultado
    return iner

def e_int_float(param):
    if not isinstance(param, (int, float)):
        raise TypeError('Adicione um int ou float')
```python
# Exemplo 2: Aplicando o decorador a uma função de adição
@type_int_float # Isso é o mesmo que _add = type_int_float(_add)
def _add(x, y):
    return x + y

print(_add(5, 10)) # Saída: 15 (funciona normalmente)
# print(_add(5, '10')) # Descomente para testar: levantaria um TypeError: 'Adicione um int ou float'
```python
# Exemplo 3: Aplicando o decorador a uma função de multiplicação
@type_int_float
def _mult(x, y):
    return x * y

print(_mult(2.5, 4)) # Saída: 10.0
# print(_mult('a', 5)) # Descomente para testar: levantaria um TypeError: 'Adicione um int ou float'
````

### Importando e Utilizando o Pacote:

Para usar as funcionalidades do pacote ``_modules_package`` no seu ``main.py`` (ou outro script), você pode importar de diferentes maneiras, aproveitando a estrutura definida pelo ``__init__.py``.

````
# Exemplo 4: Importando e usando funções do pacote
# No arquivo 'main.py':
from _modules_package import _add # Importa a função _add exposta no __init__.py
from _modules_package._modules import _mult # Importa a função _mult diretamente do módulo interno

print(f'Soma: {_add(10, 20)}') # Saída: Soma: 30
print(f'Multiplicação: {_mult(5, 6)}') # Saída: Multiplicação: 30
```python
# Exemplo 5: O papel do __init__.py na importação direta do pacote
# Se _add está definida diretamente no __init__.py, pode ser acessada assim:
import _modules_package

print(f'Soma via pacote: {_modules_package._add(7, 3)}') # Saída: Soma via pacote: 10

# Se _mult está apenas em _modules.py e não em __init__.py, precisa do caminho completo:
# print(f'Multiplicação via módulo interno: {_modules_package._modules._mult(4, 5)}')
````

### Observações Finais:

Esta parte do Dia 21 reforçou a importância da **modularização** e **estrutura de pacotes** em Python, mostrando como o arquivo __init__.py é fundamental para definir a interface de um pacote e facilitar a importação. Além disso, aprofundamos no conceito de decoradores, uma técnica avançada que permite adicionar funcionalidades a funções de forma limpa e desacoplada, como demonstrado com a validação de tipos. Dominar esses conceitos é crucial para construir aplicações Python bem organizadas, robustas e fáceis de manter.