s = 1 + 1/2 - 1/3 + 1/4
n = float(input('Qual o valor ?: '))
cont = 1
soma = 0
while cont <=n:
    if cont %2 == 0:
        soma +=(1/cont)
    else:
        soma -= 1/cont
    cont += 1
