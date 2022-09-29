#Fatorial (recursivo)



def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

n = 5       
print(f'fatorial de {n} é: {fatorial(n)}')