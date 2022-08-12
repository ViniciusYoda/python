from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} em {p} em {p}')
    sleep(2.5)

    if i < f: 
        cont = i
        while cont <= i:
            print(f'{cont} ', end='', flush=False)
            sleep(0.5)
            cont += p
        print('fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=False)
            sleep(0.5)
            cont -= p
        print('fim')



contador(1, 10, 1)
contador(10, 0, 2)
ini = int(input('Inicio: '))
fim = int(input('FIM:    '))
pas = int(input('Pass:   '))
contador(ini, fim, pas)