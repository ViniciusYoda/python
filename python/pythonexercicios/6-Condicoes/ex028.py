from random import randint
from time import sleep
computador = randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
num = int(input('Em que número eu pensei? '))
print("PROCESSANDO...")
sleep(2)
if num != computador:
    print("Ganhei! Eu pensei no número {} e não no {}!".format(computador, num))
else:
    print("PARABÉNS! Você conseguiu me vencer!")