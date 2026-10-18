import sqlite3
from pathlib import Path

# Localiza os arquivos na mesma pasta deste programa.
pasta = Path(__file__).resolve().parent
arquivo_sql = pasta / "03_banco.sql"
arquivo_banco = pasta / "schulz_calibracao.db"


def main():
    conexao = None

    try:
        # Lê as instruções para criar as tabelas.
        sql = arquivo_sql.read_text(encoding="utf-8-sig")

        # Abre o banco ou cria o arquivo, caso não exista.
        conexao = sqlite3.connect(arquivo_banco)
        conexao.execute("PRAGMA foreign_keys = ON;")

        # Executa as instruções do arquivo SQL.
        conexao.executescript(sql)
        conexao.commit()

        # Consulta as tabelas criadas pelo projeto.
        tabelas = conexao.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
              AND name NOT LIKE 'sqlite_%'
            ORDER BY name;
        """).fetchall()

        print("Banco preparado com sucesso!")
        print(f"Arquivo: {arquivo_banco.name}")
        print("\nTabelas encontradas:")

        for tabela in tabelas:
            print(f"- {tabela[0]}")

        # Confere a integridade do banco.
        integridade = conexao.execute(
            "PRAGMA integrity_check;"
        ).fetchone()[0]

        chaves_estrangeiras = conexao.execute(
            "PRAGMA foreign_keys;"
        ).fetchone()[0]

        print(f"\nIntegridade do banco: {integridade}")
        print(f"Chaves estrangeiras ativadas: {chaves_estrangeiras}")

    except (OSError, sqlite3.Error) as erro:
        print(f"Não foi possível preparar o banco: {erro}")

    finally:
        if conexao is not None:
            conexao.close()


if __name__ == "__main__":
    main()
    