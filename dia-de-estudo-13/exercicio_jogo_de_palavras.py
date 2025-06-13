"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

# Não consegui fazer tentativas ilimitadas e com isso não consegui a contagem de tentativas do usuário:

palavra_certa = "gato"
palavra_formada = ''

print(f'A palavra tem {len(palavra_certa)} letras')

for letra in palavra_certa:
    letra_digitada = input('Digite uma letra: ')
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        break
    else:
        if palavra_certa != palavra_formada:
            if letra_digitada == letra:
                palavra_formada += letra
                print(palavra_formada)
                if palavra_certa == palavra_formada:
                    print('Parabéns!!! Você acertou a palavra')
                    break
                else:
                    continue
            elif letra_digitada != letra:
                palavra_formada += '*'
                print(palavra_formada)

            if len(palavra_certa) == len(palavra_formada):
                print('Você não acertou a palavra, tente novamente')
                continue
            else:
                continue

# Solução do professor:

import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0

# Entendi, se começar com while posso ter infinitas tentativas.