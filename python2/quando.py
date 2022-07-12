i = 0
s = 1 + 1/2 + 1/3 + 1/4
n = int(input('Digite o valor: '))
while i != n:
    if n > i:
        print(s)
    else:
        if i % 2 ==0:
            s -= 1 / i 
            i += 1
    break
print(s)