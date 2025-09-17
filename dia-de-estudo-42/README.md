## Dia 42: Estrutura e Semântica do HTML

### Prefácio:

No dia 42, exploramos a importância da **semântica no HTML** para construir páginas da web organizadas e acessíveis. Analisamos um arquivo de exemplo (``semantica_estrutura.html``) que demonstra como utilizar tags como ``<header>``, ``<section>``, ``<article>``, ``<footer>`` e ``<aside>`` para dar significado à estrutura do conteúdo, em vez de depender apenas de tags genéricas como ``<div>``.

A adoção de uma estrutura semântica não apenas melhora a organização do código, mas também otimiza a experiência para leitores de tela e motores de busca, tornando o conteúdo mais fácil de ser interpretado.

### A Estrutura Semântica no HTML:
O HTML5 introduziu várias tags semânticas que ajudam a definir claramente a função de cada parte de uma página. No arquivo de exemplo, podemos ver o uso de algumas das mais importantes:

- **``<header>``**: Representa a parte introdutória de um documento ou seção. No arquivo, é usado para o cabeçalho principal da página com o título ``<h1>`` e um parágrafo.

- **``<section>``**: Agrupa conteúdos tematicamente relacionados. No exemplo, é utilizada para agrupar as "Roupas femininas" e "Roupas masculinas", com cada uma tendo seu próprio cabeçalho.

- **``<article>``**: Usado para conteúdo independente e auto-contido, como uma postagem de blog, um item de notícia ou, neste caso, produtos individuais dentro de uma seção.

- **``<aside>``**: Representa conteúdo que é relacionado ao conteúdo principal, mas separado dele. Geralmente é exibido em uma barra lateral, como a navegação do exemplo.

- **``<footer>``**: Contém informações de rodapé para a seção ou documento ao qual pertence. Pode incluir informações de contato, direitos autorais e links de navegação.

````
<header>
    <h1>
        <a href="#">Home</a>
    </h1>
    <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Iste est unde pariatur quod. At ullam dolor nobis labore, nostrum quis iste blanditiis temporibus perferendis fugit, perspiciatis quas sequi qui cum.</p>
</header>
````

### Organizando Conteúdo com Títulos e Artigos:

A hierarquia de títulos, de ``<h1>`` a ``<h6>``, é essencial para a estrutura. No arquivo, vemos como os títulos são usados dentro das tags semânticas para organizar o conteúdo:

- O ``<h1>`` é usado para o título principal da página.

- Os ``<h2>`` são usados para os títulos das seções.

- Os ``<h3>`` são usados para os títulos dos artigos dentro de cada seção.

````
<section>
    <header>
        <h2>
            Roupas femininas
        </h2>
    </header>

    <article>
        <h3>heading necessário no article</h3>
        <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Explicabo provident exercitationem necessitatibus accusantium beatae facere corrupti libero, molestias maxime impedit quas, esse temporibus odio quisquam quam iure expedita commodi excepturi?</p>
    </article>
</section>
````

### A Diferença entre ``<div>`` e Tags Semânticas:

A tag ``<div>`` é um elemento genérico de nível de bloco sem qualquer significado semântico, enquanto tags como ``<section>`` e ``<article>`` dão significado ao conteúdo. Embora o ``<div>`` ainda seja útil para agrupar elementos para fins de estilização, o uso de tags semânticas é preferível sempre que possível.

````
<div>
    <article>
        <header>
            <h3>heading</h3>
        </header>
        <div>Oi</div>
        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Veniam unde voluptate aspernatur suscipit in praesentium asperiores cumque quibusdam ullam maiores quisquam numquam temporibus laboriosam et quam, sequi nam tempore quaerat.</p>
        <footer>
            Rodapé
        </footer>
    </article>
</div>
````

### Navegação e Rodapé:

As tags ``<aside>`` e ``<footer>`` são cruciais para a usabilidade e navegação. O ``<aside>`` geralmente contém uma barra lateral com links de navegação (``<nav>``), enquanto o ``<footer>`` marca o fim de uma página ou seção.

````
<aside>
    <nav>
        <ul>
            <li><a href="#">texto 1</a></li>
            <li><a href="#">texto 2</a></li>
            <li><a href="#">texto 3</a></li>
            <li><a href="#">texto 4</a></li>
        </ul>
    </nav>
</aside>

<footer>
    Meu endereço, meu contato
</footer>
````

### Observações Finais:

Compreender e aplicar a **estrutura semântica do HTML** é um passo fundamental para o desenvolvimento web. A utilização correta de tags como ``<header>``, ``<section>``, ``<article>``, ``<aside``> e ``<footer>``, como visto no arquivo de exemplo, não só organiza visualmente a página, mas também oferece contexto para motores de busca e tecnologias assistivas. Ao combinar a estrutura semântica com uma hierarquia clara de títulos (``<h1>`` a ``<h6>``), criamos páginas mais robustas, acessíveis e fáceis de manter.