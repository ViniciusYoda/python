from classes036 import Boleto, CartaoCredito, Pix


def main():
    boleto = Boleto(dias_para_vencer=5)
    pix = Pix(chave_destino="loja@exemplo.com")
    cartao = CartaoCredito(final_cartao="1234", limite=2_000)

    print(boleto.pagar(150))
    print(f"Status: {boleto.status}\n")

    print(pix.pagar(89.90))
    print(f"Status: {pix.status}\n")

    print(cartao.pagar(1_250.75, parcelas=5))
    print(f"Status: {cartao.status}")
    print(f"Limite restante: R$ {cartao.limite:.2f}")


if __name__ == "__main__":
    main()
