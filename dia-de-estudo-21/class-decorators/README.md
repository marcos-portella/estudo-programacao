## Dia 21: Decoradores de Função e com Parâmetros

### Prefácio:

Hoje aprofundamos no conceito de **decoradores**, uma funcionalidade avançada e elegante do Python que permite modificar ou estender o comportamento de funções (e classes) sem alterar seu código-fonte diretamente. Exploramos como criar decoradores de função simples, como passá-los parâmetros e a importância da ordem de aplicação de múltiplos decoradores.

### Funções Decoradoras e Decoradores:

Um **decorador** é uma função que recebe outra função como argumento, adiciona alguma funcionalidade a ela e retorna uma nova função. Eles são considerados "açúcar sintático" (``syntax sugar``) para aplicar essa transformação de forma concisa usando o símbolo ``@``. [cite: uploaded:function-decorator.py]

- **Decorar**: Significa adicionar, remover, restringir ou alterar o comportamento de uma função. [cite: uploaded:function-decorator.py]

- **Funções Decoradoras**: São funções que "decoram" outras funções.

- **Decoradores (``@``)**: São a sintaxe que o Python usa para aplicar funções decoradoras.

````
# Exemplo 1: Decorador simples para adicionar funcionalidade
def criar_funcao(func): # 'func' é a função a ser decorada
    def interna(*args, **kwargs): # A função 'interna' será a nova versão da 'func'
        print('Vou te decorar!')
        resultado = func(*args, **kwargs) # Executa a função original
        resultado += ' (decorado com loucura)' # Adiciona funcionalidade
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada!')
        return resultado
    return interna

@criar_funcao # Aplica o decorador 'criar_funcao' à 'inverte_string'
def inverte_string(string):
    return string[::-1]

invertida = inverte_string('Python')
# Saída:
# Vou te decorar!
# O seu resultado foi nohtyP (decorado com loucura).
# Ok, agora você foi decorada!
# nohtyP (decorado com loucura)
```python
# Exemplo 2: Decorador com validação de tipo (reforçando o aprendizado do dia 21 - parte 4)
def e_string(param):
    if not isinstance(param, str):
        raise TypeError('O parâmetro deve ser uma string')

def validar_string(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            e_string(arg) # Valida se o argumento é string
        return func(*args, **kwargs)
    return wrapper

@validar_string
def saudacao(nome):
    return f'Olá, {nome}!'

print(saudacao('Mundo')) # Saída: Olá, Mundo!
# print(saudacao(123)) # Levantaria TypeError: O parâmetro deve ser uma string
````

### Decoradores com Parâmetros:

Para que um decorador aceite parâmetros, ele precisa ser implementado como uma **fábrica de decoradores**. Isso significa que a função que você usa com ``@`` na verdade retorna o decorador real.

- **Fábrica de Decoradores**: Uma função externa que recebe os parâmetros do decorador e retorna a função decoradora. A função decoradora, por sua vez, recebe a função a ser decorada e retorna a função aninhada (o ``wrapper``).

````
# Exemplo 3: Fábrica de decoradores com parâmetros
def fabrica_de_decoradores(param1=None, param2=None): # Esta é a fábrica que recebe os parâmetros
    def decorador_real(func): # Esta é a função decoradora que recebe a função a ser decorada
        print(f'Decorador real criado com parâmetros: {param1}, {param2}')
        def aninhada(*args, **kwargs): # Esta é a função que substituirá a original
            print(f'Executando função decorada. Parâmetros do decorador: {param1}, {param2}')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return decorador_real

@fabrica_de_decoradores(param1='log', param2='tempo') # Chamada da fábrica com parâmetros
def somar_numeros(x, y):
    return x + y

resultado = somar_numeros(10, 20)
print(f'Resultado da soma: {resultado}')
# Saída:
# Decorador real criado com parâmetros: log, tempo
# Executando função decorada. Parâmetros do decorador: log, tempo
# Resultado da soma: 30
````

### Ordem dos Decoradores:

Quando múltiplos decoradores são aplicados a uma única função, eles são executados de **baixo para cima** (ou de dentro para fora). O decorador mais próximo da função é aplicado primeiro, e o resultado é passado para o próximo decorador acima.

````
# Exemplo 4: Ordem de aplicação de decoradores
def decorador_externo(func):
    def wrapper_externo(*args, **kwargs):
        print('--> Decorador EXTERNO')
        res = func(*args, **kwargs)
        print('<-- Decorador EXTERNO')
        return res
    return wrapper_externo

def decorador_interno(func):
    def wrapper_interno(*args, **kwargs):
        print('  --> Decorador INTERNO')
        res = func(*args, **kwargs)
        print('  <-- Decorador INTERNO')
        return res
    return wrapper_interno

@decorador_externo
@decorador_interno
def minha_funcao():
    print('Executando minha_funcao')

minha_funcao()
# Saída:
# --> Decorador EXTERNO
#   --> Decorador INTERNO
# Executando minha_funcao
#   <-- Decorador INTERNO
# <-- Decorador EXTERNO
```python
# Exemplo 5: Ordem de decoradores com parâmetros (do arquivo decorators_order.py)
def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome) # Esta linha executa no momento da definição da função
        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}' # Adiciona o nome do decorador ao resultado
            return final
        return sua_nova_funcao
    return decorador

@parametros_decorador(nome='5') # Aplicado por último, envolve tudo
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1') # Aplicado primeiro, mais interno
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
# A ordem de impressão dos 'Decorador: X' será de 5 a 1 (de fora para dentro),
# mas a aplicação e modificação do resultado será de 1 para 5.
# Saída esperada (simplificada, a ordem exata dos prints do decorador pode variar):
# Decorador: 5
# Decorador: 4
# Decorador: 3
# Decorador: 2
# Decorador: 1
# 15 1 2 3 4 5  (o resultado final é 15 + os nomes dos decoradores aplicados em ordem)
````

### Observações Finais:

Decoradores são uma ferramenta poderosa para metaprogramação em Python, permitindo a reutilização de lógica de forma elegante e desacoplada. Compreender como criar decoradores de função, como eles aceitam parâmetros através de fábricas de decoradores e a importância da ordem de aplicação é crucial para utilizá-los efetivamente. Eles são amplamente usados em frameworks web (como Flask e Django para rotas), para logging, cache, validação de permissões e muito mais. A prática na criação e utilização de seus próprios decoradores solidificará seu domínio sobre este conceito avançado.