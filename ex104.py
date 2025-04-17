def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print("Erro! Digite um número inteiro válido.")

n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}.")