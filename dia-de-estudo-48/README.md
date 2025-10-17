## Dia 48: Pseudo-Classes em CSS

### Prefácio:

No Dia 48, focamos no conceito poderoso das **Pseudo-Classes em CSS**. Elas permitem selecionar e estilizar elementos com base em um estado, relação ou condição específica que não pode ser alcançada com seletores de classe ou ID simples. Exploramos como estilizar links em diferentes estados, elementos de formulário em foco ou marcados, e como selecionar elementos com base em sua posição ou ausência de uma classe. O arquivo CSS que contém todos esses estilos está no caminho: ``dia-de-estudo-48/assets/css/styles.css``.

### Pseudo-Classes de Interação e Foco:

Essas pseudo-classes são essenciais para criar feedback visual ao usuário, indicando um estado interativo do elemento.

- **``:hover``**: Estiliza o elemento quando o ponteiro do mouse está sobre ele. É comummente usado com a propriedade transition para criar um efeito suave.

- **``:focus``**: Aplica estilos ao elemento que recebeu o foco, geralmente campos de formulário como <input>. É crucial para a acessibilidade.

- **``:active``**: Estiliza o elemento no momento em que ele está sendo ativado (clicado ou pressionado).

````
/* Exemplo 1: Estilos de Interação e Foco */
.heading {
    transition: all 200ms ease-in-out /* Transição suave */
}

.heading:hover {
    background: red; /* Estilo ao passar o mouse */
}

input:focus {
    box-shadow: 0 0 5px rgba (0, 0, 0, 0.5); /* Sombra ao focar */
    outline: none;
    border: 1px solid black
}
````

### Pseudo-Classes para Links:

Os links possuem uma sequência específica de pseudo-classes que definem seu estilo em diferentes estágios de navegação:

- **``:link``**: Estiliza links que ainda não foram visitados.

- **``:visited``**: Estiliza links que o usuário já visitou.

- **``:hover``**: Estiliza quando o mouse está sobre o link.

- **``:active``**: Estiliza o link no momento do clique.

````
/* Exemplo 2: Estados de Links */
a:link {
    color: aqua; /* Link não visitado */
}

a:visited {
    color: firebrick; /* Link visitado */
}

a:hover {
    background: darkslateblue;
    color: white;
    text-decoration: none;
}
````

### Pseudo-Classes de Estado de Formulário:

Estas pseudo-classes permitem estilizar inputs com base no seu estado de formulário:

- **``:checked``**: Seleciona elementos (como checkboxes ou radio buttons) que estão marcados.

- **``:not(:checked)``**: Seleciona elementos que não estão marcados.

- **``:required``**: Seleciona campos de formulário que possuem o atributo required.

- ``input:enabled`` (embora o código use ``input:enabled`` para definir um ``background-color: blue;`` e ``cursor: not-allowed;``, o estado ``enabled`` é o padrão para inputs não desabilitados).

````
/* Exemplo 3: Estilos para Elementos de Formulário */
input:checked {
    width: 50px;
    height: 50px;
}

input:checked + p {
    background: red; /* Estiliza o parágrafo irmão que segue o input marcado */
}

input:not(:checked) + p {
    background: yellow; /* Estiliza o parágrafo irmão que segue o input não marcado */
}

input:required {
    background: aquamarine; /* Estiliza inputs com atributo 'required' */
}
````

### Pseudo-Classes Estruturais e Negação:

As pseudo-classes estruturais selecionam elementos com base em sua posição dentro de seu grupo de irmãos, e o seletor ``:not()`` é usado para excluir elementos:

- **``:last-child``**: Seleciona o último elemento de uma lista de irmãos.

- **``:not(seletor)``**: Nega um seletor. No exemplo, ele seleciona todos os itens da lista que não possuem a classe ``.meio``.

````
/* Exemplo 4: Seleção Estrutural e Negação */
.pai .lista li:last-child {
    background: pink; /* Estiliza o último item da lista */
}

li:not(.meio) {
    color: brown; /* Estiliza todos os <li> que não têm a classe 'meio' */
}
````

### Observações Finais:
O uso de pseudo-classes eleva a qualidade do CSS, permitindo criar interfaces altamente interativas e acessíveis sem a necessidade de JavaScript para lidar com estados simples. A prática com ``:hover``, ``:focus`` e os seletores estruturais, como ``:last-child`` e o poderoso ``:not()``, fornece as ferramentas necessárias para estilizar a página de forma detalhada e responsiva ao comportamento do usuário.