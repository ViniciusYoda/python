from random import randint
from time import sleep
from traceback import print_tb
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #Pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogandor vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogada inválida')
elif computador == 1: #Papel
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('Jogada inválida')
elif computador == 2: #Tesoura
    if jogador == 0:
        print('jogador vence')
    elif jogador == 1:
        print('Computado vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida')