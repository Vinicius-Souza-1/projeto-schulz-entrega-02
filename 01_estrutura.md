# Organização dos dados do projeto Schulz

## Objetivo
O banco de dados será utilizado para organizar os dados das medições dos equipamentos.
A proposta é facilitar as consultas e reduzir a repetição de cadastros.
O modelo terá três tabelas: responsaveis, equipamentos e medicoes.

## Técnico e solicitante: tabela responsaveis
Esta tabela guardará os dados de quem realiza ou solicita a medição.
Cada responsável terá um identificador, um código e um nome.
O cadastro indicará se o responsável é uma pessoa ou um setor.
O técnico será uma pessoa responsável pela realização da medição.
O solicitante poderá ser uma pessoa ou um setor que pediu o serviço.
Uma pessoa poderá atuar como técnico e solicitante sem precisar de dois cadastros.
A função de cada responsável será indicada no registro da medição.

## Equipamento: tabela equipamentos
Esta tabela guardará os dados do equipamento que será calibrado.
Cada equipamento terá um identificador e um código único.
Também poderão ser registrados descrição, fabricante, modelo e número de série.
O mesmo equipamento poderá estar relacionado a várias medições.
Seus dados serão cadastrados uma vez e utilizados nas próximas medições.

## Medição: tabela medicoes
Esta tabela guardará cada leitura realizada durante a calibração.
Cada registro será ligado a um equipamento, a um técnico e a um solicitante.
Serão registrados o parâmetro, a unidade, o valor nominal e as tolerâncias.
Também serão armazenados o valor obtido, a data e o status da medição.
O código da calibração permitirá agrupar as leituras do mesmo atendimento.
O número da sequência distinguirá as leituras repetidas de uma característica.
Duas leituras com valores iguais poderão ser mantidas quando forem repetições válidas.
O arquivo de origem e a localização do dado ajudarão na conferência das informações.

## Relacionamentos e prevenção de duplicidades
A chave primária será o identificador único de cada registro.
As chaves estrangeiras ligarão a medição aos cadastros de equipamento e responsáveis.
Um equipamento poderá ter várias medições, mas cada medição terá apenas um equipamento.
Um responsável poderá participar de várias medições como técnico ou solicitante.
Os códigos únicos ajudarão a evitar cadastros repetidos de equipamentos e responsáveis.
A combinação de equipamento, calibração, característica e sequência evitará leituras duplicadas.

## Limite desta proposta
O modelo foi organizado em três tabelas para atender à atividade.
Alguns dados da calibração serão repetidos nas linhas de medição.
O programa deverá verificar se esses dados permanecem iguais dentro da mesma calibração.
Em uma ampliação futura, a calibração poderá ter uma tabela própria.