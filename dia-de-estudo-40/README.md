## Dia 40

### Prefácio:

Hoje mergulhamos nos conceitos fundamentais da estrutura de documentos HTML, focando em como organizar o conteúdo e como atribuir identificadores e classificações para estilização. Exploramos a hierarquia dos títulos com as tags ``<h1>`` a ``<h6>`` e a importância dos atributos globais ``id`` e ``class`` para a manipulação e estilização de elementos.

### Hierarquia de Títulos (Headings):
Os títulos são essenciais para estruturar e organizar o conteúdo de uma página. As tags de cabeçalho, que vão de ``<h1>`` a ``<h6>``, representam os seis níveis de títulos ou seções de um documento. O ``<h1>`` é o mais importante e deve ser usado para o título principal da página, enquanto os demais (``<h2>`` a ``<h6>``) são usados para subtítulos, seguindo uma hierarquia decrescente de importância.

````
<h1>Meu título</h1>
<p>Lorem ipsum dolor sit amet consectetur...</p>
<h2>Meu título</h2>
<h3>Meu título</h3>
<h4>Meu título</h4>
<h5>Meu título</h5>
<h6>Meu título</h6>
````

### Atributos Globais: ``id`` e ``class``:

Os atributos ``id`` e ``class`` são usados para identificar e agrupar elementos HTML, respectivamente. Eles são cruciais para aplicar estilos (com CSS) e comportamentos (com JavaScript) a elementos específicos ou a conjuntos de elementos.

- **``id``**: Deve ser único em toda a página. Ele é usado para identificar um único elemento de forma exclusiva. Por exemplo, ``#cabecalho-dois`` seleciona o elemento com este id.

- **``class``**: Pode ser usado em vários elementos. É ideal para aplicar o mesmo estilo a múltiplos elementos. Por exemplo, a classe ``fundo-vermelho`` pode ser aplicada a mais de um elemento para dar um fundo vermelho a todos eles.

Veja como eles são usados para estilizar elementos:

````
<style>
    h1 {
        background: brown;
    }
    #cabecalho-dois {
        background: purple;
    }
    .fundo-vermelho {
        background: red;
    }
    .bold {
        background: yellow;
    }
</style>
````

No código HTML, os atributos são aplicados da seguinte forma:

````
<h1 id="cabecalho-um" class="fundo-vermelho borda-esquerda">Vai vir aqui</h1>
<h1 id="cabecalho-dois" class="fundo-vermelho">Vai vir aqui</h1>
<p>
    Um texto <b class="bold">qualquer</b>
</p>
````

### Observações Finais:

A correta utilização de cabeçalhos garante uma estrutura semântica clara para a página, o que é fundamental para a acessibilidade e para o SEO. Já os atributos ``id`` e ``class`` permitem uma estilização modular e reutilizável com CSS. A principal diferença entre eles é a exclusividade do ``id``, enquanto a ``class`` é flexível e pode ser aplicada a vários elementos, o que é fundamental para a criação de estilos eficientes.