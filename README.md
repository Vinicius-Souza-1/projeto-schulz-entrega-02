# Projeto Schulz — Entrega 02

Trabalho da unidade curricular Projeto Aplicado I, do curso de Análise e Desenvolvimento de Sistemas do SENAI.

## Integrantes

- Victor Gabriel Jaeger
- Vinicius de Assis Mendes
- Vinícius Itamar de Souza

## Objetivo

Criar um banco de dados SQLite para organizar técnicos, equipamentos e medições, como base para o desenvolvimento do projeto Schulz.

## Estrutura do banco

O modelo possui três tabelas e vinte campos:

| Tabela | Finalidade | Quantidade de campos |
| --- | --- | --- |
| tecnico | Cadastrar os técnicos responsáveis pelas medições. | 5 |
| equipamento | Cadastrar os equipamentos avaliados. | 5 |
| medicao | Registrar os valores medidos e relacioná-los ao técnico e ao equipamento. | 10 |

Cada tabela possui uma chave primária gerada automaticamente.
A tabela medicao utiliza chaves estrangeiras para relacionar os registros.
A matrícula do técnico e o código do equipamento não podem ser repetidos.

## Arquivos do projeto

| Arquivo | Função |
| --- | --- |
| 01_estrutura.md | Explica as tabelas, os relacionamentos e os limites do modelo. |
| 02_dicionario.md | Descreve os campos, os tipos e as restrições do banco. |
| 03_banco.sql | Contém as instruções SQL para criar as tabelas. |
| executar_banco.py | Executa o SQL e verifica a integridade do banco. |
| gerar_estrutura_md.py | Gera o documento 01_estrutura.md. |
| gerar_dicionario_md.py | Gera o documento 02_dicionario.md. |
| schulz_calibracao.db | Banco SQLite gerado pelo programa. |
| Relatorio_Entrega_02.pdf | Relatório explicativo da atividade. |
| README.md | Apresenta o projeto e as instruções de execução. |

## Requisitos para executar

- Python 3 instalado.
- Os arquivos SQL e Python na mesma pasta.
- Um terminal para executar os comandos.

O projeto utiliza sqlite3 e pathlib, que fazem parte da biblioteca padrão do Python.
Não é necessário instalar pacotes adicionais.

## Como executar

Abra o terminal na pasta do projeto e execute os comandos abaixo, um de cada vez.

### 1. Criar o banco

```bash
python executar_banco.py
```

O programa cria o arquivo schulz_calibracao.db, caso ele não exista, e executa o SQL.

O resultado esperado inclui:

```text
Tabelas encontradas:
- equipamento
- medicao
- tecnico

Integridade do banco: ok
Chaves estrangeiras ativadas: 1
```

Executar novamente o programa não apaga os registros existentes.
O comando CREATE TABLE IF NOT EXISTS também não atualiza a estrutura de tabelas já criadas.

### 2. Gerar a documentação da estrutura

```bash
python gerar_estrutura_md.py
```

### 3. Gerar o dicionário de dados

```bash
python gerar_dicionario_md.py
```

Os geradores substituem os respectivos arquivos Markdown.
Para alterar esses documentos de forma permanente, edite o conteúdo nos scripts e execute-os novamente.

## Limites desta entrega

- O banco é criado sem registros.
- Os scripts de documentação não extraem dados das planilhas.
- A importação e a higienização dos dados ainda não foram implementadas.
- O resultado da medição é informado, sem cálculo automático.
- A emissão de certificados ainda não foi implementada.
- A matrícula e o código do equipamento possuem controle de duplicidade.
- O controle de reimportação de medições ainda precisa ser desenvolvido.

## Repositório

https://github.com/Vinicius-Souza-1/projeto-schulz-entrega-02
