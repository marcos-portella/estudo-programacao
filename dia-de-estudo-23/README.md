## Dia 23: Manipulação de Arquivos e o Módulo ``json``

### Prefácio:

Hoje, focamos na manipulação de arquivos em Python, explorando como ler, escrever e gerenciar dados de forma eficiente. Revisitamos o conceito de gerenciadores de contexto (``with``), que garantem que os arquivos sejam abertos e fechados corretamente, e aprofundamos no uso do módulo ``json`` para serializar (salvar) e desserializar (carregar) dados em arquivos, uma prática fundamental para persistência de dados.

### Manipulação de Arquivos com Python:
A função ``open()`` é a porta de entrada para trabalhar com arquivos em Python. Ela aceita o caminho do arquivo e o modo de operação como argumentos.

- **Modos de Operação**:

    - ``r``: leitura (padrão).

    - ``w``: escrita (cria ou sobrescreve o arquivo).

    - ``x``: criação exclusiva (levanta um erro se o arquivo já existe).

    - ``a``: anexa ao final do arquivo.

    - ``+``: leitura e escrita.

- **Gerenciador de Contexto (``with``)**: É a forma recomendada de lidar com arquivos, pois ele garante que o arquivo seja fechado automaticamente, mesmo se ocorrer um erro.

### Métodos úteis para manipulação de arquivos:

- ``write()``: escreve uma string no arquivo.

- ``writelines()``: escreve uma sequência de strings (por exemplo, uma tupla ou lista).

- ``read()``: lê o conteúdo completo do arquivo.

- ``readline()``: lê uma única linha.

- ``readlines()``: lê todas as linhas e retorna uma lista de strings.

- ``seek()``: move o cursor para uma posição específica no arquivo.

````
# Exemplo 1: Escrevendo e lendo um arquivo de texto
caminho_arquivo = 'meu_arquivo.txt'

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.seek(0, 0) # Volta o cursor para o início
    print(arquivo.read())

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
````

### O Módulo ``json``:

O módulo ``json`` é essencial para trabalhar com a notação de objeto JavaScript (JSON). Ele permite converter estruturas de dados Python (como dicionários, listas, tuplas) em strings JSON (serialização) e vice-versa (desserialização).

- ``json.dump()``: Serializa um objeto Python e o salva em um arquivo aberto.

- ``json.load()``: Carrega dados de um arquivo JSON e os desserializa em um objeto Python.

````
# Exemplo 2: Usando json.dump para serializar e salvar um dicionário em um arquivo
import json

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'altura': 1.8,
    'dev': True,
}

caminho_arquivo_json = 'dados.json'

with open(caminho_arquivo_json, 'w', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo, indent=2, ensure_ascii=False)
Python
````
````
# Exemplo 3: Usando json.load para carregar dados de um arquivo JSON
import json

caminho_arquivo_json = 'dados.json'

with open(caminho_arquivo_json, 'r', encoding='utf8') as arquivo:
    dados_carregados = json.load(arquivo)
    print(dados_carregados)
    print(type(dados_carregados)) # A saída será <class 'dict'>
````

### Problema dos Parâmetros Mutáveis:

É importante ter cuidado ao usar tipos de dados mutáveis (como listas e dicionários) como valores padrão em parâmetros de funções. Isso pode levar a comportamentos inesperados, pois o mesmo objeto mutável é compartilhado entre todas as chamadas da função se nenhum novo argumento for fornecido.

A solução correta é usar ``None`` como valor padrão e inicializar o objeto mutável dentro da função, como demonstrado abaixo.

````
# Exemplo 4: Forma correta de lidar com parâmetros mutáveis
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Helena')
print(cliente2)
````

Exercício Prático: Lista de Tarefas com Persistência:
Um exemplo prático que integra a manipulação de arquivos com o módulo json é a criação de um aplicativo de lista de tarefas com funcionalidades de desfazer e refazer. A lista de tarefas pode ser salva em um arquivo JSON ao final de cada operação e carregada ao iniciar o programa, garantindo que os dados persistam entre as execuções.

````
# Exemplo 5: Trecho de código do exercício de lista de tarefas
import json

def ler(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        return []
    return dados

def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)

CAMINHO_ARQUIVO = 'lista_tarefas.json'
tarefas = ler(CAMINHO_ARQUIVO)
print(f'Tarefas carregadas: {tarefas}')
````

### Observações Finais:

A manipulação de arquivos é uma habilidade crucial para persistir dados e interagir com o sistema de arquivos. O uso do gerenciador de contexto ``with`` é fundamental para evitar problemas de recursos não fechados. O módulo ``json`` oferece uma maneira padrão e eficiente de salvar e carregar dados estruturados, sendo uma ferramenta indispensável para o desenvolvimento de aplicações robustas. O exercício da lista de tarefas exemplifica como esses conceitos se combinam para criar uma aplicação prática e funcional.