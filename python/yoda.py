credito = float(input('Seu crédito: '))
total = 0 #variavel acumuladora 

preco = float(input('Preço do Produto: R$'))

while credito >= preco:
    if preco > credito:
        print('Credito insuficiente')
    total += preco
    credito -= preco #credito = credito - preco
    preco = float(input('Preço do Produto: R$'))
print(f'Total: R$ {total:.2f}')
print(f'Crédito restante: R$ {credito:.2f}')
continuar = str(input('Quer continuar comprando? [s/n]'))
    if continuar == 's':
       preco = float(input('Preço do Produto: R$'))

while credito >= preco:
    if preco > credito:
        print('Credito insuficiente')
    total += preco
    credito -= preco #credito = credito - preco
    preco = float(input('Preço do Produto: R$'))
print(f'Total: R$ {total:.2f}')
print(f'Crédito restante: R$ {credito:.2f}')
    else:
        print('Obrigado pela preferencia')
