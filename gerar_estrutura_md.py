from pathlib import Path

pasta = Path(__file__).resolve().parent
arquivo = pasta / "01_estrutura.md"

conteudo = """# Estrutura do Banco de Dados — Schulz

## Identificação
- Unidade curricular: Projeto Aplicado I.
- Atividade: Entrega 02 — Modelagem de Banco de Dados.
- Integrantes: Victor Gabriel Jaeger, Vinicius de Assis Mendes e Vinícius Itamar de Souza.
- Professores: Hugo Menezes Barra e Rodrigo Losina.

## Objetivo
Organizar os cadastros de técnicos, equipamentos e medições em um banco SQLite.
Essa organização busca reduzir a repetição de informações presentes nas planilhas.
O banco também permite relacionar cada medição ao equipamento e ao técnico responsável.

## Tabela tecnico
Armazena o nome, a matrícula, o e-mail e o setor do técnico.
O campo id_tecnico identifica cada cadastro e é gerado automaticamente.
A matrícula é obrigatória e não pode ser repetida.
Um técnico pode estar relacionado a várias medições.

## Tabela equipamento
Armazena o código de identificação, o nome, o fabricante e o modelo do equipamento.
O campo id_equipamento identifica cada equipamento e é gerado automaticamente.
O campo codigo_tag é obrigatório e não pode ser repetido.
Um equipamento pode estar relacionado a várias medições.

## Tabela medicao
Armazena o parâmetro medido, o valor nominal, as tolerâncias e o valor obtido.
Também registra o resultado e a data da medição.
O campo id_medicao identifica cada registro e é gerado automaticamente.
Cada medição deve estar vinculada a um equipamento e a um técnico cadastrados.
O resultado aceita somente APROVADO ou REPROVADO.
O banco valida essas opções, mas não calcula automaticamente o resultado.
Quando a data é omitida, o SQLite registra a data e a hora atuais em UTC.

## Relacionamentos
A tabela medicao utiliza id_tecnico para identificar o responsável pela medição.
Ela também utiliza id_equipamento para identificar o equipamento medido.
Esses campos são chaves estrangeiras e apontam para os respectivos cadastros.
A exclusão de um técnico ou equipamento com medições vinculadas é bloqueada.

## Controle de duplicidade
A matrícula única impede dois técnicos cadastrados com a mesma matrícula.
O código único impede dois equipamentos cadastrados com o mesmo codigo_tag.
Os cadastros são reutilizados nas medições por meio de seus identificadores.
Isso evita repetir todos os dados do técnico e do equipamento a cada medição.
O identificador da medição é único, mas não impede repetir seu conteúdo.
O controle de reimportação de uma mesma medição deverá ser definido na aplicação.

## Limites desta etapa
O modelo possui três tabelas e vinte campos.
Esta entrega cria a estrutura do banco, sem inserir dados das planilhas.
A importação, a higienização e o cálculo dos resultados ainda não estão implementados.
A geração de certificados também será tratada em uma etapa posterior.
"""

arquivo.write_text(conteudo, encoding="utf-8")

print(f"Arquivo gerado com sucesso: {arquivo.name}")
