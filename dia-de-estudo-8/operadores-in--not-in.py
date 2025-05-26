# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 # ídices positivos
#  O t á v i o
# -6-5-4-3-2-1 # índices negativos

nome = 'Otávio'

print(nome[2])
print(nome[-4])

# in, not in:

print('á' in nome) # True
print('z' in nome) # False
print('Otá' not in nome) # False
print('zin' not in nome) # True

nome2 = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')