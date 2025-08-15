## Dia 35: CSV

### Prefácio:

Hoje focamos no formato de arquivo **CSV (Comma Separated Values)**, um dos mais simples e amplamente utilizados para o armazenamento e troca de dados tabulares. Exploramos suas características, como os dados são organizados em linhas e colunas, e as regras básicas para sua criação. Em seguida, aprofundamos no módulo ``csv`` do Python, aprendendo a ler e escrever arquivos CSV de forma eficiente.

### O que é CSV?

CSV, ou "Valores Separados por Vírgulas", é um formato de arquivo de texto simples, ideal para dados tabulares. Cada linha no arquivo representa um registro de dados, e os campos dentro de cada linha são separados por um delimitador, geralmente uma vírgula. É comumente usado para importar e exportar dados entre planilhas eletrônicas e bancos de dados.

- **Regras de Formatação**: As regras do CSV são simples. Os valores das colunas devem ser separados por um delimitador único (como a vírgula), cada registro deve estar em uma linha separada, e caracteres de escape (``"``) devem ser usados se o delimitador aparecer dentro de um valor.

````
# Exemplo 1: Estrutura básica de um arquivo CSV
Nome,Idade,Endereço
Luiz Otávio,32,"Av Brasil, 21, Centro"
João da Silva,55,"Rua 22, 44, Nova Era"
````

### Lendo Arquivos CSV com o Módulo ``csv``:

O módulo ``csv`` do Python oferece ferramentas robustas para ler arquivos CSV, tratando corretamente os delimitadores e caracteres de escape.

- **``csv.reader``**: Lê o arquivo CSV linha por linha, retornando cada linha como uma lista de strings.

- **``csv.DictReader``**: Uma opção mais poderosa que lê cada linha como um dicionário. As chaves do dicionário correspondem aos cabeçalhos das colunas.

````
# Exemplo 2: Usando csv.DictReader para ler dados
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'csv_reader.csv'

with open(CAMINHO_CSV, 'r', encoding='utf8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        # Acessa os dados por nome da coluna, como em um dicionário
        print(linha['Nome'], linha['Idade'], linha['Endereço'])
````

### Escrevendo Arquivos CSV com o Módulo ``csv``:

Escrever em arquivos CSV é igualmente simples, usando ``csv.writer`` e ``csv.DictWriter``.

- ``csv.writer``: Escreve dados em um arquivo a partir de uma lista de listas.

- ``csv.DictWriter``: Escreve dados a partir de uma lista de dicionários, o que é mais intuitivo quando se trabalha com dados estruturados. É necessário fornecer os nomes das colunas (``fieldnames``).

````
# Exemplo 3: Usando csv.DictWriter para escrever dados
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'saida.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
]

with open(CAMINHO_CSV, 'w', encoding='utf8') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()
    escritor.writerows(lista_clientes)
````

### Observações Finais:

O módulo ``csv`` do Python é uma ferramenta indispensável para lidar com dados tabulares de forma simples e segura. Em vez de manipular strings manualmente para extrair ou formatar dados, as classes ``reader`` e ``writer`` (junto com suas versões ``Dict``) tratam de todos os detalhes, como delimitadores, aspas e quebras de linha. Essa abordagem torna a leitura e escrita de arquivos CSV em Python muito mais robusta e menos propensa a erros, especialmente quando os dados contêm caracteres especiais.