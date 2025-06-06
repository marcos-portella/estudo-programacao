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