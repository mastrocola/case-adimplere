## Projeto
 - Case Adimplere (Teste Adimplere.pdf)


## Autor
 - Marcio Mastrocola Alcantara


## Considerações
 - Como não há acesso aos endpoints das API's, eu criei uma pasta de mocks com os arquivos de exemplo e faço a consulta através dela quando a variável ENVIRONMENT for diferente de 'production'
 - Como não foram informados endpoints específicos p/ a consulta de long_description, eu estou usando a mesma fonte de dados da consulta de short_description e aplicando o filtro pelo nome
 - No descritivo do teste não existia o campo 'nome' no retorno dos endpoints. Eu considerei a informação importante e a incluí nos objetos de saída
 - Com relação ao uuid dos retornos, eu estou apenas fazendo a geração randômica no retorno. Caso essa informação fosse utilizada como um ID fixo, precisaríamos persistir essas informações em banco de dados. Porém, para fins deste teste eu preferi fazer dessa forma para não sair do escopo do mesmo