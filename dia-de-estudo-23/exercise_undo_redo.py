# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os

l1 = None
l2 = []

while True:
    command = input('Digite o quer adicionar a lista ou selecione os comandos: sair, listar, desfazer e refazer : ')
    os.system('clear')
    command_lower = command.lower()

    if command_lower == 'sair':
        os.system('clear')
        break
    
    elif command_lower == 'listar':
        if l1 == None:
            print('Nada a listar')
            print()

        else:
            print(l1)
            print()
    
    elif command_lower == 'desfazer':
        if l1 == [] or l1 == None:
            print('Nada para desfazer')
            print()

        else:
            item = l1.pop()
            l2.append(item)
            print(l1)
            print()

    elif command_lower == 'refazer':
        if l2 == []:
            print('Nada para refazer')
            print()

        else:
            item = l2.pop()
            l1.append(item)
            print(l1)
            print()

    else:
        if l1 == None:
            l1 = []
            l1.append(command)

        else:
            l1.append(command)

# Solução do professor:

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'clear':
        os.system('clear')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue