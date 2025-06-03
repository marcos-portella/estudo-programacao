"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""


condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        condicao = False

print('Acabou')


# Contador genérico:
contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)

print('Acabou')