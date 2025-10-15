## Dia 46: Separação de HTML e CSS

### Prefácio:

No Dia 46, abordamos uma prática fundamental no desenvolvimento web: a separação clara entre a **estrutura** (HTML) e a **apresentação** (CSS). Entendemos como vincular folhas de estilo externas a um documento HTML, promovendo um código mais limpo, organizado e fácil de manter. O foco principal foi o uso da tag ``<link>`` na seção ``<head>`` do HTML para fazer essa conexão.

### Vinculando CSS Externo:

A melhor prática para aplicar estilos em um documento HTML é utilizar folhas de estilo externas, ou seja, arquivos CSS separados. Isso é feito através da tag ``<link>`` na seção ``<head>`` do HTML.

Os atributos essenciais da tag ``<link>`` são:

- ``rel="stylesheet"``: Indica que o arquivo vinculado é uma folha de estilo.

- ``href``: Especifica o caminho para o arquivo CSS.

````
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="assets/css/styles.css">
    <link rel="stylesheet" href="assets/css/exemplo.css">
</head>
````

### Caminho dos Arquivos CSS:

Os arquivos CSS foram organizados em uma estrutura de diretórios seguindo a prática comum de separar os assets. O caminho (ou ``href``) que utilizamos na tag ``<link>`` reflete essa estrutura: ``assets/css/nomedoarquivo``.

- **Arquivo ``styles.css``**: O caminho para este arquivo é ``assets/css/styles.css``.

- **Arquivo ``exemplo.css``**: O caminho para este arquivo é ``assets/css/exemplo.css``.

Essa organização é fundamental para manter grandes projetos organizados.

### Conflitos de Estilos (Cascata):

É possível vincular múltiplas folhas de estilo ao mesmo documento. Quando diferentes arquivos CSS definem estilos para o mesmo elemento, o CSS segue regras de cascata e especificidade para determinar qual estilo será aplicado. Seletivamente, o último estilo definido para um seletor com a mesma especificidade (lido de cima para baixo) geralmente prevalece.

No exemplo, a classe ``.caixa`` é definida em dois arquivos:

- ``styles.css`` define o fundo como **vermelho**.

- ``exemplo.css`` define o fundo como **amarelo**.

Como ``exemplo.css`` é lido depois de ``styles.css`` no HTML, o estilo definido em ``exemplo.css`` (fundo amarelo) tem precedência, assumindo que a especificidade dos seletores seja a mesma.

````
/* Conteúdo do styles.css */
.caixa {
    background: red;
    height: 120px;
    width: 120px;
}
````

````
/* Conteúdo do exemplo.css */
.caixa {
    background: yellow; /* Este será aplicado */
    height: 120px;
    width: 120px;
}
````

### Observações Finais:

A separação de HTML e CSS é uma pedra angular do desenvolvimento web moderno. Ela não apenas simplifica a manutenção do código, permitindo que alterações de design sejam feitas sem tocar na estrutura, mas também melhora a performance ao permitir que o navegador armazene o arquivo CSS em cache. O entendimento da **cascata** é vital, pois é a regra que governa como o navegador decide qual estilo aplicar quando há conflito entre diferentes folhas de estilo ou regras.