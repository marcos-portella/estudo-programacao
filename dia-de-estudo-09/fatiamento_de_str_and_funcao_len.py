"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4:]) # Omitir o final ele vai pegar o resto da frase
print(variavel[4:6]) # Escolhendo aonde ele para o fatiamento
print(variavel[:5]) # Omitir o início ele vai começar pelo começo da frase

# Função len

print(len(variavel[3])) # Mostra a quantidade de caracteres dentos da fatia escolhida
print(len(variavel)) # Mostra a quantidade de caracteres dentos da sua str

print(variavel[0:len(variavel):1]) # Neste modelo len(variavel) equivale a 9

# Passo:

print(variavel[0:9:1]) # Passo de um em um 
print(variavel[0:9:2]) # Passo de dois em dois 
print(variavel[-1:-10:-1]) # Passo de trás para frente
