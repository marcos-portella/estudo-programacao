## Python do Básico ao Avançado

Este arquivo contém resumos e anotações das aulas
do curso de Python feito na plataforma Udemy.

Os resumos vão se tornando mais didáticos e legíveis 
conforme as aulas avançam, mostrando minha evolução

Lembre-se de verificar os arquivos README.md presentes para melhor 
entendimento da matéria




## Dia 32

### Prefácio:

Hoje concentramos nossos esforços em duas ferramentas para o desenvolvimento de aplicações robustas: a **manipulação de datas e calendários** e a **modularização do código**. A capacidade de gerenciar e calcular datas com precisão é vital para uma infinidade de sistemas, desde agendamentos até cálculos financeiros. Complementarmente, a modularização nos permite organizar nosso código de forma lógica e reutilizável, facilitando a colaboração e a manutenção de projetos maiores.

### Manipulação de Datas e Horas com ``datetime`` e ``calendar``:
Python oferece módulos poderosos para trabalhar com datas e horas, sendo ``datetime`` e ``calendar`` os mais proeminentes.

#### Criando e Formatando Datas com ``datetime``:

O módulo ``datetime`` permite a criação de objetos que representam datas e horas com alta precisão. Podemos criar um ``datetime`` a partir de valores numéricos ou converter strings formatadas em objetos ``datetime`` usando ``strptime``. Para exibir datas e horas em formatos específicos, utilizamos ``strftime``. O ``timestamp`` também é uma forma de representar datas como um número único, que pode ser convertido de volta para ``datetime``.

````
from datetime import datetime

# Criando um objeto datetime
data_atual = datetime.now()
print(f"Data e Hora Atual: {data_atual}") # Ex: 2025-07-11 20:14:06.123456

# Convertendo string para datetime
data_str = '2022-12-13 07:59:23'
data_obj = datetime.strptime(data_str, '%Y-%m-%d %H:%M:%S')
print(f"Data de String: {data_obj.strftime('%d/%m/%Y %H:%M:%S')}") # Saída: 13/12/2022 07:59:23
````

#### Calculando Diferenças com ``timedelta`` e ``relativedelta``:

Para realizar operações com datas, como adicionar ou subtrair períodos, o ``datetime`` oferece ``timedelta``. Para cálculos mais complexos, como adicionar meses ou anos de forma flexível (considerando o número de dias em cada mês, por exemplo), a biblioteca ``dateutil`` e seu ``relativedelta`` são extremamente úteis, lidando com nuances que ``timedelta`` não cobre diretamente.

````
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

data_inicio = datetime(2020, 1, 15)
data_fim = datetime(2020, 3, 15)

# Calculando diferença com timedelta
diferenca_dias = data_fim - data_inicio
print(f"Diferença em dias: {diferenca_dias.days}") # Saída: 60

# Adicionando um mês com relativedelta (mais preciso para meses/anos)
um_mes_depois = data_inicio + relativedelta(months=1)
print(f"Um mês depois: {um_mes_depois.strftime('%d/%m/%Y')}") # Saída: 15/02/2020 (considera o número de dias de janeiro)

# Exemplo prático: Cálculo de parcelas de empréstimo
valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos
# ... lógica para calcular parcelas iterando com relativedelta(months=+1)
````

#### Usando o Módulo ``calendar``:
O módulo ``calendar`` é projetado para lidar com tarefas de calendário em geral, permitindo verificar o último dia do mês, o dia da semana de uma data específica, ou até mesmo gerar calendários completos. Ele é útil para exibir informações de calendário ou para lógica que dependa da estrutura do calendário.

````
import calendar

# Retorna o número do dia da semana (0=segunda-feira, 6=domingo)
dia_da_semana = calendar.weekday(2025, 7, 11)
print(f"11/07/2025 é um(a) {calendar.day_name[dia_da_semana]}") # Saída: 11/07/2025 é um(a) Friday

# Obtendo o último dia de um mês
primeiro_dia_mes, ultimo_dia_mes = calendar.monthrange(2025, 7)
print(f"Último dia de Julho/2025: {ultimo_dia_mes}") # Saída: 31
````

### Modularização: Organizando o Código:

A modularização é a prática de dividir um programa em partes menores e independentes, chamadas módulos. Cada módulo pode conter funções, classes e variáveis relacionadas a uma tarefa específica. Isso promove a reutilização de código, melhora a legibilidade e facilita a manutenção de projetos grandes.

#### Importando Módulos:

Em Python, podemos importar módulos inteiros ou partes específicas de módulos usando as declarações ``import`` ou ``from ... import.``

````
# modulo.py
def soma(x: float, y: float) -> float:
    return x + y

# app.py
from modulo import soma # Importa apenas a função 'soma' do módulo 'modulo'

resultado = soma(4, 2)
print(resultado) # Saída: 6
````

### O Bloco ``if __name__ == '__main__':``:
Este bloco é uma construção comum em Python que permite que o código dentro dele seja executado somente quando o script é executado diretamente, e não quando é importado como um módulo em outro script. É uma prática recomendada para incluir código de teste ou de inicialização que não deve ser executado automaticamente ao importar o módulo.

````
# modulo.py
def soma(x: float, y: float) -> float:
    return x + y

if __name__ == '__main__':
    # Este código só será executado se 'modulo.py' for o script principal
    print("Executando como script principal em modulo.py")
    print(soma(10, 30)) # Saída: 40
````

### Observações Finais:

A maestria dos módulos ``datetime`` e ``calendar`` é indispensável para qualquer aplicação que envolva agendamentos, logs ou cálculos baseados em tempo. Simultaneamente, a compreensão e aplicação da modularização através de importações e do bloco ``if __name__ == '__main__':`` são cruciais para escrever código Python limpo, organizado, reutilizável e, acima de tudo, manutenível em projetos de qualquer escala.