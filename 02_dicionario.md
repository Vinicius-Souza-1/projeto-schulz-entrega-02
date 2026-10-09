# Dicionário de dados do sistema

Este documento descreve os campos propostos para o banco de dados do projeto Schulz.
Os tipos utilizados serão Texto (TEXT), Inteiro (INTEGER) e Real (REAL).
No SQLite, as datas deste projeto serão armazenadas como texto.
Os campos foram definidos a partir do levantamento de requisitos e da organização proposta para os dados.
O arquivo main.py disponível realiza apenas um teste do ambiente e não extrai dados.
Por isso, a correspondência com campos extraídos por Python não foi verificada nesta etapa.

## Tabela responsaveis

Armazena as pessoas ou os setores envolvidos nas medições.

| Campo | Tipo | Descrição |
| --- | --- | --- |
| id_responsavel | Inteiro | Identificador único do responsável. Chave primária. |
| codigo | Texto | Código único utilizado para identificar a pessoa ou o setor. |
| nome | Texto | Nome da pessoa ou do setor. |
| tipo | Texto | Indica PESSOA ou SETOR. |
| ativo | Inteiro | Indica se o cadastro está ativo: 1 para sim e 0 para não. |

## Tabela equipamentos

Armazena os dados dos equipamentos que serão calibrados.

| Campo | Tipo | Descrição |
| --- | --- | --- |
| id_equipamento | Inteiro | Identificador único do equipamento. Chave primária. |
| codigo | Texto | Código único do equipamento. |
| descricao | Texto | Descrição que permite reconhecer o equipamento. |
| fabricante | Texto | Nome do fabricante. Pode ficar vazio quando não informado. |
| modelo | Texto | Modelo do equipamento. Pode ficar vazio quando não informado. |
| numero_serie | Texto | Número de série. Pode ficar vazio quando não informado. |
| ativo | Inteiro | Indica se o cadastro está ativo: 1 para sim e 0 para não. |

## Tabela medicoes

Armazena cada leitura e sua ligação com o equipamento e os responsáveis.

| Campo | Tipo | Descrição |
| --- | --- | --- |
| id_medicao | Inteiro | Identificador único da medição. Chave primária. |
| id_equipamento | Inteiro | Identificador do equipamento medido. Chave estrangeira. |
| id_tecnico | Inteiro | Identificador do responsável que realizou a medição. Chave estrangeira. |
| id_solicitante | Inteiro | Identificador do responsável que solicitou o serviço. Chave estrangeira. |
| codigo_calibracao | Texto | Código que agrupa as leituras de uma mesma calibração. |
| data_medicao | Texto | Data da medição no formato AAAA-MM-DD. |
| codigo_caracteristica | Texto | Código da característica avaliada no relatório de origem. |
| parametro | Texto | Nome do que foi medido, como diâmetro ou comprimento. |
| sequencia | Inteiro | Número da leitura de uma característica, começando em 1. |
| unidade | Texto | Unidade de medida, como mm. |
| valor_nominal | Real | Valor de referência da característica medida. |
| tolerancia_inferior | Real | Desvio inferior permitido em relação ao valor nominal. |
| tolerancia_superior | Real | Desvio superior permitido em relação ao valor nominal. |
| valor_obtido | Real | Resultado numérico da leitura realizada. |
| valor_original | Texto | Valor conforme registrado na origem, antes da conversão numérica. |
| status | Texto | Situação da medição: PENDENTE, CONFORME, NAO_CONFORME ou INDETERMINADO. |
| arquivo_origem | Texto | Nome do arquivo de onde a leitura foi retirada. |
| local_origem | Texto | Localização da leitura na origem, como aba e célula ou página e linha. |
| registrado_em | Texto | Data e hora em que o registro foi inserido no banco, em UTC. |
| observacao | Texto | Informação complementar. Pode ficar vazia quando não houver observações. |

## Regras de preenchimento

- As chaves primárias identificam cada registro sem repetição.
- As chaves estrangeiras devem apontar para cadastros existentes.
- O técnico deve estar cadastrado como PESSOA.
- Os códigos e os demais textos obrigatórios não podem ficar vazios.
- Os campos opcionais sem informação serão armazenados como NULL.
- NULL significa ausência de informação e não deve ser substituído por zero.
- Os valores numéricos devem ser convertidos antes da gravação no banco.
- As datas devem seguir o formato AAAA-MM-DD e representar datas válidas.
- Neste modelo, as tolerâncias representam desvios em relação ao valor nominal.
- A interpretação das tolerâncias deverá ser confirmada nos arquivos de origem.
- O status inicial será PENDENTE, até que o resultado seja avaliado.
- Leituras repetidas válidas serão diferenciadas pelo campo sequencia.
- A combinação de equipamento, calibração, característica e sequência não poderá se repetir.

## Validações que dependem do programa

O SQL verifica os campos obrigatórios, os códigos únicos e os relacionamentos.
O programa de cadastro ou importação deverá realizar as seguintes verificações:
- Confirmar que o responsável indicado como técnico é do tipo PESSOA.
- Validar se a data existe no calendário, pois o SQL verifica apenas seu formato.
- Converter campos opcionais sem informação para NULL.
- Padronizar os códigos antes da gravação, evitando diferenças de espaços e letras.
- Conferir se os dados gerais são consistentes nas leituras da mesma calibração.