"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency: int, account: int, balance: float = 0) -> None:
        self.agency = agency
        self.account = account
        self.balance = balance

    def show_info(self, msg: str = '') -> None:
        print(f'{msg}\nO seu saldo atual é {self.balance}')

    def deposit(self, value: float) -> float:
        print('---')
        self.balance += value
        self.show_info(f'Depositando {value} na sua conta\n')
        return self.balance

    @abstractmethod
    def draw_out(self, value: float) -> float: ...

    def __repr__(self):
        class_name = type(self).__name__
        attr = f'({self.agency!r}, {self.balance!r})'
        return f'{class_name}{attr}'


class CurrentAccount(Account):
    def __init__(
            self, agency: int, account: int,
            balance: float = 0,  limit: float = 0
            ):
        super().__init__(agency, account, balance)
        self.limit = limit

    def draw_out(self, value: float) -> float:
        print('---')
        make_draw_out = self.balance - value
        max_limit = self.limit

        if make_draw_out >= max_limit:
            self.balance -= value
            self.show_info(f'Sacando {value}\n')
            print()
            return self.balance

        print('Não foi possível sacar o valor desejado\n')
        print(f'Seu limite é {self.limit:.2f}\n')
        self.show_info(f'Saque negado ({value:.2f})\n')
        return self.balance

    def __repr__(self):
        class_name = type(self).__name__
        attr = f'({self.agency!r}, {self.account!r}, {self.balance!r},'\
            f' {self.limit!r})'
        return f'{class_name}{attr}'


class SavingsAccount(Account):
    def draw_out(self, value: float) -> float:
        print('---')
        make_draw_out = self.balance - value

        if make_draw_out >= 0:
            self.balance -= value
            self.show_info(f'Sacando {value}\n')
            print()
            return self.balance

        print('Não foi possível sacar o valor desejado')
        print()
        self.show_info(f'Saque negado ({value:.2f})\n')
        return self.balance


class People():
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    def __repr__(self):
        class_name = type(self).__name__
        attr = f'({self.name!r}, {self.age!r})'
        return f'{class_name}{attr}'


class Client(People):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account = None


class Bank():
    def __init__(
            self,
            agencies: list[int] | None = None,
            clients: list[People] | None = None,
            accounts: list[Account] | None = None,
            ):
        self.agencies = agencies or []
        self.clients = clients or []
        self.accounts = accounts or []

    def _check_agency(self, account):
        if account.agency in self.agencies:
            return True
        return False

    def _check_account(self, account):
        if account.agency in self.agencies:
            return True
        return False

    def _check_client(self, client):
        if client in self.clients:
            return True
        return False

    def _check_client_accont(self, client, account):
        if account in self.accounts:
            return True
        return False

    def authenticate(self, client: People, account: Account):
        return self._check_agency(account) and \
            self._check_client(client) and \
            self._check_account(account) and \
            self._check_client_accont(client, account)

    def __repr__(self):
        class_name = type(self).__name__
        attr = f'({self.agencies!r}, {self.clients!r}, {self.accounts!r},)'
        return f'{class_name}{attr}'


if __name__ == '__main__':
    c1 = Client('Luiz', 30)
    cc1 = CurrentAccount(111, 222, 0, 0)
    c1.account = cc1
    c2 = Client('Maria', 18)
    cp1 = SavingsAccount(112, 223, 100)
    c2.account = cp1
    banco = Bank()
    banco.clients.extend([c1, c2])
    banco.accounts.extend([cc1, cp1])
    banco.agencies.extend([111, 222])

    if banco.authenticate(c1, cc1):
        cc1.deposit(10)
        c1.account.deposit(100)
        print(c1.account)
    else:
        print('Não possível autenticar')  # depois temos que fazer uma lógica
