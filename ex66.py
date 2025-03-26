s = t = 0
while True:
    n = int(input('Digite um número: (999) para parar '))
    if n == 999:
        break
    s += n
    t += 1
print(f'A soma vale {s} e foram digitados {t} números.')