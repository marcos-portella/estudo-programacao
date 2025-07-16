## Dia 5

### Prefácio:

A capacidade de coletar informações diretamente do usuário. Hoje prendemos a usar a função ``input()`` para receber dados e, crucialmente, como lidar com o tipo de dado retornado por essa função para realizar operações matemáticas e evitar erros comuns.

### Coleta de Dados com ``input()``:

A função ``input()`` é a principal ferramenta para interagir com o usuário e solicitar que ele digite informações. Tudo o que o usuário digita é lido como uma string.

- **Sintaxe básica**: ``variavel = input('Mensagem para o usuário: ')``

- A mensagem entre aspas é o prompt que será exibido ao usuário.

- O valor digitado pelo usuário é armazenado na variável especificada.

````
nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}') 
````

Neste exemplo, o programa solicita o nome do usuário e o exibe de volta.

### Conversão de Tipos (Type Casting):

Um ponto fundamental ao trabalhar com ``input()`` é que, por padrão, ele sempre retorna uma ``string``. Isso significa que, mesmo que o usuário digite um número, Python o tratará como texto.

- **O Problema**: Tentar realizar operações aritméticas (como soma) diretamente com strings resultará em concatenação (para o operador ``+``) ou erro (para outros operadores).

````
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
# print(f'A soma do primeiro par de números é: {numero_1+numero_2}')
# Este código concatenaria '1' e '2' resultando em '12', não 3.
# Se fosse uma operação de subtração, resultaria em erro.
````

- **A Solução**: Para realizar operações matemáticas, é necessário converter explicitamente a string para o tipo numérico desejado, como ``int`` (inteiro) ou ``float`` (ponto flutuante), usando as funções ``int()`` ou ``float()``.

````
numero_3 = int(input('Digite um número: '))
numero_4 = int(input('Digite outro número: '))
print(f'A soma do segundo par de números é: {numero_3+numero_4}') #
````

Aqui, int() converte as entradas de string para inteiros, permitindo a soma correta.

### Observações Finais:

A função input() é simples, mas requer atenção especial à conversão de tipos. Lembre-se sempre: dados coletados via input() são strings e precisam ser convertidos para os tipos apropriados (int, float, etc.) antes de serem usados em operações que exigem esses tipos. Este é um passo crucial para construir programas interativos e funcionais em Python.