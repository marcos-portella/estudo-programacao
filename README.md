## Python do Básico ao Avançado

Este arquivo contém resumos e anotações das aulas
do curso de Python feito na plataforma Udemy.

Os resumos vão se tornando mais didáticos e legíveis 
conforme as aulas avançam, mostrando minha evolução


## Dia 15

1. Operação Ternária
2. Cálculo dos Dígitos do CPF (Validação)



### 1. Operação Ternária

A operação ternária é uma forma reduzida de escrever condicionais:
```
condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

digito = 9  # > 9 = 0
novo_digito = digito if digito <= 9 else 0
print(novo_digito)

digito = 8
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

print('Valor' if False else 'Outro valor' if False else 'Fim')
```


### 2. Cálculo dos Dígitos do CPF (Validação):

Este código valida um CPF baseado no cálculo dos dois dígitos verificadores finais.
Eu poderia ter diminuido o código fundindo várias partes deles em apenas uma linhas, mas fiz deste modo para ficar mais óbvio o que está acontecendo no código, mesmo que tendo que repetir em algumas partes

```
import os

cpf = '746.824.890-70'

digit1 = (f'{cpf[-2]}')
digit2 = (f'{cpf[-1]}')
digit1 = int(digit1)
digit2 = int(digit2)

while True:
    cpf_typed = input('Digite seu CPF: ')
    multiplier = 11
    digit_added = 0
    os.system('clear')

    if cpf_typed == 'sair':
        break

    cpf_modified = cpf_typed.replace('.', '').replace('-','')
    nine_digit = (f'{cpf_modified[:9]}')
    last_digit = (f'{cpf_modified[-1]}')
    last_digit_i = int(last_digit)

    if  last_digit_i == digit2:
        ...
    else:
        print('ERRO: CPF inválido.')
        break

    try:
        cpf_modified_i = int(cpf_modified)
    except ValueError:
        print('Digite apenas números.')
        break

    for cpf_typed_digit in nine_digit:
        multiplier -= 1
        digit_added += int(cpf_typed_digit) * multiplier

    cpf_typed_rest = (digit_added * 10) % 11

    if cpf_typed_rest > 9:
        cpf_typed_rest = 0
    else:
        cpf_typed_rest = cpf_typed_rest

    try:
        if cpf_typed_rest != digit1:
            print('ERRO: CPF inválido.')
        elif cpf_typed_rest == digit1:
            ...
    except:
        print('ERRO DESCONHECIDO')

    multiplier = 12
    ten_digits = (f'{cpf_modified[:10]}')
    digit_added = 0

    for cpf_typed_digit in ten_digits:
        multiplier -= 1
        digit_added += int(cpf_typed_digit) * multiplier
    
    cpf_typed_rest = digit_added * 10 % 11

    if cpf_typed_rest > 9:
        cpf_typed_rest = 0
    else:
        cpf_typed_rest = cpf_typed_rest
    
    try:
        if cpf_typed_rest != digit2:
            print('ERRO: CPF inválido.')
        elif cpf_typed_rest == digit2:
            print('CPF válido')
    except:
        print('ERRO DESCONHECIDO')
```

### Observações Finais:
- A operação ternária é útil para expressar condições simples de forma compacta.
- A validação de CPF envolve multiplicações por pesos decrescentes e operações com módulo 11.
- Importante usar try/except para proteger o código contra entradas inválidas do usuário.



## Dia 16

### Resumo:

Hoje, aprendi a criar funções com parâmetros e valores padrão.
Entendi como funciona o escopo local e global das variáveis,
e a usar o comando return para devolver resultados.

Explorei o uso de argumentos variáveis com *args, que me permitem
passar múltiplos valores para uma função. Também conheci funções
de ordem superior, que podem receber ou retornar outras funções.

Aprendi sobre argumentos nomeados, closures (funções que retornam funções)
e fiz exercícios práticos para multiplicar números, verificar se um número
é par ou ímpar, e criar multiplicadores personalizados.

Esses conceitos me ajudam a escrever códigos mais modulares,
reutilizáveis e expressivos em Python.


### Conteúdo:
1. Introdução às funções (def) em Python
2. Escopo de funções em Python
3. Retorno de valores das funções (return)
4. Valores padrão para parâmetros
5. args - Argumentos não nomeados (*args)
6. Exercícios com funções (multiplicação e par/impar)
7. Higher Order Functions (funções que recebem funções)
8. Argumentos nomeados e não nomeados em funções
9. Closure e funções que retornam outras funções
10. Exercícios com funções que retornam funções (multiplicadores)


1. Introdução às funções (def) em Python:
```
def saudacao(nome= 'Sem nome'):
    print(f'Olá {nome}')

saudacao('Luiz Otávio')
saudacao()
```

2. Escopo de funções em Python:
```
x = 1

def escopo(va):
    x = 10
    print(x)
    print(va)
    def outra_funcao():
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo(x)
print(x)
```

3. Retorno de valores das funções (return):
```
def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))
```

4. Valores padrão para parâmetros:
```
def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)
```

5. args - Argumentos não nomeados (*args):
```
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros))
```

6. Exercícios com funções:
```
# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def mult(*args):
    result = 1
    for number in args:
        result *= number
    return result

total = (mult(1, 2, 3, 4, 5))
print(total)


# Exercício 2 Solução do professor:
# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'


outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)

print(par_impar(3))

print(par_impar is outro_par_impar)
```

7. Higher Order Functions:
```
def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)
```

8. Argumentos nomeados e não nomeados em funções Python:
```
def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

soma(1, 2, 3)
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')
```

9. Closure e funções que retornam outras funções:
```
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
```

10. Exercícios com funções que retornam funções (multiplicadores):
```
total = 1

def multiplier(mult):
    def number(number):
        return number * mult 
    return number

duplicate = multiplier(2)
triple = multiplier(3)
quadruple = multiplier(4)

print(duplicate(5))
print(triple(5))
print(quadruple(5))
```

### Observações finais:
- Funções em Python são blocos reutilizáveis de código que podem receber parâmetros e retornar valores.
- O escopo de variáveis pode ser local (dentro da função) ou global (fora da função).
- O uso de valores padrão nos parâmetros facilita a chamada das funções.
- *args permite passar número variável de argumentos não nomeados.
- Funções podem ser passadas como argumentos e retornadas, permitindo programação funcional e uso de closures.
- Entender closures é essencial para criar funções dinâmicas e personalizadas.
- Exercitar funções com argumentos variáveis e funções retornando funções ajuda a consolidar conceitos avançados.


## Dia 17

### Tópicos estudados:
1. Dicionários (dict)
2. Manipulação de chaves e valores
3. Métodos úteis de dicionários
4. Exercício: sistema de perguntas e respostas com dicionários
5. Sets (conjuntos)
6. Exercício com sets: adivinhação de letra
7. Exercício: encontrar o primeiro número duplicado

### Prefácio:
Hoje aprendi a trabalhar com dicionários e conjuntos (sets) em Python. Estudei como criar, acessar, modificar e remover pares de chave e valor em dicionários, além de usar métodos úteis como get, pop, update e setdefault. Também desenvolvi um pequeno sistema de perguntas e respostas, reforçando o uso prático dos dicionários.

Em seguida, conheci os sets, estruturas que armazenam apenas valores únicos. Aprendi suas operações mais importantes, como união, interseção e diferença, e vi como eles podem ser usados para resolver problemas, como no exercício que identifica a primeira duplicata em uma lista.


### 1. Dicionários:

- São estruturas mutáveis do tipo chave:valor.
- Criados com `{}` ou `dict()`.
- Exemplo:
```
    pessoa = {
        'nome': 'Luiz',
        'idade': 30
    }
```
- Suportam valores compostos (listas, dicionários).

### 2. Manipulação de dicionários
- Adicionar/modificar com `dict[chave] = valor`.
- Remover com `del dict[chave]` ou `pop()`.
- Verificação com `get()` (evita erro caso chave não exista).

### 3. Métodos úteis de dicionário
- `len()`: número de chaves.
- `keys()`, `values()`, `items()`: iteráveis das partes do dicionário.
- `setdefault()`: define valor se chave não existir.
- `copy()`: cópia rasa.
- `pop()`, `popitem()`: removem valores.
- `update()`: atualiza/adiciona pares chave-valor.

### 4. Exercício: Quiz
- Estrutura de perguntas em lista de dicionários.
- Validação de entrada com `input()` e conversão.
- Contador de acertos e mensagens de feedback.

### 5. Sets
- Conjuntos que armazenam valores únicos e imutáveis.
- Criados com `set()` ou `{}`.
- Removem duplicatas automaticamente.
- Não têm ordem nem índice.
- Métodos: `add()`, `update()`, `discard()`, `clear()`.
- Operações: união (`|`), interseção (`&`), diferença (`-`), diferença simétrica (`^`).

### 6. Exercício com sets: adivinhação de letra
- Usuário digita letras.
- Ao acertar a letra "l", o programa encerra com parabéns.

### 7. Exercício: encontrar primeiro número duplicado
- Recebe lista de inteiros.
- Utiliza `set()` para checar duplicação.
- Retorna a primeira duplicata com base na segunda aparição.
"""



## Dia 18

### Prefácio:

Hoje aprendi bastante sobre compreensões de listas, dicionários e conjuntos, que são formas práticas e elegantes de criar coleções em Python. Vi como usar funções lambda para criar funções rápidas e anônimas, e como usá-las para ordenar listas de dicionários. Também explorei funções que recebem outras funções como argumento, entendendo melhor o conceito de funções de ordem superior.

Estudei o empacotamento e desempacotamento de dicionários, além de entender como passar argumentos nomeados usando **kwargs. Reforcei o uso do isinstance para verificar tipos de dados, e aprendi sobre valores "truthy" e "falsy", que são importantes para entender como Python avalia condições.

Finalmente, aprendi a usar hasattr e getattr para verificar e chamar métodos dinamicamente, e diferenciei iteráveis, iteradores e geradores, entendendo como economizar memória com generator expressions.

### Sumário:
1. Introdução à List Comprehension;
2. List Comprehension com múltiplos for e listas aninhadas;
3. Mapeamento de dados com List Comprehension e condição;
4. pprint e filtro com if em list comprehension;
5. Dictionary Comprehension e Set Comprehension;
6. Funções Lambda e sorted com chave customizada;
7. Funções de ordem superior e lambda complexas;
8. Empacotamento e desempacotamento de dicionários e argumentos;
9. isinstance para checagem de tipos;
10. Valores Truthy e Falsy, tipos mutáveis e imutáveis;
11. dir, hasattr e getattr;
12. Generator expression, Iterables e Iterators;


### 1. Introdução à List Comprehension:
```
print(list(range(10))) # O que queremos fazer manualmente
print()

lista = [] #  Forma tradicional
for numero in range(10):
    lista.append(numero)
print(lista)

lista = [ # Usando o list comprehension
    numero * 2
    for numero in range(10)
]
print(lista)
```

### 2. List comprehension com múltiplos for e listas aninhadas:
```
lista = [] # Método básico
for x in range(3):
    for y in range(3):
        lista.append((x, y))
print(lista)
print()


lista = [ # Usando o list comprehesion
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(lista)
print()


lista = [
    [(x, letra) for letra in 'Luiz'] # Um list comprehension dentro de outro, complexo até demais
    for x in range(3)
]

print(lista)
```

### 3. Mapeamento de dados em list comprehension com condição:
```
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(novos_produtos)
print(*novos_produtos, sep='\n')
```

### 4. pprint para exibir dados de forma bonita + filtro com if:
```
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
```

### 5. Dictionary Comprehension e Set Comprehension:
```
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = { # o que vale para lista vale para o diconário
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
dc = {
    chave: valor
    for chave, valor in lista
}

dict(lista) # Torna lista em dictionary


s1 = {2 ** i for i in range(10)} # set comprehension
print(s1)
```

### 6. Funções Lambda e sorted com chave customizada:
```
lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
lista.sort() # Ordena os itens

lista.sort(reverse=True) # Ordena os itens ao contrário, sort modifica a lista diretamente

sorted(lista) # também ordena


lista2 = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista2, key=lambda item: item['nome']) # Expressão lambda, sorted cópia rasa
l2 = sorted(lista2, key=lambda item: item['sobrenome']) 

exibir(l1)
exibir(l2)
```

### 7. Funções executando funções (Higher-order functions) e lambda complexas:
```
def executa(funcao, *args): # Função de execução
    return funcao(*args)


def soma(x, y): #Função de soma
    return x + y


def cria_multiplicador(multiplicador): # Função de multiplicão
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


duplica = cria_multiplicador(2)


duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))

print(
    executa(
        lambda x, y: x + y, # Acaba ficando muito complexo, usar lambda para coisas rápidas
        2, 3
    ),
)

print(
    executa(
        lambda *args: sum(args), # Soma todos os parâmetros que ela receber
        1, 2, 3, 4, 5, 6, 7
    )
)
```

### 8. Empacotamento e desempacotamento de dicionários e argumentos:
```
a, b = 1, 2
a, b = b, a # invertendo o valor dos itens de forma rápida
print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}


(a1, a2), (b1, b2) = pessoa.items() # Desempacota os item diretamente nas variáveies
print(a1, a2)
print(b1, b2)


for chave, valor in pessoa.items(): # Desempacotando com for
    print(chave, valor)



dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa} # Desempacontando dentro de outro dicionário
print(pessoas_completa)


# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs): # Mostra argumentos nomeados
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


mostro_argumentos_nomeados(nome='Joana', qlq=123) # Melhor para adicionar argumentos um por um
mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = { # Adiconando argumentos e valores de forma mais organizada
     'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes) # Pode usar para executar um print
```

### 9. isinstance para tipo, cuidado com misturar tipos:
```
# EVITE MISTURA DE TIPOS DESTA FORMA!!
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)
        
    else:
        print('OUTRO')
        print(item)
```

### 10. Valores Truthy e Falsy, tipos mutáveis e imutáveis:
```
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteito = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


def falsy(valor):
    return 'falsy'if not valor else 'truthy'


print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteito=}', falsy(inteito))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))
```

### 11. dir, hasattr e getattr:
```
string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)
```

### 12. Generator expression, Iterables e Iterators:
```
import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)

for n in generator:
    print(n)
```


## Dia 19

### Prefácio:
No estudo de hoje, aprendi sobre funções geradoras em Python, que são funções especiais que usam o yield para produzir valores um a um, pausando e retomando a execução conforme necessário. Também explorei o tratamento de exceções utilizando os blocos try e except para capturar erros específicos, como divisão por zero, além de entender o uso dos blocos else e finally para controlar o que acontece após o tratamento dos erros.

Além disso, aprendi sobre modularização em Python, conhecendo o papel do módulo principal `__main__` e diferentes formas de importar módulos e suas partes, inclusive com alias para facilitar o uso dos nomes. Vi também como usar o yield from para delegar a execução de um gerador a outro, o que torna o código com múltiplos geradores mais simples e limpo. Por fim, pratiquei como lançar exceções com o comando raise, criando funções que verificam tipos e valores para evitar erros comuns

### Sumário:
1. Funções Geradoras (Generator functions);
2. Tratamento de Exceções com try e except;
3. Blocos try, except, else e finally;
4. Modularização e o módulo `__main__`;
5. Módulos Padrão do Python (import, from, as, *);
6. Yield from - Delegando Geradores;
7. Raise - Lançando Exceções;


### 1. Funções Geradoras (Generator functions):
```
def generator(n=0, maximum=10): # Função generator
    while True:
        yield n # Pausado aqui no yield
        n += 1

        if n > maximum:
            return

gen = generator(maximum=1000000)

for n in gen:
    print(n)
```

### 2. Tratamento de Exceções com try e except:
```
try:
    a = 18
    b = 0
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')
```

### 3. try, except, else e finally:
```
try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')
```

### 4. Modularização e o módulo `__main__`:
```
import sys
print('Este módulo se chama', __name__)
print(*sys.path, sep='\n')
```
### 5. Módulos Padrão do Python (import, from, as, *):
```
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
import sys

platform = 'A MINHA'
print(sys.platform)
print(platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo

from sys import exit, platform

print(platform)

# alias 1 - import nome_modulo as apelido

import sys as s # Nunca modifique o nome dos módulos do python

sys = 'alguma coisa'
print(s.platform)
print(sys)

# alias 2 - from nome_modulo import objeto as apelido
# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem
from sys import exit as ex
from sys import platform as pf

print(pf)

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo

from sys import exit, platform

print(platform)
exit()
```

### 6. Yield from - Delegando Geradores:
```
# Yield from
def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')

def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')

def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')

g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()
```
### 7. Raise - Lançando Exceções:
```
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True

def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d


print(divide(8, '0'))
```


## Dia 21

### Prefácio

No dia 21, mergulhei em recursos mais avançados e elegantes da linguagem Python. Este estudo teve como foco a composição e transformação de funções, a organização do código com decoradores e modularização, além do uso de ferramentas poderosas como `itertools` e `copy`. Foi um dia dedicado a entender como escrever código mais expressivo, reutilizável e robusto.

### Manipulação de Listas com `zip` e `zip_longest`:

Comecei com a união de listas usando `zip`, que combina os elementos de duas listas na mesma posição.

```
zip([1, 2, 3], [4, 5, 6]) → [(1, 4), (2, 5), (3, 6)]
```

Usei também `zip_longest`, do módulo `itertools`, que permite combinar listas de tamanhos diferentes preenchendo com um valor padrão.

```
zip_longest(['a', 'b'], [1], fillvalue='X') → [('a', 1), ('b', 'X')]
```

### Variáveis Livres e `nonlocal`:

Estudei o conceito de variáveis livres, que são capturadas por funções aninhadas. Com `nonlocal`, consigo modificar o valor de uma variável de escopo externo (mas não global), preservando o estado entre chamadas.

```
def contador():
    total = 0
    def interno():
        nonlocal total
        total += 1
        return total
    return interno

c = contador()
c() → 1
c() → 2
```

### Funções Decoradoras:

Aprendi a criar decoradores, que são funções que modificam o comportamento de outras funções. Servem para adicionar funcionalidades de forma elegante e reutilizável.

```
def decorador(func):
    def wrapper(*args):
        print("Antes")
        resultado = func(*args)
        print("Depois")
        return resultado
    return wrapper
```

Apliquei decoradores com a sintaxe ``@decorador``, o chamado açúcar sintático.

```
@decorador
def saudacao(nome):
    return f"Olá, {nome}"
```

### Decoradores com Parâmetros:

Vi que é possível criar decoradores que recebem argumentos próprios, criando uma "fábrica de decoradores".

```
def com_prefixo(texto):
    def decorador(func):
        def wrapper(*args):
            return f"{texto} {func(*args)}"
        return wrapper
    return decorador

@com_prefixo(">>")
def saudacao(nome):
    return f"Olá, {nome}"
```

### Ordem de Execução de Decoradores:

Quando usamos múltiplos decoradores empilhados, o Python executa de baixo para cima. Isso significa que o decorador mais próximo da função é executado primeiro.

```
@A
@B
def func(): pass

# A ordem é: func → B(func) → A(B(func))
```

### Criação de Funções Parcialmente Aplicadas:

Usei funções para criar outras funções com parte dos argumentos já definidos, um conceito inspirado em programação funcional.

```
def multiplicar_por(x):
    def resultado(y):
        return x * y
    return resultado

dobro = multiplicar_por(2)
dobro(5) → 10
```

### Validação com Decoradores:

Implementei decoradores para validar os argumentos passados a uma função. Por exemplo, rejeitar valores que não sejam ``int`` ou ``float``.

```
def somente_numeros(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("Apenas números permitidos")
        return func(*args)
    return wrapper
```

### ``itertools.count`` como contador infinito:

Usei o ``count`` da biblioteca ``itertools`` para criar um contador infinito controlável por condição:

```
from itertools import count

for i in count(start=0, step=2):
    if i > 10:
        break
    print(i)  # 0, 2, 4, 6, 8, 10

```

### Cópia Profunda e Ordenação de Dicionários:

Usei ``copy.deepcopy`` para modificar estruturas de dados sem afetar o original, ideal para listas de dicionários.
````
import copy
novo = copy.deepcopy(lista_original)
````

Ordenei listas de dicionários com ``sorted``, usando ``lambda`` como chave:

````
sorted(produtos, key=lambda p: p['preco'])
````

### Uso de ``__init__.py``:

Vi que o arquivo especial ``__init__.py`` dentro de uma pasta permite que ela seja tratada como um pacote Python, podendo assim importar funções ou objetos diretamente dela com:

````
from minha_pasta import minha_funcao
````

### Considerações Finais
O estudo de hoje foi essencial para me preparar para um código mais modular, reutilizável e seguro. Aprendi a manipular funções como objetos, controlar escopos internos com ``nonlocal``, e tornar minha lógica mais flexível com decoradores — inclusive com parâmetros. Ferramentas como ``zip``, ``itertools``, ``copy`` e a estruturação com ``__init__.py`` aumentam muito a capacidade de escrever código Python mais limpo, organizado e profissional.



## Dia 22

### Prefácio:

Neste resumo, exploraremos conceitos fundamentais e avançados da linguagem Python, com ênfase em funções recursivas, ferramentas funcionais, itertools e ambientes virtuais. Cada tópico é abordado com explicações claras e pequenos exemplos para consolidar a compreensão.

### Sumário:

1. Funções Recursivas
2. Funções Funcionais: map, partial, reduce, filter
3. Itertools: combinations, permutations, product, groupby
4. Ambientes Virtuais e pip
5. Considerações Finais

### 1. Funções Recursivas:

Recursão é uma técnica em que uma função se chama a si mesma para resolver problemas menores de um problema maior. Uma função recursiva precisa de:

- Um caso base (que para a recursão)
- Um caso recursivo (que continua a chamada)

Exemplo:
```
# Contagem de 0 até fim
def recursiva(inicio, fim):
    print(inicio)
    if inicio >= fim:
        return fim
    return recursiva(inicio + 1, fim)

recursiva(0, 4)
```

Outro exemplo clássico é o fatorial:

```
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

### 2. Funções Funcionais:

- `map` aplica uma função a cada item de um iterável:
```
print(list(map(lambda x: x * 2, [1, 2, 3])))  # [2, 4, 6]
```

- `partial` fixa argumentos de uma função:
```
from functools import partial

def aumentar(valor, taxa):
    return valor * taxa

aumentar10 = partial(aumentar, taxa=1.1)
print(aumentar10(100))  # 110.0
```

- `reduce` reduz um iterável a um único valor:
```
from functools import reduce

numeros = [1, 2, 3, 4]
soma = reduce(lambda acc, x: acc + x, numeros, 0)
print(soma)  # 10
```

- `filter` filtra elementos com base em uma condição:

```
numeros = [10, 20, 5, 8]
maiores = filter(lambda x: x > 10, numeros)
print(list(maiores))  # [20]
```

### 3. Itertools:

- `combinations`: gera combinações sem importar a ordem:

```
from itertools import combinations
print(list(combinations(['A', 'B', 'C'], 2)))  # [('A', 'B'), ('A', 'C'), ('B', 'C')]
```

- `permutations`: considera a ordem:

```
from itertools import permutations
print(list(permutations(['A', 'B'], 2)))  # [('A', 'B'), ('B', 'A')]
```

- `product`: produto cartesiano com repetição:

```
from itertools import product
print(list(product([1, 2], repeat=2)))  # [(1, 1), (1, 2), (2, 1), (2, 2)]
```

- `groupby`: agrupa elementos semelhantes:

```
from itertools import groupby

alunos = [
    {'nome': 'Ana', 'nota': 'A'},
    {'nome': 'Bia', 'nota': 'B'},
    {'nome': 'Carlos', 'nota': 'A'}
]

alunos.sort(key=lambda x: x['nota'])
grupo = groupby(alunos, key=lambda x: x['nota'])
for chave, grupo_de_alunos in grupo:
    print(chave, list(grupo_de_alunos))
```

### 4. Ambientes Virtuais e pip:

Ambientes virtuais permitem isolar dependências de projetos Python, evitando conflitos entre bibliotecas.

- Criar:
```
python -m venv venv
```

- Ativar (Windows Bash):
```
. nome_do_arquivo/Scripts/activate
```

- Usar pip:

```
pip install nome_pacote
pip freeze > requirements.txt
pip install -r requirements.txt
```

### 5. Considerações Finais:

Este resumo abordou tópicos essenciais para quem deseja dominar Python em um nível mais funcional e profissional. O uso de recursão, funções como `map` e `filter`, e ferramentas como `itertools` permitem escrever código mais expressivo e eficiente. O gerenciamento com `venv` e `pip` é indispensável para projetos organizados.


## Dia 23

### Prefácio:

Hoje exploramos funcionalidades importantes para manipulação de arquivos, parâmetros de funções, controle de listas de tarefas e a serialização com JSON. Vários exemplos foram usados para mostrar práticas recomendadas, como uso de context manager, tratamento de parâmetros padrão mutáveis, entre outros.

### Sumário:

1. Manipulação de arquivos com `with open` e o módulo `os`;
2. Parâmetros padrão mutáveis e boas práticas;
3. Leitura e gravação de JSON com o módulo `json`;
4. Lista de tarefas com desfazer e refazer;
5. Persistência de tarefas com JSON;
6. Parâmetros apenas posicionais e nomeados com `/` e `*`;

### 1. Manipulação de arquivos com `with open` e o módulo `os`:

Para manipular arquivos com segurança e sem precisar se preocupar em fechar manualmente, 
utilizamos o `with open`.

Exemplo:
```
with open('arquivo.txt', 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.seek(0)
    print(arquivo.read())
```
Também vimos como:

Usar os modos `'r'`, `'w'`, `'a'`, `'x'`, `'b'`, ```'t'`` e ``'+'``

Apagar arquivos com ``os.remove`` ou ``os.unlink``

Renomear com ``os.rename``

### 2. Parâmetros padrão mutáveis e boas práticas:

Evite usar listas ou dicionários como valores padrão diretamente nos parâmetros.

Errado:

````
def func(lista=[]): ...
````

Correto:
````
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista
````

### 3. Leitura e gravação de JSON com o módulo ``json``:

Aprendemos a salvar e ler dicionários no formato JSON, útil para persistência de dados.

Salvar:

````
with open('arquivo.json', 'w', encoding='utf8') as f:
    json.dump(objeto, f, indent=2, ensure_ascii=False)
````

Carregar:

````
with open('arquivo.json', 'r', encoding='utf8') as f:
    dados = json.load(f)
````

### 4. Lista de tarefas com desfazer e refazer:

Criamos uma lista de tarefas com a habilidade de desfazer e refazer operações,
usando duas listas: ``tarefas`` e ``tarefas_refazer``.

Funções principais:

- ``listar(tarefas)``;

- ``desfazer(tarefas, tarefas_refazer)``;

- ``refazer(tarefas, tarefas_refazer)``;

- ``adicionar(tarefa, tarefas)``;

### 5. Persistência de tarefas com JSON:

A versão evoluída do sistema de tarefas salva e carrega automaticamente os dados
em um arquivo JSON, mantendo as tarefas mesmo após o programa ser fechado.

````
def salvar(tarefas, caminho):
    with open(caminho, 'w', encoding='utf8') as f:
        json.dump(tarefas, f, indent=2, ensure_ascii=False)

def ler(caminho):
    try:
        with open(caminho, 'r', encoding='utf8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
````

### 6. Parâmetros apenas posicionais e nomeados com ``/`` e ``*``:

Python permite forçar parâmetros a serem:

- Apenas posicionais (``/``);

- Apenas nomeados (``*``);

Exemplo:

````
def soma(a, b, /, *, c, **kwargs):
    print(a + b + c)

soma(1, 2, c=3)
````

Tudo antes da ``/`` deve ser passado posicionalmente.
Tudo depois de ``*`` deve ser passado como argumento nomeado.

### Considerações Finais:

Neste dia, revisitamos conceitos fundamentais com profundidade prática. O uso de arquivos,
listas com controle de estado e estruturas como JSON nos dá mais poder para criar aplicações persistentes e seguras. 

Além disso, aprendemos a tornar funções mais robustas com o uso adequado de parâmetros, reforçando a importância da clareza e previsibilidade no código Python.



## Dia 24

### Prefácio:
Hoje nos aprofundamos em Programação Orientada a Objetos (POO), aprendendo os fundamentos das classes, atributos, instâncias, métodos, encapsulamento de estado, atributos de classe, métodos de classe, e também como salvar e carregar dados de objetos usando JSON.
Esses conceitos são essenciais para construção de sistemas organizados, modulares e reutilizáveis.

### Sumário:
1. Criando classes e instâncias;
2. Métodos de instância e uso do ``self``;
3. Mantendo estados internos com atributos;
4. Atributos de instância com ``__dict__`` e ``vars()``;
5. Atributos de classe e valores compartilhados;
6. Métodos de classe e padrão fábrica;
7. Salvando e carregando instâncias com JSON;


### 1. Criando classes e instâncias:

Uma classe é um molde para criar objetos. Ao instanciar uma classe, obtemos um objeto com atributos próprios.

````
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Luiz', 'Otávio')
print(p1.nome)  # Luiz
````

Também criamos outras classes como ``Carro`` e ``Animal``, com métodos próprios:

````
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')
````
### 2. étodos de instância e uso do self:

O ``self`` é a referência para a instância atual. É obrigatório em métodos que manipulam dados do objeto.

````
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
````

Usamos ``self.nome`` para acessar os atributos da instância dentro dos métodos.

### 3. Mantendo estados internos com atributos:

Criamos a classe ``Camera`` que mantinha um estado interno (``filmando``) para controlar o comportamento:

````
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando...')
        else:
            self.filmando = True
            print(f'{self.nome} começou a filmar.')
````

Isso nos permite controlar o estado de cada instância separadamente.

### 4. Atributos de instância com ``__dict__`` e ``vars()``:

Cada instância armazena seus atributos no dicionário ``__dict__``. Podemos acessar com ``vars()``:

````
p1 = Pessoa('João', 35)
print(vars(p1))  # {'nome': 'João', 'idade': 35}
````

Esse recurso é útil para inspeção e para serializar objetos em formatos como JSON.

### 5. Atributos de classe e valores compartilhados:

Atributos de classe são compartilhados entre todas as instâncias da mesma classe.

````
class Pessoa:
    ano_atual = 2022
````

Alterar esse valor afeta todos os objetos que utilizam esse dado:

````
Pessoa.ano_atual = 2025
````

É útil quando um valor é comum a todos os objetos.

### 6. Métodos de classe e padrão fábrica:

Métodos de classe recebem a própria classe (``cls``) como primeiro parâmetro. Servem, por exemplo, para criar fábricas de objetos com valores pré-definidos:

````
@classmethod
def criar_com_50_anos(cls, nome):
    return cls(nome, 50)
````

Isso permite criar objetos de forma padronizada:

````
p = Pessoa.criar_com_50_anos('Helena')
````
### 7. Salvando e carregando instâncias com JSON:

Aprendemos a serializar dados de objetos usando JSON. Primeiro, usamos ``vars()`` ou ``__dict__`` para obter os dados da instância, e salvamos em arquivo:

````
with open('arquivo.json', 'w', encoding='utf8') as f:
    json.dump([vars(p1), vars(p2)], f, indent=2)
````
Depois, para recriar os objetos, usamos ``Pessoa(**dicionario)``:

````
with open('arquivo.json', 'r', encoding='utf8') as f:
    dados = json.load(f)
    p = Pessoa(**dados[0])
````

Essa técnica é útil para persistência de dados entre execuções do programa.

### Considerações Finais:
Hoje vimos os fundamentos práticos da orientação a objetos em Python. Aprendemos como modelar entidades
com classes, armazenar e manipular estados internos, definir comportamentos e persistir objetos em disco.
Esses conceitos são fundamentais para projetos organizados, reutilizáveis e fáceis de manter. A capacidade de
salvar e carregar objetos com JSON prepara o terreno para aplicações mais robustas e completas.


## Dia 25

### Prefácio:
No dia 25 de estudos, aprofundamos nossos conhecimentos em Programação Orientada a Objetos com foco em boas práticas, encapsulamento, propriedades com ``@property``, métodos de classe, estáticos e tipos de relacionamento entre classes, além de práticas aplicadas com exercícios. Foi um passo importante para escrever códigos mais robustos e profissionais.

### Sumário:
1. Encapsulamento: public, protected e private;
2. ``@property`` e @setter: getters e setters pythônicos;
3. ``@staticmethod``: métodos estáticos;
4. Relações entre classes: associação, agregação, composição;
5. Exercício prático de composição (Carro, Motor, Fabricante);
6. Diferenças entre method, classmethod e staticmethod;


### 1. Encapsulamento: public, protected e private:

Python não impõe modificadores de acesso, mas utiliza convenções:
- `public`: sem underline (livre acesso);
- `_protected`: underline simples (uso interno);
- `__private`: underline duplo (name mangling);

````
class Foo:
    def __init__(self):
        self.public = 'público'
        self._protected = 'protegido'
        self.__private = 'privado'

    def metodo_publico(self):
        print(self.__private)  # Acessando atributo privado
````
### 2. ``@property`` e ``@setter``: getters e setters pythônicos:

O ``@property`` transforma um método em atributo de leitura.
O ``@setter`` permite modificar valores com validações.

````
class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError('Não aceito esta cor')
        self._cor = valor
````

### 3. @staticmethod: métodos estáticos:

Métodos estáticos não recebem ``self`` nem ``cls``. São funções organizadas dentro de uma classe.

````
class Classe:
    @staticmethod
    def funcao_estatica(*args, **kwargs):
        print('Oi', args, kwargs)
````

Eles são úteis para agrupar lógica relacionada à classe, mas que não dependem do estado.

### 4. Relações entre classes: associação, agregação, composição:

- *Associação:* objetos se relacionam, mas vivem separadamente:

````
class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self.ferramenta = None
````

- *Agregação:* objetos relacionados mantêm vida própria:

````
class Carrinho:
    def __init__(self):
        self._produtos = []
````

- *Composição:* um objeto "compõe" outro; se o pai for apagado, os filhos também:

````
class Cliente:
    def __init__(self, nome):
        self.enderecos = []
````

### 5.Exercício prático de composição (Carro, Motor, Fabricante):

Relacionamos classes com has-a (tem-um) utilizando atributos compostos:

````
class car:
    def __init__(self, name):
        self.name = name
        self.factory = None
        self.engine = None

    @classmethod
    def create_car(cls, name, factory, engine):
        car = cls(name)
        car.factory = factory
        car.engine = engine
        return car
````

Demonstrações:

````
car1 = car.create_car('Gato', factory1, engine1)
print(car1.name, car1.factory.name, car1.engine.name)
````

### 6.Diferenças entre method, classmethod e staticmethod:

- **method:** recebe ``self`` (instância);

- **@classmethod:** recebe ``cls`` (classe);

- **@staticmethod:** não recebe nada automaticamente;

````
class Connection:
    def __init__(self):
        self.user = None

    @classmethod
    def create_with_auth(cls, user, password):
        c = cls()
        c.user = user
        c.password = password
        return c

    @staticmethod
    def log(msg):
        print('LOG:', msg)
````

Uso:

````
c1 = Connection.create_with_auth('luiz', '1234')
Connection.log('Mensagem')
````

### Considerações Finais:
Nesta etapa do curso, aprendemos boas práticas fundamentais da programação orientada a objetos:
encapsulamento, uso moderno de ``property`` e ``setter``, tipos de métodos dentro da classe, e os diferentes tipos de relacionamento entre objetos. Também aplicamos esse conhecimento em exercícios práticos que fortalecem o entendimento.

A POO é uma das bases para projetos escaláveis, organizados e reutilizáveis em Python.



## Dia 26

Livro - Arquitetura Limpa by Robert C. Martim

Capítulos do 1 ao 5:

### 1. Design vs Arquitetura:
- Não há diferença real entre design e arquitetura;
- Arquitetura está associada a decisões de alto nível;
- Design está associado a detalhes de baixo nível;
- Exemplo: Na construção civil, o arquiteto define desde a forma da casa até a posição de tomadas e interruptores;
- No software: decisões de alto e baixo nível formam um todo contínuo;

### 2. Objetivo da Arquitetura de Software:
- Principal objetivo: Minimizar os recursos humanos necessários para construir e manter o sistema;
- Bom design: Facilita mudanças sem aumento exponencial de custos;
- Mau design: Custo de manutenção cresce a cada novo release;

### 3. Estudo de Caso: O Problema da Bagunça no Código:
- Crescimento da equipe não significa aumento de produtividade;
- Problema observado: Custo por linha de código aumentou 40 vezes entre o 1º e 8º release;
- Causa principal: Acúmulo de código mal estruturado;
- Consequência: Desenvolvedores gastam mais tempo corrigindo problemas do que adicionando funcionalidades;
- Gráficos mostram produtividade tendendo a zero com o tempo;

### 4. O Erro da Mentalidade "Depois a Gente Limpa":
- Mito comum: "Podemos escrever código rápido agora e arrumar depois";
- Realidade: A bagunça raramente é corrigida posteriormente;
- Experimento com TDD:

  * Dias usando Test-Driven Development foram 10% mais eficientes;
  * Até o dia mais lento com TDD foi mais rápido que o dia mais rápido sem TDD;
  
- Conclusão: Manter o código limpo desde o início é mais eficiente;

### 5. Os Dois Valores do Software:

5.1 Comportamento (Funcionalidade):

- O que o software deve fazer;
- Valor urgente, mas nem sempre o mais importante;

5.2 Arquitetura (Flexibilidade):

- Facilidade de realizar mudanças;
- Valor importante, mas frequentemente negligenciado;
- Prioridade: Arquitetura > Comportamento;
- Argumento: Um sistema flexível pode ser adaptado para novos requisitos;

### 6. Paradigmas de Programação:

6.1 Programação Estruturada (Dijkstra, 1968):

- Substitui GOTO por estruturas if/else e loops;
- Permite decomposição funcional;
- Base para testes eficazes;

6.2 Programação Orientada a Objetos (1966):

- Baseada em: Encapsulamento, Herança e Polimorfismo;
- Principal vantagem: Inversão de dependência;

6.3 Programação Funcional (Cálculo-λ, 1930):

- Princípio da imutabilidade;
- Disciplina na atribuição de valores;

### 7. O Poder do Polimorfismo:
- Permite inversão de dependência;
- Benefícios:

  * Regras de negócio independentes de UI e banco de dados;
  * Implantação independente de componentes;
  * Desenvolvimento paralelo por diferentes equipes;

### 8. Conclusões Principais:
- Princípio fundamental: "A única maneira de seguir rápido é seguir bem";
- Boa arquitetura permite:
  * Manutenção sustentável;
  * Adaptação a mudanças;
  * Redução de custos a longo prazo;
- Recomendações:
  * Evitar dívida técnica desde o início;
  * Adotar práticas como TDD;
  * Manter equilíbrio entre funcionalidade e estrutura;


## Dia 27

Livro - Arquitetura Limpa by Robert C. Martim

Capítulos do 6 ao 8:

CAPÍTULO 6: PROGRAMAÇÃO FUNCIONAL

- **Conceito Central: Imutabilidade**
  - Dados não são alterados após criação (variáveis não variam).
  - Evita problemas de concorrência: race conditions, deadlocks e atualizações concorrentes.

- **Benefícios Arquiteturais**
  - Sistemas robustos em ambientes multi-thread/multi-processador.
  - Previsibilidade e ausência de efeitos colaterais.

- **Estratégias Práticas**
  1. **Segregação de Mutabilidade**:
     - Dividir aplicação em componentes:
       * **Imutáveis**: Lógica puramente funcional (sem estado mutável).
       * **Mutáveis**: Gerenciam estado com proteção (ex: memória transacional).
  2. **Event Sourcing**:
     - Armazenar transações (eventos), não estado final.
     - Reconstruir estado aplicando eventos desde o início.
     - Vantagens: Elimina atualizações concorrentes e permite auditoria.

- **Conclusão do Paradigma**:
  - Restringe atribuição de variáveis, complementando OO e programação estruturada.


CAPÍTULO 7: SRP (PRINCÍPIO DA RESPONSABILIDADE ÚNICA)

- **Definição Corrigida**:
  - "Um módulo deve ser responsável por **um, e apenas um, ator**".
  - *Ator*: Grupo de stakeholders com mesma razão para mudança (ex: RH, Contabilidade).

- **Sintomas de Violação**:
  1. **Duplicação Acidental**:
     - Múltiplos atores compartilham código (ex: `Employee` com `calculatePay()` (CFO) e `reportHours()` (COO)).
     - Mudança para um ator quebra funcionalidade de outro.
  2. **Fusões em Código-Fonte**:
     - Múltiplas equipes alteram mesmo arquivo por motivos distintos.

- **Soluções**:
  1. **Separar Dados Das Funções**:
     - Criar classes distintas por ator (ex: `PayCalculator`, `HourReporter`).
  2. **Usar Padrão Facade**:
     - Classe `EmployeeFacade` coordena classes especializadas.
  3. **Manter Regras de Negócio Centralizadas**:
     - Classe principal delega para classes auxiliares.

- **Escopo do Princípio**:
  - Aplica-se a funções, classes, componentes e limites arquiteturais.

 
CAPÍTULO 8: OCP (PRINCÍPIO ABERTO/FECHADO)

- **Definição**:
  - Entidades devem ser **abertas para extensão**, mas **fechadas para modificação**.

- **Implementação**:
  - **Abstrações e Polimorfismo**:
    - Comportamentos variáveis são definidos em interfaces/classes abstratas.
    - Novas funcionalidades: novas implementações, sem alterar código existente.
  - **Exemplo Prático**:
    - Interface `PaymentProcessor` com implementações `CreditCardProcessor`, `PayPalProcessor`.

- **Benefícios**:
  - Extensibilidade sem refatoração constante.
  - Minimiza riscos de regressão em código existente.

- **Conclusão dos Princípios SOLID**:
  - Objetivo: Criar estruturas tolerantes a mudanças, compreensíveis e reutilizáveis.


## Dia 28

### Prefácio

Neste dia 28, aprofundamos conceitos importantes da orientação a objetos em Python, como herança, polimorfismo, mixins, tratamento de exceções, métodos mágicos e classes abstratas. Esses conceitos são fundamentais para criar código organizado, reutilizável e robusto.

## Resumo

A herança simples permite que uma classe filha herde atributos e métodos da classe pai, estabelecendo uma relação “é um”. Por exemplo, a classe `Cliente` herda de `Pessoa` e pode sobrescrever métodos para alterar seu comportamento:

````
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f'Pessoa: {self.nome}')

class Cliente(Pessoa):
    def falar(self):
        print(f'Cliente: {self.nome}')
````

Além disso, Python suporta herança múltipla, onde uma classe pode derivar de várias classes ao mesmo tempo. Isso exige cuidado com a ordem de resolução dos métodos (MRO), que pode ser consultada via ``Classe.mro()`` para garantir que os métodos sejam chamados na ordem correta e evitar ambiguidades.

O polimorfismo é a capacidade de diferentes classes implementarem o mesmo método com comportamentos distintos, permitindo que o código trate objetos diferentes de forma uniforme. Por exemplo, uma classe abstrata ``Notificacao`` define um método abstrato ``enviar`` que deve ser implementado pelas subclasses:

````
from abc import ABC, abstractmethod

class Notificacao(ABC):
    @abstractmethod
    def enviar(self):
        pass

class NotificacaoEmail(Notificacao):
    def enviar(self):
        print("Enviando e-mail")

class NotificacaoSMS(Notificacao):
    def enviar(self):
        print("Enviando SMS")
````

Para garantir que as chamadas aos métodos das superclasses respeitem a hierarquia correta, utilizamos ``super()``. Isso permite estender o comportamento das classes pai sem quebrar a cadeia de herança. Por exemplo:

````
class A:
    def metodo(self):
        print("Método A")

class B(A):
    def metodo(self):
        super().metodo()
        print("Método B")
````

Também aprendemos que é simples criar exceções personalizadas ao herdar da classe base ``Exception``, podendo relançar erros para preservar o histórico:

````
class MeuErro(Exception):
    pass

try:
    raise MeuErro("Erro customizado")
except MeuErro as e:
    print(f"Caught: {e}")
````

Além disso, métodos mágicos (``dunder methods``) como ``__repr__`` permitem controlar a forma como objetos são representados, facilitando debug e logs. Exemplo:

````
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Ponto(x={self.x}, y={self.y})'

p = Ponto(1, 2)
print(p)  # Saída: Ponto(x=1, y=2)
````

Por fim, os mixins são classes usadas para adicionar funcionalidades específicas, como logging, sem alterar a hierarquia principal das classes. Por exemplo, uma classe ``Smartphone`` pode herdar de ``Eletronico`` e incluir um mixin para registrar logs:

````
class LogMixin:
    def log(self, msg):
        print(f'LOG: {msg}')

class Eletronico:
    def __init__(self, nome):
        self.nome = nome

class Smartphone(Eletronico, LogMixin):
    def ligar(self):
        self.log(f'{self.nome} está ligado')
````

### Observações Finais:

Dominar herança múltipla e polimorfismo, entender o MRO e utilizar ``super()`` adequadamente são essenciais para evitar erros difíceis em sistemas complexos. Mixins e classes abstratas promovem código modular e contratos claros, enquanto exceções personalizadas melhoram o controle de erros. A prática desses conceitos aprimora muito a qualidade do código orientado a objetos em Python.



## Dia 29

### Prefácio:

Hoje exploramos conceitos que nos permitem ir além do uso básico da linguagem, adentrando o que meu professor decreveu como o "coração" da programação orientada a objetos e a manipulação de fluxo de controle de forma mais refinada. Compreender metaclasses, decoradores (com funções e classes), os métodos especiais ``__new__`` e ``__call__``, e os **gerenciadores de contexto** é fundamental para escrever códigos mais flexíveis, poderosos e Pythonicos. Esses tópicos, embora possam parecer complexos à primeira vista, são pilares para o desenvolvimento de frameworks e bibliotecas, e nos dão um controle granular sobre como nossos objetos e classes são criados e se comportam.

### Metaclasses: O Tipo das Classes:

Em Python, tudo é um objeto, e isso inclui as próprias classes. Se uma classe é um objeto, ela precisa ter um tipo, certo? Esse tipo é a metaclasse. A metaclasse padrão para todas as classes em Python é ``type``. Pense na metaclasse como a "fábrica" que cria suas classes. Ela permite que você intercepte o processo de criação de uma classe e modifique seu comportamento antes mesmo que qualquer instância seja criada.

O processo de criação de uma classe e suas instâncias é uma orquestra bem definida. Primeiro, o método ``__new__`` da metaclasse é chamado para criar a nova classe. Em seguida, o ``__call__`` da metaclasse entra em ação, que por sua vez chama o ``__new__`` da classe para criar a instância, e então o ``__init__`` da classe para inicializar essa instância.

````
def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'

class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234 # Adiciona um atributo à classe
        cls.__repr__ = meu_repr # Modifica o __repr__ da classe
        return cls

class Pessoa(metaclass=Meta):
    def __init__(self, nome):
        self.nome = nome

# Ao criar a classe Pessoa, a metaclasse Meta entra em ação.
# Pessoa já terá o atributo 'attr' e um __repr__ personalizado.
p1 = Pessoa('Luiz')
print(p1) # Saída: Pessoa({'nome': 'Luiz', 'attr': 1234})
````

### Métodos Especiais ``__new__`` e ``__init__``:
``__new__`` e ``__init__`` são métodos cruciais no ciclo de vida de um objeto em Python, mas com responsabilidades distintas. O método ``__new__`` é o responsável por criar e retornar o novo objeto (a instância da classe). Ele recebe a classe (``cls``) como primeiro argumento. Já o método ``__init__`` é responsável por inicializar a instância recém-criada, ou seja, configurar seus atributos. Ele recebe a própria instância (``self``) como primeiro argumento e, por convenção, não deve retornar nada.

````
class A:
    def __new__(cls, *args, **kwargs):
        print('Sou o new')
        # Cria e retorna a nova instância
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, x):
        print('Sou o init')
        self.x = x

a = A(123) # Primeiro 'Sou o new', depois 'Sou o init'
print(a.x) # Saída: 123
````

## O Método Especial ``__call__``:

O método especial ``__call__`` permite que as instâncias de uma classe se comportem como funções. Isso significa que você pode "chamar" um objeto como se fosse uma função, usando parênteses. Um objeto que pode ser chamado é conhecido como ``callable``.

````
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        return "Chamada efetuada!"

call1 = CallMe('123-4567')
retorno = call1('Maria') # Chama a instância como se fosse uma função
print(retorno) # Saída: Maria está chamando 123-4567 | Chamada efetuada!
````

### Decoradores: Funções e Classes:
Decoradores são uma forma poderosa e elegante de estender ou modificar o comportamento de funções ou classes sem alterar seu código-fonte. Eles são basicamente funções que recebem outra função (ou classe) como argumento e retornam uma nova função (ou classe) com o comportamento modificado.

Podemos criar decoradores usando funções ou classes.

#### Decoradores com Funções:
Um decorador de função geralmente é uma função que define uma função interna (ou wrapper) que executa a lógica adicional e, em seguida, chama a função original.

````
def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        if 'Terra' in resultado:
            return 'Você está em casa'
        return resultado
    return interno

class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta # Aplica o decorador meu_planeta ao método falar_nome
    def falar_nome(self):
        return f'O planeta é {self.nome}'

terra = Planeta('Terra')
marte = Planeta('Marte')

print(terra.falar_nome()) # Saída: Você está em casa
print(marte.falar_nome()) # Saída: O planeta é Marte
````

#### Decoradores com Classes:

Quando uma classe é usada como decorador, ela geralmente implementa o método ``__call__``, que é invocado quando a classe é usada como decorador.

````
class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna

@Multiplicar(2) # A classe Multiplicar é instanciada com 2, e seu __call__ é usado para decorar soma
def soma(x, y):
    return x + y

dois_mais_quatro = soma(2, 4) # (2 + 4) * 2 = 12
print(dois_mais_quatro) # Saída: 12`
````

### Gerenciadores de Contexto: ``with`` Statement:
**Gerenciadores de Contexto** são objetos que definem o comportamento de entrada (``__enter__``) e saída (``__exit__``) de um bloco de código, como o que vemos com o ``with`` statement. Eles são excelentes para gerenciar recursos (como arquivos, conexões de banco de dados, etc.) que precisam ser abertos e fechados de forma garantida, mesmo em caso de erros.

O Python utiliza o conceito de Duck Typing aqui: ele não se importa com o tipo específico do seu objeto, mas sim se ele implementa os métodos ``__enter__`` e ``__exit__``.

#### Gerenciadores de Contexto com Classes:
Para criar um gerenciador de contexto com uma classe, você precisa implementar os métodos ``__enter__`` e ``__exit__``. O ``__enter__`` retorna o recurso que será usado dentro do bloco with, e o ``__exit__`` é chamado quando o bloco ``with`` é finalizado, garantindo a liberação do recurso.

````
class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        if self._arquivo:
            self._arquivo.close()
        # Se você retornar True, qualquer exceção que ocorrer dentro do bloco with será suprimida.
        # return True # Descomente para suprimir exceções

with MyOpen('meu_arquivo.txt', 'w') as arquivo:
    arquivo.write('Olá, mundo!\n')
    print('Dentro do WITH') # Saída: Dentro do WITH
# Saída final: ABRINDO ARQUIVO | Dentro do WITH | FECHANDO ARQUIVO
````

### Gerenciadores de Contexto com Funções (usando ``contextlib``):
A biblioteca ``contextlib`` em Python oferece um decorador chamado ``@contextmanager`` que facilita a criação de gerenciadores de contexto usando funções geradoras. Você usa ``yield`` para entregar o recurso ao bloco ``with``, e o código após o ``yield`` será executado na saída do bloco.

````
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo # O arquivo é entregue ao bloco 'with'
    finally:
        print('Fechando arquivo')
        if arquivo:
            arquivo.close()

with my_open('outro_arquivo.txt', 'w') as arquivo:
    arquivo.write('Linha via função!\n')
    print('Com função:', arquivo)
# Saída final: Abrindo arquivo | Com função: <_io.TextIOWrapper name='outro_arquivo.txt' mode='w' encoding='utf8'> | Fechando arquivo
````

### Observações Finais:
A jornada através de metaclasses, decoradores e gerenciadores de contexto nos revela a profunda flexibilidade de Python. Esses recursos, embora avançados, são ferramentas poderosas que capacitam o desenvolvedor a escrever código mais limpo, modular e robusto. Entender como e quando usá-los pode elevar significativamente a qualidade e a manutenibilidade dos seus projetos. Meu professor meu deu de exemplo o conselho de Tim Peters: "se você se pergunta se precisa de metaclasses, provavelmente não precisa" – mas ter o conhecimento de sua existência e funcionalidade é um passo importante para se tornar um desenvolvedor Python mais completo.

## Dia 30

### Prefácio:

O dia 30 nos trouxe a oportunidade de aplicar e consolidar conceitos fundamentais da programação orientada a objetos (POO), como Abstração, Herança, Encapsulamento e Polimorfismo, através da construção de um sistema bancário simplificado. Além disso, introduzimos o uso de Enumerações (Enums), uma ferramenta elegante para lidar com conjuntos fixos de valores, que enriquece a clareza e a segurança do nosso código.

### Enumerações (Enums): Organizando Constantes:
**Enumerações** são coleções de nomes simbólicos (membros) ligados a valores únicos e constantes. Elas são ideais para  cenários onde você tem um número predefinido de opções para escolher, como dias da semana, status de um pedido ou, como no exemplo, direções. Em Python, a classe ``enum.Enum`` serve como superclasse para suas enumerações personalizadas, garantindo que os membros sejam iteráveis e permitindo o uso com type annotations e ``isinstance`` para verificação de tipo. O uso de ``enum.auto()`` facilita a atribuição automática de valores sequenciais aos membros.

````
import enum

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()

def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')
    print(f'Movendo para {direcao.name} ({direcao.value})')

mover(Direcoes.ESQUERDA) # Saída: Movendo para ESQUERDA (1)
````

### Sistema Bancário Simplificado: POO na Prática:
O exercício do sistema bancário demonstrou a aplicação prática de vários pilares da Programação Orientada a Objetos:

#### Abstração e Polimorfismo: A Classe ``Account``:
A classe ``Account`` (Conta) é uma classe abstrata (``ABC`` - Abstract Base Class), o que significa que ela não pode ser instanciada diretamente. Ela define o comportamento comum a todas as contas, como ``deposit`` (depositar) e ``show_info`` (mostrar informações), e um método abstrato ``draw_out`` (sacar), que deve ser implementado por suas subclasses. Isso garante o **polimorfismo**, onde diferentes tipos de conta (corrente e poupança) podem responder ao mesmo método ``draw_out`` de maneiras distintas.

````
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, agency: int, account: int, balance: float = 0) -> None:
        self.agency = agency
        self.account = account
        self.balance = balance

    def deposit(self, value: float) -> float:
        self.balance += value
        return self.balance

    @abstractmethod
    def draw_out(self, value: float) -> float: ...

# As classes CurrentAccount e SavingsAccount implementariam 'draw_out'
````

#### Herança: ``CurrentAccount`` e ``SavingsAccount``:
As classes ``CurrentAccount`` (Conta Corrente) e ``SavingsAccount`` (Conta Poupança) **herdam** da classe ``Account``. A ``CurrentAccount`` estende o comportamento da ``Account`` adicionando um ``limit`` (limite) extra para saques. Ambas as subclasses fornecem sua própria implementação concreta do método ``draw_out``, demonstrando como o polimorfismo funciona na prática, com regras diferentes para saque em cada tipo de conta.

````
class CurrentAccount(Account):
    def __init__(self, agency: int, account: int, balance: float = 0, limit: float = 0):
        super().__init__(agency, account, balance)
        self.limit = limit

    def draw_out(self, value: float) -> float:
        # Lógica de saque para conta corrente com limite
        if (self.balance - value) >= self.limit: # Correção: deveria ser self.balance + self.limit
            self.balance -= value
            print(f'Sacando {value} na conta corrente.')
        else:
            print('Saldo e limite insuficientes.')
        return self.balance
````

#### Encapsulamento: Propriedades em ``People``:
A classe ``People`` (Pessoa) utiliza **encapsulamento** através de ``@property`` para controlar o acesso e a modificação dos atributos ``name`` (nome) e ``age`` (idade). Embora os setters no exemplo dado não contenham lógica de validação complexa, eles ilustram o padrão para adicionar tal lógica quando necessário, protegendo a integridade dos dados.

````
class People():
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name # Exemplo de encapsulamento
````

#### Agregação: ``Client`` e ``Bank``:
A classe ``Client`` (Cliente) demonstra **agregação** ao "ter" uma ``Account``. Isso significa que um cliente está associado a uma conta, mas a vida útil da conta não depende diretamente da vida útil do cliente. Similarmente, a classe ``Bank`` (Banco) agrega tanto ``Client`` quanto ``Accounts``. O banco é responsável por gerenciar e autenticar clientes e contas, verificando se a agência, o cliente e a conta pertencem ao banco antes de permitir operações como saques.

````
class Client(People):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account = None # Cliente TEM uma conta (agregação)

class Bank():
    def __init__(self, agencies: list[int] | None = None,
                 clients: list[People] | None = None,
                 accounts: list[Account] | None = None):
        self.agencies = agencies or []
        self.clients = clients or []
        self.accounts = accounts or []

    def authenticate(self, client: Client, account: Account):
        # Lógica de autenticação do banco
        return self._check_agency(account) and \
               self._check_client(client) and \
               self._check_account(account) and \
               self._check_client_accont(client, account)

# Exemplo de uso no main.py e accounts_.py:
# c1 = Client('Luiz', 30)
# cc1 = CurrentAccount(111, 222, 0, 0)
# c1.account = cc1
# banco = Bank()
# banco.clients.append(c1)
# banco.accounts.append(cc1)
# banco.agencies.append(111)
# if banco.authenticate(c1, cc1):
#     cc1.deposit(100)
#     print(c1.account)`
````

### Documentação de Código: Docstrings:
A documentação é uma parte essencial do desenvolvimento de software, e Python oferece docstrings como uma maneira padrão de documentar módulos, classes, funções e métodos. As docstrings são strings literais que aparecem como o primeiro enunciado em uma definição de módulo, classe ou função. Elas são acessíveis em tempo de execução através do atributo ``__doc__`` do objeto e são usadas por ferramentas como ``help()``.

#### Docstrings de Módulo:
As docstrings no nível do módulo descrevem o propósito geral do arquivo.

````
"""O que seu módulo faz""" # Exemplo de docstring de módulo em uma_linha.py

# ou com várias linhas:
"""O que seu módulo faz
Lorem ipsum dolor sit amet. Et praesentium nisi non quam mollitia At saepe
quisquam qui quae voluptatem.
""" # Exemplo de docstring de módulo em varias_linhas.py
````

#### Docstrings de Funções e Métodos:
As docstrings para funções e métodos descrevem o que a função faz, seus parâmetros (``:param``), seus tipos (``:type``), o valor de retorno (``:return``), o tipo de retorno (``:rtype``), e possíveis exceções que podem ser levantadas (``:raises``).

````
def soma(x: int | float, y: int | float) -> int | float:
    """Soma x e y

    Este módulo contém funções e exemplos de documentação de funções.
    A função soma você já conhece bastante.

    :param x: Número 1
    :type x: int or float
    :param y: Número 2
    :type y: int or float

    :return: A soma entre x e y
    :rtype: int or float
    """
    return x + y

def bar() -> int:
    """O que ele faz
    
    :raises  NotIMplementedError: se o método não for definido
    :raises ValueError:  Se  o método não for defiinido
    """
    raise NotImplementedError('Teste')
````

#### Docstrings de Classes:
As docstrings de classes descrevem o propósito da classe.

````
class Foo:
    """Este é um módulo de exemplo""" # Exemplo de docstring de classe em classes.py

    """
    Este módulo contém funções e exemplos de documentação de funções.
    A função soma você já conhece bastante.
    """
    # ... métodos
````

### Observações Finais:

Os exercícios do dia 29 foram cruciais para solidificar a compreensão dos paradigmas de POO em Python. Ao construir o sistema bancário, não apenas vimos Abstração, Herança, Encapsulamento e Polimorfismo em ação, mas também a importância da organização do código em módulos separados (``accounts_.py`` e ``main.py``). O uso de Enumerações, por sua vez, complementou essa estrutura, mostrando como podemos tornar nosso código mais legível e menos propenso a erros ao lidar com conjuntos fixos de valores. A prática com esses conceitos é fundamental para o desenvolvimento de sistemas complexos e bem estruturados.


## Dia 31

### Prefácio:

Hoje apredi ferramentas poderosas para a criação de classes mais concisas e eficientes, além de aprofundar nossa compreensão sobre a interação com coleções. Exploramos as **dataclasses**, um "açúcar sintático" que simplifica a criação de classes de dados; as **namedtuples**, que oferecem tuplas com campos nomeados para maior clareza; e a implementação de **protocolos de iteradores** usando o módulo ``collections.abc``, permitindo que nossas estruturas de dados personalizadas se comportem como tipos built-in do Python.

### Dataclasses: Simplificando Classes de Dados:

**Dataclasses** são uma adição ao Python (PEP 557, a partir da versão 3.7) que fornecem um decorador e funções para gerar automaticamente métodos comuns como ``__init__()``, ``__repr__()``, ``__eq__()`` e outros. Essencialmente, elas são um "açúcar sintático" para criar classes que servem principalmente para armazenar dados.

### Criação e Uso Básico:
Ao usar o decorador ``@dataclass``, você pode definir atributos de classe com anotações de tipo, e o Python cuidará da geração dos métodos Dunder automaticamente.

````
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

p1 = Pessoa('Luiz', 'Otávio')
print(p1) # Saída: Pessoa(nome='Luiz', sobrenome='Otávio')
````

### Configurações de Dataclasses e ``__post_init__``:
As dataclasses podem ser configuradas com argumentos no decorador ``@dataclass``, como ``repr=True`` para controlar a representação da classe. Além disso, o método mágico ``__post_init__`` pode ser implementado para executar lógica de inicialização adicional após a criação do objeto pelos métodos gerados pela dataclass.

````
from dataclasses import dataclass

@dataclass(repr=True) # repr=True é o padrão, mas demonstra a configuração
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        print('POST INIT EXECUTADO') # Exemplo de lógica pós-inicialização

p1 = Pessoa('Ana', 'Silva') # Saída: POST INIT EXECUTADO | Pessoa(nome='Ana', sobrenome='Silva')
print(p1)
````

### Manipulando Atributos com ``field``:
O módulo ``dataclasses`` também oferece a função ``field`` para configurações mais granulares dos atributos. Com ``field``, é possível definir valores padrão, controlar se o atributo aparece no ``repr``, e usar ``default_factory`` para valores padrão mutáveis (como listas), evitando problemas de referência.

````
from dataclasses import dataclass, field

@dataclass
class Produto:
    nome: str = field(default='Sem Nome', repr=True) # Valor padrão e inclusão no repr
    tags: list[str] = field(default_factory=list) # Uso de default_factory para listas

p1 = Produto(nome='Livro')
p1.tags.append('ficção')
p2 = Produto()
print(p1) # Saída: Produto(nome='Livro', tags=['ficção'])
print(p2) # Saída: Produto(nome='Sem Nome', tags=[])
````

### ``asdict`` e ``astuple``:

As funções ``asdict`` e ``astuple`` do módulo ``dataclasses`` permitem converter instâncias de dataclasses para dicionários e tuplas, respectivamente, facilitando a manipulação dos dados.

````
from dataclasses import asdict, astuple, dataclass

@dataclass
class Coordenada:
    x: int
    y: int

c = Coordenada(10, 20)
print(asdict(c)) # Saída: {'x': 10, 'y': 20}
print(astuple(c)) # Saída: (10, 20)
````

### Namedtuples: Tuplas com Nomes para Valores:
As **namedtuples** (tuplas nomeadas) são tuplas imutáveis que permitem acessar seus elementos por nomes de atributos, além de índices, tornando o código mais legível. Elas são ideais para criar objetos que são apenas um agrupamento de atributos, sem a necessidade de métodos complexos, funcionando como registros de dados. ``collections.namedtuple`` e ``typing.NamedTuple`` são as formas de criá-las.

````
from typing import NamedTuple

class Carta(NamedTuple):
    valor: str
    naipe: str = 'Copas' # Atributo com valor padrão

as_copas = Carta('A')
print(as_copas.valor) # Saída: A
print(as_copas.naipe) # Saída: Copas
print(as_copas[0])    # Saída: A
print(as_copas._asdict()) # Converte para dicionário
````

### Protocolos de Iteradores: ``collections.abc``:
O módulo ``collections.abc`` (Abstract Base Classes) fornece classes abstratas que definem os "protocolos" para diferentes tipos de coleções, como ``Sequence``, ``Mapping``, ``Set``, ``Iterator``, etc.. Ao herdar dessas ABCs e implementar seus métodos abstratos, suas classes personalizadas podem se comportar como os tipos built-in correspondentes, permitindo que funcionem com funções e construções Python que esperam esses protocolos (como for loops, ``len()``, ``[]`` para acesso por índice).

Para criar um iterador personalizado, é necessário implementar os métodos ``__iter__`` (que retorna o próprio iterador) e ``__next__`` (que retorna o próximo item da iteração e levanta ``StopIteration`` quando não há mais itens).

````
from collections.abc import Sequence

class MyList(Sequence): # Herda de Sequence para implementar protocolo de sequência
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self) -> int:
        return self._index # Implementa o método len()

    def __getitem__(self, index):
        return self._data[index] # Permite acesso por índice

    def __iter__(self):
        self._next_index = 0 # Reinicia o índice para nova iteração
        return self # Retorna o próprio objeto como iterador

    def __next__(self):
        if self._next_index >= self._index:
            raise StopIteration # Sinaliza o fim da iteração
        value = self._data[self._next_index]
        self._next_index += 1
        return value # Retorna o próximo item

lista = MyList()
lista.append('Banana', 'Maçã', 'Uva')
for item in lista:
    print(item) # Saída: Banana, Maçã, Uva (cada um em uma linha)
print(len(lista)) # Saída: 3
print(lista[1]) # Saída: Maçã
````

### Observações Finais:
A imersão em dataclasses, namedtuples e protocolos de coleções nos oferece ferramentas valiosas para escrever código Python mais limpo, eficiente e robusto. As dataclasses e namedtuples simplificam a criação de classes de dados, reduzindo o código boilerplate e aumentando a legibilidade. A compreensão e implementação dos protocolos de ``collections.abc`` nos permitem criar estruturas de dados personalizadas que se integram perfeitamente com o ecossistema Python, comportando-se de maneira previsível e familiar. Esses conceitos são fundamentais para desenvolver aplicações Pythonicas de alta qualidade e escaláveis.

## Dia 32

### Prefácio:

Hoje concentramos nossos esforços em duas ferramentas para o desenvolvimento de aplicações robustas: a **manipulação de datas e calendários** e a **modularização do código**. A capacidade de gerenciar e calcular datas com precisão é vital para uma infinidade de sistemas, desde agendamentos até cálculos financeiros. Complementarmente, a modularização nos permite organizar nosso código de forma lógica e reutilizável, facilitando a colaboração e a manutenção de projetos maiores.

### Manipulação de Datas e Horas com ``datetime`` e ``calendar``:
Python oferece módulos poderosos para trabalhar com datas e horas, sendo ``datetime`` e ``calendar`` os mais proeminentes.

#### Criando e Formatando Datas com ``datetime``:

O módulo ``datetime`` permite a criação de objetos que representam datas e horas com alta precisão. Podemos criar um ``datetime`` a partir de valores numéricos ou converter strings formatadas em objetos ``datetime`` usando ``strptime``. Para exibir datas e horas em formatos específicos, utilizamos ``strftime``. O ``timestamp`` também é uma forma de representar datas como um número único, que pode ser convertido de volta para ``datetime``.

````
from datetime import datetime

# Criando um objeto datetime
data_atual = datetime.now()
print(f"Data e Hora Atual: {data_atual}") # Ex: 2025-07-11 20:14:06.123456

# Convertendo string para datetime
data_str = '2022-12-13 07:59:23'
data_obj = datetime.strptime(data_str, '%Y-%m-%d %H:%M:%S')
print(f"Data de String: {data_obj.strftime('%d/%m/%Y %H:%M:%S')}") # Saída: 13/12/2022 07:59:23
````

#### Calculando Diferenças com ``timedelta`` e ``relativedelta``:

Para realizar operações com datas, como adicionar ou subtrair períodos, o ``datetime`` oferece ``timedelta``. Para cálculos mais complexos, como adicionar meses ou anos de forma flexível (considerando o número de dias em cada mês, por exemplo), a biblioteca ``dateutil`` e seu ``relativedelta`` são extremamente úteis, lidando com nuances que ``timedelta`` não cobre diretamente.

````
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

data_inicio = datetime(2020, 1, 15)
data_fim = datetime(2020, 3, 15)

# Calculando diferença com timedelta
diferenca_dias = data_fim - data_inicio
print(f"Diferença em dias: {diferenca_dias.days}") # Saída: 60

# Adicionando um mês com relativedelta (mais preciso para meses/anos)
um_mes_depois = data_inicio + relativedelta(months=1)
print(f"Um mês depois: {um_mes_depois.strftime('%d/%m/%Y')}") # Saída: 15/02/2020 (considera o número de dias de janeiro)

# Exemplo prático: Cálculo de parcelas de empréstimo
valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos
# ... lógica para calcular parcelas iterando com relativedelta(months=+1)
````

#### Usando o Módulo ``calendar``:
O módulo ``calendar`` é projetado para lidar com tarefas de calendário em geral, permitindo verificar o último dia do mês, o dia da semana de uma data específica, ou até mesmo gerar calendários completos. Ele é útil para exibir informações de calendário ou para lógica que dependa da estrutura do calendário.

````
import calendar

# Retorna o número do dia da semana (0=segunda-feira, 6=domingo)
dia_da_semana = calendar.weekday(2025, 7, 11)
print(f"11/07/2025 é um(a) {calendar.day_name[dia_da_semana]}") # Saída: 11/07/2025 é um(a) Friday

# Obtendo o último dia de um mês
primeiro_dia_mes, ultimo_dia_mes = calendar.monthrange(2025, 7)
print(f"Último dia de Julho/2025: {ultimo_dia_mes}") # Saída: 31
````

### Modularização: Organizando o Código:

A modularização é a prática de dividir um programa em partes menores e independentes, chamadas módulos. Cada módulo pode conter funções, classes e variáveis relacionadas a uma tarefa específica. Isso promove a reutilização de código, melhora a legibilidade e facilita a manutenção de projetos grandes.

#### Importando Módulos:

Em Python, podemos importar módulos inteiros ou partes específicas de módulos usando as declarações ``import`` ou ``from ... import.``

````
# modulo.py
def soma(x: float, y: float) -> float:
    return x + y

# app.py
from modulo import soma # Importa apenas a função 'soma' do módulo 'modulo'

resultado = soma(4, 2)
print(resultado) # Saída: 6
````

### O Bloco ``if __name__ == '__main__':``:
Este bloco é uma construção comum em Python que permite que o código dentro dele seja executado somente quando o script é executado diretamente, e não quando é importado como um módulo em outro script. É uma prática recomendada para incluir código de teste ou de inicialização que não deve ser executado automaticamente ao importar o módulo.

````
# modulo.py
def soma(x: float, y: float) -> float:
    return x + y

if __name__ == '__main__':
    # Este código só será executado se 'modulo.py' for o script principal
    print("Executando como script principal em modulo.py")
    print(soma(10, 30)) # Saída: 40
````

### Observações Finais:

A maestria dos módulos ``datetime`` e ``calendar`` é indispensável para qualquer aplicação que envolva agendamentos, logs ou cálculos baseados em tempo. Simultaneamente, a compreensão e aplicação da modularização através de importações e do bloco ``if __name__ == '__main__':`` são cruciais para escrever código Python limpo, organizado, reutilizável e, acima de tudo, manutenível em projetos de qualquer escala.