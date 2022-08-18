def entrada_de_dados():
    n = int(input(f'Digite o número para o delta: '))
    return n

def delta(a, b, c):
    delta = a ** 2 + b + c 
    return delta

def imprimir_raiz(delta):
    if delta < 0:
        print(-1)
    else:
        print(delta)

def principal():
    a = entrada_de_dados()
    b = entrada_de_dados()
    c = entrada_de_dados()
    delta = delta(a, b, c)
    imprimir_raiz(delta)

principal()
    
