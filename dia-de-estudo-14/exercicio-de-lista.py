"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista = []
import os

while True:
    print('Selecione uma opção:')
    entrada = input('[i]nserir [a]pagar [l]istar [s]air: ')
    os.system('clear')
    if entrada == 'i':
        novo_item = input('Digite um item: ')
        lista.append(novo_item)

    elif entrada == 'l':
        if lista == []:
            print('Ainda não a nada na lista.')
        else:
            for indice, item in enumerate(lista):
                    print(indice, item)

    elif entrada == 'a':
        try:
            indice_apagar = input('Digite o índice do item para apagá-lo da lista: ')
            indice_apagar_int = int(indice_apagar)
            lista.pop(indice_apagar_int)
        except ValueError:
            print('Você não colocou um número inteiro.')
        except IndexError: 
            print('O item selecionado não existe.')
        except Exception: 
            print('Erro desconhecido')

    elif entrada == 's':
        break
    else:
        print('Você não colocou um caractere válido.')

# Solução do professor:
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
