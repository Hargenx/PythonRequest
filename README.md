# Estudo de Uso do módulo Requests para Requisições de uma API

Este repositório contém exemplos de código Python para exemplificar o uso de diferentes métodos para realizar requisições a uma API pública (https://httpbin.org). O código foi desenvolvido com propósitos educativos e de estudo para demonstrar como fazer requisições HTTP utilizando o Python.

## Inspirado por

Este projeto foi inspirado no vídeo "Requests vs Httpx vs Aiohttp | Which One to Pick?" do canal ArjanCodes no YouTube. Você pode assistir ao vídeo [aqui](https://www.youtube.com/watch?v=OPyoXx0yA0I).

## Funcionalidades

### Usando `requests`

O código incluído neste repositório realiza diferentes tipos de requisições HTTP (GET, POST, PUT, DELETE) utilizando o módulo `requests` do Python para interagir com a API pública do httpbin.org. Cada tipo de requisição é demonstrado em funções separadas, proporcionando um exemplo claro de como utilizar diferentes métodos HTTP.

### Usando `urllib`

Também há um exemplo alternativo utilizando a biblioteca interna do Python, `urllib`, para realizar as mesmas requisições HTTP à API do httpbin.org. O código demonstra como utilizar esta biblioteca para efetuar chamadas HTTP.

### Usando `asyncio` e `aiohttp`

Além disso, há um exemplo avançado utilizando `asyncio` e `aiohttp` para realizar requisições de forma assíncrona. Este método permite fazer várias requisições simultaneamente, potencialmente aumentando a eficiência, especialmente ao lidar com múltiplas chamadas de rede.

## Pré-requisitos

- Python 3.x instalado
- Biblioteca `requests` e `aiohttp` instaladas.
- Ambiente Python para execução dos exemplos.

Isso executará o script Python correspondente, realizando as requisições à API e exibindo os resultados no terminal.

## Contribuições

Contribuições são bem-vindas! Se você identificar melhorias possíveis ou tiver sugestões para tornar o código mais eficiente, legível ou pythonico, sinta-se à vontade para abrir uma issue ou criar um pull request.

## Notas adicionais

Estes códigos foram desenvolvidos com o objetivo de serem educativos e não para uso em produção. Certifique-se de estar em conformidade com os termos de serviço da API ao utilizá-la para fins comerciais ou de produção.