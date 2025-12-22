print('{:=^40}'.format(' LOJAS '))
preco = float(input('Preços das compras R$'))
print(''' Forma de pagamento
      [ 1 ] A vistia dinheiro/cheque
      [ 2 ] a vista cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão ''')
opcao = int(input('Qual opção: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preco
    print('Opção inválida de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))