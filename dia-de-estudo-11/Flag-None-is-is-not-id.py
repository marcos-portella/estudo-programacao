'''
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (9tipo, valor, identidade)
id = Identidade
'''

# O id pode acabar sendo o mesmo dependendo o valor da variavel
v1 = 'a'
v2 = 'a' 
print(id(v1))
print(id(v2))


# None, is, is not:
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True # Nossa bandeira
    print('Faça alogo')
else:
    print('Não faça algo')

print(passou_no_if is None) # Se passar na bandeira retorna False
print(passou_no_if is not None) # Se passar na bandeira retorna True

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')

# Pode usar o debuger também