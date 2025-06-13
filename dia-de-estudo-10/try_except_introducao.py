"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_float = float(numero_str) # fail fast
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float*2:.2f}')
except:
    print('Isso não é um número')



# Testando a mensagem de erro (exceção):

print(1234) # Vai executar normalmente
print(456) # vai executar normalmente
int('a') # Ocorreu um erro, ele descreve o erro para você