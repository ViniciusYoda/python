import sqlite3
from contextlib import closing
from pathlib import Path


CAMINHO_BANCO = Path(__file__).resolve().parent / "meubanco.db"


def buscar_amigos(busca: str) -> list[sqlite3.Row]:
    """Consulta amigos pelo nome; uma busca vazia retorna todos."""
    # O modo de leitura evita criar outro banco ou alterar o existente.
    endereco_banco = f"{CAMINHO_BANCO.as_uri()}?mode=ro"

    with closing(sqlite3.connect(endereco_banco, uri=True)) as banco:
        banco.row_factory = sqlite3.Row

        with closing(banco.cursor()) as cursor:
            cursor.execute(
                "SELECT * FROM amigos WHERE nome LIKE ? ORDER BY nome COLLATE NOCASE",
                (f"%{busca}%",),
            )
            return cursor.fetchall()


def main() -> None:
    try:
        busca = input("Quem você está procurando? (Enter para listar todos): ").strip()

        if not CAMINHO_BANCO.is_file():
            raise FileNotFoundError(f"Banco de dados não encontrado: {CAMINHO_BANCO}")

        amigos = buscar_amigos(busca)

    except FileNotFoundError as erro:
        print(erro)
        return
    except sqlite3.OperationalError as erro:
        print(f"Não foi possível abrir o banco ou consultar a tabela amigos: {erro}")
        return
    except sqlite3.DatabaseError as erro:
        print(f"Erro no banco de dados: {erro}")
        return
    except OSError as erro:
        print(f"Erro ao acessar o arquivo do banco: {erro}")
        return
    except (EOFError, KeyboardInterrupt):
        print("\nConsulta cancelada.")
        return

    if not amigos:
        print("Nenhum amigo encontrado." if busca else "Nenhum amigo cadastrado.")
        return

    for numero, amigo in enumerate(amigos, start=1):
        print(f"{numero}. {dict(amigo)}")

    print(f"\nTotal de amigos encontrados: {len(amigos)}")


if __name__ == "__main__":
    main()
