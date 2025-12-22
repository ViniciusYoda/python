from random import randint

def sorteia(lista):
    print("Sorteando 5 números para a lista: ", end="")
    for _ in range(5):
        num = randint(1, 10)
        lista.append(num)
        print(num, end=" ")
    print()

def somaPar(lista):
    soma = sum(num for num in lista if num % 2 == 0)
    print(f"Somando os valores pares de {lista}, temos {soma}")

numeros = []
sorteia(numeros)
somaPar(numeros)