from pathlib import Path

caminho_projeto = Path()
print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
print(caminho_arquivo)

print(caminho_arquivo.parent.parent)

ideias = caminho_arquivo.parent / 'ideias'
print(ideias / 'arquivo.txt')

arquivo = Path.home() / 'Desktop' / 'arquivo.txt'

# Geralmente usado para coisas rápidasa assim:
arquivo.touch()
print(arquivo)
arquivo.write_text('Olá mundo')
arquivo.write_text('Olá de novo')
print(arquivo.read_text())
arquivo.unlink()