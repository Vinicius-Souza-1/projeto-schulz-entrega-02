from pathlib import Path

pasta = Path(__file__).resolve().parent
arquivo = pasta / "02_dicionario.md"

conteudo = """# Dicionário de Dados — Schulz

Este documento descreve os vinte campos das três tabelas do banco.
Os nomes, tipos e restrições correspondem ao arquivo 03_banco.sql.

## Significado dos termos
- INTEGER: número inteiro.
- TEXT: texto.
- REAL: número com casas decimais.
- DATETIME: declaração utilizada para data e hora neste modelo.
- PRIMARY KEY: chave que identifica cada registro.
- AUTOINCREMENT: gera automaticamente o identificador.
- NOT NULL: impede valores nulos, mas não impede texto vazio.
- UNIQUE: impede a repetição do valor no campo.
- FOREIGN KEY: relaciona o registro a outra tabela.
- CHECK: verifica uma condição definida no banco.
- DEFAULT: fornece um valor quando o campo é omitido na inserção.

## Tabela tecnico — 5 campos

| Campo | Tipo declarado no SQLite | Restrições / Chaves | Descrição |
| --- | --- | --- | --- |
| id_tecnico | INTEGER | PRIMARY KEY AUTOINCREMENT | Identificador automático do técnico. |
| nome_tecnico | TEXT | NOT NULL | Nome do técnico responsável pela medição. |
| matricula | TEXT | NOT NULL, UNIQUE | Matrícula do técnico, sem repetição. |
| email | TEXT | NOT NULL | E-mail do técnico. O banco não verifica o formato do endereço. |
| setor | TEXT | NOT NULL | Setor em que o técnico trabalha. |

## Tabela equipamento — 5 campos

| Campo | Tipo declarado no SQLite | Restrições / Chaves | Descrição |
| --- | --- | --- | --- |
| id_equipamento | INTEGER | PRIMARY KEY AUTOINCREMENT | Identificador automático do equipamento. |
| codigo_tag | TEXT | NOT NULL, UNIQUE | Código usado para identificar o equipamento, sem repetição. |
| nome_equipamento | TEXT | NOT NULL | Nome ou descrição do equipamento. |
| fabricante | TEXT | NOT NULL | Fabricante do equipamento. |
| modelo | TEXT | NOT NULL | Modelo do equipamento. |

## Tabela medicao — 10 campos

| Campo | Tipo declarado no SQLite | Restrições / Chaves | Descrição |
| --- | --- | --- | --- |
| id_medicao | INTEGER | PRIMARY KEY AUTOINCREMENT | Identificador automático da medição. |
| id_equipamento | INTEGER | NOT NULL, FOREIGN KEY | Referência ao id_equipamento da tabela equipamento. |
| id_tecnico | INTEGER | NOT NULL, FOREIGN KEY | Referência ao id_tecnico da tabela tecnico. |
| parametro_medido | TEXT | NOT NULL | Característica avaliada na medição. |
| valor_nominal | REAL | NOT NULL | Valor de referência esperado para o parâmetro. |
| tolerancia_min | REAL | NOT NULL | Tolerância inferior utilizada para determinar o limite mínimo. |
| tolerancia_max | REAL | NOT NULL | Tolerância superior utilizada para determinar o limite máximo. |
| valor_obtido | REAL | NOT NULL | Valor encontrado durante a medição. |
| status_resultado | TEXT | NOT NULL, CHECK | Aceita somente APROVADO ou REPROVADO. |
| data_medicao | DATETIME | DEFAULT CURRENT_TIMESTAMP | Data e hora da medição. Se omitida, recebe o horário atual em UTC. Aceita nulo explícito. |

## Regras dos relacionamentos
Cada medição deve apontar para um técnico e um equipamento existentes.
ON DELETE RESTRICT impede excluir um cadastro que possui medições vinculadas.
ON UPDATE CASCADE atualiza as referências quando o identificador do cadastro muda.
A verificação das chaves estrangeiras deve ser ativada em cada conexão ao banco.

## Interpretação das tolerâncias
As tolerâncias representam os desvios permitidos em relação ao valor nominal.
Conforme o material da aula, o limite mínimo é o nominal menos o módulo da tolerância inferior.
O limite máximo é o nominal mais o módulo da tolerância superior.
Esses cálculos ainda não são executados pelo banco desta entrega.

## Observações
O SQLite não possui um tipo exclusivo de armazenamento para data e hora.
CURRENT_TIMESTAMP gera texto no formato AAAA-MM-DD HH:MM:SS.
A declaração DATETIME, sozinha, não valida datas fornecidas pelo usuário.
Os campos REAL indicam valores numéricos, mas este modelo não utiliza tabelas STRICT.
A validação dos valores importados deverá ser realizada pela aplicação.
O resultado da medição é informado; o CHECK apenas valida as duas opções permitidas.
Este script gera a documentação e não extrai dados das planilhas operacionais.
"""

arquivo.write_text(conteudo, encoding="utf-8")

print(f"Arquivo gerado com sucesso: {arquivo.name}")
print("Total documentado: 3 tabelas e 20 campos.")
