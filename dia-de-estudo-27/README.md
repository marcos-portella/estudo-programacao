## Dia 27: Programação Funcional e Princípios de Design de Software (SOLID)

### Prefácio:

Hoje aprofundamos em conceitos de design de software com base na leitura dos capítulos 6 a 8 do livro "Arquitetura Limpa". O foco principal foi a **Programação Funcional** e o poder da **Imutabilidade**, e uma introdução aos princípios de design de software, com uma ênfase especial no **Princípio de Responsabilidade Única (SRP)** e no **Princípio Aberto/Fechado (OCP)**.

### O Paradigma da Programação Funcional:

A Programação Funcional (PF) tem como conceito central a **imutabilidade**: os dados não são alterados após a sua criação. Isso elimina os "efeitos colaterais" e permite que as funções sejam puras, sempre retornando o mesmo resultado para a mesma entrada. Embora Python não seja puramente funcional, podemos aplicar seus princípios usando funções como objetos de primeira classe e funções de ordem superior.

- **Imutabilidade**: Garantir que variáveis e objetos não possam ser modificados.

- **Funções de Primeira Classe**: Funções podem ser tratadas como qualquer outro objeto, podendo ser atribuídas a variáveis, passadas como argumentos e retornadas de outras funções.

- **Funções de Ordem Superior**: Funções que recebem outras funções como argumentos ou retornam uma função.

````
# Exemplo 1: Imutabilidade com tuplas
dados_originais = ('produto A', 'preço', 100) # Tuplas são imutáveis
print(f'Dados originais: {dados_originais}')

# Tentativa de alteração resulta em erro: TypeError: 'tuple' object does not support item assignment
# dados_originais[2] = 120

# Para "modificar", criamos uma nova tupla
dados_novos = (dados_originais[0], dados_originais[1], 120)
print(f'Dados novos: {dados_novos}')
````

### Princípios SOLID:

Os princípios SOLID são diretrizes de design que visam criar software fácil de manter, escalável e compreensível.

- **SRP (Single Responsibility Principle - Princípio da Responsabilidade Única)**: Um módulo (classe, função, etc.) deve ter uma e apenas uma razão para mudar.

- **OCP (Open/Closed Principle - Princípio Aberto/Fechado)**: Um módulo deve ser aberto para extensão, mas fechado para modificação.

````
# Exemplo 2: O Princípio da Responsabilidade Única (SRP)
# Ruim: a classe tem responsabilidades demais
class Pedido:
    def __init__(self, cliente, itens):
        self.cliente = cliente
        self.itens = itens

    def salvar_no_banco_de_dados(self):
        # Lógica para salvar o pedido
        pass
    
    def enviar_email_confirmacao(self):
        # Lógica para enviar o email
        pass

# Bom: separando as responsabilidades
class Pedido: # Apenas a responsabilidade de ser um pedido
    def __init__(self, cliente, itens):
        self.cliente = cliente
        self.itens = itens

class RepositorioPedido: # Apenas a responsabilidade de persistência
    def salvar(self, pedido):
        # Lógica para salvar
        pass

class NotificadorEmail: # Apenas a responsabilidade de notificação
    def enviar(self, pedido):
        # Lógica para enviar
        pass
````

### O Princípio Aberto/Fechado (OCP):

Este princípio afirma que a arquitetura deve ser desenhada para permitir que novas funcionalidades sejam adicionadas sem que o código existente precise ser modificado. Isso é comumente alcançado através do uso de herança e polimorfismo. Ao invés de usar ``if/else`` para tratar novos tipos, criamos novas classes que estendem uma classe base e implementam a nova funcionalidade.

````
# Exemplo 3: O Princípio Aberto/Fechado (OCP)
# Ruim: o código da função 'calcular_area' precisa ser modificado
# para cada novo tipo de forma geométrica
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

def calcular_area(forma):
    if isinstance(forma, Retangulo):
        return forma.largura * forma.altura
    # Se uma nova forma, como Círculo, for adicionada,
    # esta função precisa ser modificada.

# Bom: Usando polimorfismo, a função está "fechada" para modificação
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura

class Circulo(Forma): # Extensão, sem modificar a função original
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        import math
        return math.pi * self.raio ** 2

def calcular_area(forma):
    return forma.calcular_area()

# Agora podemos adicionar novas formas sem alterar a função 'calcular_area'
````

### As Quatro Coisas de Um Software:

O autor destaca que existem quatro componentes em um software: **Dados**, **Funções**, **Estruturas de Dados** e **Funções de Transição de Dados**. A programação funcional, com sua ênfase em funções puras e imutabilidade, minimiza a complexidade e os erros relacionados aos estados de um sistema.

````
# Exemplo 4: Abordagem imperativa vs. funcional
# Imperativo (altera o estado original)
numeros = [1, 2, 3]
def dobrar_imperativo(lista):
    for i in range(len(lista)):
        lista[i] *= 2
dobrar_imperativo(numeros)
print(numeros) # [2, 4, 6]

# Funcional (não altera o estado original)
numeros_originais = [1, 2, 3]
def dobrar_funcional(lista):
    return [x * 2 for x in lista]
numeros_dobrados = dobrar_funcional(numeros_originais)
print(numeros_originais) # [1, 2, 3]
print(numeros_dobrados) # [2, 4, 6]
````

### Observações Finais:
A adoção dos princípios de Programação Funcional e SOLID nos guia para a criação de um código mais limpo, previsível e fácil de manter. A imutabilidade e a separação de responsabilidades são pilares que, quando aplicados, reduzem a probabilidade de bugs e simplificam o processo de adição de novas funcionalidades. O Princípio Aberto/Fechado, em particular, é um norte valioso para construir arquiteturas que resistem à passagem do tempo e à mudança de requisitos.

````
# Exemplo 5: OCP e SRP combinados
from abc import ABC, abstractmethod

class Notificador(ABC): # OCP: aberto para novas formas de notificação
    @abstractmethod
    def enviar(self, mensagem):
        pass

class NotificadorEmail(Notificador): # SRP: tem uma única responsabilidade
    def enviar(self, mensagem):
        print(f'Enviando e-mail: {mensagem}')

class NotificadorSMS(Notificador): # Nova funcionalidade sem mudar o código existente
    def enviar(self, mensagem):
        print(f'Enviando SMS: {mensagem}')

class ServicoDeNotificacao:
    def __init__(self, notificador: Notificador):
        self._notificador = notificador
    
    def notificar_usuario(self, mensagem):
        self._notificador.enviar(mensagem)

# Uso
servico = ServicoDeNotificacao(NotificadorEmail())
servico.notificar_usuario('Olá, mundo!')
# A infraestrutura (ServicoDeNotificacao) não precisa ser alterada
# para usar NotificadorSMS.
````