# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.


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
