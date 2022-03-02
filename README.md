# Temperature Logger

O objetivo desta aplicação é exercitar os conteúdos aprendidos sobre Docker, Python e Git. Trata-se de uma aplicação para registrar a temperatura e umidade do meu quarto ao longo do tempo.

## Frequência de Coleta

1 medida a cada 2 minutos.

## Fonte dos Dados

Há um sensor de temperatura e umidade no meu quarto conectado a um NodeMCU. O NodeMCU hospeda uma página e uma API com IP fixo.

## Banco de Dados

Será usado o banco de dados MySQL com uma tabela de 3 colunas:
 - Datetime
 - Temperatura
 - Umidade