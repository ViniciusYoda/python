def a():
    vetorA = [1,2,3,4,5]
    return vetorA

def b():
    vetorB = [6,7,8,9,10]
    return vetorB

def produto(a, b):
    for i in a:
        for j in b:
            produto = i * j
    return produto

def resultado(res):
    print(res)

v1 = a()
v2 = b()
valor = produto(v1, v2)
resultado(valor)