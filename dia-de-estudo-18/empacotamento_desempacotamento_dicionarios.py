# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a # invertendo o valor dos itens de forma rápida
print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}


(a1, a2), (b1, b2) = pessoa.items() # Desempacota os item diretamente nas variáveies
print(a1, a2)
print(b1, b2)


for chave, valor in pessoa.items(): # Desempacotando com for
    print(chave, valor)



dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa} # Desempacontando dentro de outro dicionário
print(pessoas_completa)



# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs): # Mostra argumentos nomeados
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


mostro_argumentos_nomeados(nome='Joana', qlq=123) # Melhor para adicionar argumentos um por um
mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = { # Adiconando argumentos e valores de forma mais organizada
     'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes) # Pode usar para executar um print
