# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu): 0   0.0   ''  False
# Também existe o tipo None que é
# usado para representar um não valor


# # Um exemplo do operador "and":

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

## Avaliação de curto cicuito:
print(True and 0 and True ) # Ele para no 0

senha = input('Senha: ') or 'Sem senha'
print(senha) # Se não digitar nada ele mostra "sem senha"

# Um exemplo do operador "or":
entrada2 = input('[E]ntrar [S]air: ')
senha_digitada2 = input('Senha: ')

senha_permitida2 = '123456'

if (entrada2 == 'E' or entrada == 'e') and senha_digitada2 == senha_permitida2:
    print('Entrar')
else:
    print('Sair')

# Um exemplo do operador not:

# Operador lógico "not" usado para inverter expressões
#not True = False
#not False = True

senha2 = input('Senha: ')

if not senha2:
    print('Você não digitou nada')

# exemplos de "not":
print(not 0)
print(not True)
print(not False)