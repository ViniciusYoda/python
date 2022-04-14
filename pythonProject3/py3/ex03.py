altura = float(input("Informe a sua altura: "))
peso = float(input("Informe também o seu peso: "))
massa = (peso/altura**2)
if massa < 26:
    print("normal")
elif  massa >= 26 and massa < 30:
    print("obeso")
elif massa >= 30:
    print("Obseo Mórbido")