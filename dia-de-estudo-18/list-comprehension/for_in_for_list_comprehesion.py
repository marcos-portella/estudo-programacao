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