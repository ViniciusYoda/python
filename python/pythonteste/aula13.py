from traceback import print_tb


for c in range(1, 7):
    print(c)
print('fim')

for t in range(6, 0, -1):
    print(t)
print('fim')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('fim')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')

s = 0
for c in range(0, 4):
    n = input('Digite um valor: ')
    s += n
print('O somatório entre os valores é {}'.format(s))
