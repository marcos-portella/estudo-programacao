## Dia 28: Herança, Polimorfismo e Métodos Especiais (Dunder)

### Prefácio:

No dia de hoje, aprofundamos nos pilares da Programação Orientada a Objetos (POO), concentrando-nos em como as classes podem se relacionar e interagir de maneiras mais complexas. Exploramos a **Herança**, tanto simples quanto múltipla, entendendo como ela promove a reutilização de código. Em seguida, abordamos o **Polimorfismo** e a **Sobreposição de Métodos**, conceitos que permitem a flexibilidade e a substituição de objetos. Por fim, exploramos os **Métodos Especiais** (``Dunder``), que dão superpoderes às classes ao definirem o comportamento dos objetos em situações específicas.

### Herança (Simples e Múltipla):

A **Herança** é um mecanismo que permite que uma classe (subclasse ou classe filha) herde atributos e métodos de outra classe (superclasse ou classe pai).

- **Herança Simples**: Uma classe filha herda de apenas uma classe pai. É o tipo mais comum e direto de herança.

- **Herança Múltipla**: Uma classe pode herdar de múltiplas classes pai. Em Python, o M**ethod Resolution Order (MRO)**, que pode ser verificado com ``.__mro__``, ``.mro()`` ou ``help()``, determina a ordem em que os métodos são procurados nas classes pai.

````
# Exemplo 1: Herança Simples
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}')

class Cliente(Pessoa):
    pass # Cliente herda todos os métodos de Pessoa

c1 = Cliente('Luiz', 30)
c1.exibir_dados()
````

### Polimorfismo e Sobreposição de Métodos:

- **Polimorfismo**: O termo significa "muitas formas". Em POO, o polimorfismo permite que objetos de diferentes classes respondam a uma mesma chamada de método de maneiras distintas, desde que as classes compartilhem uma interface comum (mesmo nome de método).

- **Sobreposição de Métodos (Method Overriding)**: Ocorre quando uma subclasse implementa um método que já existe na superclasse, mas com um comportamento diferente. Para acessar a implementação original da superclasse, usamos a função ``super()``.

````
# Exemplo 2: Sobreposição de métodos e uso de 'super()'
class Animal:
    def falar(self):
        return 'animal falando'

class Cachorro(Animal):
    def falar(self): # Método 'falar' foi sobreposto
        return 'au au'

class Gato(Animal):
    def falar(self): # Método 'falar' foi sobreposto
        return 'miau'

# Exemplo 3: Polimorfismo
def falar(animal):
    print(animal.falar())

c = Cachorro()
g = Gato()

falar(c) # Saída: au au
falar(g) # Saída: miau
````

### Métodos Especiais (``Dunder``):

Os "Dunder Methods" (abreviação de double underscore) são métodos especiais que permitem que classes emulem o comportamento de tipos nativos do Python. Eles são chamados automaticamente em certas operações.

- ``__init__``: Construtor da classe, chamado na criação do objeto.

- ``__repr__``: Representação oficial do objeto, ideal para desenvolvedores (ex: ``Pessoa('Luiz', 30)``).

- ``__str__``: Representação amigável do objeto para usuários (ex: ``Luiz (30 anos)``).

- ``__del__``: Chamado quando o objeto é "coletado" pelo garbage collector.

- ``__len__``: Permite que o objeto responda à função ``len()``.

````
# Exemplo 4: Usando dunder methods
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Ponto(x={self.x}, y={self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __len__(self):
        return self.x + self.y

p = Ponto(1, 2)
print(repr(p)) # Saída: Ponto(x=1, y=2)
print(p)       # Saída: (1, 2)
print(len(p))    # Saída: 3
````

### O Tratamento de Exceções na POO:

Embora o conteúdo do arquivo ``exceptions_poo.py`` não tenha sido disponibilizado, o tema de exceções na POO é crucial. Em Python, as exceções são classes, o que nos permite criar exceções personalizadas para erros específicos. A herança é fundamental aqui, pois as exceções personalizadas geralmente herdam da classe ``Exception``.

````
# Exemplo 5: Criando uma exceção personalizada
class ErroPersonalizado(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

def minha_funcao(valor):
    if valor < 0:
        raise ErroPersonalizado('O valor não pode ser negativo.')

try:
    minha_funcao(-5)
except ErroPersonalizado as e:
    print(f'Erro capturado: {e}')
````

### Observações Finais:

Esta parte do dia 28 consolidou conceitos avançados de POO, fornecendo as ferramentas para modelar sistemas mais complexos e flexíveis. A herança permite a reutilização de código de forma eficaz, enquanto o polimorfismo e a sobreposição de métodos são a base para o desenvolvimento de designs adaptáveis e modulares. Os métodos especiais (``dunder``) são a "magia" por trás de muitas funcionalidades intuitivas de Python, permitindo que nossas classes se integrem de maneira mais harmoniosa com a linguagem. A capacidade de criar exceções personalizadas com classes nos dá um controle mais granular sobre o tratamento de erros.