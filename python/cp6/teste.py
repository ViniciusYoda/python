def soma1(x, y):
    return sum(range(x, y+1))

def soma2(x, y):
    soma = 0
    for i in range(x, y+1):
        soma += i
    return soma

import time

# verifica o tempo de resposta da função soma1
ini = time.time()
soma1(1, 1000000)
fim = time.time()
print ("Função soma1: ", fim-ini)

# verifica o tempo de resposta da função soma2
ini = time.time()
soma2(1, 1000000)
fim = time.time()
print ("Função soma2: ", fim-ini)

time.sleep(arg)