## Dia 34: JSON

### Prefácio:

Hoje exploramos o **JSON (JavaScript Object Notation)**, um formato leve de intercâmbio de dados. Entendemos sua estrutura, os tipos de dados que ele suporta e, mais importante, como manipular dados JSON em Python usando o módulo ``json``. Abordamos a conversão de objetos Python para strings JSON e vice-versa, e como trabalhar com arquivos JSON.

### O que é JSON?

JSON é uma estrutura de dados textual utilizada para serializar objetos e facilitar a comunicação de dados entre diferentes sistemas, como em APIs web. Ele suporta vários tipos de dados, incluindo números (inteiros e floats), strings (entre aspas duplas), booleanos (``true`` e ``false``), arrays (listas ordenadas), objetos (pares chave-valor) e ``null`` para representar ausência de valor.

- **Conversão Python para JSON**: Tipos de dados Python são mapeados para tipos JSON. Por exemplo, um ``dict`` em Python se torna um ``object`` em JSON, e uma ``list`` ou ``tuple`` se torna um ``array``.

- **Conversão JSON para Python**: O inverso também é verdadeiro. Quando dados JSON são carregados em Python, eles são convertidos para os tipos de dados correspondentes.

````
# Exemplo 1: Conversão de string JSON para objeto Python
import json
from pprint import pprint

string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf"]
}
'''

# json.loads carrega uma string JSON
filme = json.loads(string_json)
pprint(filme)
print(f'Ano do filme: {filme["year"]}')
````

### Serializando e Deserializando com o Módulo json:

O módulo ``json`` do Python oferece duas funções principais para a manipulação de dados JSON:

- ``json.dumps()``: Converte um objeto Python para uma string JSON.

- ``json.loads()``: Converte uma string JSON de volta para um objeto Python.

````
# Exemplo 2: Usando json.dumps para formatar uma string JSON
import json

movie = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

# Converte o dicionário Python para uma string JSON formatada
json_string_formatado = json.dumps(movie, ensure_ascii=False, indent=2)
print(json_string_formatado)
````

### Manipulação de Arquivos JSON:

Para trabalhar com arquivos, o módulo ``json`` fornece funções específicas que facilitam a leitura e a escrita direta de arquivos.

- ``json.dump()``: Serializa um objeto Python para um arquivo JSON.

- ``json.load()``: Desserializa um arquivo JSON para um objeto Python.

Essas funções são ideais para persistir dados.

````
# Exemplo 3: Usando json.dump e json.load com arquivos
import json
import os

NOME_ARQUIVO = 'meu_filme.json'

movie = {
    'title': 'O Senhor dos Anéis',
    'year': 2001,
    'characters': ['Frodo', 'Gandalf']
}

# Escreve o dicionário no arquivo
with open(NOME_ARQUIVO, 'w', encoding='utf8') as arquivo:
    json.dump(movie, arquivo, ensure_ascii=False, indent=2)

print(f'Arquivo "{NOME_ARQUIVO}" criado com sucesso!')

# Lê o arquivo e carrega os dados em um dicionário Python
with open(NOME_ARQUIVO, 'r', encoding='utf8') as arquivo:
    filme_do_json = json.load(arquivo)
    print(filme_do_json)

# Limpa o arquivo de exemplo
os.remove(NOME_ARQUIVO)
````

### Observações Finais:

O formato JSON é uma pedra angular na comunicação entre sistemas modernos. Saber como usar o módulo ``json`` em Python para serializar e desserializar dados é uma habilidade fundamental para qualquer programador que lide com APIs, armazenamento de configurações ou troca de dados. As funções ``dumps`` e ``loads`` para strings, e ``dump`` e ``load`` para arquivos, simplificam enormemente essas tarefas, tornando o processo seguro e intuitivo.