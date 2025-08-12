## Dia 34: pathlib

### Prefácio:

Hoje exploramos a biblioteca ``pathlib``, uma forma moderna e orientada a objetos de manipular caminhos de sistemas de arquivos em Python. Diferentemente do módulo ``os.path``, ``pathlib`` oferece uma interface mais intuitiva e robusta para interagir com arquivos e diretórios, tornando o código mais legível e menos propenso a erros.

### Manipulação de Caminhos com Pathlib:

A classe ``Path`` da biblioteca ``pathlib`` representa caminhos do sistema de arquivos. Em vez de strings, trabalhamos com objetos ``Path``, que possuem métodos e propriedades úteis para diversas operações.

- **Criação de Objetos ``Path``**: É possível criar um objeto ``Path`` para o diretório atual ``Path()``, para o diretório do script ``Path(__file__)``, ou para caminhos específicos, como o diretório home do usuário ``Path.home()``.

- **Construção de Caminhos**: A união de caminhos é feita de forma simples e segura com o operador ``/`` (barra), que garante a sintaxe correta do sistema operacional.

- **Informações do Caminho**: Propriedades como ``parent`` (diretório pai) e ``absolute()`` (caminho absoluto) fornecem informações sobre o caminho.

````
# Exemplo 1: Criação e manipulação de caminhos
from pathlib import Path

# Caminho para o diretório atual
caminho_atual = Path()
print(f'Caminho absoluto: {caminho_atual.absolute()}')

# Caminho para um arquivo no Desktop do usuário
caminho_arquivo = Path.home() / 'Desktop' / 'relatorio.txt'
print(f'Caminho do arquivo: {caminho_arquivo}')
````

### Operações Básicas com Arquivos:

``pathlib`` simplifica as operações de arquivo, eliminando a necessidade de usar o módulo ``os`` para muitas tarefas.

- ``Criação e Exclusão``: É possível criar arquivos vazios com ``touch()`` e excluí-los com ``unlink()``.

Leitura e Escrita Rápida: Para operações simples, ``write_text()`` e ``read_text()`` permitem ler e escrever conteúdo de forma direta.

Leitura e Escrita Avançada: O método ``open()`` permite abrir o arquivo com um gerenciador de contexto (``with``), garantindo que o arquivo seja fechado automaticamente.

````
# Exemplo 2: Operações de arquivo
from pathlib import Path

caminho_arquivo = Path.home() / 'Desktop' / 'teste.txt'

# Cria e escreve no arquivo
caminho_arquivo.write_text('Olá, pathlib!')
print(caminho_arquivo.read_text()) # Saída: Olá, pathlib!

# Exclui o arquivo
caminho_arquivo.unlink()
````

### Operações com Diretórios:

Manipular diretórios também se torna mais claro com ``pathlib``.

- **Criação de Diretórios**: O método ``mkdir()`` cria um diretório. O parâmetro ``exist_ok=True`` evita erros caso o diretório já exista.

- **Listagem de Conteúdo**: O método ``glob('*')`` retorna um iterador para listar todos os arquivos e diretórios dentro de um caminho.

**Remoção de Diretórios**: ``rmdir()`` remove um diretório vazio. Para remover diretórios não vazios, pode-se usar o módulo ``shutil.rmtree``.

````
# Exemplo 3: Operações com diretórios
from pathlib import Path
from shutil import rmtree

caminho_pasta = Path.home() / 'Desktop' / 'projeto'
subpasta = caminho_pasta / 'docs'

# Cria diretórios
subpasta.mkdir(parents=True, exist_ok=True)

# Cria um arquivo dentro da subpasta
arquivo_doc = subpasta / 'documento.txt'
arquivo_doc.touch()

# Exclui o arquivo
arquivo_doc.unlink()

# Remove a subpasta (deve estar vazia)
subpasta.rmdir()

# Exemplo de remoção de pastas com shutil.rmtree
# rmtree(caminho_pasta) # Descomente para apagar o diretório
````

### Iterando sobre o Conteúdo de um Diretório:

``pathlib`` permite a iteração sobre arquivos e pastas de forma simples, facilitando a automação de tarefas.

````
# Exemplo 4: Iterando sobre arquivos em uma pasta
from pathlib import Path

caminho_pasta = Path.home() / 'Desktop' / 'Pasta_Exemplo'
caminho_pasta.mkdir(exist_ok=True)

# Cria alguns arquivos de exemplo
for i in range(3):
    (caminho_pasta / f'file_{i}.txt').touch()

# Itera sobre os arquivos da pasta
print('Arquivos na pasta:')
for item in caminho_pasta.iterdir():
    if item.is_file():
        print(f'- Arquivo: {item.name}')

# Limpa a pasta
for item in caminho_pasta.iterdir():
    item.unlink()
caminho_pasta.rmdir()
````

### Observações Finais:

``pathlib`` é a abordagem recomendada para manipulação de caminhos em Python, substituindo o uso de ``os.path`` em novos projetos. Sua interface orientada a objetos é mais segura e expressiva, minimizando erros comuns. A transição para ``pathlib`` resulta em código mais claro, conciso e portável entre diferentes sistemas operacionais.