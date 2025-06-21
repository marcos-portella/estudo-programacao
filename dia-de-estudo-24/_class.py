# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Luiz', 'Otávio')

p2 = Pessoa('Maria', 'Joana')

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)


# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código
# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()


# Escopo da classe e de métodos da classe
class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comando {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('maçã'))