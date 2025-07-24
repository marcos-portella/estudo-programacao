## Dia 13

### Prefácio:

Hoje consolidamos nosso entendimento sobre as estruturas de repetição, explorando funcionalidades avançadas dos loops ``while`` e ``for``, e aplicando esses conhecimentos na resolução de problemas práticos, como a criação de uma calculadora e um jogo de adivinhação de palavras. Aprofundamos na utilização do ``else`` com ``while``, na contagem de caracteres e na iteração de listas. Além disso, introduzimos as listas, um tipo de dado mutável e versátil, e os cuidados necessários ao copiá-las.

### Loops ``while`` e ``for`` em Detalhe:

Revisitamos os loops ``while`` e ``for``, compreendendo suas aplicações ideais. O ``while`` é preferível quando o número de repetições é desconhecido e depende de uma condição, enquanto o ``for`` é mais adequado para iterar sobre sequências (como strings e listas) onde o número de iterações é geralmente conhecido.

- ``while/else``: Embora não seja muito comum, o bloco ``else`` em um loop ``while`` é executado quando a condição do ``while`` se torna falsa naturalmente (ou seja, o loop não foi interrompido por um ``break``).

````
# Exemplo 1: while/else
string = 'Valorqualquer'
i = 0
while i < len(string):
    letra = string[i]
    if letra == ' ':
        break # Se encontrar um espaço, o else não será executado
    print(letra)
    i += 1
else: # Este bloco só executa se o loop while terminar sem um 'break'
    print('Não encontrei um espaço na string.')
print('Fora do while')
````

- **``for`` com ``range()``**: A ``função range()`` é comumente usada com o ``for`` para gerar sequências numéricas, permitindo iterar um número específico de vezes ou sobre índices.

````
# Exemplo 2: for com range
numeros = range(0, 10, 2) # Gera números de 0 a 9, pulando de 2 em 2 (0, 2, 4, 6, 8)
for numero in numeros:
    print(numero)
````

- **``for`` com ``break`` e ``continue``**: Assim como no ``while``, ``break`` e ``continue`` funcionam da mesma forma no for para controlar o fluxo da iteração. O ``else`` também pode ser usado com ``for``, executando se o loop terminar sem um ``break``.

````
# Exemplo 3: for com break, continue e else
for i in range(5):
    if i == 2:
        print('Pulando o 2...')
        continue # Pula a iteração atual
    if i == 4:
        print('Encerrando no 4.')
        break # Sai do loop
    print(i)
else: # Só executa se o loop não for interrompido por 'break'
    print('Loop for completo com sucesso!')
````

### Introdução às Listas:

As **listas** em Python são um tipo de dado **mutável** que pode armazenar vários valores de qualquer tipo. Elas são ordenadas, indexadas e suportam fatiamento, similar às strings.

- **Criação e Acesso**: Listas são criadas usando colchetes ``[]`` e os elementos são separados por vírgulas. O acesso aos elementos é feito por índice.

````
# Exemplo 4: Criação e acesso a elementos de uma lista
lista = [123, True, 'Luiz Otávio', 1.2, []] # Pode conter diferentes tipos de dados
print(lista[2]) # Saída: 'Luiz Otávio'
lista[2] = 'Maria' # Listas são mutáveis, podemos alterar elementos
print(lista) # Saída: [123, True, 'Maria', 1.2, []]
````

- **Métodos Úteis de Listas**:

    - ``append()``: Adiciona um elemento ao final da lista.

    - ``insert(indice, valor)``: Insere um elemento em um índice específico.

    - ``pop(indice)``: Remove e retorna um elemento de um índice específico (ou o último, se o índice for omitido).

    - ``del lista[indice]``: Deleta um elemento de um índice específico.

    - ``clear()``: Remove todos os elementos da lista.

    - ``extend()``: Adiciona os elementos de um iterável ao final da lista.

    - ``+``: Concatena duas listas, criando uma nova lista.

````
# Exemplo 5: Métodos de listas
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_a.append(7) # Adiciona 7
print(lista_a) # Saída: [1, 2, 3, 7]

lista_a.insert(0, 'Inicio') # Insere 'Inicio' no índice 0
print(lista_a) # Saída: ['Inicio', 1, 2, 3, 7]

removido = lista_a.pop() # Remove o último elemento (7)
print(lista_a, 'Removido:', removido) # Saída: ['Inicio', 1, 2, 3] Removido: 7

del lista_a[0] # Deleta o elemento no índice 0 ('Inicio')
print(lista_a) # Saída: [1, 2, 3]

lista_c = lista_a + lista_b # Concatena as listas
print(lista_c) # Saída: [1, 2, 3, 4, 5, 6]

lista_a.extend(lista_b) # Estende lista_a com os elementos de lista_b
print(lista_a) # Saída: [1, 2, 3, 4, 5, 6] (lista_a foi modificada)
````

### Cuidados com Dados Mutáveis (Cópia de Listas):
Ao atribuir uma lista a outra variável usando ``=``, não estamos criando uma cópia independente, mas sim uma **referência** para a mesma lista na memória. Isso significa que alterações em uma variável afetarão a outra. Para criar uma cópia independente, usamos o método ``.copy()``.

````
# Exemplo 6: Cópia de listas e dados mutáveis
lista_original = ['item1', 'item2']
lista_referencia = lista_original # Ambas apontam para o mesmo objeto na memória
lista_copia = lista_original.copy() # Cria uma nova lista independente

lista_original[0] = 'NOVO ITEM'

print(lista_original)  # Saída: ['NOVO ITEM', 'item2']
print(lista_referencia) # Saída: ['NOVO ITEM', 'item2'] (também foi alterada)
print(lista_copia)     # Saída: ['item1', 'item2'] (permanece inalterada)
````

### Observações Finais:

As listas são estruturas de dados extremamente versáteis e fundamentais em Python, permitindo organizar e manipular coleções de informações. O entendimento de sua mutabilidade e dos métodos disponíveis é crucial para o desenvolvimento eficaz. A distinção entre atribuição por referência e cópia explícita (``.copy()``) é vital para evitar bugs sutis em programas que manipulam dados mutáveis. Continue praticando a criação, manipulação e iteração de listas em conjunto com os loops para aprimorar suas habilidades de programação.