## Dia 4
### Prefácio:

Hoje nós focamos nos **operadores aritméticos** e na **precedência** com que o Python os avalia. Além disso, aprimoramos nossas habilidades de manipulação de texto, explorando a **concatenação de strings**, a **repetição de strings** e, fundamentalmente, as modernas técnicas de **formatação de strings** para exibir informações de maneira clara e controlada.

### Operadores Aritméticos:

Os operadores aritméticos são símbolos que realizam cálculos matemáticos. Python oferece um conjunto completo de operadores para diversas operações.

- **Adição (``+``)**: Soma dois valores.

- **Subtração (``-``)**: Subtrai um valor do outro.

- **Multiplicação (``*``)**: Multiplica dois valores.

- **Divisão (``/``)**: Divide um valor por outro, sempre retornando um float.

- **Divisão Inteira (``//``)**: Divide um valor por outro e retorna apenas a parte inteira do resultado (arredondada para baixo).

- **Exponenciação (``**``)**: Eleva um número à potência de outro.

- **Módulo (``%``)**: Retorna o resto da divisão de um número por outro. É útil, por exemplo, para verificar se um número é divisível por outro.

````
adicao = 10 + 10          # 20
subtracao = 10 - 5        # 5
multiplicacao = 10 * 10   # 100
divisao = 10 / 2.2        # 4.5454... (float)
divisao_inteira = 10 // 2.2 # 4.0
exponenciacao = 2 ** 10   # 1024
modulo = 55 % 2           # 1 (resto da divisão de 55 por 2)

print(f"Adição: {adicao}, Subtração: {subtracao}, Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}, Divisão Inteira: {divisao_inteira}, Exponenciação: {exponenciacao}")
print(f"Módulo: {modulo}, 16 é divisível por 8? {16 % 8 == 0}") #
````

### Precedência dos Operadores:

A precedência determina a ordem em que as operações são avaliadas em uma expressão. É fundamental entender essa ordem para evitar resultados inesperados. A ordem geral é:

1. **Parênteses (``()``)**: As operações dentro de parênteses são sempre avaliadas primeiro.

2. **Exponenciação (``**``)**: Em seguida, as potências.

3. **Multiplicação (``*``), Divisão (``/``), Divisão Inteira (``//``), Módulo (``%``)**: Avaliadas da esquerda para a direita.

4. **Adição (``+``), Subtração (``-``)**: Avaliadas da esquerda para a direita.

````
conta_1 = 1 + 1 ** 5 + 5 # 1 + 1 + 5 = 7 (exponenciação primeiro)
print(f"Resultado conta_1: {conta_1}") 

conta_2 = (1 + 1) ** (5 + 5) # (2) ** (10) = 1024 (parênteses primeiro)
print(f"Resultado conta_2: {conta_2}")
````

### Concatenação e Repetição de Strings:

Além de operações numéricas, aprendemos a manipular strings de formas básicas, mas muito úteis.

- **Concatenação (``+``)**: O operador ``+`` pode ser usado para unir duas ou mais strings.

- **Repetição (``*``)**: O operador ``*`` (multiplicação) pode ser usado para repetir uma string um determinado número de vezes.

````
concatenacao = 'A' + 'B' + 'C'       # 'ABC'
concatenacao2 = 'Gorro' + ' ' + 'Escuro' # 'Gorro Escuro'

a_dez_vezes = 'A' * 10             # 'AAAAAAAAAA'
tres_vezes_luiz = 3 * 'Luiz'       # 'LuizLuizLuiz'

print(f"Concatenação: {concatenacao}")
print(f"Concatenação 2: {concatenacao2}")
print(f"Repetição 'A' 10 vezes: {a_dez_vezes}")
print(f"Repetição 'Luiz' 3 vezes: {tres_vezes_luiz}") 
````

### Introdução à Formatação de Strings:

Apresentar informações de forma clara e legível é essencial. Python oferece maneiras poderosas de formatar strings.

#### f-strings (Formated String Literals):

Introduzidas no Python 3.6, as **f-strings** são a maneira mais moderna e recomendada para formatar strings. Elas permitem incorporar expressões Python diretamente dentro de strings literais, prefixando a string com ``f`` ou ``F``.

````
nome = 'Carlos Miguel'
altura = 1.80
peso = 95
imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura,' # Formata altura com 2 casas decimais
linha_2 = f'{peso} de peso e seu imc é {imc:.2f}.'   # Formata IMC com 2 casas decimais

print(linha_1)
print(linha_2) 
````

No exemplo acima, observe o uso de ``:.2f`` para formatar números de ponto flutuante com duas casas decimais.

### Método ``format()``:

O método ``format()`` é outra forma flexível de formatar strings. Ele usa chaves ``{}`` como placeholders que são preenchidos pelos argumentos passados ao método. É possível usar índices ou argumentos nomeados.

````
a = 'A'
b = 'BB'
c = 1.1

string_formatada = 'a={1} b={nome2:.2f} c={0} new={nome3}'
formato = string_formatada.format(a, b, nome2=c, nome3=1234)

print(formato) # Saída: a=BB b=1.10 c=A new=1234
````

### Observações Finais:
A compreensão dos operadores aritméticos e sua precedência é a base para a lógica matemática em programas. Dominar as técnicas de concatenação e, especialmente, a formatação de strings com ``f-strings`` e o método ``format()``, nos permite criar saídas de programa mais claras, informativas e amigáveis ao usuário. Estes conceitos são aplicáveis em praticamente todos os tipos de programas, desde scripts simples até sistemas complexos.