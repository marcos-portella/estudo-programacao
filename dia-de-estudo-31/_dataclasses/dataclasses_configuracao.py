from dataclasses import dataclass


@dataclass(repr=True)
class Pessoa:
    nome: str
    sobrenome: str


lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
print(ordenadas)
