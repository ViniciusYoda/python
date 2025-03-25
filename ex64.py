n = 0
s = 0
c = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        s += n
        c += 1
print('Você digitou {} números e a soma entre eles foi {}'.format(c, s))
print('Fim')