kwh = int(input("Digite seu gasto de energia "))

if kwh < 150:
    valor = kwh * 0.20
    print(f"Você pagará: R$ {valor:.2f}")
elif kwh >= 150 and kwh < 500:
    valor = kwh * 0.25
    print(f"Você pagará: R$ {valor:.2f}")
elif kwh > 500:
    valor = kwh * 0.30
    print(f"Valor a pagar: R$ {valor:.2f}")
else:
    print("Valor a pagar é de: R$11.90")