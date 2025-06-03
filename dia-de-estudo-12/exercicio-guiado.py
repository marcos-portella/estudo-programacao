"""
Exercício iterando strings com while
"""

nome = 'Luiz Otávio'  
repeticao = 0
num = 0
nome2 = ''

while repeticao < len(nome):
    nome_edit = ('*' + nome[num])
    nome2 += nome_edit
    num += 1
    repeticao += 1
nome2 += '*'
print(nome2)


# Solução do professor:

nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)