import pprint

# Dados iniciais
produtos = [
    {'nome': 'Caneta Azul', 'preco': 2.5, 'categoria': 'Escritório', 'estoque': 100},
    {'nome': 'Caderno', 'preco': 15.0, 'categoria': 'Escritório', 'estoque': 50},
    {'nome': 'Lápis', 'preco': 1.2, 'categoria': 'Escritório', 'estoque': 200},
    {'nome': 'Mochila', 'preco': 120.0, 'categoria': 'Escritório', 'estoque': 10},
    {'nome': 'Borracha', 'preco': 0.8, 'categoria': 'Escritório', 'estoque': 0},
    {'nome': 'Livro de Python', 'preco': 100.0, 'categoria': 'Livros', 'estoque': 5},
]

def print_produtos(lista):
    pprint.pprint(lista, sort_dicts=False, width=60)

def ajustar_precos(produtos, regra_ajuste):
    return [
        {**produto, 'preco': regra_ajuste(produto['preco'])}
        for produto in produtos
    ]

def filtrar_produtos(produtos, filtros):
    resultado = produtos
    for f in filtros:
        resultado = [p for p in resultado if f(p)]
    return resultado

def ordenar_produtos(produtos, chave_ordem, reverse=False):
    return sorted(produtos, key=chave_ordem, reverse=reverse)

def aplicar_metodo(produtos, metodo_nome):
    for produto in produtos:
        if hasattr(produto['nome'], metodo_nome):
            metodo = getattr(produto['nome'], metodo_nome)
            produto['nome_maiusculo'] = metodo()
    return produtos

def input_float(prompt):
    while True:
        valor = input(prompt)
        try:
            return float(valor)
        except ValueError:
            print("Por favor, digite um número válido.")

def input_bool(prompt):
    while True:
        valor = input(prompt + " (s/n): ").lower()
        if valor in ('s', 'n'):
            return valor == 's'
        print("Digite 's' para sim ou 'n' para não.")

def gerenciador_interativo(produtos):
    print("=== Gerenciador de Produtos Interativo ===")

    # Pergunta para ajuste percentual
    aplicar_ajuste = input_bool("Quer aplicar ajuste de preço para produtos abaixo de um valor?")
    if aplicar_ajuste:
        limite = input_float("Digite o valor limite do preço para ajuste: ")
        percentual = input_float("Digite o percentual de ajuste (exemplo: 10 para 10%): ")

        regra_ajuste = lambda preco: round(preco * (1 + percentual / 100), 2) if preco < limite else preco
        produtos = ajustar_precos(produtos, regra_ajuste)
        print(f"Preços ajustados para produtos abaixo de {limite} com {percentual}% de aumento.")
    else:
        print("Nenhum ajuste de preço será aplicado.")

    # Filtros interativos
    filtros = []

    filtrar_estoque = input_bool("Filtrar produtos que estão em estoque?")
    if filtrar_estoque:
        filtros.append(lambda p: p['estoque'] > 0)

    filtrar_categoria = input_bool("Filtrar produtos por categoria?")
    if filtrar_categoria:
        categorias_disponiveis = list(set(p['categoria'] for p in produtos))
        print("Categorias disponíveis:", ", ".join(categorias_disponiveis))
        categoria = input("Digite a categoria desejada: ")
        filtros.append(lambda p: p['categoria'].lower() == categoria.lower())

    produtos = filtrar_produtos(produtos, filtros)

    # Ordenação
    print("Ordenar produtos por:")
    print("1 - Nome")
    print("2 - Preço")
    print("3 - Estoque")
    escolha_ordem = input("Escolha uma opção (1-3): ")

    if escolha_ordem == '1':
        produtos = ordenar_produtos(produtos, lambda p: p['nome'])
    elif escolha_ordem == '2':
        produtos = ordenar_produtos(produtos, lambda p: p['preco'])
    elif escolha_ordem == '3':
        produtos = ordenar_produtos(produtos, lambda p: p['estoque'], reverse=True)
    else:
        print("Opção inválida. Ordenando por nome.")
        produtos = ordenar_produtos(produtos, lambda p: p['nome'])

    # Aplica método upper no nome
    produtos = aplicar_metodo(produtos, 'upper')

    # Mostrar produtos finais
    print("\n=== Produtos disponíveis após filtros e ajustes ===")
    print_produtos(produtos)


# Executa a interface interativa
if __name__ == "__main__":
    gerenciador_interativo(produtos)