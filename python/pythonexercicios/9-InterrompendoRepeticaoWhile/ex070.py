totG = totmil = menor = cont = 0 
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    totG += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print("{:-^40}".format('Fim do programa'))
print(f'O total da compra foi R${totG:.2f}')
print(f'Temos {totmil} valendo mais de mil reais')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')