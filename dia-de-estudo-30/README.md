## Dia 30

### Prefácio:

O dia 30 nos trouxe a oportunidade de aplicar e consolidar conceitos fundamentais da programação orientada a objetos (POO), como Abstração, Herança, Encapsulamento e Polimorfismo, através da construção de um sistema bancário simplificado. Além disso, introduzimos o uso de Enumerações (Enums), uma ferramenta elegante para lidar com conjuntos fixos de valores, que enriquece a clareza e a segurança do nosso código.

### Enumerações (Enums): Organizando Constantes:
**Enumerações** são coleções de nomes simbólicos (membros) ligados a valores únicos e constantes. Elas são ideais para  cenários onde você tem um número predefinido de opções para escolher, como dias da semana, status de um pedido ou, como no exemplo, direções. Em Python, a classe ``enum.Enum`` serve como superclasse para suas enumerações personalizadas, garantindo que os membros sejam iteráveis e permitindo o uso com type annotations e ``isinstance`` para verificação de tipo. O uso de ``enum.auto()`` facilita a atribuição automática de valores sequenciais aos membros.

````
import enum

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()

def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')
    print(f'Movendo para {direcao.name} ({direcao.value})')

mover(Direcoes.ESQUERDA) # Saída: Movendo para ESQUERDA (1)
````

### Sistema Bancário Simplificado: POO na Prática:
O exercício do sistema bancário demonstrou a aplicação prática de vários pilares da Programação Orientada a Objetos:

#### Abstração e Polimorfismo: A Classe ``Account``:
A classe ``Account`` (Conta) é uma classe abstrata (``ABC`` - Abstract Base Class), o que significa que ela não pode ser instanciada diretamente. Ela define o comportamento comum a todas as contas, como ``deposit`` (depositar) e ``show_info`` (mostrar informações), e um método abstrato ``draw_out`` (sacar), que deve ser implementado por suas subclasses. Isso garante o **polimorfismo**, onde diferentes tipos de conta (corrente e poupança) podem responder ao mesmo método ``draw_out`` de maneiras distintas.

````
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, agency: int, account: int, balance: float = 0) -> None:
        self.agency = agency
        self.account = account
        self.balance = balance

    def deposit(self, value: float) -> float:
        self.balance += value
        return self.balance

    @abstractmethod
    def draw_out(self, value: float) -> float: ...

# As classes CurrentAccount e SavingsAccount implementariam 'draw_out'
````

#### Herança: ``CurrentAccount`` e ``SavingsAccount``:
As classes ``CurrentAccount`` (Conta Corrente) e ``SavingsAccount`` (Conta Poupança) **herdam** da classe ``Account``. A ``CurrentAccount`` estende o comportamento da ``Account`` adicionando um ``limit`` (limite) extra para saques. Ambas as subclasses fornecem sua própria implementação concreta do método ``draw_out``, demonstrando como o polimorfismo funciona na prática, com regras diferentes para saque em cada tipo de conta.

````
class CurrentAccount(Account):
    def __init__(self, agency: int, account: int, balance: float = 0, limit: float = 0):
        super().__init__(agency, account, balance)
        self.limit = limit

    def draw_out(self, value: float) -> float:
        # Lógica de saque para conta corrente com limite
        if (self.balance - value) >= self.limit: # Correção: deveria ser self.balance + self.limit
            self.balance -= value
            print(f'Sacando {value} na conta corrente.')
        else:
            print('Saldo e limite insuficientes.')
        return self.balance
````

#### Encapsulamento: Propriedades em ``People``:
A classe ``People`` (Pessoa) utiliza **encapsulamento** através de ``@property`` para controlar o acesso e a modificação dos atributos ``name`` (nome) e ``age`` (idade). Embora os setters no exemplo dado não contenham lógica de validação complexa, eles ilustram o padrão para adicionar tal lógica quando necessário, protegendo a integridade dos dados.

````
class People():
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name # Exemplo de encapsulamento
````

#### Agregação: ``Client`` e ``Bank``:
A classe ``Client`` (Cliente) demonstra **agregação** ao "ter" uma ``Account``. Isso significa que um cliente está associado a uma conta, mas a vida útil da conta não depende diretamente da vida útil do cliente. Similarmente, a classe ``Bank`` (Banco) agrega tanto ``Client`` quanto ``Accounts``. O banco é responsável por gerenciar e autenticar clientes e contas, verificando se a agência, o cliente e a conta pertencem ao banco antes de permitir operações como saques.

````
class Client(People):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account = None # Cliente TEM uma conta (agregação)

class Bank():
    def __init__(self, agencies: list[int] | None = None,
                 clients: list[People] | None = None,
                 accounts: list[Account] | None = None):
        self.agencies = agencies or []
        self.clients = clients or []
        self.accounts = accounts or []

    def authenticate(self, client: Client, account: Account):
        # Lógica de autenticação do banco
        return self._check_agency(account) and \
               self._check_client(client) and \
               self._check_account(account) and \
               self._check_client_accont(client, account)

# Exemplo de uso no main.py e accounts_.py:
# c1 = Client('Luiz', 30)
# cc1 = CurrentAccount(111, 222, 0, 0)
# c1.account = cc1
# banco = Bank()
# banco.clients.append(c1)
# banco.accounts.append(cc1)
# banco.agencies.append(111)
# if banco.authenticate(c1, cc1):
#     cc1.deposit(100)
#     print(c1.account)`
````

### Documentação de Código: Docstrings:
A documentação é uma parte essencial do desenvolvimento de software, e Python oferece docstrings como uma maneira padrão de documentar módulos, classes, funções e métodos. As docstrings são strings literais que aparecem como o primeiro enunciado em uma definição de módulo, classe ou função. Elas são acessíveis em tempo de execução através do atributo ``__doc__`` do objeto e são usadas por ferramentas como ``help()``.

#### Docstrings de Módulo:
As docstrings no nível do módulo descrevem o propósito geral do arquivo.

````
"""O que seu módulo faz""" # Exemplo de docstring de módulo em uma_linha.py

# ou com várias linhas:
"""O que seu módulo faz
Lorem ipsum dolor sit amet. Et praesentium nisi non quam mollitia At saepe
quisquam qui quae voluptatem.
""" # Exemplo de docstring de módulo em varias_linhas.py
````

#### Docstrings de Funções e Métodos:
As docstrings para funções e métodos descrevem o que a função faz, seus parâmetros (``:param``), seus tipos (``:type``), o valor de retorno (``:return``), o tipo de retorno (``:rtype``), e possíveis exceções que podem ser levantadas (``:raises``).

````
def soma(x: int | float, y: int | float) -> int | float:
    """Soma x e y

    Este módulo contém funções e exemplos de documentação de funções.
    A função soma você já conhece bastante.

    :param x: Número 1
    :type x: int or float
    :param y: Número 2
    :type y: int or float

    :return: A soma entre x e y
    :rtype: int or float
    """
    return x + y

def bar() -> int:
    """O que ele faz
    
    :raises  NotIMplementedError: se o método não for definido
    :raises ValueError:  Se  o método não for defiinido
    """
    raise NotImplementedError('Teste')
````

#### Docstrings de Classes:
As docstrings de classes descrevem o propósito da classe.

````
class Foo:
    """Este é um módulo de exemplo""" # Exemplo de docstring de classe em classes.py

    """
    Este módulo contém funções e exemplos de documentação de funções.
    A função soma você já conhece bastante.
    """
    # ... métodos
````

### Observações Finais:

Os exercícios do dia 29 foram cruciais para solidificar a compreensão dos paradigmas de POO em Python. Ao construir o sistema bancário, não apenas vimos Abstração, Herança, Encapsulamento e Polimorfismo em ação, mas também a importância da organização do código em módulos separados (``accounts_.py`` e ``main.py``). O uso de Enumerações, por sua vez, complementou essa estrutura, mostrando como podemos tornar nosso código mais legível e menos propenso a erros ao lidar com conjuntos fixos de valores. A prática com esses conceitos é fundamental para o desenvolvimento de sistemas complexos e bem estruturados.