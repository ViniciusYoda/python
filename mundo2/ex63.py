print('-=' * 10)
print('Sequência de Fibonacci')
print('-=' * 10)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} -> {}'.format(t1, t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print(' -> Fim')
print('~' * 30)
print('Fim')
print('-=' * 10)