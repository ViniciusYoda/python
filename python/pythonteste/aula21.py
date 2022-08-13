def somar(a = 0, b = 0, c = 0):
    """
    Soma os números
    """
    s = a + b + c  
    print(f'A soma vale {s}')

somar(3,2,5)
somar(8, 4)

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(fatorial(n))

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = 4
if par(num):
    print('è par')

