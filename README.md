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