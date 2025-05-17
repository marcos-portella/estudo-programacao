# if / elif      / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou  "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'Entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu no sistema')
elif entrada == 'Sair':
    print('Você saiu no sistema')
else:
    print('Você não digitou nem entrar e nem sair. ')

print('FORA DOS BLOCOS') # Sempre será executado


condicao = True # Vai ser executado

if condicao:
    print('Este é o código do if')


condicao2 = False # Não vai ser executado

if condicao2:
    print('Este é o código do if2') # Não foi executado
else:
    print('Este é o novo código do if2') #Foi executado no lugar

# Outro exemplo:

if 10==10: # True
    print('Verdadeiro if3')
else:
    print('Falso if3')

if 10==11: #False
    print('Verdadeiro if4')
else:
    print('Falso if4')
print('Fora do if') # Sempre será executado

# Especificando condições:

condicao1 = False
condicao2 = False
condicao3 = False
condicao4 = False

if condicao1:
    print('Verdadeiro 1')
elif condicao2:
    print('Verdadeiro 2')
elif condicao3:
    print('Verdadeiro 3')
elif condicao4:
    print('Verdadeiro 4')
else:
    print('Nenhuma condição foi satisfeita ')