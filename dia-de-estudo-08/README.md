## Dia 8

### Prefácio:

Dominar a formatação e a manipulação de strings é crucial para a saída de dados amigável ao usuário e para a construção de lógicas baseadas em texto.

### Formatação de Strings:

Exploramos os métodos mais comuns e eficazes para formatar strings em Python.

#### F-strings (Formatação Recomendada):

As f-strings (formatted string literals), introduzidas no Python 3.6, são a forma mais moderna, legível e eficiente de formatar strings. Elas permitem incorporar expressões Python diretamente dentro de literais de string, prefixando a string com ``f`` ou ``F``.

- **Interpolação direta**: Variáveis e expressões são colocadas entre chaves ``{}``.

- **Controle de casas decimais**: Utilize ``:.xf`` para floats, onde ``x`` é o número de casas decimais.

- **Alinhamento e preenchimento**:

    - ``:`` seguido por um caractere de preenchimento, um alinhamento (``<`` para esquerda, ``>`` para direita, ``^`` para centro) e a largura total. Ex: ``{variavel: >10}``.

    - O caractere ``=`` pode forçar o preenchimento zero após o sinal (para números).

- **Sinal**: ``+`` ou ``-`` para exibir sempre o sinal de um número.

- **Hexadecimal**: Use ``:x`` para hexadecimal minúsculo ou ``:X`` para maiúsculo. É possível adicionar zeros à esquerda com ``:08x.``

- **Conversion Flags**: ``!r`` para ``repr()``, ``!s`` para ``str()``, ``!a`` para ``ascii()``.

Exemplo:

````
variavel = 'ABC'
pi = 3.1415926535

print(f'{variavel}')
print(f'{variavel: >10}')      # '       ABC'
print(f'{variavel:$<10}')      # 'ABC$$$$$$$'
print(f'{variavel:!^10}')      # '!!!ABC!!!!'
print(f'{1000.4873648123746:0=+10,.1f}') # '+0001,0.5' (com separador de milhar)
print(f'O hexadecimal de 1500 é {1500:08x}') # '000005dc'
print(f'{variavel!r}')         # "'ABC'" (representação oficial da string)
````

#### Interpolação com ``%`` (Método Antigo):
Este é um método mais antigo, inspirado na linguagem C. Embora ainda funcione, as f-strings são preferíveis pela sua legibilidade e flexibilidade.

- **``%s``**: para strings

- **``%d`` ou ``%i``**: para inteiros

- **``%f``**: para floats (pode-se especificar casas decimais com ``%.xf``)

- **``%x`` ou ``%X``**: para hexadecimal

Exemplo:

````
nome = 'Luiz'
preco = 1000.95897643

variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel) # 'Luiz, o preço é R$1000.96'

print('O hexadecimal de %d é %04x' % (1500, 1500)) # 'O hexadecimal de 1500 é 05dc'`
````

### Operadores ``in`` e ``not in``:

Estes operadores são utilizados para verificar se uma sequência de caracteres (substring) está presente ou ausente dentro de outra string. Strings em Python são iteráveis, o que significa que podemos acessar seus caracteres por índice e verificar a existência de subconjuntos.

- ``in``: Retorna ``True`` se a substring for encontrada na string, ``False`` caso contrário.

- ``not in``: Retorna ``True`` se a substring não for encontrada na string, ``False`` caso contrário.

#### Conceito de Índices:

Strings possuem índices positivos (do início para o fim, começando em 0) e negativos (do fim para o início, começando em -1).

````
  0 1 2 3 4 5  <- Índices positivos
  O t á v i o
 -6-5-4-3-2-1  <- Índices negativos
````

Exemplo:

````
nome = 'Otávio'

print(nome[2])       # Saída: 'á'
print(nome[-4])      # Saída: 'á'

print('á' in nome)   # Saída: True
print('z' in nome)   # Saída: False
print('Otá' not in nome) # Saída: False
print('zin' not in nome) # Saída: True

# Uso prático com input do usuário:
nome_usuario = input('Digite seu nome: ')
buscar = input('O que deseja encontrar no seu nome? ')

if buscar in nome_usuario:
    print(f'"{buscar}" está em "{nome_usuario}".')
else:
    print(f'"{buscar}" não está em "{nome_usuario}".')
````
### Observações Finais:

O domínio da manipulação e formatação de strings é um pilar fundamental para qualquer desenvolvedor Python. As f-strings são seu melhor amigo para criar saídas de programa limpas e informativas, enquanto os operadores ``in`` e ``not in`` são cruciais para lógicas que dependem da análise de texto.

**Próximos Passos**: Continue praticando a formatação em diferentes cenários e experimente com os operadores ``in``/``not in`` em diversas strings. Lembre-se que cada dia de aprendizado se constrói sobre o anterior; o conhecimento de operadores lógicos e condicionais (``if``/``elif``/``else``) do dia anterior é diretamente aplicável ao uso desses operadores. A repetição e a experimentação são chaves para solidificar seu aprendizado.