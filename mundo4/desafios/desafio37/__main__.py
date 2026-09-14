from classes037 import Alerta, Erro, Mensagem


def main():
    mensagens = [
        Mensagem("Operacao iniciada."),
        Alerta("Confira os dados antes de continuar."),
        Erro("Nao foi possivel concluir a operacao."),
    ]

    for mensagem in mensagens:
        mensagem.mostrar()


if __name__ == "__main__":
    main()
