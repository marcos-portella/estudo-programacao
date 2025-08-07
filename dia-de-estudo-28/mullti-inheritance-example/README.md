## Dia 28: Herança Múltipla, Mixins e Lançamento de Exceções

### Prefácio:

No dia de hoje, aprofundamos em conceitos mais avançados de Herança em Python, focando na **Herança Múltipla** e no poderoso padrão de design **Mixin**. Vimos como os Mixins nos permitem reutilizar código de forma granular, compondo classes com funcionalidades específicas de maneira mais flexível do que a herança tradicional. Além disso, exploramos a criação de classes para o tratamento de logs e a importância de lançar exceções para gerenciar o fluxo de controle em situações de erro.

### Herança Múltipla e o Padrão Mixin:

- **Herança Múltipla**: Permite que uma classe herde de várias classes pai. No entanto, o uso excessivo pode levar a complexidade e a problemas de ambiguidade.

- **Mixin**: Um Mixin é uma classe que não se destina a ser instanciada por si só. Seu propósito é "mixar" funcionalidades em outras classes através da herança múltipla. Isso promove o princípio da composição em detrimento da herança tradicional, permitindo que uma classe ``Eletronico`` possa ter funcionalidades de log (``LogPrintMixin``) sem ter uma relação "é um".

````
# Exemplo 1: Uso de Mixins para adicionar funcionalidade de log
# Definindo as classes Mixin
class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método _log')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

class LogFileMixin(Log):
    def _log(self, msg):
        with open('log.txt', 'a') as f:
            f.write(f'{msg} ({self.__class__.__name__})\n')

# A classe 'Eletronico' herda de uma das classes Mixin
class Eletronico(LogPrintMixin):
    def __init__(self, nome):
        self._nome = nome
    
    def ligar(self):
        self._log(f'Ligando o aparelho {self._nome}')

    def desligar(self):
        self._log(f'Desligando o aparelho {self._nome}')

celular = Eletronico('Celular')
celular.ligar()
celular.desligar()
````

### Lançando e Tratando Exceções:

Exceções são eventos que ocorrem durante a execução de um programa e que alteram seu fluxo normal. A palavra-chave ``raise`` é usada para lançar uma exceção explicitamente. Isso é fundamental para a validação de dados e para garantir que o programa se comporte como esperado em situações de erro.

````
# Exemplo 2: Lançando uma exceção para um atributo inválido
class Eletronico(LogFileMixin):
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            self._log(f'{self._nome} já está ligado.')
            return
        
        self._log(f'{self._nome} ligou.')
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            self._log(f'{self._nome} já está desligado.')
            return

        self._log(f'{self._nome} desligou.')
        self._ligado = False

class SmartPhone(Eletronico):
    def ligar(self):
        super().ligar()
        # Aqui podemos adicionar lógica específica para o smartphone
        
    def desligar(self):
        super().desligar()
        # Aqui podemos adicionar lógica específica para o smartphone

smartphone = SmartPhone('iPhone')
smartphone.ligar()
smartphone.desligar()
````

### O ``NotImplementedError``:

O ``NotImplementedError`` é um tipo de exceção que indica que uma funcionalidade esperada de uma classe abstrata ou de um método mixin não foi implementada pela subclasse. É uma forma de garantir que as classes filhas sigam o "contrato" definido pela classe pai ou mixin.

````
# Exemplo 3: Levantando NotImplementedError em um método abstrato
class Log:
    def _log(self, msg):
        # A classe 'Log' espera que as classes filhas implementem o método '_log'.
        # Se não o fizerem, este erro será levantado.
        raise NotImplementedError('Implemente o método _log na subclasse')

# Tentativa de criar uma classe que não implementa o método
class MinhaClasse(Log):
    pass

try:
    c = MinhaClasse()
    c._log('Teste')
except NotImplementedError as e:
    print(f'Erro: {e}')
````

### O Poder da Composição com Mixins:

A abordagem com Mixins nos permite ter flexibilidade. Podemos facilmente mudar a forma como a classe ``Eletronico`` realiza seus logs apenas trocando a classe Mixin da qual ela herda.

````
# Exemplo 4: Trocando o Mixin de log
class EletronicoComLogNoArquivo(LogFileMixin):
    def __init__(self, nome):
        self._nome = nome
    
    def ligar(self):
        self._log(f'Ligando o aparelho {self._nome}')

celular = EletronicoComLogNoArquivo('Android')
celular.ligar()
# O log agora é escrito no arquivo 'log.txt'
````

### Observações Finais:

O dia 28 nos mostrou uma abordagem poderosa para a reutilização de código e para a arquitetura de software: os Mixins. Em vez de depender de uma herança hierárquica rígida, podemos compor funcionalidades em classes de forma modular. O uso de NotImplementedError e a prática de lançar exceções são cruciais para garantir que nosso código seja robusto e que os contratos entre as classes sejam respeitados. Essa abordagem leva a um design mais flexível e fácil de manter.

````
# Exemplo 5: O método 'ligar' na classe 'Eletronico'
# A lógica de ligar/desligar está na classe principal,
# e o log é uma funcionalidade "misturada" (mixed in)
class Eletronico(LogPrintMixin):
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        
        self._log(f'{self._nome} ligou.')
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            return

        self._log(f'{self._nome} desligou.')
        self._ligado = False

tv = Eletronico('Televisão')
tv.ligar() # Executa a lógica de ligar e também o método _log do Mixin.
tv.desligar()
````