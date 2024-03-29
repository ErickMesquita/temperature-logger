# Temperature Logger

| :placard: Vitrine.Dev |     |
| -------------  | --- |
| :sparkles: Nome        | Temperature Logger
| :label: Tecnologias | Python, PostgreSQL, Docker
| :rocket: URL         | https://github.com/ErickMesquita/temperature-logger
| :fire: Desafio     | 

O objetivo desta aplicação é exercitar os conteúdos aprendidos sobre Docker, Python e Git. Trata-se de uma aplicação para registrar a temperatura e umidade do meu quarto ao longo do tempo. Os dados são obtidos de uma API e armazenados num banco de dados.

*Read this in other languages: [English](README.en-US.md)*

## Frequência de Coleta

1 medição a cada 90 segundos.

## Fonte dos Dados

Há um sensor de temperatura e umidade conectado a um NodeMCU. O NodeMCU hospeda uma página web e uma API com IP fixo.

## Banco de Dados

Será usado o banco de dados SQL com uma tabela de 3 colunas:
 - Datetime
 - Temperatura
 - Umidade
