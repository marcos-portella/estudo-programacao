nome = input('Qual o seu nome? ')

print(f'O seu nome é {nome}')


numero_1 = input('Digite um número: ') # Aqui deu erro por ser str
numero_2 = input('Digite outro número: ') # Aqui també deu erro por ser str
numero_3 = int(input('Digite um número: ')) # Aqui deu ser por ter mudado o tipo, mas existem outras formas melhores
numero_4 = int(input('Digite outro número: ')) # Aqui também deu certo, mas existe outras formas melhores

print(f'A soma do primeiro par de números é: {numero_1+numero_2}')
print(f'A soma do segundo par de números é: {numero_3+numero_4}')



# Melhor forma por enquanto

numero_5 = input('Digite um número: ')
numero_6 = input('Digite outro número: ')

# Zona para ver se o usuário escreveu realmente um número, mas ainda não aprendi isso

int_numero_5 = int(numero_5)
int_numero_6 = int(numero_6)