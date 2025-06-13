# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

import os

correct = 0
counter = 0
flag = 0

for pergunta in perguntas:
    counter += 1
    print('Pergunta', pergunta['Pergunta'])
    print()

    for index, options in enumerate(pergunta['Opções']):
        print(f'({index + 1})', options)

    print()

    answer = input('Escreva o índice da resposta correta: ')

    if answer == 'sair':
        break
    
    try:
        answer = int(answer)
    except ValueError:
        os.system('clear')
        print('Digite apenas ídices válidos.')
        counter = 0
        break

    if answer > 4 or answer < 1:
        os.system('clear')
        print()
        print('Digite apenas ídices válidos')
        counter = 0
        break

    if counter == 1:
        if answer == 3:
            print()
            print('Parabéns, você acertou esta questão.🎉🎊')
            print()
            correct += 1
        else:
            print()
            print('Resposta incorreta.❌')
            print()

    elif counter == 2:
        if answer == 1:
            print()
            print('Parabéns, você acertou esta questão.🎉🎊')
            print()
            correct += 1
        else:
            print()
            print('Resposta incorreta.❌')
            print()

    elif counter == 3:
        if answer == 2:
            print()
            print('Parabéns, você acertou esta questão.🎉🎊')
            correct += 1
            flag = 1
        else:
            flag = 1
            print()
            print('Resposta incorreta.❌')

if flag == 1:
    print()
    if correct == 1:
        print('Você acertou 1 de 3.')
    elif correct == 2:
        print('Você acertou 2 de 3.')
    elif correct == 3:
        print('Você acertou 3 de 3.')
    if correct == 0:
        print('Você acertou 0 de 3.')

# Solução do professor:

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
    


    
        