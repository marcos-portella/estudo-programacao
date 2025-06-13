"""
Exercício
Exiba os ídices da lista
Adicione um valor na sua lista
"""

lista = ['Maria', 'Pedro', 'Luiza']
lista.append('João')
pos = -1

for itens in lista:
    pos += 1
    print(pos, itens)


# Solução do professor:
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
    