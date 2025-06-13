# É possível alterar facilmente as listas se necessário:
lista2 = [10, 20, 30, 40]
numero = [lista2[2]]
print(numero)

lista2[2] = 300
print(lista2[2])
print(lista2)

#  Adcionando valores na lista:
lista2.append(50)
lista2.append(60)
print(lista2)


#  Removendo valores na lista:
lista2.append(50)
lista2.append(60)
lista2.pop() # Remove o último item da lista
lista2.append(70)
lista2.append(80)
print(lista2)
ultimo_valor = lista2.pop()
print (lista2, 'Removido:', ultimo_valor)

#  Removendo valores específicos na lista:
lista2.pop(2)
print(lista2)

# Deletando itens da lista:
del lista2[-1]
print(lista2)

#inserindo valores na lista:
lista2.insert(0, 'MM')
print(lista2)

# Limpando a lista:
lista2.clear()
print(lista2)

# Concatenando listas:
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b) # Modifica diretamente a lista_a
print(lista_c)
print(lista_d) # Não retorna nada por ter modificado a lista_a
print(lista_a) #lista_a modificadas