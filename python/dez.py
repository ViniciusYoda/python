altura = float(input("Digite sua altura: "))
peso = float(input("Digite o seu peso: "))
massa = peso / (altura ** 2)

if massa < 26:
    print("normal")
elif massa >= 26 and massa < 30:
    print("Obeso")
else: 
    print("Obeso Morbido")