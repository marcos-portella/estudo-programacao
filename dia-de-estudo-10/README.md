### Dia 10

### Prefácio:

Hoje mergulhamos em dois pilares cruciais para o desenvolvimento de software robusto e de fácil manutenção: o **tratamento de erros (exceções)** usando ``try`` e ``except``, e as boas práticas de organização de código através de **variáveis e constantes**, com foco na redução da **complexidade**.

### Tratamento de Erros com ``try`` e ``except``:

O tratamento de exceções é fundamental para criar programas que não "quebrem" inesperadamente quando algo dá errado, como uma entrada de usuário inválida.

- ``try``: Bloco de código onde você tenta executar uma operação que pode gerar um erro.

- ``except``: Bloco de código que é executado se um erro ocorrer dentro do bloco ``try``.

A ideia é "tentar" uma operação e, se ela falhar (gerar uma exceção), "excetuar" esse erro e lidar com ele de forma controlada, evitando que o programa encerre abruptamente.

````
# Exemplo 1: Tratamento de erro ao converter string para float
numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_float = float(numero_str) # Tenta converter a string para float
    print(f'O dobro de {numero_str} é {numero_float*2:.2f}')

except: # Se a conversão falhar, este bloco é executado
    print('Isso não é um número')

# Exemplo 2: O Python descreve o erro se não houver tratamento
# int('a') # Este código geraria um ValueError sem try/except
````

O conceito de "fail fast" (falhar rápido) é importante aqui: se uma operação é crítica e pode falhar, é melhor tratar o erro imediatamente do que permitir que ele se propague e cause problemas maiores no futuro.

### Variáveis, Constantes e Complexidade de Código:

Uma boa organização do código é vital para a legibilidade e manutenibilidade. Isso inclui o uso adequado de variáveis e a compreensão de como a complexidade pode ser gerenciada.

- **Constantes**: São "variáveis" cujo valor não deve mudar durante a execução do programa. Por convenção, são escritas em letras maiúsculas para indicar sua natureza imutável e ajudar outros desenvolvedores a entenderem seu propósito.

- **Complexidade de Código**: Evitar muitas condições aninhadas ou múltiplas condições complexas em um único ``if`` melhora a clareza do código. É melhor dividir a lógica em variáveis booleanas claras e blocos condicionais mais simples.

````
# Exemplo 3: Definição de variáveis e constantes
velocidade = 60  # velocidade atual do carro
local_carro = 107  # local em que o carro está na estrada


RADAR_1 = 60  # velocidade máxima do radar 1 (CONSTANTE)
LOCAL_1 = 100  # local onde o radar 1 está (CONSTANTE)
RADAR_RANGE = 1  # A distância onde o radar pega (CONSTANTE)


# Exemplo 4: Dividindo condições complexas em variáveis booleanas claras
velocidade_do_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE)


# Exemplo 5: Usando as variáveis booleanas para lógica condicional mais clara
if velocidade_do_carro_passou_radar_1:

    print('Carro está acima do limite de velocidade')
else:
    print('Carro abaixo do limite de velocidade')


if carro_passou_radar_1 and velocidade_do_carro_passou_radar_1:
    print('Carro multado em radar 1')
else:
    print('Carro não multado')

````

### Observações Finais:

O tratamento de exceções com ``try`` e ``except`` é uma habilidade fundamental para tornar seus programas mais robustos e amigáveis ao usuário, lidando com situações inesperadas de forma elegante. Paralelamente, o uso de constantes e a simplificação da lógica condicional através de variáveis booleanas claras são práticas essenciais para escrever um código limpo, legível e de fácil manutenção. Combinar esses conhecimentos permite construir aplicações mais confiáveis e fáceis de entender, tanto para você quanto para outros desenvolvedores.