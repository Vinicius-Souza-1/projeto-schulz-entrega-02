# Projeto Schulz — Entrega 02

Trabalho acadêmico da unidade curricular Projeto Aplicado I,
do curso de Análise e Desenvolvimento de Sistemas do SENAI.

Autores:
- Victor Gabriel Jaeger
- Vinicius de Assis Mendes
- Vinícius Itamar de Souza

## Objetivo

Organizar os cadastros de responsáveis, equipamentos e medições
em um banco de dados SQLite.

## Estrutura do banco

- responsaveis: pessoas e setores envolvidos nas medições.
- equipamentos: equipamentos que serão calibrados.
- medicoes: leituras e seus vínculos com equipamentos e responsáveis.

## Arquivos principais

- 01_estrutura.md: organização dos dados e relacionamentos.
- 02_dicionario.md: descrição dos 32 campos e seus tipos.
- 03_banco.sql: comandos de criação das três tabelas.
- executar.py: execução do SQL e conferência do banco.

## Como executar

É necessário ter Python 3 instalado.

1. Baixe os arquivos do projeto na mesma pasta.
2. Abra um terminal nessa pasta.
3. Execute: python executar.py

O programa criará o arquivo schulz.db e mostrará as tabelas
encontradas, a ativação das chaves estrangeiras e a integridade do banco.

## Escopo desta entrega

Esta etapa implementa a estrutura do banco de dados.
A importação das planilhas, os cálculos metrológicos e a emissão
de certificados ainda não foram implementados.

O dicionário apresenta os campos propostos para o modelo.
Não foi realizada uma comparação com a saída de um script de extração.

## Contexto acadêmico

Projeto desenvolvido para fins de estudo a partir do desafio Schulz.
Este repositório não representa um sistema oficial da empresa.
