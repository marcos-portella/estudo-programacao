## Curso Udemy - Python do Básico ao Avançado

Este arquivo contém resumos e anotações das aulas
do curso de Python feito na plataforma Udemy.

Os resumos vão se tornando mais didáticos e legíveis 
conforme as aulas avançam, mostrando minha evolução



## Dia 1 – Primeiros Passos com Python


### Configurando o Visual Studio Code:

Hoje aprendi a configurar o VS Code (Visual Studio Code)
de forma funcional para acompanhar as aulas de Python.
Usei o arquivo "settings.json" para personalizar o ambiente.
Mesmo com interfaces gráficas, aprender a configurar manualmente
ajuda a entender melhor a ferramenta.


 Meu Primeiro Código:

````
print('hello, world')  # Meu primeiro programa em Python 🎉
````

Me senti motivado e acredito que vou gostar cada vez mais
conforme o curso avança.



## Dia 2 – Impressões, Comentários e Strings


### Funções do print:


 Aprendi sobre os parâmetros:
```
\n   -> # quebra de linha
sep= -> # define o separador
end= -> # define o final da linha

print('Python', 'é', 'legal', sep='-', end='!\n')  # Exemplo usando sep e end
```


### Tipos de Comentários:


```
 Comentário de uma linha usa  # Comentário

"""

Este é um comentário
de várias linhas usando DocString

"""
```

O Python lê da esquerda para a direita e de cima para baixo.


### Tipos de Dados e Strings:


 Escape de caracteres com \

```
print("Linha 1\nLinha 2")  # \n cria uma quebra de linha
```

 Strings raw (cruas) usando o prefixo 'r'
```
print(r"C:\Users\nome")  # Mostra literalmente a barra invertida
```


### Conceitos Técnicos:


- Linguagem: Python
- Tipagem: Dinâmica / Forte
- Tipo 'str': Representa strings (textos)
- Strings são textos dentro de aspas simples ou duplas



## Dia 3 – Variáveis, Tipos e Strings


### Variáveis e Tipagem Dinâmica:


Em Python, não é necessário declarar o tipo da variável.
O interpretador define automaticamente baseado no valor:

```
nome = "Ana"        # str

idade = 25          # int

altura = 1.68       # float

ativo = True        # bool
```


 Concatenando Strings:

```
print("Olá, " + nome)             # Concatenação com +

print("Python! " * 3)             # Repetição com *
```


 Conversão de Tipos:

```
print("Idade: " + str(idade))     # Convertendo int para str

num = int("10")                   # string para int

pi = float("3.14")                # string para float
```


 Verificando tipos com type():

```
print(type(nome))                 # <class 'str'>

print(type(idade))                # <class 'int'>

print(type(pi))                   # <class 'float'>
```


### Resumo do dia:

- Variáveis são atribuídas com =
- Tipos são inferidos automaticamente
- Conversão: int(), str(), float()
- type() retorna o tipo da variável



## Dia 4 – Operações Aritméticas e Formatação


### Operações Aritméticas:

Hoje aprendi que o python permite realizar todas as operações:

 matemáticas básicas:

```
adicao = 10 + 10

print('Adição:', adicao)  # 20

subtracao = 10 - 5

print('Subtração:', subtracao)  # 5

multiplicacao = 10 * 10

print('Multiplicação:', multiplicacao)  # 100

divisao = 10 / 2.2

print('Divisão:', divisao)  # Resultado com ponto flutuante

divisao_inteira = 10 // 2.2

print('Divisão inteira:', divisao_inteira)  # Resultado sem casas decimais

exponenciacao = 2 ** 10

print('Exponenciação:', exponenciacao)  # 1024

modulo = 55 % 2

print('Módulo:', modulo)  # 1 -> útil para saber se número é par (n % 2 == 0)
```

 Verificando divisibilidade:
```
print(10 % 8 == 0)  # False

print(16 % 8 == 0)  # True
```


### Introdução à Formatação:


 Gostei da f-strings:, é forma de formatar strings:
```

nome = 'Carlos Miguel'

altura = 1.80

peso = 95

imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f}m de altura,'

linha_2 = f'pesa {peso}kg e seu IMC é {imc:.2f}.'

print(linha_1)

print(linha_2)
```

 Espaço para separar blocos de saída:
```
print(end='\n')
```


 Outra forma: format():

```
a = 'A'

b = 'BB'

c = 1.1
```

 Podemos misturar índices e nomes nomeados:
```
string = 'a={1} b={nome2:.2f} c={0} new={nome3}'

formato = string.format(a, b, nome2=c, nome3=1234)

print(formato)
```

### Resumo do Dia:

- Módulo (%) verifica restos e divisibilidade
- f-strings: forma moderna e prática de formatar textos
- format(): alternativa mais antiga, ainda útil com nomeação e ordem



## Dia 5 – Entrada de Dados e Conversão


### Coletando entrada do usuário:


 input() sempre retorna uma string (str), mesmo que o usuário digite um número:

````
nome = input('Qual o seu nome? ')

print(f'O seu nome é {nome}')
````


Tentativa de somar números diretamente:


 Erro comum: somar strings resulta em concatenação (ex: "5" + "5" = "55"):

```
numero_1 = input('Digite um número: ')

numero_2 = input('Digite outro número: ')
```

 Aqui ocorre concatenação, não soma aritmética:
```
print(f'A soma do primeiro par de números é: {numero_1 + numero_2}')  # Ex: "2" + "3" = "23"
```


### Corrigindo com conversão de tipos:


 Convertendo para int com int(), o Python entende como números:

```
numero_3 = int(input('Digite um número: '))

numero_4 = int(input('Digite outro número: '))
```

 Agora é uma soma real entre inteiros:
```
print(f'A soma do segundo par de números é: {numero_3 + numero_4}')
```


 Melhor forma (até agora):


 Separar entrada e conversão ajuda na legibilidade:

```
numero_5 = input('Digite um número: ')

numero_6 = input('Digite outro número: ')
```

 Ainda não há tratamento de erro, mas essa estrutura é mais clara:
```
int_numero_5 = int(numero_5)

int_numero_6 = int(numero_6)

print(f'Soma (forma melhorada): {int_numero_5 + int_numero_6}')
```


### Observação importante:


⚠️ Se o usuário digitar algo que não seja número, o programa vai quebrar!
Para evitar isso, é necessário tratar erros o que será aprendido depois.


### Resumo do Dia:

- input() sempre retorna uma string
- Para fazer contas, converta com int() ou float()
- Cuidado: somar strings resulta em concatenação
- Separar entrada e conversão melhora a clareza
 ! Futuramente: aprenderemos a validar entradas para não ocorrer erros



## Dia 6 – Estruturas Condicionais em Python


### if / elif / else:


Usamos essas estruturas para executar blocos de código diferentes de acordo com condições.

```
entrada = input('Você quer "entrar" ou "sair"? ')
```

 Verificando a entrada do usuário:
```
if entrada == 'entrar' or entrada == 'Entrar':
    print('Você entrou no sistema.')
elif entrada == 'sair' or entrada == 'Sair':
    print('Você saiu do sistema.')
else:
    print('Você não digitou nem "entrar" nem "sair".')

print('FORA DOS BLOCOS')  # Sempre será executado
```


 Blocos condicionais com booleans:

```
condicao = True

if condicao:
    print('Este é o código do if (condição é True)')

condicao2 = False

if condicao2:
    print('Este é o código do if2 (não será executado)')
else:
    print('Este é o novo código do if2 (executado pois condição2 é False)')
```
 Comparações diretas:


```
if 10 == 10:
    print('Verdadeiro if3')  # Será executado
else:
    print('Falso if3')

if 10 == 11:
    print('Verdadeiro if4')
else:
    print('Falso if4')  # Será executado

print('Fora do if')  # Sempre executado
```

 Encadeando condições:


```
condicao1 = False
condicao2 = False
condicao3 = False
condicao4 = False

if condicao1:
    print('Verdadeiro 1')
elif condicao2:
    print('Verdadeiro 2')
elif condicao3:
    print('Verdadeiro 3')
elif condicao4:
    print('Verdadeiro 4')
else:
    print('Nenhuma condição foi satisfeita')  # Será executado
```


### Resumo do Dia:

- if → executa um bloco se a condição for True
- elif → checa nova condição caso o if falhe
- else → executa se nenhuma condição anterior for satisfeita
- Blocos fora do if sempre são executados normalmente
- Podemos comparar valores diretamente (ex: 10 == 10)
- É possível encadear várias condições com elif



## Dia 7 – Comparações, Lógica e Debugger


### Testando estruturas condicionais:


 Avaliação encadeada com elif: apenas o primeiro True será executado

```
condicao1 = False

condicao2 = False

condicao3 = True

condicao4 = True

if condicao1:
    print('Verdadeiro 1')

elif condicao2:
    print('Verdadeiro 2')

elif condicao3:
    print('Verdadeiro 3')  # Este será executado

elif condicao4:
    print('Verdadeiro 4')

else:
    print('Nenhuma condição foi satisfeita')
```


 Comparando valores digitados:
```
primeiro_valor = input('Digite um valor: ')

segundo_valor = input('Digite outro valor: ')
```

 Comparando os valores com operadores relacionais:
```
if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que {segundo_valor=}.')

elif primeiro_valor < segundo_valor:
    print(f'{segundo_valor=} é maior que {primeiro_valor=}.')

elif primeiro_valor == segundo_valor:
    print(f'{primeiro_valor=} é igual a {segundo_valor=}.')

else:
    print('Você digitou um texto inválido.')
```


### Operadores Lógicos: and, or, not:


and → todas as condições precisam ser verdadeiras
```
entrada = input('[E]ntrar [S]air: ')

senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')

else:
    print('Sair')
```

 Curto-circuito com "and": para na primeira expressão falsa
```
print(True and 0 and True)  # Retorna 0
```

 Exemplo de uso de "or": se input for vazio, usa valor padrão
```
senha = input('Senha: ') or 'Sem senha'

print(senha)
```

 or → basta uma condição ser verdadeira
```
entrada2 = input('[E]ntrar [S]air: ')

senha_digitada2 = input('Senha: ')

senha_permitida2 = '123456'

if (entrada2 == 'E' or entrada2 == 'e') and senha_digitada2 == senha_permitida2:
    print('Entrar')

else:
    print('Sair')
```

 not → inverte o valor lógico
```
senha2 = input('Senha: ')

if not senha2:
    print('Você não digitou nada')
```


 Testando o not:

```
print(not 0)       # True

print(not True)    # False

print(not False)   # True
```


 Operadores de comparação:

```
'''
Operadores relacionais:

>   (maior)

>=  (maior ou igual)

<   (menor)

<=  (menor ou igual)

==  (igual)

!= (diferente)
'''

maior = 2 > 1                  # True

maior_ou_igual = 2 >= 2        # True

menor = 1 < 2                  # True

menor_ou_igual = 2 <= 2        # True

igual = 'a' == 'a'             # True

diferente = 'a' != 'b'         # True

print(diferente)  # Saída: True
```


### Resumo do Dia:

- elif para várias condições exclusivas
- Comparações com operadores relacionais (>, <, ==, etc.)
- Lógica com operadores: and, or, not
- Curto-circuito: expressão para no primeiro valor "falso"
- input() pode ser combinado com or para valores padrão
- not inverte valores booleanos
- ! Atenção: input() sempre retorna string, cuidado ao comparar com números



## Dia 8 – Operadores `in`, Interpolação Antiga e Formatação de Strings


### Operadores `in` e `not in`:


Strings são iteráveis, e podemos acessar seus caracteres por índice:

 Índices positivos e negativos:
 0 1 2 3 4 5

 O t á v i o
 
 -6-5-4-3-2-1

```
nome = 'Otávio'

print(nome[2])    # á
print(nome[-4])   # á
```

Verificando presença de caracteres com in / not in:

```
print('á' in nome)         # True
print('z' in nome)         # False
print('Otá' not in nome)   # False
print('zin' not in nome)   # True
```

Interagindo com o usuário:

```
nome2 = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
```

 Interpolação Antiga de Strings:

 Método antigo de formatação com o operador %:

 %s -> string
 %d ou %i -> inteiros
 %f -> float (permite casas decimais)
 %x ou %X -> hexadecimal

```
nome = 'Luiz'
preco = 1000.95897643

variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)  # Luiz, o preço é R$1000.96
```

 Representação hexadecimal:

```
print('O hexadecimal de %d é %04x' % (1500, 1500))  # 05dc
print('O hexadecimal de %i é %08X' % (1500, 1500))  # 000005DC
```

 Formatação Moderna com f-strings:

```
"""
f-strings com alinhamento e preenchimento:

(Caractere)(><^)(largura)
>  → alinha à direita
<  → alinha à esquerda
^  → centraliza
=  → força o sinal à esquerda
Sinal: + ou -
Conversão: !r (repr), !s (str), !a (ascii)
"""

variavel = 'ABC'

print(f'{variavel}')             # ABC
print(f'{variavel: >10}')        #        ABC
print(f'{variavel:$<10}')        # ABC$$$$$$$
print(f'{variavel:$^10}')        # $$$ABC$$$$
```

 Formatação numérica com sinal, separador e casas decimais:
````
print(f'{1000.4873648123746:0=+10,.1f}')  # +001,000.5
````

 Hexadecimal com f-string:
```
print(f'O hexadecimal de 150 é {1500:08x}')  # 000005dc
```

 Usando conversão com !r (iremos ver mais sobre isso no futuro):
```
print(f'{variavel!r}')           # 'ABC'
```

### Resumo do Dia:

- Strings são iteráveis e podem ser verificadas com `in` / `not in`
- Interpolação antiga usa `%s`, `%d`, `%f` e `%x`
- f-strings são a forma moderna e mais prática de formatar
- f-strings permitem controle de alinhamento, preenchimento, casas decimais e sinais
- Também permitem conversões como `!r` para debug/representações



## DIA 9

### Assuntos abordados:
- Fatiamento de strings
- A função len()
- Uso de índices negativos
- Exercício com manipulação de strings e validação de entrada

 FATIAMENTO DE STRINGS:
```
[str(início:fim:passo)] # permite acessar fatias de uma string.

# Ex:
variavel = 'Olá mundo'
print(variavel[4:])     # 'mundo' - Omitido o fim, pega do índice 4 até o final
print(variavel[4:6])    # 'mu' - Fatiamento do índice 4 até o 5 (6 é exclusivo)
print(variavel[:5])     # 'Olá m' - Omitido o início, começa do índice 0 até 4
```

 len() → retorna a quantidade de caracteres da string (ou fatia):
```
print(len(variavel[3])) # 1 - Apenas 1 caractere retornado no índice 3 (' ')
print(len(variavel))    # 9 - Total de caracteres em 'Olá mundo'
```

 Utilizando len() no fatiamento completo com passo:
```
print(variavel[0:len(variavel):1])  # 'Olá mundo'
print(variavel[0:9:1])              # Também retorna 'Olá mundo'
print(variavel[0:9:2])              # 'Oámno' - passo de 2 em 2
print(variavel[-1:-10:-1])          # 'odnum álO' - string invertida com passo negativo
```


 EXERCÍCIO: Solicita nome e idade do usuário e realiza verificações.

```
nome = input('Digite seu nome aqui: ')
idade = input('Digite sua idade  aqui: ')

if not nome:
    print('Desculpe, você deixou campos vazios') 
elif not idade:
    print('Desculpe, você deixou campos vazios') 
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in  nome:
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome não contém espaços')

    print(f'Seu nome tem {[len(nome)]} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')  
```

 Solução do professor:

```
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")
```

### Observações:
- O uso de índices negativos permite percorrer strings de trás para frente.
- O aluno resolveu o exercício com uma estrutura levemente diferente da solução do professor, mas funcional.



"""
## Dia 10

### Assuntos estudados:
- Tratamento de erros com try/except
- Conversão de tipos e verificação de dados
- Constantes (boas práticas com variáveis imutáveis)
- Avaliação de múltiplas condições com operadores lógicos (and)
- Organização de código para reduzir complexidade


### EXEMPLOS PRÁTICOS


 EXEMPLO 1 – try / except para tratamento de erro em tempo de execução:

```
numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_float = float(numero_str)  # Tentativa de conversão para float
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')  # Mensagem de erro padrão


# Mesmo com erro acima, código continua a ser executado abaixo:
print(1234)
print(456)
# int('a')  # Comentado para evitar exceção ao rodar o arquivo
```

 EXEMPLO 2 – Constantes e verificação de múltiplas condições:
```
velocidade = 60  # velocidade atual do carro
local_carro = 107  # local em que o carro está na estrada

RADAR_1 = 60         # velocidade máxima permitida no radar 1
LOCAL_1 = 100        # localização do radar 1
RADAR_RANGE = 1      # alcance de detecção do radar

# Verificações:
velocidade_do_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE)

# Resultado de cada verificação:
if velocidade_do_carro_passou_radar_1:
    print('Carro está acima do limite de velocidade')
else:
    print('Carro abaixo do limite de velocidade')

if carro_passou_radar_1:
    print('Carro passou pelo radar')
else:
    print('Carro não passou pelo radar')

# Verificando se foi multado
if carro_passou_radar_1 and velocidade_do_carro_passou_radar_1:
    print('Carro multado em radar 1')
else:
    print('Carro não multado')
```


## dia 11 

### Assuntos abordados:
- Flag (bandeira), None, is, is not, id
- Exercícios: par/ímpar, saudação por hora, tamanho do nome
- Tipos imutáveis, fatiamento e métodos de string


### Flag (bandeira), None, is, is not, id
```
v1 = 'a'
v2 = 'a'
print(id(v1))  # Mesmo id por otimização do Python
print(id(v2))

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if is None)       # True se não passou no if
print(passou_no_if is not None)   # False se não passou no if

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
```

### Exercício: par ou ímpar
```
# Resposta do professor:

numero = input('Digite um número: ')

try:
    numero_float = float(numero)
    par_impar = numero_float % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {numero_float} é {par_impar_texto}')

except:
    print('O número digitado não é inteiro')
```

### Exercício: saudação por horário
```
# Resposta do professor:

entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
```

### Exercício: tamanho do nome
```
# Resposta do professor:

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')
```

### Tipos imutáveis, fatiamento e métodos de string
```
string = '100000'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)             # Original
print(outra_variavel)     # Modificada via fatiamento
print(string.zfill(10))   # Preenche com zeros à esquerda

# Link para a documentação oficial:
# https://docs.python.org/pt-br/3/library/stdtypes.html
# Imutáveis que vimos: str, int, float, bool
```


## Dia 12
 Neste dia, estudamos os conceitos básicos de estruturas de repetição com o comando while, incluindo loops simples e aninhados, além do uso dos operadores de atribuição como +=, -=,*=, /=, **=,%=.

Também abordamos controle de fluxo dentro de loops usando continue e break para pular ou interromper iterações.

Por fim, praticamos iteração sobre strings com o while, construindo novas strings comcaracteres adicionais.


Introducao ao while:
```
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        condicao = False

print('Acabou')
```

Contador genérico:
```
contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)

print('Acabou')
```

Controle de fluxo com continue e break:
```
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break
print('Acabou')
```

Estrutura de repetição aninhada com while:
```
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1
print('Acabou')
```


### Operadores de atribuição:
+=, -=, *=, /=, //=, **=, %=

Operador de soma (int):
```
contador = 0

while contador < 10:
    contador += 1
    print(contador)
print('Acabou')
```
Operadores de soma (str):
```
contador = '1'

while contador < '12':
    contador += '2'
    print(contador)
print('Acabou')
```
Operador de multiplicação:
```
contador = 10

while contador < 10:
    contador *= '2'
    print(contador)
print('Acabou')
```
Operador de subtração:
```
contador = 20

while contador > 10:
    contador -= 1
    print(contador)
print('Acabou')
```
Operador de divisão:
```
contador = 125

while contador > 5:
    contador /= 5
    print(contador)
print('Acabou')
```
Operador de divisão inteira:
```
contador = 125

while contador > 5:
    contador /= 5
    print(contador)
print('Acabou')
```
Operador de potenciação:
```
contador = 10

while contador < 10000:
    contador **= 2
    print(contador)
print('Acabou')
```
Operador de módulo:
```
contador = 21

while contador > 10:
    contador %= 2
    print(contador)
print('Acabou')
```

Exercício de strings com while:
```
# Solução do professor:

nome = 'Maria Helena'  # Iteráveis
indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
novo_nome += '*'
print(novo_nome)
```

### Observações finais:

- O uso de while deve sempre ter uma condição que permita a saída do loop para evitar loops infinitos.
- Operadores de atribuição facilitam a escrita e tornam o código mais legível e eficiente.
- Controle de fluxo com continue e break ajuda a gerenciar a lógica dentro dos loops, evitando condições complexas.
- Iterar strings com while é útil para manipulações específicas, mas em muitos casos o for pode ser mais simples.


## Dia 13
Hoje exploramos o uso avançado dos laços while e for, incluindo a estrutura while/else. 

Vimos uma calculadora simples que valida entrada do usuário, um jogo básico de adivinhação de palavra usando loops, e os conceitos de iteradores e iteráveis. 

Também revisamos operações básicas e manipulação de listas em Python, bem como exercícios para reforçar índices e métodos de listas.


While / else
```
string = 'Valorqualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while')
```

Calculadora com while
```
while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print('Realizando sua conta. Confira o resultado abaixo:')

    if operador == '+':
        print(f'{num_1_float} + {num_2_float}=',num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float}=',num_1_float - num_2_float)

    elif operador == '/':
         print(f'{num_1_float} / {num_2_float}=',num_1_float / num_2_float)

    elif operador == '*':
        print(f'{num_1_float} * {num_2_float}=',num_1_float * num_2_float)

    else:
        print('Nunca deveria ter chegado até aqui')
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
```

Exercício: Jogo de adivinhação de palavra:
```
# Solução do professor:

import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
```

Introdução ao for:
```
senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')

    repeticoes += 1

print(repeticoes)
print('Aquele laço acima pode ter repetições infinitas')

# O for é usado em situações que sabemos quantas repetições serão feitas:

texto = 'Python'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')
```

for por baixo dos panos:
```
# for letra in texto:
texto = 'Luiz'  # iterável
iteratador = iter(texto)  # iterator

# Como funciona o for por baixo dos panos:
while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

# Como fica o for final:
for letra in texto:
    print(letra)
```

For + Range
```
numeros = range(0, 100, 8)
for numero in numeros:
    print(numero)
```

Controle de fluxo no for
```
for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')
```

Listas em Python:
```
# Pode ter vários tipos diferente na mesma lista:
#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio',  1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))

print(bool([]))  # falsy
print(lista, type(lista))
```

Removendo, inserindo e concatenando listas
```
# É possível alterar facilmente as listas se necessário:
lista2 = [10, 20, 30, 40]
numero = [lista2[2]]
print(numero)

lista2[2] = 300
print(lista2[2])
print(lista2)

#  Adcionando valores na lista:
lista2.append(50)
lista2.append(60)
print(lista2)


#  Removendo valores na lista:
lista2.append(50)
lista2.append(60)
lista2.pop() # Remove o último item da lista
lista2.append(70)
lista2.append(80)
print(lista2)
ultimo_valor = lista2.pop()
print (lista2, 'Removido:', ultimo_valor)

#  Removendo valores específicos na lista:
lista2.pop(2)
print(lista2)

# Deletando itens da lista:
del lista2[-1]
print(lista2)

#inserindo valores na lista:
lista2.insert(0, 'MM')
print(lista2)

# Limpando a lista:
lista2.clear()
print(lista2)

# Concatenando listas:
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b) # Modifica diretamente a lista_a
print(lista_c)
print(lista_d) # Não retorna nada por ter modificado a lista_a
print(lista_a) #lista_a modificadas
```

Cuidados com dados mutáveis:
```
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() # Criando uma nova lista, mas com os mesmos itens

lista_a[0] = 'Qualquer coisa' # Modificar a lista_a não vai alterar nada na lista_b
print(lista_a)
print(lista_b)
```

For in com listas:
```
lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    print(nome, type(nome))
```

Exercício: índices e adição em lista:
```
# Solução do professor:
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
```
### Observações finais:
- Estrutura while/else é pouco usada, mas útil para certos casos.

- Sempre trate entradas do usuário para evitar erros.

- A diferença entre mutável e imutável impacta diretamente como dados são manipulados na memória.

- Entender o funcionamento interno do for com iteradores ajuda a compreender o controle de fluxo em Python.



## Dia 14

### Sumário:
1. Enumerate e desempacotamento em loops;
2. Imprecisão de ponto flutuante e decimal.Decimal;
3. Manipulação de strings: split, strip e join;
4. Introdução ao empacotamento e desempacotamento;
5. Desempacotamento em chamadas de funções e métodos;
6. Listas de listas e acesso por índice;
7. Lista de compras interativa com tratamento de exceções;
8. Comandos comuns do interpretador Python e The Zen of Python;

### 1. 
Enumerate e desempacotamento em loops:
```
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
```

Desempacotando o enumerate:
```
for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)


# Desta forma fica mais legível:
for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])


# Refazendo o anterior, mas detalhando mais ou menos o que acontece:
for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')
```

### 2. 
Imprecisão de ponto flutuante e decimal.Decimal:
```
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}') # Retorna str
print(round(numero_3, 2)) # Retorna float
```

### 3. 
Manipulação de strings: split, strip e join:
```
"""
split, strip e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip()) # .strip() corta os espaços da str

print(lista_frases_cruas)
print(lista_frases)
frases_unidas = ', '.join(lista_frases) # Unir novamente a lista em uma str
print(frases_unidas)
```

### 4. 
Introdução ao empacotamento e desempacotamento:
```
# Adiciona uma variável para cada valor da lista:
nome1, nome2, nome3 = nome =['Maria', 'Helena', 'Luiz']
print(nome3)

# a variável "resto" está pegando o que sobrou da minha lista:
_, _, nome7, *resto = ['Maria', 'Helena', 'Luiz', 'Marcos', 'Pedro']
print(nome7)

# O "_" pode ser usado em  variáveis que não serão utilizadas:
_, _, nome, *_ = ['Maria', 'Helena', 'Luiz', 'Marcos', 'Pedro']

# tuples são listas imutáveis:
lista = 'Marcos', 'Gomes', 'Portella' # Pode ser sem parênteses 
lista = ('Marcos', 'Gomes', 'Portella') # Pode ser com parênteses
tuple(_) # Pode transformar listas em tuples
list(_) # Pode transformar tuples em listas
```

### 5. 
Desempacotamento em chamadas de funções e métodos:
```
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

p, b, *_, ap, u = lista
print(p, u, ap) # Desempacotando tudo, mas exibindo valores específicos

print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
print(*lista) # Desempacotando sem for
print(*string)
print(*tupla)

print(*salas, sep='\n')
```

### 6. 
Listas de listas e acesso por índice:
```
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
print(salas[1][0][2])

for numero, sala in enumerate(salas):
    print(f'Na sala {numero + 1} temos os alunos:')
    for aluno in sala:
        print(aluno)
```

### 7. 
Exercício de lista de compras interativa com tratamento de exceções:
```
"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

# Solução do professor:
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
```

### 8. 
Comandos comuns do interpretador Python e The Zen of Python:
```
Interpretador do Python mais comuns

python mod.py (executa o mod)
python -u (unbuffered)
python -m mod (lib mod como script)
python -c 'cmd' (comando)
python -i mod.py (interativo com mod)
```

The Zen of Python, por Tim Peters

Bonito é melhor que feio.

Explícito é melhor que implícito.

Simples é melhor que complexo.

Complexo é melhor que complicado.

Plano é melhor que aglomerado.

Esparso é melhor que denso.

Legibilidade conta.

Casos especiais não são especiais o bastante para quebrar as regras.

Embora a praticidade vença a pureza.

Erros nunca devem passar silenciosamente.

A menos que sejam explicitamente silenciados.

Diante da ambiguidade, recuse a tentação de adivinhar.

Deve haver um -- e só um -- modo óbvio para fazer algo.

Embora esse modo possa não ser óbvio à primeira vista a menos que você seja holandês.

Agora é melhor que nunca.

Embora nunca frequentemente seja melhor que *exatamente* agora.

Se a implementação é difícil de explicar, é uma má ideia.

Se a implementação é fácil de explicar, pode ser uma boa ideia.

Namespaces são uma grande ideia -- vamos fazer mais dessas!


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
2. Métodos de instância e uso do self;
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