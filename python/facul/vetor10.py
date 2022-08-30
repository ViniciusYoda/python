def real():
    num = 3
    return num

def reais():
    nums = [1.4, 5.6, 6.8, 10.6]
    return nums

def produto(real, reais):
    for i in real:
        if i % real == 0:
            impar = i * reais
    return impar

def resultado(res):
    print(res)
    
    
r = real()
rs = reais()
res = produto(r, rs)
resultado(res)