## Dia 45: Tabelas em HTML

### Prefácio:

No Dia 45, exploramos um dos elementos mais poderosos e essenciais do HTML: as **tabelas**. Dominamos a estrutura semântica para exibir dados tabulares de forma acessível e organizada. O foco foi entender as tags de cabeçalho, corpo e rodapé, e como usar atributos especiais para mesclar células, garantindo que o conteúdo seja robusto e responsivo.

### Estrutura Semântica da Tabela:

A tabela HTML é definida pela tag ``<table>`` e é crucial para organizar dados. Para uma estrutura semântica correta, a tabela é dividida em três partes principais:

- **Cabeçalho (``<thead>``)**: Contém os títulos das colunas (``<th>``).

- **Corpo (``<tbody>``)**: Contém os dados da tabela (``<td>``).

- **Rodapé (``<tfoot>``)**: Contém dados de resumo, como totais.

Além disso, a tag ``<caption>`` é usada para fornecer uma descrição ou título para a tabela, o que é importante para acessibilidade.

````
<div class="responsive-table">
    <table>
        <caption>Uma descrição para a tabela</caption>
        <thead>
            <tr>
                <th>Título 1</th>
                <th>Título 2</th>
                <th>Título 3</th>
            </tr>
        </thead>
        <tbody>
            </tbody>
        <tfoot>
            </tfoot>
    </table>
</div>
````
### Unindo Células com ``colspan`` e ``rowspan``:

Para criar tabelas mais complexas, os atributos ``colspan`` e ``rowspan`` são utilizados dentro das tags ``<td>`` (dados) ou ``<th>`` (cabeçalho) para fazer com que uma única célula ocupe o espaço de múltiplas colunas ou linhas, respectivamente.

- ``colspan``: Define quantas colunas uma célula deve abranger.

- ``rowspan``: Define quantas linhas uma célula deve abranger.

````
<tbody>
    <tr>
        <td colspan="2">Ocupando dois espaços</td>
        <td>Corpo 2</td>
    </tr>
    <tr>
        <td colspan="3">Ocupando três espaços</td>
    </tr>
    <tr>
        <td colspan="2" rowspan="2">Corpo 1 (2 colunas, 2 linhas)</td>
        <td>Corpo 3</td>
    </tr>
    <tr>
        <td>Corpo 3</td>
    </tr>
</tbody>
````
### Rodapé da Tabela (``<tfoot>``):

O rodapé da tabela (``<tfoot>``) é usado para exibir resumos de dados, como o total de valores apresentados nas colunas. Ele utiliza as mesmas tags de linha (``<tr>``) e célula (``<td>``) do corpo, mas possui uma semântica diferente e é frequentemente estilizado de forma distinta. No exemplo, ele também utiliza ``colspan`` e ``rowspan`` para mesclar células e alinhar o total.

````
<tfoot>
    <tr>
        <td colspan="2" rowspan="2"></td>
        <td>TOTAL:</td>
    </tr>
    <tr>
        <td>R$555</td>
    </tr>
</tfoot>
````

### Estilização e Responsividade:

Para garantir a usabilidade e visualização em diferentes dispositivos, a tabela precisa de estilos CSS. No CSS, o ``border-collapse: collapse;`` é comumente usado para garantir que as bordas das células sejam únicas e não duplas. Além disso, a estratégia de envolver a tabela em uma ``<div>`` com a classe ``responsive-table`` e as propriedades ``overflow: auto;`` assegura que em telas pequenas o usuário possa rolar a tabela lateralmente, evitando quebras de layout.

````
/* Exemplo 4: CSS para responsividade e estilo */
table {
    border-collapse: collapse; /* Bordas unidas */
    width: 800px;
}

table td, table th {
    border: 1px solid #ccc;
    padding: 5px;
    text-align: left;
}

.responsive-table {
    max-width: 100%;
    overflow: auto; /* Permite rolagem lateral em telas pequenas */
}
````

### Observações Finais:

A correta utilização das tags semânticas (``<thead>``, ``<tbody>``, ``<tfoot>``) é o alicerce para construir tabelas acessíveis e fáceis de manter. O domínio dos atributos ``colspan`` e ``rowspan`` permite flexibilidade na exibição de dados. Por fim, a implementação da classe ``responsive-table`` no CSS é uma prática moderna crucial para garantir que a tabela seja totalmente funcional e adaptável, independentemente do tamanho da tela do usuário.