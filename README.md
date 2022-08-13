# MunicipiosParanaS3
Estudo rápido sobre pipeline de dados e AWS S3

Esse pipeline de dados faz o download do arquivo csv com o código do município, nome do município e sigla do Estado da Federação que está no site de dados abertos do governo federal.
Em seguida ele filtra todas as cidades do Paraná e então salva esses dados filtrados em um novo csv.
Por fim faz o upload do novo arquivo para um bucket S3 da AWS.

O código está bastante simples e pode ser melhorado, ampliado, automatizado, entre vários outros aprimoramentos.

Como esse é o meu primeiro código desse tipo (sozinho), feedbacks serão muito bem vindos!
