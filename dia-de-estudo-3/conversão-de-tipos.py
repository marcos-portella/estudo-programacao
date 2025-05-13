'''
conversão de tipos, coerção
type convertion, typecasting, coercion
é o ato de converter um tipo em outro.
 Tipos imutáveis e primitivos:
 str, int, floatt, bool
'''

print(1+1)
print('a'+'b')
# print('1'+1) # não pode concatenar str com int


print(int('1'), type(int('1'))) # converteu o str para int
print(int('1')+1)

print(float('1')+1, type(float('1')+1)) #coverteu str em float


# converteu em bool
print(bool('')) # False
print(bool(' '))# True

print(str(11)+'b') # converte para str
