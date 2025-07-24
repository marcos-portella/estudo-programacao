## Dia 16

### Prefácio:

Hoje demos um passo fundamental no mundo da programação funcional em Python, introduzindo o conceito de **funções**. Aprendemos a definir e utilizar funções para organizar o código, torná-lo reutilizável e mais legível. Exploramos diferentes tipos de argumentos (nomeados e não nomeados), valores padrão, o retorno de valores, o escopo de variáveis e o poderoso conceito de closures e funções de ordem superior.

### Introdução às Funções (def):

Funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas ajudam a dividir programas complexos em partes menores e gerenciáveis, promovendo a modularidade e a legibilidade.

- **Definição**: Funções são definidas usando a palavra-chave ``def``, seguida pelo nome da função, parênteses ``()`` para argumentos e dois pontos ``:``. O corpo da função é indentado. [cite: uploaded:def_introducao_funcao.py]

- **Reutilização**: Uma vez definida, uma função pode ser chamada múltiplas vezes.

- **Retorno de Valor**: Por padrão, funções Python retornam ``None`` (nada). A palavra-chave ``return`` é usada para especificar um valor de retorno. [cite: uploaded:retorno_funcao.py]

````
# Exemplo 1: Função simples de saudação
def saudacao(nome='Sem nome'): # Parâmetro com valor padrão
    print(f'Olá {nome}')

saudacao('Luiz Otávio') # Chamada da função com argumento
saudacao() # Chamada da função sem argumento, usando o valor padrão
````

### Argumentos e Parâmetros:

- Argumentos Nomeados e Não Nomeados:

    - **Não nomeados (posicionais)**: Os argumentos são passados na ordem em que os parâmetros são definidos na função.

    - **Nomeados**: Os argumentos são passados usando o nome do parâmetro seguido de ``=``. Isso permite passar argumentos em qualquer ordem. [cite: uploaded:argumentos_nomeados.py]

````
# Exemplo 2: Argumentos nomeados e não nomeados
def soma(x, y, z):
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

soma(1, 2, 3) # Argumentos não nomeados
soma(1, y=2, z=5) # Argumentos nomeados para y e z
soma(z=5, x=1, y=2) # Ordem dos argumentos nomeados não importa
````

- **Valores Padrão para Parâmetros**: Parâmetros podem ter valores padrão. Se um valor não for fornecido para esse parâmetro na chamada da função, o valor padrão será utilizado. [cite: uploaded:valores_padrao.py]

````
# Exemplo 3: Parâmetros com valores padrão
def soma_com_padrao(x, y, z=None): # z tem um valor padrão de None
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma_com_padrao(1, 2) # z usa o valor padrão (None)
soma_com_padrao(7, 9, 0) # z recebe o valor 0
````

- **``*args`` (Argumentos Não Nomeados Variáveis)**: O ``*args`` permite que uma função aceite um número variável de argumentos não nomeados. Esses argumentos são empacotados em uma tupla dentro da função. [cite: uploaded:asteriscoargs.py]

````
# Exemplo 4: Usando *args para somar múltiplos números
def soma_varios_numeros(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(soma_varios_numeros(1, 2, 3)) # Saída: 6
print(soma_varios_numeros(4, 5, 6, 7, 8)) # Saída: 30

numeros_lista = [10, 20, 30]
print(soma_varios_numeros(*numeros_lista)) # Desempacota a lista para a função
````

### Escopo de Funções:

O escopo define onde uma variável ou nome pode ser acessado no código.

- **Escopo Global**: Variáveis definidas fora de qualquer função são globais e podem ser acessadas de qualquer lugar no programa.

- **Escopo Local**: Variáveis definidas dentro de uma função são locais a essa função e só podem ser acessadas dentro dela. Se uma variável local tiver o mesmo nome de uma global, a local terá precedência dentro da função. [cite: uploaded:escopo_funcao_modulos_python_global.py]

````
# Exemplo 5: Escopo de variáveis
x = 10 # Variável global

def minha_funcao():
    y = 20 # Variável local
    print(f'Dentro da função: x={x}, y={y}') # Acessa x global e y local

minha_funcao()
print(f'Fora da função: x={x}')
# print(y) # Isso geraria um erro, pois 'y' está fora do escopo
````

### Funções de Primeira Classe e Closures:

- **Funções de Primeira Classe**: Em Python, funções são "cidadãos de primeira classe", o que significa que podem ser tratadas como qualquer outra variável: passadas como argumentos, retornadas de outras funções e atribuídas a variáveis. [cite: uploaded:higher_order_functions.py]

- **Closures**: Uma closure ocorre quando uma função interna "lembra" e tem acesso a variáveis de seu escopo externo (o escopo da função onde ela foi definida), mesmo depois que a função externa já terminou sua execução. [cite: uploaded:closure_and_functions.py]

````
# Exemplo 6: Funções de primeira classe e closure
def criar_multiplicador(multiplicador): # Função externa
    def multiplicar(numero): # Função interna (closure)
        return numero * multiplicador # 'multiplicador' é lembrado do escopo externo
    return multiplicar

duplicar = criar_multiplicador(2) # 'duplicar' é uma função que multiplica por 2
triplicar = criar_multiplicador(3) # 'triplicar' é uma função que multiplica por 3

print(duplicar(5)) # Saída: 10
print(triplicar(5)) # Saída: 15
````

### Observações Finais:

As funções são o alicerce da programação estruturada e modular em Python. Dominar sua definição, o uso de argumentos (posicionais, nomeados, ``*args``), o retorno de valores e a compreensão do escopo são habilidades essenciais. Conceitos mais avançados como funções de primeira classe e closures abrem portas para padrões de design mais flexíveis e poderosos. A prática constante na criação e utilização de funções em seus projetos é a chave para escrever código limpo, eficiente e escalável.