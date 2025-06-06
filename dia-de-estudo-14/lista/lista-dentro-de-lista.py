"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
print(salas[1][0][2])

for numero, sala in enumerate(salas):
    print(f'Na sala {numero + 1} temos os alunos:')
    for aluno in sala:
        print(aluno)