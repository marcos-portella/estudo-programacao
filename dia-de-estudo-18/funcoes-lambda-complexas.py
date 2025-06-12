def executa(funcao, *args): # Função de execução
    return funcao(*args)


def soma(x, y): #Função de soma
    return x + y


def cria_multiplicador(multiplicador): # Função de multiplicão
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


duplica = cria_multiplicador(2)


duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))

print(
    executa(
        lambda x, y: x + y, # Acaba ficando muito complexo, usar lambda para coisas rápidas
        2, 3
    ),
)

print(
    executa(
        lambda *args: sum(args), # Soma todos os parâmetros que ela receber
        1, 2, 3, 4, 5, 6, 7
    )
)