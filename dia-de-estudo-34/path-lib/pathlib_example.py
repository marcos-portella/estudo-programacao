from pathlib import Path
from shutil import rmtree

caminho_projeto = Path()
print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
print(caminho_arquivo)

print(caminho_arquivo.parent.parent)

ideias = caminho_arquivo.parent / 'ideias'
print(ideias / 'arquivo.txt')

arquivo = Path.home() / 'Desktop' / 'arquivo.txt'

# Geralmente usado para coisas rápidas assim:
arquivo.touch()
print(arquivo)
arquivo.write_text('Olá mundo')
print(arquivo.read_text())
arquivo.unlink()

# Para trabalhar com arquivos:
caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'

with caminho_arquivo.open('a+') as file:
    file.write('Uma linha\n')
    file.write('outra linha\n')

print(caminho_arquivo.read_text())
arquivo.unlink()

# trabalhndo pastas:
caminho_pasta = Path.home() / 'Desktop' / 'Python'
caminho_pasta.mkdir(exist_ok=True)

subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')

# Caminho_pasta.rmdir() # Não vai funcionar


# Apagando arquivos:

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'

    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Olá mundo\n')
        text_file.write(f'file_{i}.txt')

# rmtree(caminho_pasta)  # jeito mais simples para apagar um arquivo

# Jeito mais difícil para aprendisado:


def rmtree_example(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE: ', file)
            file.unlink

    if remove_root:
        root.rmdir()
