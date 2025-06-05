"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() # Criando uma nova lista, mas com os mesmos itens

lista_a[0] = 'Qualquer coisa' # Modificar a lista_a não vai alterar nada na lista_b
print(lista_a)
print(lista_b)