nome = 'Carlos Miguel'
altura = 1.80
peso = 95
imc = peso / (altura * altura)

'f-strings'
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'{peso} de peso e seu imc é {imc:.2f}.'

print(linha_1)
print(linha_2)

print(end='\n')

'format'
a = 'A'
b = 'BB'
c = 1.1

string = 'a={1} b={nome2:.2f} c={0} new={nome3}' # Posso escolher a ordem pelo número
formato =string.format(a, b, nome2=c, nome3=1234) # nome3 agora é um parâmetro nomeado

print(formato)