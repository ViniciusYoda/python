def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")
        except KeyboardInterrupt:
            print("\nEntrada de dados interrompida pelo usuário.")
            return 0
        else:
            return valor


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except ValueError:
            print("Erro: Por favor, digite um número real válido.")
        except KeyboardInterrupt:
            print("\nEntrada de dados interrompida pelo usuário.")
            return 0.0
        else:
            return valor


inteiro = leiaInt("Digite um número inteiro: ")
real = leiaFloat("Digite um número real: ")
print(f"Você digitou o número inteiro {inteiro} e o número real {real}.")