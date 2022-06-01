horas = int(input("Quantas horas você trabalham? "))
seis = 360 * 40.40
oito = 480 * 40.40
doze = 720 * 40.40

if horas == 360:
    print(f"Você recebe {seis:.2f}")

if horas == 480:
    print(f"Você recebe {oito:.2f}")

if horas == 720:
    print(f"Você recebe {doze:.2f}")