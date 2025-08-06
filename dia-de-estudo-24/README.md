## Dia 24: Introdução à Programação Orientada a Objetos (POO)

### Prefácio:

Hoje iniciamos nossa jornada na **Programação Orientada a Objetos (POO)** em Python. Este paradigma de programação nos permite organizar o código em torno de objetos, que são modelos da vida real ou abstrações lógicas. Exploramos os conceitos fundamentais de classes, instâncias, atributos e métodos, além de como gerenciar o estado dos objetos e a diferença entre atributos de classe e de instância.

### O Conceito de Classes e Objetos:

- **Classes**: Uma classe é um "molde" ou "planta" para criar objetos. Ela define a estrutura e o comportamento que os objetos terão, mas não contém dados por si só. Por convenção, o nome das classes usa a notação **PascalCase**.

- **Objetos (Instâncias)**: Um objeto é uma instância concreta de uma classe. Ele tem seus próprios dados internos (atributos) e pode realizar ações (métodos) definidos pela classe.

````
# Exemplo 1: Classe e Instâncias
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

# Criando instâncias (objetos) da classe Pessoa
p1 = Pessoa('Luiz', 'Otávio')
p2 = Pessoa('Maria', 'Joana')

print(p1.nome, p1.sobrenome) # Acessando os atributos do objeto p1
print(p2.nome, p2.sobrenome) # Acessando os atributos do objeto p2
````

### Atributos e o Método ``__init__``:

- **Atributos**: São as variáveis que armazenam dados dentro de um objeto.

- **Método ``__init__``**: Conhecido como o "construtor" da classe, este método é executado automaticamente quando uma nova instância é criada. Ele é usado para inicializar os atributos do objeto, recebendo a própria instância (``self``) como primeiro argumento, seguido pelos parâmetros necessários para a inicialização.

- ``self``: Representa a própria instância do objeto que está sendo criado. É através dele que acessamos e modificamos os atributos de cada objeto.

````
# Exemplo 2: O método __init__ e o uso de `self`
class Carro:
    def __init__(self, nome):
        self.nome = nome # self.nome é um atributo da instância
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
fusca.acelerar() # O método acelerar usa o atributo `self.nome`
````

### Atributos de Instância vs. Atributos de Classe:

- **Atributos de Instância**: São específicos para cada objeto criado a partir da classe. Eles são definidos dentro do método ``__init__`` e acessados via ``self``.

- **Atributos de Classe**: São variáveis que pertencem à classe em si, e não a uma instância específica. Todos os objetos da classe compartilham o mesmo valor para este atributo, a menos que ele seja alterado na própria classe.

````
# Exemplo 3: Diferença entre atributos de instância e de classe
class Pessoa:
    ano_atual = 2022 # Atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome # Atributo de instância
        self.idade = idade # Atributo de instância

    def get_ano_nascimento(self):
        # Acessa o atributo de classe usando o nome da classe
        return Pessoa.ano_atual - self.idade

p1 = Pessoa('João', 35)
print(p1.get_ano_nascimento())
````

### Mantendo o Estado de um Objeto:

Os objetos podem manter um "estado" através de seus atributos. Por exemplo, uma câmera pode ter um estado ``filmando`` que é um booleano (``True`` ou ``False``). Os métodos da classe (``filmar``, ``parar_filmar``, ``fotografar``) podem modificar ou verificar este estado para definir o comportamento do objeto.

````
# Exemplo 4: Objeto com estado
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando...')
            return
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando...')
            return
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

c1 = Camera('Canon')
c1.filmar()
c1.parar_filmar()
c1.parar_filmar()
````

### Salvando e Carregando Instâncias em JSON:

O módulo ``json`` é uma ferramenta poderosa para a persistência de dados de objetos. Podemos salvar os dados de uma instância de classe em um arquivo JSON e, posteriormente, ler este arquivo para recriar as instâncias da classe. O método ``vars()`` ou o atributo ``__dict__`` de um objeto podem ser usados para obter um dicionário com seus atributos, o que facilita a serialização em JSON.

````
# Exemplo 5: Salvando e carregando dados de uma classe em JSON
import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
bd = [vars(p1), vars(p2)] # vars() retorna um dicionário dos atributos

caminho_arquivo = 'pessoas.json'

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    json.dump(bd, arquivo, indent=2, ensure_ascii=False)

# Para recriar as instâncias
# with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
#    pessoas_json = json.load(arquivo)
#    p1_novo = Pessoa(**pessoas_json[0])
#    print(p1_novo.nome)
````

### Observações Finais:

A Programação Orientada a Objetos oferece uma maneira estruturada e poderosa de modelar problemas e organizar o código. Os conceitos de classes, objetos, atributos de instância e de classe, e métodos são os alicerces para construir sistemas mais complexos e fáceis de manter. A habilidade de persistir dados de objetos em formatos como JSON, como visto no exercício, é uma etapa crucial para o desenvolvimento de aplicações reais.