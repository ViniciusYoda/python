print('Digite um número para calcular seu fatorial: ')
n = int(input('Número: '))
f = 1
c = n
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
