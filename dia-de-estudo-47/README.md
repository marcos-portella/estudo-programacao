## Dia 47: Seletores Básicos de CSS

### Prefácio:

No Dia 47, exploramos os alicerces do CSS: os **seletores**. Aprofundamos no conhecimento de como escolher e estilizar elementos HTML de maneira precisa e eficiente, utilizando uma vasta gama de seletores, desde os mais simples, como os seletores de tag e classe, até os mais complexos, como os seletores de parentesco e de atributos. Esta aula foi crucial para entender como aplicar estilos a elementos específicos em uma página web.

### Tipos de Seletores e Sintaxe:

Os seletores são a parte mais importante de uma regra CSS, pois eles "selecionam" o(s) elemento(s) HTML que você quer estilizar. A folha de estilo ``styles.css`` demonstra a aplicação de seletores para tags, classes e atributos. O arquivo CSS está vinculado ao HTML através da tag ``<link>`` com o caminho ``assets/css/styles.css``. O caminho completo, como solicitado, é ``dia-de-estudo-47/assets/css/styles.css``.

- **Seletor de Tipo**: Seleciona elementos pelo nome da tag, como ``h1`` ou ``p``.

- **Seletor de Classe**: Seleciona elementos com um atributo ``class`` específico, como ``.color-purple``. É a forma mais comum e recomendada de estilização.

- **Seletor Universal**: O asterisco (``*``) seleciona todos os elementos em uma página e é usado para aplicar estilos globais.

````
/* Exemplo 1: Seletores de Tipo e Universal */
* {
    margin: 0;
    padding: 0;
}

h1, p {
    color: yellow;
}
````

### Seletores de Relacionamento (Parentesco):

Esses seletores baseiam-se na relação entre os elementos no DOM (Document Object Model):

- **Seletor de Descendente (Espaço)**: Seleciona um elemento que é descendente de outro.

- **Seletor de Filho Direto (``>``)**: Seleciona apenas os filhos diretos de um elemento.

- **Seletores de Irmãos (``+`` e ``~``)**: O seletor de irmão adjacente (``+``) seleciona o elemento que vem imediatamente após outro, enquanto o seletor de irmão geral (``~``) seleciona todos os irmãos que o sucedem.

````
/* Exemplo 2: Seletores de Relacionamento */
body div section p,
body div section h1 {
    color: red;
}

.pai > .filha {
    color: cyan;
}

.pai2 h1+p {
    color: brown;
}

.pai2 h1~p {
    color: blueviolet;
}
````

### Seletores de Atributo:

Seletores de atributo permitem estilizar elementos com base na presença ou valor de seus atributos.

- **``[atributo]``**: Seleciona elementos que contêm o atributo.

- **``[atributo="valor"]``**: Seleciona elementos com um valor exato para o atributo.

- **``[atributo*="valor"]``**: Seleciona elementos que contêm um valor de string em qualquer lugar do atributo.

- **``[atributo^="valor"]``**: Seleciona elementos cujo valor do atributo começa com a string.

- **``[atributo$="valor"]``**: Seleciona elementos cujo valor do atributo termina com a string.

````
/* Exemplo 3: Seletores de Atributo */
[checked] {
    width: 50px;
    height: 50px;
}

[meu-atributo-2="valor"] {
    color: azure;
}

[meu-atributo-2*="uar"] {
    color: tan;
}
````

### Especificidade de Seletores:

A especificidade é a forma como o navegador decide qual regra CSS deve ser aplicada a um elemento, especialmente quando múltiplas regras podem se aplicar. Um seletor mais específico tem prioridade sobre um menos específico. Por exemplo, a regra ``body.error div.main-content h1.heading`` é mais específica e, portanto, prevalecerá sobre uma regra mais genérica como ``h1``, garantindo que o estilo desejado seja aplicado mesmo com outras regras presentes.

````
/* Exemplo 4: Seletor com alta especificidade */
body.error div.main-content h1.heading {
    font-style: italic;
}
````

### Observações Finais:

A compreensão de como diferentes seletores funcionam, bem como a sua especificidade, é essencial para evitar conflitos de estilo e para construir folhas de estilo modulares e fáceis de manter. A prática com seletores de relacionamento e de atributos abre um leque de possibilidades para estilizar elementos de forma granular, o que é um passo importante para se tornar proficiente em CSS.