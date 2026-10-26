import sqlite3

from classes041 import buscar_pessoas


def main():
    try:
        busca = input(
            "Quem voce esta procurando? (Enter para listar todos): "
        ).strip()
        pessoas = buscar_pessoas(busca)
    except FileNotFoundError as erro:
        print(erro)
        return
    except sqlite3.DatabaseError as erro:
        print(f"Erro ao consultar o banco de dados: {erro}")
        return
    except (EOFError, KeyboardInterrupt):
        print("\nConsulta cancelada.")
        return

    if not pessoas:
        mensagem = (
            f"Nenhum registro encontrado para '{busca}'."
            if busca
            else "Nenhum registro cadastrado."
        )
        print(mensagem)
        return

    print()
    for pessoa in pessoas:
        idade = (
            f"{pessoa.idade} anos"
            if pessoa.idade is not None
            else "idade nao calculada"
        )
        print(
            f"{pessoa.id}. {pessoa.nome} | "
            f"Nascimento: {pessoa.nascimento_formatado} | "
            f"Idade: {idade}"
        )

    print(f"\nTotal de registros encontrados: {len(pessoas)}")


if __name__ == "__main__":
    main()
