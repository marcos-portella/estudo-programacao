"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""


# Eu poderia ter diminuido o código fundindo várias partes deles
# em apenas uma linhas, mas fiz deste modo para ficar mais óbvio 
# o que está acontecendo no código, mesmo que tendo que repetir 
# em algumas partes

import os

cpf = '746.824.890-70'

digit1 = (f'{cpf[-2]}')
digit2 = (f'{cpf[-1]}')
digit1 = int(digit1)
digit2 = int(digit2)

while True:
    cpf_typed = input('Digite seu CPF: ')
    multiplier = 11
    digit_added = 0
    os.system('clear')

    if cpf_typed == 'sair':
        break

    cpf_modified = cpf_typed.replace('.', '').replace('-','')
    nine_digit = (f'{cpf_modified[:9]}')
    last_digit = (f'{cpf_modified[-1]}')
    last_digit_i = int(last_digit)

    if  last_digit_i == digit2:
        ...
    else:
        print('ERRO: CPF inválido.')
        break

    try:
        cpf_modified_i = int(cpf_modified)
    except ValueError:
        print('Digite apenas números.')
        break

    for cpf_typed_digit in nine_digit:
        multiplier -= 1
        digit_added += int(cpf_typed_digit) * multiplier

    cpf_typed_rest = (digit_added * 10) % 11

    if cpf_typed_rest > 9:
        cpf_typed_rest = 0
    else:
        cpf_typed_rest = cpf_typed_rest

    try:
        if cpf_typed_rest != digit1:
            print('ERRO: CPF inválido.')
        elif cpf_typed_rest == digit1:
            ...
    except:
        print('ERRO DESCONHECIDO')

    multiplier = 12
    ten_digits = (f'{cpf_modified[:10]}')
    digit_added = 0

    for cpf_typed_digit in ten_digits:
        multiplier -= 1
        digit_added += int(cpf_typed_digit) * multiplier
    
    cpf_typed_rest = digit_added * 10 % 11

    if cpf_typed_rest > 9:
        cpf_typed_rest = 0
    else:
        cpf_typed_rest = cpf_typed_rest
    
    try:
        if cpf_typed_rest != digit2:
            print('ERRO: CPF inválido.')
        elif cpf_typed_rest == digit2:
            print('CPF válido')
    except:
        print('ERRO DESCONHECIDO')