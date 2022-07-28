import enum
from random import randint
lista = list()
jogos = list()
print('Jogando no jogo de azar')
quant = int(input('Quantos jogos você quer que eu sorteia? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'Sorteando {quant} jogos')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
