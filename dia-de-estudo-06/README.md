## Dia 6

### Prefácio:

Hoje introduzimos as estruturas condicionais (if, elif, else), que são a espinha dorsal da tomada de decisões em programação, permitindo que nosso código execute diferentes ações com base em diferentes condições. Além disso, solidificamos a compreensão sobre como os blocos de código são definidos e a importância da indentação em Python.

### Estruturas Condicionais: ``if``, ``elif``, ``else``:
As estruturas condicionais permitem que o programa execute um bloco de código apenas se uma determinada condição for verdadeira.

- **``if`` (se)**: Inicia uma estrutura condicional. O bloco de código sob o ``if`` será executado se a condição for avaliada como ``True``.

- **``elif`` (senão se)**: Usado para testar condições adicionais se a condição do ``if`` (e quaisquer ``elif``s anteriores) for False. Podem existir múltiplos elifs.

- **``else`` (senão)**: Opcional, mas muito útil. O bloco de código sob o ``else`` será executado se todas as condições anteriores (``if`` e ``elif``s) forem avaliadas como ``False``.

````
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema.')
elif entrada == 'sair':
    print('Você saiu do sistema.')
else:
    print('Opção inválida. Você não digitou "entrar" nem "sair".')

print('Este texto sempre será executado, pois está fora dos blocos condicionais.')
````

#### O Fluxo da Execução:

Python avalia as condições sequencialmente:

1. Verifica a condição do ``if``. Se ``True``, executa o bloco ``if`` e *pula* o restante da estrutura (``elif`` e ``else``).

2. Se a condição do ``if`` for ``False``, passa para o primeiro ``elif``. Se ``True``, executa o bloco ``elif`` e *pula* o restante.

3. Este processo continua para cada ``elif``.

4. Se todas as condições (``if`` e ``elif``s) forem ``False``, e um ``else`` existir, o bloco ``else`` será executado.

### Blocos de Código e Indentação:

Em Python, a estrutura dos blocos de código (conjuntos de instruções que pertencem a uma mesma estrutura, como ``if``, ``elif``, ``else``, funções, loops, etc.) é definida pela **indentação**.

- **Indentar**: Significa adicionar espaços (geralmente 4 espaços) no início de uma linha de código.

- **Regra Fundamental**: Todas as linhas dentro de um mesmo bloco devem ter o mesmo nível de indentação. Se a indentação for inconsistente, Python gerará um erro (``IndentationError``).

- A falta de indentação ou indentação incorreta impede que o código seja interpretado corretamente.

````
condicao = True

if condicao:  # Dois pontos indicam o início de um bloco
    print('Esta linha está indentada e faz parte do bloco "if".')
    print('Esta também.')
else:
    print('Esta linha está indentada e faz parte do bloco "else".')

print('Esta linha não está indentada e está fora de qualquer bloco condicional.') #
````

No exemplo acima, as linhas dentro dos ``if`` e ``else`` são indentadas, enquanto as linhas fora deles não são, indicando que serão executadas independentemente das condições.

### Observações Finais:

Dominar as estruturas if, elif e else é crucial para criar programas que reagem a diferentes entradas e cenários. A compreensão da indentação como definidora de blocos de código é uma particularidade de Python que, embora possa parecer estranha no início para quem vem de outras linguagens, torna o código mais legível e padronizado. Com isso, nossos programas ganham a capacidade de tomar decisões, abrindo caminho para lógicas muito mais complexas e úteis.