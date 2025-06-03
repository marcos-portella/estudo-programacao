"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""

# Operador de soma (int):
contador = 0

while contador < 10:
    contador += 1
    print(contador)

print('Acabou')


# Operadores de soma (str):
contador = '1'

while contador < '12':
    contador += '2'
    print(contador)

print('Acabou')


# Operador de multiplicação:
contador = 10

while contador < 10:
    contador *= '2'
    print(contador)

print('Acabou')


# Operador de subtração:
contador = 20

while contador > 10:
    contador -= 1
    print(contador)

print('Acabou')


#  Operador de divisão:
contador = 125

while contador > 5:
    contador /= 5
    print(contador)

print('Acabou')


# Operador de divisão inteira:
contador = 125

while contador > 5:
    contador /= 5
    print(contador)

print('Acabou')


# Operador de potenciação:
contador = 10

while contador < 10000:
    contador **= 2
    print(contador)

print('Acabou')


# Operador de módulo:
contador = 21

while contador > 10:
    contador %= 2
    print(contador)

print('Acabou')