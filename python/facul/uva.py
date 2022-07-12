credito = float(input('Seu crédito: '))
total = 0 



quero_comprar =  input('Você gostaria de comprar alguma coisa? (s/n)')
while(quero_comprar == 's'):
    preco = float(input('Qual o preço do produto?: R$ '))
    if preco <= credito:
        print('Compra aprovada')
        total += preco
        credito -= preco
        print(f'O seu credito restante é: {credito:.2f}')
        quero_comprar = input('Você quer continuar comprando? (s/n)')
        if quero_comprar != 's':
            break
    else: 
        print('A sua compra não foi autorizada, devido a crédito insuficiente')
        print(f'O seu crédito restante é de: R$ {credito:.2f}')

print('Tudo bem... Obrigado, mas devia ter comprado algo')
print(f'O seu crédito neste momento é de: R$ {credito:.2f}')


if total > 0: 
    print(f'Total: R$ {total:.2f}')
