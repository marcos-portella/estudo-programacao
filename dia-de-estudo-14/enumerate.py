"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# Desenpacotando o enumerate:
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