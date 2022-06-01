a = int(input("Escreva um número: "))
b = int(input("Escreva um número: "))
if a == 0 and b == 0:
    print("Os dois números não podem ser iguais a zero")
    a = int(input("Escreva um número: "))
    b = int(input("Escreva um número: "))

soma = (a + b) / 2
print(soma)