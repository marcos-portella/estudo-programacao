### Dia 19

### Prefácio:

Hoje abordamos tópicos cruciais para a construção de aplicações Python robustas e escaláveis: o **tratamento avançado de exceções**, a modularização do código para melhor organização, e a introdução a **funções geradoras** para otimização de memória. Esses conceitos são fundamentais para escrever código profissional e eficiente.

### Tratamento Avançado de Exceções (``try``, ``except``, ``else``, ``finally``, ``raise``):

O tratamento de exceções é vital para criar programas tolerantes a falhas. Além do básico ``try-except``, Python oferece cláusulas adicionais e a capacidade de levantar exceções personalizadas.

- **``try`` e ``except``**: O bloco ``try`` contém o código que pode gerar um erro, e o ``except`` lida com esse erro. É possível especificar o tipo de exceção a ser capturada. [cite: uploaded:try_except_exceções.py]

- **Capturando Múltiplas Exceções**: Pode-se capturar diferentes tipos de exceções em blocos ``except`` separados ou em uma única tupla. [cite: uploaded:try_except_exceções.py]

- ``else``: O bloco ``else`` (em um ``try-except-else-finally``) é executado **apenas se nenhuma exceção** ocorrer no bloco ``try``. [cite: uploaded:try_except_else_finally.py]

- ``finally``: O bloco finally é **sempre executado**, independentemente de uma exceção ter ocorrido ou não. É ideal para limpeza de recursos (ex: fechar arquivos). [cite: uploaded:try_except_else_finally.py]

- ``raise``: A palavra-chave ``raise`` é usada para **lançar (disparar) explicitamente uma exceção**. Isso é útil para indicar que uma condição de erro foi encontrada e que o chamador da função deve lidar com ela. [cite: uploaded:_raise.py]

````
# Exemplo 1: try, except, else e finally
try:
    print('Abrindo arquivo...')
    # 8 / 0 # Descomente para testar ZeroDivisionError
    # lista[10] # Descomente para testar IndexError
except ZeroDivisionError as e:
    print(f'Erro de divisão por zero: {e}')
except IndexError as e:
    print(f'Erro de índice: {e}')
except Exception as e: # Captura qualquer outra exceção
    print(f'Erro desconhecido: {e}')
else:
    print('Nenhum erro ocorreu no bloco try.') # Executado se não houver exceção
finally:
    print('Fechando recursos (sempre executado).') # Sempre executado
```python
# Exemplo 2: Levantando exceções com 'raise'
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero!') # Lança uma exceção
    return True

def deve_ser_int_ou_float(n):
    if not isinstance(n, (float, int)):
        tipo_n = type(n).__name__
        raise TypeError(f'"{n}" deve ser int ou float. "{tipo_n}" enviado.') # Lança TypeError
    return True

def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d) # Se d for zero, uma exceção será levantada aqui
    return n / d

try:
    print(divide(8, 2)) # Saída: 4.0
    # print(divide(8, '0')) # Descomente para testar TypeError
    # print(divide(8, 0)) # Descomente para testar ZeroDivisionError
except (TypeError, ZeroDivisionError) as e:
    print(f'Erro ao dividir: {e}')
````

### Modularização:

A modularização é a prática de organizar o código em arquivos separados (módulos) e pastas (pacotes) para melhorar a organização, reusabilidade e manutenibilidade.

- **Módulos**: Arquivos ``.py`` que contêm código Python.

- **Importação**: Usamos ``import`` para trazer módulos para o escopo atual.

    - ``import nome_modulo``: Importa o módulo inteiro. Acessa-se com nome_modulo.funcao(). [cite: uploaded:modulos_import_from_as_asterisk.py]

    - ``from nome_modulo import objeto``: Importa objetos específicos (funções, classes, variáveis). Acessa-se diretamente objeto(). [cite: uploaded:modulos_import_from_as_asterisk.py]

    - ``as``: Cria um alias (apelido) para o módulo ou objeto importado. [cite: uploaded:modulos_import_from_as_asterisk.py]

    - ``from nome_modulo import *``: Importa TUDO do módulo. Considerado má prática por poluir o namespace e dificultar a rastreabilidade. [cite: uploaded:modulos_import_from_as_asterisk.py]

- ``__name__``: Uma variável especial que é definida como '__main__' quando o módulo é executado diretamente, e como o nome do módulo quando é importado. Útil para código que só deve rodar quando o módulo é o principal. [cite: uploaded:modularizacao.py]

- ``sys.path``: Lista de diretórios onde o Python procura por módulos. [cite: uploaded:modularizacao.py]

````
# Exemplo 3: Importação de módulos
import sys # Importa o módulo sys inteiro
print(sys.platform) # Acessa a plataforma do sistema

from sys import exit as sair_do_programa # Importa 'exit' com um alias
# sair_do_programa() # Chamaria a função exit()

# Exemplo 4: Usando __name__
# No arquivo 'meu_modulo.py':
# def minha_funcao():
#     print('Minha função de meu_modulo')
#
# if __name__ == '__main__':
#     print('Este código só roda se meu_modulo.py for executado diretamente')
#     minha_funcao()

# No arquivo principal:
# import meu_modulo
# meu_modulo.minha_funcao()
````

### Funções Geradoras (``yield``, ``yield`` ``from``):

Funções geradoras são uma forma eficiente de criar iteradores. Em vez de retornar uma coleção completa de uma vez (como uma lista), elas "cedem" (``yield``) valores um por um, sob demanda, pausando sua execução e retomando de onde pararam. Isso economiza memória, especialmente para sequências grandes.

- ``yield``: A palavra-chave ``yield`` transforma uma função em uma função geradora. Cada vez que ``yield`` é encontrado, o valor é retornado e o estado da função é salvo. Na próxima chamada, a execução é retomada a partir desse ponto. [cite: uploaded:generator_functions.py]

- ``yield from``: Usado para delegar a um subgerador ou iterável, permitindo que os valores sejam cedidos diretamente de outro gerador ou iterável. [cite: uploaded:yield_from.py]

````
# Exemplo 5: Função Geradora simples
def meu_gerador(n=0, maximo=3):
    print('Começou o gerador!')
    while n <= maximo:
        yield n # Cede o valor e pausa a execução
        n += 1
    print('Gerador finalizado!')

gen = meu_gerador(maximum=2) # Cria um objeto gerador
print(next(gen)) # Saída: Começou o gerador! \n 0
print(next(gen)) # Saída: 1
print(next(gen)) # Saída: 2
# print(next(gen)) # Geraria StopIteration, pois o gerador terminou

# Exemplo 6: Usando 'yield from' para encadear geradores
def gerador_secundario():
    print('Começou o gerador secundário')
    yield 'A'
    yield 'B'
    print('Acabou o gerador secundário')

def gerador_principal():
    print('Começou o gerador principal')
    yield from gerador_secundario() # Delega para gerador_secundario
    yield 'C'
    print('Acabou o gerador principal')

g = gerador_principal()
for item in g:
    print(item)
# Saída:
# Começou o gerador principal
# Começou o gerador secundário
# A
# B
# Acabou o gerador secundário
# C
# Acabou o gerador principal
````

### Observações Finais:

O Dia 19 nos equipou com ferramentas essenciais para escrever código Python mais robusto, organizado e eficiente. O **tratamento de exceções** com ``try-except-else-finally`` e ``raise`` permite criar programas que lidam elegantemente com erros. A **modularização** é crucial para a escalabilidade e manutenção de projetos. E as **funções geradoras** com ``yield`` e ``yield from`` são otimizações poderosas para trabalhar com grandes volumes de dados de forma eficiente em termos de memória. Dominar esses conceitos é um marco importante na sua jornada de programação em Python.