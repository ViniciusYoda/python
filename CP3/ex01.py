nome = []
kms = []
km = 0
for c in range(5):
    print(f"Veiculo {c + 1}")
    nome.append(input('Nome: '))
    km = float(input("KM por litro: "))
    kms.append(km)

print("Resultado: ")
menor = 0
car = ''
for c, r in enumerate(nome):
    print(f"{c + 1} - {r} - {kms[c]} - {1000/kms[c]:.2f} - R$ {1000/kms[c] * 6.89:.2f}")
    if kms[c] > menor:
        menor = kms[c]
    car = nome[c]

print(f"O menor consumo entre carros é {car}")



