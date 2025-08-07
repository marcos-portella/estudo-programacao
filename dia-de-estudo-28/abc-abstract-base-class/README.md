## Dia 28: Classes Abstratas e Métodos Abstratos

### Prefácio:

Hoje o foco foi em um dos conceitos mais importantes para a criação de arquiteturas robustas em Python: as **Classes Abstratas (ABC - Abstract Base Class)**. Exploramos como o módulo ``abc`` nos permite definir contratos de classes, garantindo que as subclasses implementem métodos específicos. Aprendemos a usar o decorador ``@abstractmethod`` para impor a implementação de métodos, e vimos como essa ferramenta pode ser combinada com outras funcionalidades da linguagem, como ``@property`` e ``@setter``, para criar interfaces claras e consistentes.

### Classes Abstratas: O Conceito de Contrato

Classes abstratas são usadas para definir um "contrato" que as classes filhas devem seguir. Uma classe que herda de uma classe abstrata é obrigada a implementar todos os seus métodos e propriedades abstratas, caso contrário, não poderá ser instanciada. Para criar uma classe abstrata, importamos ``ABC`` e ``abstractmethod`` do módulo ``abc`` e usamos a classe ``ABC`` como base.

````
# Exemplo 1: Definição de uma classe abstrata
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def falar(self):
        # A classe abstrata define o que deve ser feito, mas não como.
        # Nenhuma implementação é necessária aqui.
        pass

class B(A):
    # A classe B é obrigada a implementar o método 'falar'.
    # Se este método não for implementado, a instância de B não poderá ser criada.
    def falar(self):
        print('Falando...')

b = B()
b.falar()`
````

### Métodos Abstratos (``@abstractmethod``):
O decorador ``@abstractmethod`` é a peça central que define um método como abstrato. Isso significa que a implementação do método é delegada às classes filhas. Se uma subclasse falhar em implementar um método abstrato da classe pai, o interpretador Python levantará um erro do tipo ``TypeError``, impedindo a criação de uma instância.

````
# Exemplo 2: O erro de não implementar um método abstrato
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

# A classe Carro não implementa 'ligar'
class Carro(Veiculo):
    pass

try:
    carro = Carro()
except TypeError as e:
    print(f'Erro: {e}') # Saída: Erro: Can't instantiate abstract class Carro with abstract method ligar
````

### ``@abstractmethod`` com ``@property`` e ``@setter``:

Podemos usar ``@abstractmethod`` com outros decoradores, como ``@property`` e ``@setter``, para definir contratos para getters e setters em classes abstratas. Isso permite que a classe abstrata defina que um atributo deve ser acessível e, opcionalmente, mutável, sem especificar a lógica de como esses acessos e modificações ocorrerão.

````
# Exemplo 3: `@abstractmethod` em conjunto com `@property` e `@setter`
from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, saldo):
        self._saldo = saldo
    
    @property
    @abstractmethod
    def saldo(self):
        pass

    @saldo.setter
    @abstractmethod
    def saldo(self, valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, saldo):
        super().__init__(saldo)
    
    @property
    def saldo(self):
        print('Getter de saldo')
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        print('Setter de saldo')
        self._saldo = valor

# Agora a classe 'ContaCorrente' deve implementar tanto o getter quanto o setter
# para o atributo 'saldo'.
````
````
# Exemplo 4: Classe Abstrata com métodos concretos
from abc import ABC, abstractmethod

class Dispositivo(ABC):
    def __init__(self, nome):
        self.nome = nome

    # Método abstrato que a subclasse deve implementar
    @abstractmethod
    def ligar(self):
        pass

    # Método concreto que pode ser usado pela subclasse
    def descrever(self):
        print(f'Este é o dispositivo {self.nome}.')

class Televisao(Dispositivo):
    def ligar(self):
        print(f'A TV {self.nome} foi ligada.')

tv = Televisao('LG')
tv.descrever()
tv.ligar()
````
````
# Exemplo 5: O uso de classes abstratas em uma hierarquia de herança
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def comer(self):
        pass

class Mamifero(Animal):
    @abstractmethod
    def amamentar(self):
        pass

class Gato(Mamifero):
    def comer(self):
        print('O gato está comendo.')

    def amamentar(self):
        print('O gato está amamentando.')

gato = Gato()
gato.comer()
gato.amamentar()
````

### Observações Finais:

O uso de classes abstratas é uma prática de design de software que promove o desacoplamento e a consistência em grandes bases de código. Elas atuam como um "contrato de desenvolvimento", garantindo que as classes que herdam de uma ABC implementem a funcionalidade esperada. A habilidade de combinar ``abstractmethod`` com ``@property`` e ``@setter`` nos permite definir interfaces de forma mais granular e pythônica, assegurando que o acesso e a modificação de dados sigam regras claras e obrigatórias. Essa abordagem fortalece a arquitetura do software, tornando-o mais fácil de entender e manter a longo prazo.