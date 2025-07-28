## Dia 18: Funções Lambda

### Prefácio:

Hoje exploramos as **funções lambda** em Python, uma ferramenta concisa e poderosa para criar funções anônimas de uma única linha. Compreendemos sua sintaxe, seus casos de uso ideais e como elas se relacionam com conceitos como funções de ordem superior e a ordenação de iteráveis.

### Introdução à Função Lambda:

Uma **função lambda** é uma função anônima (sem nome) e de uma única linha em Python. Ela é definida usando a palavra-chave ``lambda`` e é ideal para tarefas simples e rápidas onde uma função ``def`` completa seria excessiva. [cite: uploaded:introducao_funcao_lambda.py]

- **Sintaxe**: ``lambda argumentos: expressão``

    - ``argumentos``: Parâmetros que a função lambda recebe.

    - ``expressão``: O corpo da função, que é avaliado e retornado. Tudo deve estar contido em uma única expressão.

````
# Exemplo 1: Lambda simples para somar dois números
soma_lambda = lambda x, y: x + y
print(soma_lambda(2, 3)) # Saída: 5

# Exemplo 2: Lambda para verificar se um número é par
eh_par_lambda = lambda num: num % 2 == 0
print(eh_par_lambda(4)) # Saída: True
print(eh_par_lambda(7)) # Saída: False
````

### Casos de Uso Comuns para Lambda:

As funções lambda são frequentemente usadas como argumentos para funções de ordem superior que esperam uma função como parâmetro, como ``sorted()``, ``map()``, ``filter()`` e ``reduce()``.

-  **``sorted()`` com ``key``**: A função ``sorted()`` retorna uma nova lista ordenada a partir de um iterável. O parâmetro ``key`` aceita uma função (muitas vezes uma lambda) para definir o critério de ordenação.

````
# Exemplo 3: Ordenando uma lista de dicionários usando lambda como key
lista_pessoas = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# Ordena por nome
lista_por_nome = sorted(lista_pessoas, key=lambda item: item['nome'])
# Ordena por sobrenome
lista_por_sobrenome = sorted(lista_pessoas, key=lambda item: item['sobrenome'])

def exibir_lista(lista):
    for item in lista:
        print(item)
    print()

print("Ordenado por nome:")
exibir_lista(lista_por_nome)

print("Ordenado por sobrenome:")
exibir_lista(lista_por_sobrenome)
````
### Lambda e Funções de Ordem Superior:

As lambdas se encaixam perfeitamente no conceito de funções de ordem superior, que são funções que podem receber outras funções como argumentos ou retornar funções.
````
# Exemplo 4: Lambda como argumento para uma função de ordem superior
def executa(funcao, *args): # Função que recebe outra função e seus argumentos
    return funcao(*args)

# Usando lambda para somar
resultado_soma = executa(lambda x, y: x + y, 10, 5)
print(f'Resultado da soma com lambda: {resultado_soma}') # Saída: 15

# Usando lambda para multiplicar
resultado_multiplicacao = executa(lambda a, b: a * b, 4, 6)
print(f'Resultado da multiplicação com lambda: {resultado_multiplicacao}') # Saída: 24
````

### Lambdas Complexas e Cuidados:

Embora lambdas sejam concisas, elas devem ser usadas para expressões simples. Tentar criar lógicas muito complexas dentro de uma lambda pode prejudicar a legibilidade do código. Nesses casos, uma função ``def`` tradicional é mais apropriada.

````
# Exemplo 5: Lambda complexa (evitar para melhor legibilidade)
# Esta lambda cria e retorna outra lambda
multiplicador_lambda = executa(
    lambda m: lambda n: n * m, # Lambda externa que retorna uma lambda interna
    2 # Argumento 'm' para a lambda externa
)
print(multiplicador_lambda(5)) # Chama a lambda interna com 'n=5'. Saída: 10

# Exemplo 6: Soma de múltiplos argumentos com lambda (ainda legível para casos simples)
soma_args_lambda = executa(
    lambda *args: sum(args), # Lambda que empacota argumentos em uma tupla e os soma
    1, 2, 3, 4, 5
)
print(f'Soma de vários argumentos com lambda: {soma_args_lambda}') # Saída: 15
````

### Observações Finais:

As funções lambda são uma adição valiosa ao conjunto de ferramentas de qualquer programador Python. Elas promovem um estilo de codificação mais funcional e conciso para tarefas específicas. No entanto, é crucial usá-las com discernimento: para lógicas simples e como argumentos de funções de ordem superior, elas brilham; para complexidade maior, as funções ``def`` tradicionais mantêm a clareza e a manutenibilidade do código. A prática em cenários como ordenação personalizada e transformações de dados ajudará a dominar o uso eficaz das lambdas.