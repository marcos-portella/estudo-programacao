## Dia 15

### Prefácio:

Hoje exploramos duas ferramentas poderosas em Python que permitem escrever código mais conciso e realizar validações complexas: a **operação ternária** para condições em uma única linha e a aplicação prática de lógica para **verificação de CPF**, que envolve manipulação de strings, conversão de tipos e estruturas condicionais.

### Operação Ternária (Condicional de Uma Linha):

A operação ternária, também conhecida como condicional de uma linha, é uma forma concisa de escrever uma instrução ``if-else`` simples. Ela permite atribuir um valor a uma variável com base em uma condição, tudo em uma única linha de código.

- **Sintaxe**: ``<valor_se_verdadeiro> if <condicao> else <valor_se_falso>``

````
# Exemplo 1: Atribuição de valor com base em uma condição
condicao = 10 == 11
variavel = 'Valor Verdadeiro' if condicao else 'Outro valor (Falso)'
print(variavel) # Saída: Outro valor (Falso)

# Exemplo 2: Usando a operação ternária para lógica de dígito
digito = 9
novo_digito = digito if digito <= 9 else 0 # Se digito for <= 9, usa digito; caso contrário, usa 0
print(novo_digito) # Saída: 9

digito = 12
novo_digito = digito if digito <= 9 else 0 # Se digito for <= 9, usa digito; caso contrário, usa 0
print(novo_digito) # Saída: 0

# Exemplo 3: Encadeamento de operações ternárias (usar com moderação para manter a legibilidade)
resultado = 'Primeiro' if False else 'Segundo' if True else 'Terceiro'
print(resultado) # Saída: Segundo
````

A operação ternária é útil para simplificar o código quando a lógica condicional é direta e o objetivo é atribuir um valor. No entanto, para condições mais complexas, é preferível usar blocos ``if/elif/else`` tradicionais para manter a legibilidade.

### Verificador Básico de CPF:

A criação de um verificador de CPF é um excelente exercício prático que integra diversos conceitos de Python aprendidos anteriormente: entrada de dados (``input``), manipulação de strings (``replace``, fatiamento), conversão de tipos (``int``), loops (``for``, ``while``), operações aritméticas e tratamento de erros (``try-except``).

O cálculo dos dígitos verificadores de um CPF segue uma lógica matemática específica, envolvendo multiplicação dos dígitos por uma contagem regressiva, soma dos resultados, multiplicação por 10 e obtenção do resto da divisão por 11.

````
# Exemplo 4: Removendo caracteres não numéricos e fatiando o CPF
cpf_digitado = '123.456.789-00'
cpf_modificado = cpf_digitado.replace('.', '').replace('-', '') # Remove pontos e traços
nove_primeiros_digitos = cpf_modificado[:9] # Pega os 9 primeiros dígitos
print(f'CPF modificado: {cpf_modificado}')
print(f'Nove primeiros dígitos: {nove_primeiros_digitos}')

# Exemplo 5: Lógica simplificada para cálculo do primeiro dígito verificador (DV1)
# Este é um fragmento para ilustrar a lógica, não um verificador completo.
cpf_parcial = '123456789'
multiplicador = 10
soma_digitos = 0

for digito_str in cpf_parcial:
    soma_digitos += int(digito_str) * multiplicador
    multiplicador -= 1

primeiro_dv_calculado = (soma_digitos * 10) % 11
if primeiro_dv_calculado > 9:
    primeiro_dv_calculado = 0

print(f'Primeiro DV calculado: {primeiro_dv_calculado}')

# Exemplo 6: Estrutura geral de um verificador de CPF com tratamento de erro
import os

while True:
    cpf_input = input('Digite o CPF (ou "sair" para finalizar): ')
    os.system('clear') # Limpa a tela (funciona em sistemas Unix-like)

    if cpf_input.lower() == 'sair':
        break

    cpf_limpo = cpf_input.replace('.', '').replace('-', '')

    try:
        # Tenta converter para int para garantir que são apenas números
        int(cpf_limpo) 
    except ValueError:
        print('Erro: Digite apenas números para o CPF.')
        continue # Volta para o início do loop

    if len(cpf_limpo) != 11:
        print('Erro: CPF deve ter 11 dígitos.')
        continue

    # Lógica de cálculo e validação dos dígitos verificadores (DV1 e DV2)
    # ... (código completo do cálculo dos DVs e comparação)

    # Exemplo de validação final (simplificado)
    if cpf_limpo == '12345678900': # Apenas para demonstração, substituir pela lógica real
        print('CPF Válido!')
    else:
        print('CPF Inválido.')
````

### Observações Finais:

A operação ternária é uma ferramenta elegante para expressar condições simples de forma compacta. No entanto, sua aplicação deve ser ponderada para não comprometer a legibilidade do código em cenários mais complexos. A construção de um verificador de CPF, por sua vez, é um excelente exercício que integra e solidifica múltiplos conceitos fundamentais de Python, desde a manipulação de strings e tipos de dados até o controle de fluxo e o tratamento de exceções. A prática com esses tipos de problemas reais é crucial para desenvolver habilidades de programação robustas e eficazes.