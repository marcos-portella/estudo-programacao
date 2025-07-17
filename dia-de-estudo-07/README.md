## Dia 7

### Prefácio:

Hoje introduzimos os **operadores de comparação** (também conhecidos como relacionais) e os **operadores lógicos** (``and``, ``or``, ``not``), que são essenciais para criar condições sofisticadas. Além disso, começamos a explorar uma ferramenta vital para o desenvolvimento: o **debugger**, que nos ajuda a entender e corrigir o comportamento do nosso código passo a passo.

### Operadores de Comparação (Relacionais):

Os operadores de comparação são usados para comparar dois valores e sempre retornam um valor booleano (``True`` ou ``False``). Eles são a base para as condições usadas em estruturas ``if``/``elif``/``else``.

|Operador | Significado | Exemplo (Resultado True)
| ``>`` | Maior que | 5 > 3
| ``>=`` | Maior ou igual a | 5 >= 5
| ``<`` | Menor que | 3 < 5
| ``<=`` | Menor ou igual a	| 3 <= 3
| ``==`` | Igual a | 'Python' == 'Python'
| ``!=`` | Diferente de	| 'Python' != 'Java'
Exemplo:

````
maior = 2 > 1  # True
igual = 'a' == 'a' # True
diferente = 'a' != 'b' # True
print(f"2 > 1: {maior}")
print(f"'a' == 'a': {igual}")
print(f"'a' != 'b': {diferente}")
````

### Operadores Lógicos: ``and``, ``or``, ``not``:

Esses operadores combinam expressões booleanas ou alteram seu valor lógico, permitindo a criação de condições mais elaboradas.

#### ``and`` (E):

Retorna ``True`` se **todas** as condições forem verdadeiras. Se uma condição for falsa, toda a expressão é falsa. Python avalia ``and`` usando "curto-circuito": ele para de avaliar assim que encontra uma condição falsa.
Valores "falsy" (que se comportam como ``False`` em um contexto booleano): ``0``, ``0.0``, ``''`` (string vazia), ``[]`` (lista vazia), ``()`` (tupla vazia), ``{}`` (dicionário vazio), ``set()`` (conjunto vazio), ``None`` e ``False``.

````
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Acesso concedido!')
else:
    print('Acesso negado ou opção inválida.')

print(True and 0 and True) # Saída: 0 (curto-circuito no primeiro falsy)
````

#### ``or`` (OU):

Retorna ``True`` se **pelo menos uma** das condições for verdadeira. Se todas as condições forem falsas, toda a expressão é falsa. Também usa "curto-circuito": ele para de avaliar assim que encontra uma condição verdadeira.

````
entrada2 = input('[E]ntrar [S]air: ')
senha_digitada2 = input('Senha: ')
senha_permitida2 = '123456'

if (entrada2 == 'E' or entrada2 == 'e') and senha_digitada2 == senha_permitida2:
    print('Bem-vindo!')
else:
    print('Credenciais incorretas.')

senha_padrao = input('Digite sua senha: ') or 'Sem senha'
print(f"Sua senha: {senha_padrao}") # Se nada for digitado, usa 'Sem senha'
````

#### ``not`` (NÃO):
Inverte o valor booleano de uma expressão. ``not True`` é ``False``, e ``not False`` é ``True``.

````
print(not True)   # Saída: False
print(not False)  # Saída: True
print(not 0)      # Saída: True (0 é falsy)
print(not '')     # Saída: True (string vazia é falsy)
````

### Exercício de Comparação e Condicionais:

Praticamos a aplicação dos operadores de comparação e estruturas condicionais para resolver problemas práticos, como determinar qual de dois valores é maior.

````
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

# É crucial converter os valores para numéricos se quisermos comparação numérica
# Se a intenção é comparar strings lexicograficamente, não precisa de conversão.
# Assumindo que a intenção é numérica para um exemplo mais robusto:
try:
    val1 = float(primeiro_valor)
    val2 = float(segundo_valor)

    if val1 > val2:
        print(f'{val1=} é maior que {val2=}.')
    elif val1 < val2:
        print(f'{val2=} é maior que {val1=}.')
    else: # val1 == val2
        print(f'{val1=} é igual a {val2=}.')
except ValueError:
    print('Entrada inválida. Por favor, digite apenas números.')
````

### Debugger: Entendendo o Fluxo do Código:

O debugger é uma ferramenta indispensável para encontrar e corrigir erros (bugs) no código. Ele permite "pausar" a execução do programa em pontos específicos (breakpoints) e inspecionar o estado das variáveis, o fluxo de execução e a pilha de chamadas.

Embora o arquivo ``debugger.PY`` seja um exemplo simples, a prática de usar um debugger (disponível em IDEs como VS Code ou PyCharm) é crucial para:

- Visualizar o valor das variáveis a cada linha.

- Entender por que uma condição está sendo avaliada como ``True`` ou ``False``.

- Seguir o caminho exato que o programa toma através dos blocos ``if``/``elif``/``else``.

````
# Exemplo simplificado para ilustrar o conceito de debug.
# Ao rodar este código com um debugger, você pode definir breakpoints
# nas linhas com 'print' e ver qual condição é satisfeita.
condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Verdadeiro 1')
elif condicao2:
    print('Verdadeiro 2')
elif condicao3: # Este bloco será executado
    print('Verdadeiro 3')
elif condicao4:
    print('Verdadeiro 4')
else:
    print('Nenhuma condição foi satisfeita')
````

Utilizar o debugger ajuda a desmistificar o comportamento do código, especialmente em lógicas complexas com múltiplos operadores lógicos e condicionais aninhados.

### Conclusão:

O Dia 07 solidificou nossa capacidade de controlar o fluxo dos programas Python. Com os operadores de comparação, podemos realizar avaliações básicas. Com os operadores lógicos, podemos criar condições complexas e poderosas. Finalmente, a introdução ao debugger nos equipou com uma ferramenta essencial para analisar e depurar nosso código, transformando a resolução de problemas em um processo mais metódico e eficiente. Continuamos construindo uma base sólida para desenvolver aplicações mais robustas e interativas.