import json

from _class_exercise_a import CAMINHO_ARQUIVO, Pessoa, fazer_dump

# fazer_dump()

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)