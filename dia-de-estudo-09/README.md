## Dia 9

### Prefácio:

Dominar o fatiamento de strings e a função ``len()`` é fundamental para manipular e extrair partes específicas de textos em Python, bem como para obter o tamanho de sequências de caracteres. Essas ferramentas são cruciais para o processamento de texto e a validação de entradas.

### Fatiamento de Strings:

O fatiamento permite extrair um subconjunto de caracteres de uma string, utilizando uma sintaxe específica. Strings em Python são sequências ordenadas, e seus caracteres podem ser acessados por índices.

- **Sintaxe básica**: ``[início:fim:passo]``.

    - ``início``: O índice de onde o fatiamento começa (inclusivo). Se omitido, começa do início da string (índice 0).

    - ``fim``: O índice de onde o fatiamento termina (exclusivo). Se omitido, vai até o final da string.

    - ``passo``: O incremento entre os caracteres. Se omitido, o passo padrão é 1. Um passo negativo inverte a string ou a seleção.

- **Índices Positivos e Negativos**:

    - **Positivos**: Começam em ``0`` para o primeiro caractere e aumentam da esquerda para a direita.

    - **Negativos**: Começam em ``-1`` para o último caractere e diminuem da direita para a esquerda.

````
variavel = 'Olá mundo'

print(variavel[4:])       # Saída: 'mundo' (do índice 4 até o final)
print(variavel[:5])       # Saída: 'Olá m' (do início até o índice 5, exclusivo)
print(variavel[4:6])      # Saída: 'mu' (do índice 4 até o índice 6, exclusivo)
print(variavel[::2])      # Saída: 'Oámd' (do início ao fim, com passo de 2)
print(variavel[::-1])     # Saída: 'odnum álO' (inverte a string)
````

### Função ``len()``:

A função ``len()`` retorna o número de caracteres (o comprimento) de uma string ou de qualquer outra sequência.

````
variavel = 'Olá mundo'

print(len(variavel))        # Saída: 9 (o número total de caracteres)
print(len(variavel[0:3]))   # Saída: 3 (o número de caracteres na fatia 'Olá')
````

#### Uso em Exercícios Práticos:

O fatiamento e ``len()`` são frequentemente combinados com a entrada do usuário e estruturas condicionais para criar lógicas mais robustas. Por exemplo, para verificar se um campo foi preenchido ou para exibir informações formatadas sobre o nome do usuário.

````
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade: # Verifica se ambos os campos foram preenchidos
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}') # Usa fatiamento para inverter o nome
    if ' ' in nome: # Verifica se o nome contém espaços
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')
    print(f'Seu nome tem {len(nome)} letras') # Usa len() para contar as letras
    print(f'A primeira letra do seu nome é {nome[0]}') # Acessa o primeiro caractere
    print(f'A última letra do seu nome é {nome[-1]}') # Acessa o último caractere
else:
    print("Desculpe, você deixou campos vazios.")`
````

### Observações Finais:

O fatiamento de strings e a função len() são ferramentas poderosas no arsenal de um desenvolvedor Python, especialmente ao lidar com dados textuais. A capacidade de extrair partes específicas de uma string e de saber seu comprimento é crucial para tarefas como validação de entrada, formatação de saída e manipulação de texto. A prática contínua com diferentes cenários de fatiamento e a integração dessas funções com lógica condicional solidificarão seu aprendizado.