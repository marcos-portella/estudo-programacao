## Dia 37: Variáveis de Ambiente e Envio de E-mail

### Prefácio:

No dia 37, abordamos duas práticas fundamentais para o desenvolvimento de aplicações seguras e dinâmicas em Python: a utilização de **variáveis de ambiente** para gerenciar dados sensíveis, como senhas e chaves de API, e o processo de **envio de e-mails** de forma programática, utilizando os módulos ``smtplib`` e ``email``. Exploramos como combinar essas duas habilidades para criar sistemas de notificação robustos, mantendo as credenciais fora do código-fonte.

### Variáveis de Ambiente: Segurança e Boas Práticas

Variáveis de ambiente são uma forma segura de armazenar informações de configuração que não devem ser versionadas, como chaves de acesso e senhas. O módulo ``os`` do Python permite acessar essas variáveis no sistema operacional, enquanto a biblioteca ``python-dotenv`` simplifica a leitura de um arquivo .env localmente.

- A utilização de arquivos ``.env`` garante que dados sensíveis não sejam expostos publicamente ao serem enviados para um repositório, como o GitHub.

- O acesso aos valores é feito de maneira simples e padronizada.

````
# Exemplo 1: Usando os.getenv para acessar variáveis de ambiente
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do arquivo .env

bd_password = os.getenv('BD_PASSWORD')
print(bd_password)
````

### Enviando E-mails com Python

O envio de e-mails com Python é realizado principalmente através do módulo ``smtplib``, que lida com o protocolo SMTP (Simple Mail Transfer Protocol), e do módulo ``email``, que ajuda a formatar as mensagens corretamente. A combinação de ambos permite enviar e-mails de texto simples ou com formatação mais complexa, como HTML.

- **SMTP**: O ``smtplib`` é responsável por estabelecer a conexão com um servidor de e-mail (como o Gmail) e enviar a mensagem.

- **MIMEMultipart**: A classe ``MIMEMultipart`` permite criar e-mails com múltiplas partes (como texto e HTML), enquanto a ``MIMEText`` define o conteúdo e o tipo de cada parte.

````
# Exemplo 2: Estrutura básica para enviar um e-mail com HTML
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from string import Template

load_dotenv()

remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente
subject = 'Este é o assunto do e-mail'

# Conteúdo HTML do e-mail
html_content = """
    Olá ${nome},
    <br />
    Estou testando
    <span style="color: red; font-weight: bold;">este e-mail</span>
    em HTML.
    <br />
    <br />

    <em>
      Atenciosamente,
      <br />
      Luiz Otávio.
    </em>
"""
html_template = Template(html_content)
email_body = html_template.substitute(nome='Helena')

# Criação do objeto MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = subject

# Adiciona o corpo do e-mail em HTML
mime_multipart.attach(MIMEText(email_body, 'html', 'utf-8'))
````

### Templating para E-mails HTML

Para criar e-mails dinâmicos, com variáveis que mudam de acordo com o usuário, o ``string.Template`` é uma ferramenta excelente. Ele permite definir um esqueleto em HTML ou texto e, em seguida, preencher os espaços reservados (``${nome}``) com dados específicos. Isso facilita a manutenção e a reutilização do código do e-mail.

````
Olá ${nome},
<br />
Estou testando
<span style="color: red; font-weight: bold;">este e-mail</span>
em HTML.
<br />
<br />

<em>
  Atenciosamente,
  <br />
  Luiz Otávio.
</em>
````

### Observações Finais:

O uso de variáveis de ambiente e o envio de e-mails são habilidades essenciais na automação e no desenvolvimento web. A combinação do ``os.getenv`` com o ``python-dotenv`` garante que as credenciais fiquem separadas do código, elevando o nível de segurança da aplicação. Por sua vez, o uso de ``smtplib`` e ``email.mime`` em conjunto com templates de string permite criar mensagens de e-mail complexas e personalizadas de forma programática, que podem ser usadas para notificações de sistema, marketing ou redefinição de senhas, tornando o fluxo de trabalho mais eficiente e seguro.