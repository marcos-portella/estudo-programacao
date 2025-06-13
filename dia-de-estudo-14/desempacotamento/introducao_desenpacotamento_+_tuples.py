"""
Introdução ao empacotamento e desempacotamento
"""
# Adiciona uma variável para cada valor da lista:
nome1, nome2, nome3 = nome =['Maria', 'Helena', 'Luiz']
print(nome3)

# a variável "resto" está pegando o que sobrou da minha lista:
_, _, nome7, *resto = ['Maria', 'Helena', 'Luiz', 'Marcos', 'Pedro']
print(nome7)

# O "_" pode ser usado em  variáveis que não serão utilizadas:
_, _, nome, *_ = ['Maria', 'Helena', 'Luiz', 'Marcos', 'Pedro']

# tuples são listas imutáveis:
lista = 'Marcos', 'Gomes', 'Portella' # Pode ser sem parênteses 
lista = ('Marcos', 'Gomes', 'Portella') # Pode ser com parênteses
tuple(_) # Pode transformar listas em tuples
list(_) # Pode transformar tuples em listas


