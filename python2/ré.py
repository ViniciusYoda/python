credito = float(input('Crédito: '))
total = 0
valor = float(input('Valor: '))

while valor <= credito:
    total = total + valor
    credito -= valor
    print(f'Crédito: {credito:.2f}')
    valor = float(input('Valor: '))
print(f'Total da compra:  {total:.2f}')
print(f'Crédito restante: {credito:.2f}')