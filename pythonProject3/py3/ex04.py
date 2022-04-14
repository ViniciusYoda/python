consumo = float(input("informe o consumo da sua energia elétrica: " ))

valor_minimo = 11.9

if consumo < 150:
    total = consumo * 0.2
elif consumo >= 150 and consumo < 500:
    total = consumo * 0.25
elif consumo >= 500:
    total = consumo * 0.3

if total > valor_minimo:
    print("total: ", total)
else:
    print("total: ", total)