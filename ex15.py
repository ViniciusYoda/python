alugados = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
total = (alugados * 60) + (km * 0.15)
print(f'O total a pagar é de R${total:.2f}')