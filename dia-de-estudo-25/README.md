## Dia 25: Conceitos Avançados de POO e Relações entre Classes

### Prefácio:

Dando continuidade à nossa exploração da Programação Orientada a Objetos, o dia de hoje foi dedicado a conceitos mais avançados que aprimoram a estrutura e a flexibilidade do nosso código. Abordamos os diferentes tipos de métodos em classes (``method``, ``classmethod``, ``staticmethod``), o encapsulamento e as convenções de modificadores de acesso (``public``, ``protected``, ``private``), a utilidade da ``@property`` para criar getters e setters pythônicos e as relações fundamentais entre classes: associação, agregação e composição.

### Tipos de Métodos em Classes:

- **Métodos de Instância (``self``)**: São os métodos mais comuns. Eles operam em uma instância da classe e têm acesso aos atributos e outros métodos através do parâmetro ``self``.

- **Métodos de Classe (``@classmethod``)**: São métodos que operam na classe em si, não em uma instância específica. Recebem a própria classe (``cls``) como primeiro argumento. São frequentemente usados como "fábricas" para criar instâncias da classe de formas alternativas.

- **Métodos Estáticos (``@staticmethod``)**: São funções que pertencem à classe, mas não têm acesso nem à instância (``self``) nem à classe (``cls``). Eles não dependem do estado do objeto e são, na prática, funções comuns organizadas dentro do escopo da classe.

````
# Exemplo 1: Diferença entre métodos de instância, classe e estático
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    
    # Método de instância
    def set_user(self, user):
        self.user = user

    # Método de classe (factory)
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    # Método estático
    @staticmethod
    def log(msg):
        print(f'LOG: {msg}')

# Usando o método de classe para criar uma instância
c1 = Connection.create_with_auth('luiz', '1234')
print(c1.user)

# Chamando o método estático
Connection.log('Conexão criada com sucesso.')
````

### Encapsulamento e Convenções de Acesso:

Python não tem modificadores de acesso (``public``, ``private``, ``protected``) no sentido estrito de outras linguagens. Em vez disso, utilizamos convenções para indicar a visibilidade dos atributos e métodos.

- ``public``: Nomes sem underscore. Podem ser acessados de qualquer lugar.

- ``protected``: Nomes com um underscore no início (ex: ``_protected``). Indica que o atributo/método não deve ser acessado diretamente fora da classe ou suas subclasses.

- ``private``: Nomes com dois underscores no início (ex: ``__private``). Python realiza um processo de "name mangling" (``_NomeDaClasse__nome_do_atributo``) para dificultar o acesso externo, mas ainda é tecnicamente possível. O uso é estritamente na classe onde foi declarado.

````
# Exemplo 2: Convenções de encapsulamento
class Foo:
    def __init__(self):
        self.publico = 'Isso é público'
        self._protegido = 'Isso é protegido'
        self.__privado = 'Isso é privado'

    def metodo_publico(self):
        return f'Acessando atributos: {self.publico}, {self._protegido}, {self.__privado}'
    
f = Foo()
print(f.publico)       # Acesso direto (ok)
print(f._protegido)    # Acesso direto (ok, mas desaconselhado)
# print(f.__privado)   # Erro: AttributeError
print(f.metodo_publico())
````

### O Decorador ``@property``:

``@property`` é uma forma "pythônica" de criar getters e setters para atributos de forma elegante e transparente. Ele permite que métodos se comportem como atributos, protegendo o acesso e a modificação de dados internos da classe.

- **``@property`` (getter)**: O decorador transforma um método que retorna um valor no acesso a um atributo.

- **``@.setter``**: Permite definir um método para modificar o valor do atributo, possibilitando a validação de dados antes da atribuição.

````
# Exemplo 3: Usando @property e @setter
class Caneta:
    def __init__(self, cor):
        self._cor = cor # O underline sugere que o atributo é protegido

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError('Cor não aceita')
        self._cor = valor

caneta = Caneta('Azul')
print(caneta.cor)
caneta.cor = 'Vermelha'
print(caneta.cor)
# caneta.cor = 'Rosa' # Levanta um ValueError
````

### Relações entre Classes:

- **Associação**: É a relação mais básica, onde um objeto usa outro. O ciclo de vida dos objetos não está estritamente ligado.

- **Agregação**: Uma forma mais forte de associação. Um objeto "tem" outros objetos, mas estes objetos agregados podem existir independentemente do objeto principal.

- **Composição**: É a relação mais forte. Um objeto "é dono" de outro, e os objetos "filhos" não podem existir sem o objeto "pai". Quando o objeto principal é destruído, os objetos filhos também são.

````
# Exemplo 4: Associação
class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class Ferramenta:
    def __init__(self, nome):
        self.nome = nome
    
    def escrever(self):
        return f'{self.nome} está escrevendo.'

escritor = Escritor('Luiz')
caneta = Ferramenta('Caneta')
escritor.ferramenta = caneta
print(escritor.ferramenta.escrever())
Python
````
````
# Exemplo 5: Agregação e Composição (exemplo de carrinho de compras)
class CarrinhoDeCompras: # Agregação
    def __init__(self):
        self.produtos = [] # Uma lista de objetos Produto

    def inserir_produtos(self, *produtos):
        self.produtos.extend(produtos)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 50)
p2 = Produto('Calça', 100)

carrinho.inserir_produtos(p1, p2)
# Se 'carrinho' for apagado, 'p1' e 'p2' continuam a existir. Isso é agregação.

# Exemplo de Composição (endendeço só existe se o cliente existir)
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = [] # A lista de endereços é criada com o cliente

    def inserir_endereco(self, rua, numero):
        # O Endereço é criado DENTRO da classe Cliente
        self.enderecos.append(Endereco(rua, numero))

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
````

### Observações Finais:

Compreender e aplicar esses conceitos de POO é essencial para escrever código Python mais robusto e bem estruturado. A escolha entre os tipos de métodos, a correta aplicação do encapsulamento e a modelagem adequada das relações entre classes (associação, agregação, composição) são decisões de design que impactam diretamente na manutenibilidade e na clareza do projeto. ``@property`` em particular é uma ferramenta poderosa que nos permite seguir o princípio da "propriedade de dados" de forma elegante em Python.