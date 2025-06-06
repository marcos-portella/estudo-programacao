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


import os
cpf_guardado = '746.824.890-70'
digito_1_guardado = (f'{cpf_guardado[-2]}')
digito_2_guardado = (f'{cpf_guardado[-1]}')
digito_1_guardado = int(digito_1_guardado)
digito_2_guardado = int(digito_2_guardado)

while True:
    cpf_digitado = input('Digite seu CPF: ')
    multiplicador = 11
    digitos_cpf_digitado_somados = 0
    os.system('clear')

    if cpf_digitado == 'sair':
        break

    cpf_digitado_modificado = cpf_digitado.replace('.', '').replace('-','')
    nove_digitos_cpf_digitado = (f'{cpf_digitado_modificado[:9]}')
    ultimo_digito = (f'{cpf_digitado_modificado[-1]}')
    ultimo_digito_int = int(ultimo_digito)

    if  ultimo_digito_int == digito_2_guardado:
        ...
    else:
        print('ERRO: CPF inválido.')
        break

    try:
        cpf_digitado_modificado_int = int(cpf_digitado_modificado)
    except ValueError:
        print('Digite apenas números.')
        break

    for digito_atual_cpf_digitado in nove_digitos_cpf_digitado:
        multiplicador -= 1
        digito_atual_cpf_digitado_int = int(digito_atual_cpf_digitado)
        digito_atual_cpf_digitado_mult = digito_atual_cpf_digitado_int * multiplicador
        digitos_cpf_digitado_somados += digito_atual_cpf_digitado_mult
    
    digitos_cpf_digitado_somados_mult = digitos_cpf_digitado_somados * 10
    digitos_cpf_digitado_somados_mult_resto = digitos_cpf_digitado_somados_mult % 11

    if digitos_cpf_digitado_somados_mult_resto > 9:
        digitos_cpf_digitado_somados_mult_resto = 0
    else:
        digitos_cpf_digitado_somados_mult_resto = digitos_cpf_digitado_somados_mult_resto

    try:
        if digitos_cpf_digitado_somados_mult_resto != digito_1_guardado:
            print('ERRO: CPF inválido.')
        elif digitos_cpf_digitado_somados_mult_resto == digito_1_guardado:
            ...
    except:
        print('ERRO DESCONHECIDO')

    multiplicador = 12
    dez_digitos_cpf_digitado = (f'{cpf_digitado_modificado[:10]}')
    digitos_cpf_digitado_somados = 0

    for digito_atual_cpf_digitado in dez_digitos_cpf_digitado:
        multiplicador -= 1
        digito_atual_cpf_digitado_int = int(digito_atual_cpf_digitado)
        digito_atual_cpf_digitado_mult = digito_atual_cpf_digitado_int * multiplicador
        digitos_cpf_digitado_somados += digito_atual_cpf_digitado_mult
    
    digitos_cpf_digitado_somados_mult = digitos_cpf_digitado_somados * 10
    digitos_cpf_digitado_somados_mult_resto = digitos_cpf_digitado_somados_mult % 11

    if digitos_cpf_digitado_somados_mult_resto > 9:
        digitos_cpf_digitado_somados_mult_resto = 0
    else:
        digitos_cpf_digitado_somados_mult_resto = digitos_cpf_digitado_somados_mult_resto
    
    try:
        if digitos_cpf_digitado_somados_mult_resto != digito_2_guardado:
            print('ERRO: CPF inválido.')
        elif digitos_cpf_digitado_somados_mult_resto == digito_2_guardado:
            print('CPF válido')
    except:
        print('ERRO DESCONHECIDO')

# Solução do professor:

import re
import sys


entrada = input('CPF [746.824.890-70]: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')

# Achei que era para puxar um CPF que já estaria em um banco de dados
# salvo na empresa :(
    