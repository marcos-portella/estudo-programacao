import json

# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('/Users/marco/Documents/Projects/curso-python-udemy/dia-de-estudo-23/file_23.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False, # Não é necessário usar o ensure_ascii
        indent=2, # Para formatar o arquivo para ele ficar mais legível
    )


# importando informaçõs diretamente do arquivo json
with open('/Users/marco/Documents/Projects/curso-python-udemy/dia-de-estudo-23//file_23.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa)