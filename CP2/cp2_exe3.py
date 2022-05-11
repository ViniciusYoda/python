continuar = 's'
while continuar =='s':

    n = int(input('Número: '))
    cont = 1
    while cont <= 10:
        print(f'{n} * {cont} = {n*cont}')
        cont+=1
    continuar = input('Continuar? s-n')
print('Fim')
