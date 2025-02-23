produto = float(input('Qual é o preço do produto? R$'))
desconto = produto * 0.05
novo = produto - desconto
print(f'O produto que custava R${produto:.2f}, na promoção com desconto de 5% vai custar R${novo:.2f}')