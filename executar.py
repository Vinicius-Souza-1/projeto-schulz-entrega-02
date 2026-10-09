import sqlite3
from pathlib import Path

# Localiza a pasta onde este programa está salvo.
pasta = Path(__file__).resolve().parent

arquivo_sql = pasta / "03_banco.sql"
arquivo_banco = pasta / "schulz.db"

# Lê os comandos que escrevemos no arquivo SQL.
comandos = arquivo_sql.read_text(encoding="utf-8-sig")

# Abre o banco ou cria o arquivo, caso ele não exista.
conexao = sqlite3.connect(arquivo_banco)

try:
    # Ativa a verificação das chaves estrangeiras.
    conexao.execute("PRAGMA foreign_keys = ON;")

    # Executa os comandos para criar as tabelas.
    conexao.executescript(comandos)

    # Consulta as tabelas existentes.
    tabelas = conexao.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
          AND name NOT LIKE 'sqlite_%'
        ORDER BY name;
    """).fetchall()

    print("SQL executado com sucesso!")
    print(f"Banco: {arquivo_banco}")
    print("\nTabelas encontradas:")

    for tabela in tabelas:
        print(f"- {tabela[0]}")

    chaves = conexao.execute(
        "PRAGMA foreign_keys;"
    ).fetchone()[0]

    integridade = conexao.execute(
        "PRAGMA integrity_check;"
    ).fetchone()[0]

    print(f"\nChaves estrangeiras ativadas: {chaves}")
    print(f"Integridade do banco: {integridade}")

finally:
    conexao.close()