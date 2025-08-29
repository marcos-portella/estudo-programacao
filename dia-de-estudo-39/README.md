## Dia 39: Introdução ao HTML

### Prefácio:

No dia 39, fizemos uma imersão na linguagem de marcação **HTML (HyperText Markup Language)**, a espinha dorsal de qualquer página da web. Através da análise de arquivos HTML simples, entendemos como essa linguagem é usada para estruturar o conteúdo de um site, organizando elementos como títulos, parágrafos e textos. Exploramos a sintaxe básica de tags e atributos, que definem a aparência e o comportamento dos elementos.

### Estrutura Básica de um Documento HTML:

Todo documento HTML bem-formado segue uma estrutura fundamental, que delimita as seções da página. A declaração ``<!DOCTYPE html>`` define a versão do HTML. A tag ``<html>`` é o elemento raiz, que engloba todo o conteúdo da página, e a tag ``<body>`` contém tudo o que é visível para o usuário, como textos, imagens e links.

````
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Meu HTML</title>
</head>
<body>
    </body>
</html>
````

### Tags da Seção ``<head>``:
A seção ``<head>`` é um contêiner para metadados, ou seja, dados sobre o documento HTML que não são exibidos na página. O elemento ``<title>`` define o título da página que aparece na aba do navegador, enquanto a tag ``<meta>`` fornece metadados cruciais, como o conjunto de caracteres (``charset="UTF-8"``) para garantir a correta exibição de caracteres especiais.

````
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu HTML</title>
</head>
````

### Tags de Conteúdo e Formatação:

As tags dentro do ``<body>`` são usadas para estruturar e formatar o conteúdo que o usuário visualiza. O elemento ``<h1>`` define um título de primeiro nível, enquanto ``<p>`` é usado para parágrafos. A tag ``<span>`` é um contêiner genérico em linha, usado para aplicar estilos ou outras lógicas a uma pequena parte do texto. A tag ``<br>`` insere uma quebra de linha, separando o conteúdo verticalmente.

````
<h1>Meu HTML</h1>
<p>Lorem ipsum dolor sit amet consectetur, adipisicing 
    elit. Accusamus, veritatis amet impedit numquam molestias, 
    alias perferendis esse incidunt aut vero nisi optio dolore
     sit voluptas eum dicta adipisci inventore saepe.
</p>

<span>Luiz Otávio</span><br>
<span>Luiz Otávio</span><br>
<span>Luiz Otávio</span><br>
````

### Atributos em Elementos HTML:

Atributos fornecem informações adicionais sobre as tags HTML, como ``lang`` para definir o idioma do documento ou ``charset`` para a codificação de caracteres. Eles são declarados no formato ``nome="valor"`` dentro da tag de abertura. Embora existam tags e atributos padrão, o HTML é flexível o suficiente para processar tags personalizadas com atributos, como o exemplo abaixo.

````
<escreve atributo="valor1 valor2">
    <algumoutratag atributo="valor1 valor2">
        <naotenhocorpo atributo="valor1 valor2">
    </algumoutratag>
</escreve>`
````

### Observações Finais:

O HTML, com sua sintaxe baseada em tags e atributos, é a fundação de toda a construção web. Ele nos permite criar uma estrutura hierárquica e semântica para o conteúdo, que é então renderizada pelo navegador. A compreensão da estrutura básica, como as seções ``head`` e ``body``, e o uso adequado de tags e atributos é o primeiro e mais importante passo para construir qualquer tipo de página ou aplicação web.