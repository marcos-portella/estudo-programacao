## Dia 12

### Prefácio:

Este dia foi dedicado a explorar as poderosas **estruturas de repetição**, com foco principal no laço ``while``. Aprendemos a executar blocos de código repetidamente enquanto uma condição for verdadeira, controlando o fluxo com as palavras-chave ``continue`` e ``break``, e até mesmo aninhando loops. Complementarmente, aprofundamos nos **operadores de atribuição**, que oferecem uma forma mais concisa de realizar operações e atualizar variáveis.

### Estruturas de Repetição: O Loop while:

O ``while`` é uma estrutura de controle que permite executar um bloco de código repetidamente enquanto uma determinada condição for avaliada como ``True``. É essencial para automatizar tarefas e criar interações contínuas.

- **Condição e Loop Infinito**: É crucial que a condição do ``while`` eventualmente se torne ``False`` para que o loop termine. Caso contrário, teremos um "loop infinito", que consumirá recursos e não permitirá que o programa continue.

````
# Exemplo 1: Loop while com contador
contador = 0
while contador < 5:
    print(contador)
    contador += 1 # Garante que a condição eventualmente se torne False
print('Contagem finalizada!') #

# Exemplo 2: Loop while controlado por entrada do usuário
condicao = True
while condicao:
    nome = input('Qual o seu nome? (Digite "sair" para finalizar): ')
    if nome == 'sair':
        condicao = False # Altera a condição para encerrar o loop
    else:
        print(f'Seu nome é {nome}')
print('Programa encerrado.')
````

### Controlando o Fluxo do ``while``: ``continue`` e ``break``:

Dentro de um loop ``while``, podemos usar duas palavras-chave para controlar seu fluxo de execução de forma mais granular:

- ``continue``: Pula o restante do bloco de código na iteração atual e avança para a próxima iteração do loop, reavaliando a condição do ``while``.

- ``break``: Encerra o loop completamente, saindo do bloco ``while`` e continuando a execução do código logo após o loop.

````
# Exemplo 3: Uso de continue e break em um loop
contador = 0
while contador <= 10:
    contador += 1

    if contador == 5:
        print('Pulando o 5.')
        continue # Pula para a próxima iteração

    if contador == 8:
        print('Encerrando no 8.')
        break # Sai do loop completamente

    print(contador)
print('Loop finalizado.') 
````

### Loops ``while`` Aninhados:

É possível ter um loop ``while`` dentro de outro loop ``while``, criando uma estrutura aninhada. Isso é útil para iterar sobre múltiplas dimensões, como linhas e colunas em uma matriz, ou para realizar tarefas repetitivas dentro de outras repetições.

````
# Exemplo 4: Loops while aninhados
qtd_linhas = 3
qtd_colunas = 3

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'Linha {linha}, Coluna {coluna}')
        coluna += 1
    linha += 1
print('Tabela gerada.') 
````

### Operadores de Atribuição:

Os operadores de atribuição são atalhos para realizar uma operação aritmética (ou de outra natureza) e atribuir o resultado de volta à variável, tornando o código mais conciso e legível.

- ``=``: Atribuição simples.

- ``+=``: Adição e atribuição (ex: ``x += y`` é o mesmo que ``x = x + y``).

- ``-=``: Subtração e atribuição.

- ``*=``: Multiplicação e atribuição.

- ``/=``: Divisão e atribuição.

- ``//=``: Divisão inteira e atribuição.

- ``**=``: Exponenciação e atribuição.

- ``%=``: Módulo e atribuição.

````
# Exemplo 5: Uso de operadores de atribuição
x = 10
x += 5  # x agora é 15 (10 + 5)
print(f'x depois de +=: {x}')

y = 20
y -= 3  # y agora é 17 (20 - 3)
print(f'y depois de -=: {y}')

s = 'Olá'
s += ' Mundo' # s agora é 'Olá Mundo' (concatenação)
print(f's depois de +=: {s}')

z = 2
z **= 3 # z agora é 8 (2 elevado a 3)
print(f'z depois de **=: {z}')
````

### Observações Finais:

O domínio dos loops ``while`` é essencial para qualquer tarefa que envolva repetição e iteração. A capacidade de controlar o fluxo com ``continue`` e ``break``, e de aninhar loops, oferece grande flexibilidade. Combinado com os operadores de atribuição, que tornam o código mais compacto e expressivo, você tem ferramentas poderosas para construir programas eficientes e limpos. Continue praticando a aplicação desses conceitos em diferentes cenários para solidificar seu aprendizado.