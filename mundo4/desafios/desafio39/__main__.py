from classes039 import ValidadorEmail, ValidadorSenha, ValidadorUsuario


def testar(nome, validador, exemplos):
    print(f"\n{nome.upper()}")

    for exemplo in exemplos:
        resultado = "valido" if validador.validar(exemplo) else "invalido"
        print(f"{exemplo!r}: {resultado}")

        if resultado == "invalido":
            print(f"  Motivo: {'; '.join(validador.erros(exemplo))}")


def main():
    testar(
        "Usuarios",
        ValidadorUsuario,
        ["ana_25", "joao", "Usuario", "usuario-invalido"],
    )
    testar(
        "Senhas",
        ValidadorSenha,
        ["Python@2026", "semmaiuscula!", "SemSimbolo1", "Curta@1"],
    )
    testar(
        "Emails",
        ValidadorEmail,
        [
            "ana.silva+loja@exemplo.com.br",
            "usuario@dominio.com",
            "dois@@dominio.com",
            "usuario@dominio",
        ],
    )


if __name__ == "__main__":
    main()
