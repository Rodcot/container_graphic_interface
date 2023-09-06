## Aplicativo de Rastreamento de Contêineres Docker
Este script cria uma aplicação web mínima usando Flask que lista todos os contêineres Docker em execução e permite parar um contêiner selecionado. Ele usa a biblioteca Docker SDK para Python para interagir com o Docker.

Para rodar o script também é necessário criar o arquivo HTML index.html no mesmo diretório em que o script Python está localizado. Este arquivo HTML exibe a lista de contêineres e fornecer um botão "Parar" para cada contêiner.