## Dia 31

### Prefácio:

Hoje apredi ferramentas poderosas para a criação de classes mais concisas e eficientes, além de aprofundar nossa compreensão sobre a interação com coleções. Exploramos as **dataclasses**, um "açúcar sintático" que simplifica a criação de classes de dados; as **namedtuples**, que oferecem tuplas com campos nomeados para maior clareza; e a implementação de **protocolos de iteradores** usando o módulo ``collections.abc``, permitindo que nossas estruturas de dados personalizadas se comportem como tipos built-in do Python.

### Dataclasses: Simplificando Classes de Dados:

**Dataclasses** são uma adição ao Python (PEP 557, a partir da versão 3.7) que fornecem um decorador e funções para gerar automaticamente métodos comuns como ``__init__()``, ``__repr__()``, ``__eq__()`` e outros. Essencialmente, elas são um "açúcar sintático" para criar classes que servem principalmente para armazenar dados.

### Criação e Uso Básico:
Ao usar o decorador ``@dataclass``, você pode definir atributos de classe com anotações de tipo, e o Python cuidará da geração dos métodos Dunder automaticamente.

````
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

p1 = Pessoa('Luiz', 'Otávio')
print(p1) # Saída: Pessoa(nome='Luiz', sobrenome='Otávio')
````

### Configurações de Dataclasses e ``__post_init__``:
As dataclasses podem ser configuradas com argumentos no decorador ``@dataclass``, como ``repr=True`` para controlar a representação da classe. Além disso, o método mágico ``__post_init__`` pode ser implementado para executar lógica de inicialização adicional após a criação do objeto pelos métodos gerados pela dataclass.

````
from dataclasses import dataclass

@dataclass(repr=True) # repr=True é o padrão, mas demonstra a configuração
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        print('POST INIT EXECUTADO') # Exemplo de lógica pós-inicialização

p1 = Pessoa('Ana', 'Silva') # Saída: POST INIT EXECUTADO | Pessoa(nome='Ana', sobrenome='Silva')
print(p1)
````

### Manipulando Atributos com ``field``:
O módulo ``dataclasses`` também oferece a função ``field`` para configurações mais granulares dos atributos. Com ``field``, é possível definir valores padrão, controlar se o atributo aparece no ``repr``, e usar ``default_factory`` para valores padrão mutáveis (como listas), evitando problemas de referência.

````
from dataclasses import dataclass, field

@dataclass
class Produto:
    nome: str = field(default='Sem Nome', repr=True) # Valor padrão e inclusão no repr
    tags: list[str] = field(default_factory=list) # Uso de default_factory para listas

p1 = Produto(nome='Livro')
p1.tags.append('ficção')
p2 = Produto()
print(p1) # Saída: Produto(nome='Livro', tags=['ficção'])
print(p2) # Saída: Produto(nome='Sem Nome', tags=[])
````

### ``asdict`` e ``astuple``:

As funções ``asdict`` e ``astuple`` do módulo ``dataclasses`` permitem converter instâncias de dataclasses para dicionários e tuplas, respectivamente, facilitando a manipulação dos dados.

````
from dataclasses import asdict, astuple, dataclass

@dataclass
class Coordenada:
    x: int
    y: int

c = Coordenada(10, 20)
print(asdict(c)) # Saída: {'x': 10, 'y': 20}
print(astuple(c)) # Saída: (10, 20)
````

### Namedtuples: Tuplas com Nomes para Valores:
As **namedtuples** (tuplas nomeadas) são tuplas imutáveis que permitem acessar seus elementos por nomes de atributos, além de índices, tornando o código mais legível. Elas são ideais para criar objetos que são apenas um agrupamento de atributos, sem a necessidade de métodos complexos, funcionando como registros de dados. ``collections.namedtuple`` e ``typing.NamedTuple`` são as formas de criá-las.

````
from typing import NamedTuple

class Carta(NamedTuple):
    valor: str
    naipe: str = 'Copas' # Atributo com valor padrão

as_copas = Carta('A')
print(as_copas.valor) # Saída: A
print(as_copas.naipe) # Saída: Copas
print(as_copas[0])    # Saída: A
print(as_copas._asdict()) # Converte para dicionário
````

### Protocolos de Iteradores: ``collections.abc``:
O módulo ``collections.abc`` (Abstract Base Classes) fornece classes abstratas que definem os "protocolos" para diferentes tipos de coleções, como ``Sequence``, ``Mapping``, ``Set``, ``Iterator``, etc.. Ao herdar dessas ABCs e implementar seus métodos abstratos, suas classes personalizadas podem se comportar como os tipos built-in correspondentes, permitindo que funcionem com funções e construções Python que esperam esses protocolos (como for loops, ``len()``, ``[]`` para acesso por índice).

Para criar um iterador personalizado, é necessário implementar os métodos ``__iter__`` (que retorna o próprio iterador) e ``__next__`` (que retorna o próximo item da iteração e levanta ``StopIteration`` quando não há mais itens).

````
from collections.abc import Sequence

class MyList(Sequence): # Herda de Sequence para implementar protocolo de sequência
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self) -> int:
        return self._index # Implementa o método len()

    def __getitem__(self, index):
        return self._data[index] # Permite acesso por índice

    def __iter__(self):
        self._next_index = 0 # Reinicia o índice para nova iteração
        return self # Retorna o próprio objeto como iterador

    def __next__(self):
        if self._next_index >= self._index:
            raise StopIteration # Sinaliza o fim da iteração
        value = self._data[self._next_index]
        self._next_index += 1
        return value # Retorna o próximo item

lista = MyList()
lista.append('Banana', 'Maçã', 'Uva')
for item in lista:
    print(item) # Saída: Banana, Maçã, Uva (cada um em uma linha)
print(len(lista)) # Saída: 3
print(lista[1]) # Saída: Maçã
````

### Observações Finais:
A imersão em dataclasses, namedtuples e protocolos de coleções nos oferece ferramentas valiosas para escrever código Python mais limpo, eficiente e robusto. As dataclasses e namedtuples simplificam a criação de classes de dados, reduzindo o código boilerplate e aumentando a legibilidade. A compreensão e implementação dos protocolos de ``collections.abc`` nos permitem criar estruturas de dados personalizadas que se integram perfeitamente com o ecossistema Python, comportando-se de maneira previsível e familiar. Esses conceitos são fundamentais para desenvolver aplicações Pythonicas de alta qualidade e escaláveis.
