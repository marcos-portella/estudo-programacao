## Curso Udemy - Python do Básico ao Avançado

Este arquivo contém resumos e anotações das aulas
do curso de Python feito na plataforma Udemy.



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