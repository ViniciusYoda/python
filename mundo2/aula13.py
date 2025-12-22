i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')

s = 0
for v in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'A soma dos valores é {s}')