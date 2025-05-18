# =====================================
# 🐍 Curso Udemy - Python do Básico ao Avançado
# =====================================

### Este arquivo contém resumos e anotações das aulas
### do curso de Python feito na plataforma Udemy.

# =====================================
# 📅 Dia 1 – Primeiros Passos com Python
# =====================================

## ---------- Configurando o Visual Studio Code ----------
### Hoje aprendi a configurar o VS Code (Visual Studio Code)
### de forma funcional para acompanhar as aulas de Python.
### Usei o arquivo "settings.json" para personalizar o ambiente.
### Mesmo com interfaces gráficas, aprender a configurar manualmente
### ajuda a entender melhor a ferramenta.

## ---------- Meu Primeiro Código ----------
print('hello, world')  # Meu primeiro programa em Python 🎉

### Me senti motivado e acredito que vou gostar cada vez mais
### conforme o curso avança.

# =====================================
# 📅 Dia 2 – Impressões, Comentários e Strings
# =====================================

## ---------- Funções do print ----------

## Aprendi sobre os parâmetros:
### \n   -> quebra de linha
### sep= -> define o separador
### end= -> define o final da linha

print('Python', 'é', 'legal', sep='-', end='!\n')  # Exemplo usando sep e end

## ---------- Tipos de Comentários ----------

## Comentário de uma linha usa #
"""

Este é um comentário
de várias linhas usando DocString

"""

### O Python lê da esquerda para a direita e de cima para baixo.

## ---------- Tipos de Dados e Strings ----------

## Escape de caracteres com \
print("Linha 1\nLinha 2")  # \n cria uma quebra de linha

## Strings raw (cruas) usando o prefixo 'r'
print(r"C:\Users\nome")  # Mostra literalmente a barra invertida

## ---------- Conceitos Técnicos ----------

### Linguagem: Python
### Tipagem: Dinâmica / Forte
### Tipo 'str': Representa strings (textos)
### Strings são textos dentro de aspas simples ou duplas


# =====================================
# 📅 Dia 3 – Variáveis, Tipos e Strings
# =====================================

## ---------- Variáveis e Tipagem Dinâmica ----------

### Em Python, não é necessário declarar o tipo da variável.
### O interpretador define automaticamente baseado no valor.

nome = "Ana"        # str

idade = 25          # int

altura = 1.68       # float

ativo = True        # bool

## ---------- Concatenando Strings ----------
print("Olá, " + nome)             # Concatenação com +

print("Python! " * 3)             # Repetição com *

## ---------- Conversão de Tipos ----------
print("Idade: " + str(idade))     # Convertendo int para str

num = int("10")                   # string para int

pi = float("3.14")                # string para float

## ---------- Verificando tipos com type() ----------
print(type(nome))                 # <class 'str'>

print(type(idade))                # <class 'int'>

print(type(pi))                   # <class 'float'>

## ---------- Resumo ----------

### ✅ Variáveis são atribuídas com =
### ✅ Tipos são inferidos automaticamente
### ✅ Conversão: int(), str(), float()
### ✅ type() retorna o tipo da variável


# =====================================
# 📅 Dia 4 – Operações Aritméticas e Formatação
# =====================================

## ---------- Operações Aritméticas ----------
### Hoje aprendi que o python permite realizar todas as operações 
### matemáticas básicas

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

## Verificando divisibilidade
print(10 % 8 == 0)  # False

print(16 % 8 == 0)  # True

## ---------- Introdução à Formatação ----------
### Gostei da f-strings:, é forma de formatar strings 

nome = 'Carlos Miguel'

altura = 1.80

peso = 95

imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f}m de altura,'

linha_2 = f'pesa {peso}kg e seu IMC é {imc:.2f}.'

print(linha_1)

print(linha_2)

## Espaço para separar blocos de saída
print(end='\n')

## ---------- Outra forma: format() ----------
a = 'A'

b = 'BB'

c = 1.1

## Podemos misturar índices e nomes nomeados
string = 'a={1} b={nome2:.2f} c={0} new={nome3}'

formato = string.format(a, b, nome2=c, nome3=1234)

print(formato)

## ---------- Resumo do Dia ----------
### ✅ Operações: +, -, *, /, //, **, %
### ✅ Módulo (%) verifica restos e divisibilidade
### ✅ f-strings: forma moderna e prática de formatar textos
### ✅ format(): alternativa mais antiga, ainda útil com nomeação e ordem


# =====================================
# 📅 Dia 5 – Entrada de Dados e Conversão
# =====================================

## ---------- Coletando entrada do usuário ----------
### input() sempre retorna uma string (str), mesmo que o usuário digite um número

nome = input('Qual o seu nome? ')

print(f'O seu nome é {nome}')

## ---------- Tentativa de somar números diretamente ----------
### Erro comum: somar strings resulta em concatenação (ex: "5" + "5" = "55")

numero_1 = input('Digite um número: ')

numero_2 = input('Digite outro número: ')

## Aqui ocorre concatenação, não soma aritmética
print(f'A soma do primeiro par de números é: {numero_1 + numero_2}')  # Ex: "2" + "3" = "23"

## ---------- Corrigindo com conversão de tipos ----------
### Convertendo para int com int(), o Python entende como números

numero_3 = int(input('Digite um número: '))

numero_4 = int(input('Digite outro número: '))

## Agora é uma soma real entre inteiros
print(f'A soma do segundo par de números é: {numero_3 + numero_4}')

## ---------- Melhor forma (até agora) ----------
### Separar entrada e conversão ajuda na legibilidade

numero_5 = input('Digite um número: ')

numero_6 = input('Digite outro número: ')

## Ainda não há tratamento de erro, mas essa estrutura é mais clara
int_numero_5 = int(numero_5)

int_numero_6 = int(numero_6)

print(f'Soma (forma melhorada): {int_numero_5 + int_numero_6}')

## ---------- Observação importante ----------
### ⚠️ Se o usuário digitar algo que não seja número, o programa vai quebrar!
### Para evitar isso, é necessário tratar erros o que será aprendido depois.

## ---------- Resumo do Dia ----------
### ✅ input() sempre retorna uma string
### ✅ Para fazer contas, converta com int() ou float()
### ✅ Cuidado: somar strings resulta em concatenação
### ✅ Separar entrada e conversão melhora a clareza
### 🚨 Futuramente: aprenderemos a validar entradas para não ocorrer erros


# =====================================
# 📅 Dia 6 – Estruturas Condicionais em Python
# =====================================

## ---------- if / elif / else ----------
## Usamos essas estruturas para executar blocos de código diferentes de acordo com condições.

entrada = input('Você quer "entrar" ou "sair"? ')

## Verificando a entrada do usuário
if entrada == 'entrar' or entrada == 'Entrar':
    print('Você entrou no sistema.')
elif entrada == 'sair' or entrada == 'Sair':
    print('Você saiu do sistema.')
else:
    print('Você não digitou nem "entrar" nem "sair".')

print('FORA DOS BLOCOS')  # Sempre será executado

## ---------- Blocos condicionais com booleanos ----------

condicao = True

if condicao:
    print('Este é o código do if (condição é True)')

condicao2 = False

if condicao2:
    print('Este é o código do if2 (não será executado)')
else:
    print('Este é o novo código do if2 (executado pois condição2 é False)')

## ---------- Comparações diretas ----------

if 10 == 10:
    print('Verdadeiro if3')  # Será executado
else:
    print('Falso if3')

if 10 == 11:
    print('Verdadeiro if4')
else:
    print('Falso if4')  # Será executado

print('Fora do if')  # Sempre executado

## ---------- Encadeando condições ----------

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

## ---------- Resumo do Dia ----------
### ✅ if → executa um bloco se a condição for True
### ✅ elif → checa nova condição caso o if falhe
### ✅ else → executa se nenhuma condição anterior for satisfeita
### ✅ Blocos fora do if sempre são executados normalmente
### ✅ Podemos comparar valores diretamente (ex: 10 == 10)
### ✅ É possível encadear várias condições com elif
