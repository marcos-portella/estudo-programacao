# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

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