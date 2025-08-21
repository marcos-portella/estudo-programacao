## Dia 36

### Prefácio:

Hoje exploramos três módulos essenciais da biblioteca padrão do Python, cada um com um propósito distinto. Iniciamos com o módulo ``random`` para a geração de números pseudoaleatórios, um conceito fundamental em diversas aplicações. Em seguida, diferenciamos seu uso do módulo ``secrets``, crucial para a geração de dados aleatórios criptograficamente seguros. Finalizamos com o ``string.Template``, uma ferramenta elegante para a substituição de variáveis em strings, ideal para a criação de templates e mensagens dinâmicas.

### Geração de Números Aleatórios: ``random`` e ``secrets``

- **Módulo ``random``**: Este módulo é usado para gerar números pseudoaleatórios. Os números gerados parecem aleatórios, mas são previsíveis se a "semente" (seed) do gerador for conhecida, o que os torna inadequados para aplicações de segurança ou criptográficas.

````
# Exemplo 1: Uso do módulo random
import random

# Gera um inteiro aleatório entre 10 e 20 (incluindo 20)
r_int = random.randint(10, 20)
print(f'Inteiro aleatório: {r_int}')

# Escolhe um item aleatório de uma lista
nomes = ['João', 'Maria', 'Pedro', 'Ana']
r_choice = random.choice(nomes)
print(f'Nome aleatório: {r_choice}')

# Embaralha a lista no local
random.shuffle(nomes)
print(f'Lista embaralhada: {nomes}')
````

- **Módulo ``secrets``**: O módulo ``secrets`` é projetado especificamente para gerar números aleatórios seguros, apropriados para gerenciar dados sensíveis, como senhas, tokens de segurança e chaves de conta. Ele utiliza o gerador de números aleatórios do sistema operacional, que é mais seguro do que o do módulo ``random``.

````
# Exemplo 2: Uso do módulo secrets
import secrets
import string

# Gera um token hexadecimal de 32 bytes
token = secrets.token_hex(32)
print(f'Token Hex: {token}')

# Gera uma URL segura (reset_token)
url_safe_token = secrets.token_urlsafe(32)
print(f'Token URL-safe: {url_safe_token}')

# Gera uma senha aleatória
senha_segura = ''.join(
    secrets.SystemRandom().choices(
        string.ascii_letters + string.digits + string.punctuation,
        k=16
    )
)
print(f'Senha segura: {senha_segura}')
````

### Substituição de Variáveis em Strings: ``string.Template``

O ``string.Template`` é uma classe do módulo ``string`` que facilita a substituição de variáveis em textos, de forma mais legível do que a formatação com f-strings ou o método ``.format()``. É útil para criar templates de e-mails, documentos ou outras strings que precisam de valores variáveis.

- **Sintaxe**: O delimitador padrão é ``$``, seguido pelo nome da variável. Variáveis com nomes compostos devem ser envoltas em chaves ``{}``.

- **Métodos**: ``substitute()`` levanta um erro (``KeyError``) se uma variável não for encontrada, enquanto ``safe_substitute()`` não levanta um erro, substituindo a variável ausente por sua sintaxe original.

````
# Exemplo 3: Usando string.Template
from string import Template

template_string = Template('Olá, $nome! Seja bem-vindo à $empresa.')
texto = template_string.substitute(nome='Luiz', empresa='Google')
print(texto)
````

Para uso com arquivos de texto, a classe ``Template`` pode ser combinada com gerenciadores de contexto para ler o template e substituir as variáveis.

````
# Exemplo 4: Usando string.Template com um arquivo
from string import Template
from pathlib import Path

# Supondo que o arquivo '_string.template_.txt' existe com o conteúdo adequado
CAMINHO_ARQUIVO = Path(__file__).parent / '_string.template_.txt'

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    conteudo = arquivo.read()
    template = Template(conteudo)

dados_cliente = {
    'nome': 'João',
    'valor': 'R$ 1.234,56',
    'data': '29/08/2023',
    'empresa': 'ACME Inc.',
    'telefone': '(99) 99999-9999'
}

# Realiza a substituição usando o dicionário
mensagem = template.safe_substitute(dados_cliente)
print(mensagem)
````

### Observações Finais:

O entendimento de ``random`` e ``secrets`` é crucial para escolher a ferramenta correta para a tarefa. Enquanto ``random`` é ideal para simulações e jogos, o ``secrets`` é a escolha segura para criptografia. Por sua vez, o ``string.Template`` oferece uma alternativa elegante e de fácil leitura para a formatação de strings, sendo uma excelente opção para templates, onde a sintaxe ``$`` é mais clara e menos propensa a erros do que os marcadores ``{}`` ou ``%``.