## Dia 11

### Prefácio:

Hoje exploramos conceitos mais aprofundados sobre os tipos de dados em Python, focando na **imutabilidade** e em **métodos de string** que expandem nossas capacidades de manipulação de texto. Além disso, compreendemos a distinção entre comparação de valor (``==``) e comparação de identidade (``is``), introduzindo o uso de ``None`` como um "não valor" e a função ``id()``.

### Tipos Imutáveis e Métodos de String:

Em Python, alguns tipos de dados são **imutáveis**, o que significa que seu valor não pode ser alterado após a criação. Ao invés de modificar um objeto imutável, uma nova instância é criada. Os tipos que já vimos e são imutáveis incluem **strings (``str``)**, **inteiros (``int``)**, **ponto flutuante (``float``)** e **booleanos (``bool``)**.

Strings, por exemplo, não podem ser modificadas diretamente. Quando parecemos "modificá-las", na verdade estamos criando uma nova string. Para manipular strings, usamos **métodos de string**, que são funções que operam sobre objetos string e retornam uma nova string com as modificações desejadas.

Exemplos de métodos de string e imutabilidade:

````
# Exemplo 1: Imutabilidade de strings
string = '1000'
# string[0] = '2' # Isso geraria um erro, pois strings são imutáveis

# Exemplo 2: Uso de f-string para "modificar" uma string (na verdade, cria uma nova)
outra_variavel = f'{string[:3]}ABC{string[3:]}' 
print(string)         # Saída: 1000
print(outra_variavel) # Saída: 100ABC0 (nota: o exemplo original tinha [4:] o que resultaria em 100ABC)
                      # Correção para o exemplo do arquivo: se string = '1000', [4:] é vazio.
                      # Para o resultado desejado, a string original deveria ser maior ou o slice diferente.
                      # Considerando o '1000', string[:3] é '100', string[3:] é '0'. Então, '100ABC0'

# Exemplo 3: Método de string zfill() - preenche com zeros à esquerda
print(string.zfill(10)) # Saída: 0000001000
````

É importante consultar a documentação oficial do Python ([Python Standard Library](https://docs.python.org/pt-br/3/library/stdtypes.html)) para explorar a vasta gama de métodos de string e funções built-in disponíveis.

### ``None``, ``is``, ``is not`` e ``id()`` (Comparação por Identidade):

Além da comparação de valor (``==`` e ``!=``), Python oferece operadores para comparar a identidade de objetos na memória.

- ``None``: Representa a ausência de valor ou um valor nulo. É frequentemente usado como um placeholder para indicar que uma variável não tem um valor significativo ainda.

- ``is`` e ``is not``: Operadores que verificam se duas variáveis referenciam o **mesmo objeto** na memória (ou seja, se têm a mesma identidade, o mesmo ``id``). Isso é diferente de ``==`` e ``!=``, que comparam apenas os valores dos objetos.

- ``id()``: Função built-in que retorna a identidade única de um objeto. Essencialmente, é o endereço de memória do objeto.

Exemplos:

````
# Exemplo 4: Comparando identidade vs. valor
v1 = 'a'
v2 = 'a'
v3 = 'b'

print(id(v1)) # Imprime o ID de memória de v1
print(id(v2)) # Imprime o ID de memória de v2. Pode ser o mesmo de v1 para strings pequenas.
print(v1 == v2) # Saída: True (mesmo valor)
print(v1 is v2) # Saída: True (pode ser True para strings pequenas devido à otimização do Python)

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(lista1 == lista2) # Saída: True (mesmo valor)
print(lista1 is lista2) # Saída: False (objetos diferentes na memória)
print(lista1 is lista3) # Saída: True (referenciam o mesmo objeto)

# Exemplo 5: Usando None como Flag (bandeira)
condicao = False
passou_no_if = None # Inicialmente, não passou em nenhuma condição relevante

if condicao:
    passou_no_if = True # Nossa bandeira é levantada
    print('Faça algo')
else:
    print('Não faça algo')

# Verificando o estado da flag
print(passou_no_if is None)     # Saída: True (se 'condicao' for False, como no exemplo)
print(passou_no_if is not None) # Saída: False (se 'condicao' for False)

if passou_no_if is None:
    print('Não passou no if') 
else:
    print('Passou no if') 
````

### Observações Finais:

Compreender a imutabilidade dos tipos de dados é crucial para evitar comportamentos inesperados em seus programas. Os métodos de string fornecem um arsenal poderoso para manipulação de texto de forma eficiente. A distinção entre comparação de valor (``==``) e identidade (``is``) e o uso estratégico de ``None`` como uma "bandeira" são conhecimentos avançados que contribuem para a escrita de código mais preciso e depurável. Continue explorando a documentação oficial e praticando esses conceitos para solidificar seu domínio em Python.