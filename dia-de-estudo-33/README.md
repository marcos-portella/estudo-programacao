## Dia 33

### Prefácio:
Hoje estudamos a interação com o sistema operacional e na manipulação de arquivos e diretórios. O módulo ``os`` e a biblioteca ``shutil`` são ferramentas indispensáveis para qualquer desenvolvedor que precise automatizar tarefas como organização de arquivos, backups ou processamento de dados. Além disso, exploramos o módulo ``locale``, crucial para garantir que nossas aplicações se adaptem a diferentes configurações regionais, um passo importante para a internacionalização de software.

### Interagindo com o Sistema Operacional: O Módulo ``os``:

O módulo ``os`` (Operating System) fornece uma interface para interagir com o sistema operacional onde o Python está sendo executado. Ele permite realizar diversas operações, desde executar comandos do sistema até manipular caminhos de arquivos.

#### Funções Básicas do ``os``:
O ``os.system()`` permite executar comandos shell diretamente do seu script Python, como limpar o console (``cls`` no Windows, ``clear`` no Linux/Mac) ou exibir mensagens.

````
import os

# Limpa o console (depende do SO)
os.system('cls' if os.name == 'nt' else 'clear')
print('Console limpo!')
````

#### Trabalhando com Caminhos: ``os.path``:
O submódulo ``os.path`` é essencial para lidar com caminhos de arquivos e diretórios de forma independente do sistema operacional (Windows, Linux, macOS). Ele abstrai as diferenças de separadores de caminho (``\`` ou ``/``).

``os.path.join()``: Concatena componentes de caminho de forma inteligente.

``os.path.split()``: Divide um caminho em uma tupla (diretório, arquivo).

``os.path.splitext()``: Separa o nome do arquivo de sua extensão.

``os.path.exists()``: Verifica se um caminho existe.

``os.path.isdir()`` / ``os.path.isfile()``: Verificam se um caminho é um diretório ou um arquivo, respectivamente.

``os.path.getsize()``: Retorna o tamanho de um arquivo em bytes.

````
import os

caminho_exemplo = os.path.join('pasta', 'subpasta', 'arquivo.txt')
print(f"Caminho formatado: {caminho_exemplo}") # Saída: pasta/subpasta/arquivo.txt (no Linux/Mac)

diretorio, arquivo = os.path.split(caminho_exemplo)
print(f"Diretório: {diretorio}, Arquivo: {arquivo}")

nome, extensao = os.path.splitext(arquivo)
print(f"Nome: {nome}, Extensão: {extensao}")

# Verificando existência e tipo (requer que o arquivo/pasta exista)
# if os.path.exists('meu_arquivo.txt'):
#     print('Arquivo existe!')
````

#### Listando Conteúdo de Diretórios: ``os.listdir()`` e ``os.walk()``:
- ``os.listdir()``: Retorna uma lista de todas as entradas (arquivos e diretórios) em um determinado caminho. É útil para listar o conteúdo imediato de uma pasta.

````
import os

# Supondo que 'meu_diretorio' exista no mesmo nível do script
# for entrada in os.listdir('meu_diretorio'):
#     print(entrada)
````

``os.walk()``: Permite percorrer uma estrutura de diretórios de forma recursiva, gerando uma tupla ``(root, dirs, files)`` para cada diretório encontrado. Isso é extremamente útil para operações que precisam inspecionar todos os arquivos e subdiretórios de uma árvore.

````
import os

# Exemplo de caminhamento recursivo de um diretório
caminho_base = os.path.expanduser('~') # Diretório Home do usuário

for root, dirs, files in os.walk(caminho_base):
    print(f'Pasta atual: {root}')
    for dir_name in dirs:
        print(f'  Subdiretório: {dir_name}')
    for file_name in files:
        print(f'  Arquivo: {file_name}')
        # Exemplo: obter metadados do arquivo
        caminho_completo_arquivo = os.path.join(root, file_name)
        # stat_info = os.stat(caminho_completo_arquivo)
        # print(f'    Tamanho: {stat_info.st_size} bytes') # Mais detalhes em os.stat_.py
````

#### Obtendo Metadados com ``os.stat()``:
O ``os.stat()`` retorna informações detalhadas sobre um arquivo ou diretório, como tamanho (``st_size``), horários de criação, modificação e último acesso (``st_ctime``, ``st_mtime``, ``st_atime``), entre outros. Isso é útil para auditoria, organização ou qualquer lógica que dependa dos atributos do sistema de arquivos.

````
import os
import math

def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    """Formata um tamanho em bytes para uma unidade legível (B, KB, MB, GB, etc.)"""
    if tamanho_em_bytes <= 0:
        return "0B"
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    indice = int(math.log(tamanho_em_bytes, base))
    potencia = base ** indice
    tamanho_final = tamanho_em_bytes / potencia
    abreviacao = abreviacao_tamanhos[indice]
    return f'{tamanho_final:.2f} {abreviacao}'

# Exemplo de uso:
# path_do_arquivo = 'caminho/para/seu/arquivo.txt'
# if os.path.exists(path_do_arquivo):
#     info_arquivo = os.stat(path_do_arquivo)
#     print(f"Tamanho do arquivo: {formata_tamanho(info_arquivo.st_size)}")
#     print(f"Última modificação: {datetime.fromtimestamp(info_arquivo.st_mtime)}")
````

### Manipulação Avançada de Arquivos e Diretórios: ``shutil``:
O módulo ``shutil`` (shell utilities) oferece operações de alto nível com arquivos e coleções de arquivos, facilitando tarefas comuns que seriam mais complexas apenas com ``os``.

``shutil.copy(src, dst)``: Copia o arquivo ``src`` para ``dst``.

``shutil.copytree(src, dst)``: Copia recursivamente um diretório inteiro (e seu conteúdo).

``shutil.move(src, dst)``: Move (ou renomeia) um arquivo ou diretório de src para dst.

``shutil.rmtree(path)``: Remove um diretório e todo o seu conteúdo recursivamente (USE COM CAUTELA!).

``os.unlink(path)``: Remove um arquivo.

````
import os
import shutil

# Exemplo (cuidado ao executar, pode modificar seus arquivos!)
# Criar uma pasta temporária para o exemplo
# os.makedirs('pasta_teste/sub_pasta', exist_ok=True)
# with open('pasta_teste/arquivo_original.txt', 'w') as f:
#     f.write('Conteúdo do arquivo original.')

# Copiar arquivo
# shutil.copy('pasta_teste/arquivo_original.txt', 'pasta_teste/copia_arquivo.txt')

# Mover/Renomear arquivo
# shutil.move('pasta_teste/copia_arquivo.txt', 'pasta_teste/arquivo_movido.txt')

# Apagar arquivo
# os.unlink('pasta_teste/arquivo_movido.txt')

# Apagar diretório e conteúdo (usar com extrema cautela!)
# shutil.rmtree('pasta_teste')
````

### Internacionalização: O Módulo ``locale``:
O módulo ``locale`` permite que programas Python lidem com configurações culturais específicas de diferentes regiões, como formatação de números, moedas, datas e ordenação de strings. Ao configurar o ``locale``, funções do Python que dependem dessas configurações (como a exibição de nomes de meses e dias da semana no ``calendar``) se adaptarão.

````
import calendar
import locale

# Define o locale para o padrão do sistema (ou um específico, ex: 'pt_BR.UTF-8')
# Pode variar dependendo do SO. Em Windows, 'Portuguese_Brazil.1252' ou 'pt_BR'
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    # Tenta uma alternativa para Windows
    try:
        locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
    except locale.Error:
        print("Não foi possível definir o locale para pt_BR.")

print(calendar.calendar(2025)) # Agora, nomes de meses e dias podem aparecer em português
````

### Observações Finais:

A manipulação de arquivos e diretórios via ``os`` e ``shutil`` é uma competência fundamental para automação de tarefas e gerenciamento de dados. A capacidade de inspecionar metadados de arquivos com ``os.stat`` adiciona uma camada de controle e análise. Por fim, a compreensão do módulo ``locale`` é um passo crucial para desenvolver aplicações que sejam verdadeiramente globais, adaptando-se às nuances culturais de seus usuários. Dominar essas ferramentas é essencial para construir sistemas Python robustos e completos.