"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

# Exemplificando todos os tipos:

variavel = 'ABC'

print(f'{variavel}')

print(f'{variavel: >10}') # Ele adciona caracteres para a esquerda até somar 10
print(f'{variavel:$<10}') # Ele adciona caracteres para a direita até somar 10
print(f'{variavel:$^10}') # Ele centraliza a str e adciona nas laterais até somar 10
print(f'{1000.4873648123746:0=+10,.1f}') # O + mostra se o número é positivo oou negativo, apenas para saber que existe, provavemente não iremos usar
print(f'O hexadecimal de 150 é {1500:08x}') # hexadecimal em formatação fstrings
print(f'{variavel!r}') # Chama o método __repr_ de dentro desta str, mais para frente veremos mais sobre isto
