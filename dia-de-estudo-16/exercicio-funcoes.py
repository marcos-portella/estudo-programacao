# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.



def mult(*args):
    result = 1
    for number in args:
        result *= number
    return result

total = (mult(1, 2, 3, 4, 5))
print(total)

# Solução do professor:

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicação = multiplicar(10, 2, 3, 4, 5)
print(multiplicação)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(number):
    rest= number % 2
    if rest == 0:
        return f'{number} é Par'
    return f'{number} é Impar'

print(par_impar(7))


# Solução do professor:

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'


outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)

print(par_impar(3))

print(par_impar is outro_par_impar)