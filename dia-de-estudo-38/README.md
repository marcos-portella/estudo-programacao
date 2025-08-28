## Dia 38: Protocolo HTTP, Argumentos de Linha de Comando e Compressão de Arquivos

### Prefácio:

No dia 38, mergulhamos em um conjunto de ferramentas essenciais para o desenvolvimento de aplicações robustas em Python. O foco foi a compreensão do **protocolo HTTP** para comunicação via web, o uso de **argumentos de linha de comando** para tornar scripts mais flexíveis e o gerenciamento de arquivos com a biblioteca ``zipfile`` para **compactação e descompactação**.

### Básico do Protocolo HTTP

O **HTTP (HyperText Transfer Protocol)** é a base da comunicação na internet, funcionando em um modelo de cliente/servidor. O cliente (como o seu navegador) envia uma requisição para o servidor (um site), que responde com os dados solicitados. As requisições e respostas são compostas por métodos (como GET, POST, DELETE), endereços de recursos, cabeçalhos e, opcionalmente, o corpo da mensagem. O servidor, por sua vez, responde com um código de status (como 200 para sucesso ou 404 para não encontrado) e os dados solicitados.

````
# Exemplo 1: Estrutura conceitual de uma requisição e resposta HTTP
# Requisição do cliente (ex: navegador)
# Método: GET
# Endereço: /users/profile
# Cabeçalhos: Accept: text/html
# Corpo: (Vazio para GET)

# Resposta do servidor
# Código de status: 200 OK
# Cabeçalhos: Content-Type: text/html
# Corpo: <html><body>...</body></html>
````

### Argumentos de Linha de Comando

Aprender a passar argumentos para scripts via linha de comando é crucial para criar automações flexíveis. O módulo ``sys`` oferece uma forma simples de fazer isso através de ``sys.argv``, uma lista que contém todos os argumentos passados, onde o primeiro elemento (``sys.argv[0]``) é o nome do próprio script.

````
# Exemplo 2: Usando sys.argv para ler argumentos
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos > 1:
    print(f'Você passou os argumentos {argumentos[1:]}')
````

Para scripts mais complexos, a biblioteca ``argparse`` é a solução ideal. Ela fornece uma maneira robusta de analisar argumentos, lidar com opções curtas (``-v``), longas (``--verbose``), definir tipos, valores padrão e até gerar automaticamente a ajuda do script.

````
# Exemplo 3: Usando argparse para argumentos complexos
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs',
    action='store_true'
)

args = parser.parse_args()
print(args.verbose)
````

### Compactando e Descompactando Arquivos

O módulo ``zipfile`` é a maneira padrão em Python de manipular arquivos e diretórios compactados no formato ZIP. Ele permite criar, extrair, listar e adicionar arquivos a um pacote ZIP de forma programática.

````
# Exemplo 4: Compactando arquivos com zipfile
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'diretorio_exemplo'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'arquivos.zip'

# Criação de arquivos de exemplo
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)
with open(CAMINHO_ZIP_DIR / 'exemplo.txt', 'w') as f:
    f.write('Este é um arquivo de teste.')

with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            zip.write(os.path.join(root, file))

print('Arquivos compactados com sucesso!')
````

### Observações Finais:

Aprofundar-se nesses tópicos é crucial para o desenvolvimento de aplicações práticas. O entendimento de HTTP é a base para qualquer interação com serviços e APIs web, enquanto a manipulação de argumentos de linha de comando permite a criação de ferramentas mais versáteis e automatizadas. Por fim, a capacidade de compactar e descompactar arquivos é indispensável para tarefas como backup de dados e distribuição de software, mostrando como essas três habilidades se complementam para construir soluções completas e eficientes.