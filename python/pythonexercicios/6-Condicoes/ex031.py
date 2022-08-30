km = float(input('Qual é a distância da sua viagem? '))
'''if km <= 200:
    preco = km * 0.50
else: 
    preco = km * 0.45'''
preco = km * 0.50 if km <= 200 else km * 0.45
print(f"A passagem vai custar R${preco:.2f}")