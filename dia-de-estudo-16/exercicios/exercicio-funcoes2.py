# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
total = 1


def multiplier(mult):
    def number(number):
        return number * mult 
    return number


duplicate = multiplier(2)
triple = multiplier(3)
quadruple = multiplier(4)


print(duplicate(5))
print(triple(5))
print(quadruple(5))


# Solução do professor:

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))