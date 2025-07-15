## DIA 2

### Prefácio:

Este dia foi dedicado a explorar as nuances da função ``print()``, a entender a importância dos comentários para um código legível e a introduzir os primeiros conceitos sobre tipos de dados, com foco especial nas strings, o tipo fundamental para trabalhar com texto.

### Detalhes da Função ``print()``:
A função ``print()`` é mais versátil do que parece à primeira vista. Além de simplesmente exibir valores, ela permite controlar como esses valores são separados e como a linha termina.

#### Argumentos ``sep`` e ``end``:
- ``sep`` **(separator)**: Define o caractere ou string que será usado para separar os múltiplos argumentos passados para ``print()``. Por padrão, o separador é um espaço.

- ``end``: Define o que será adicionado ao final da linha após todos os argumentos serem impressos. O padrão é uma quebra de linha (``\n``).

````
# Usando sep para separar por hífen e end para nova linha
print(12, 34, 1011, sep="-", end='\r\n') # Saída: 12-34-1011

# Usando sep com uma string personalizada e end com exclamações
print(56, 78, sep=' arroz doce ', end="!!\n") # Saída: 56 arroz doce 78!!
````

### Comentários: Clareza no Código:

Comentários são partes do código que são ignoradas pelo interpretador Python, mas são cruciais para desenvolvedores. Eles servem para explicar o que o código faz, por que foi feito de determinada maneira, ou para desativar temporariamente uma linha de código.

#### Tipos de Comentários em Python:
- **Comentários de uma linha**: Iniciam com o caractere ``#``. Tudo o que vem depois do ``#`` na mesma linha é considerado um comentário.

````
# Este é um comentário de uma linha
print(123) # O comentário pode vir após o código também
````

- **DocStrings (comentários de múltiplas linhas)**: Embora não sejam tecnicamente "comentários" no sentido estrito (o Python as armazena em atributos ``__doc__``), strings de múltiplas linhas delimitadas por aspas triplas (``"""`` ou ``'''``) são frequentemente usadas como comentários estendidos ou para documentar módulos, classes e funções.

````
"""
Este é um DocString
Ele pode pular várias linhas
e é usado para documentar o código.
"""
print('Exemplo de DocString')
````

### Tipos de Dados Fundamentais: Strings:
Python é uma linguagem de tipagem dinâmica e forte. Isso significa que você não precisa declarar o tipo de uma variável, e o Python não fará conversões implícitas que possam levar a perdas de dados inesperadas. O primeiro tipo de dado que exploramos a fundo foi a **string**.

#### Strings (``str``): Representando Texto:

Strings são sequências de caracteres usadas para representar texto em Python. Elas podem ser definidas de diversas maneiras:

- Aspas simples (``''``): O método mais comum.

````
print('Marcos Portella') #
````

- **Aspas duplas (``""``)**: Funciona exatamente como aspas simples, sendo uma questão de preferência ou para lidar com aspas internas.

````
print("Marcos Portella") #
````

- **Caracteres de Escape (\)**: Usados para incluir caracteres especiais (como aspas) dentro de uma string que já usa o mesmo tipo de aspas. O backslash (\) "escapa" o próximo caractere.

````
print("Marcos \\\"Portella\\\"") # Saída: Marcos "Portella"
````

- **Alternativa para Aspas**: Usar o tipo de aspas diferente do que está dentro da string para evitar escapes.

````
print('Marcos "Portella"') # Saída: Marcos "Portella"
````

- **Raw Strings (``r''`` ou ``r""``)**: Prefixir a string com ``r`` a torna uma "raw string" (string bruta). Nela, os caracteres de escape são tratados como caracteres literais, o que é útil para caminhos de arquivo no Windows ou expressões regulares.

````
print(r"Marcos \"Portella\"") # Saída: Marcos \"Portella\" (o backslash não é um escape)
````

### Observações Finais:

Aprofundar-se na função print() nos deu mais controle sobre a saída dos nossos programas. A introdução aos comentários e DocStrings destacou a importância da legibilidade e documentação do código, práticas essenciais para qualquer programador. Por fim, a exploração das strings e suas diversas formas de definição nos preparou para lidar com dados textuais de maneira eficaz em projetos futuros.