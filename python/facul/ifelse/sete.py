ar = input(" + | - | * | / ")
num1 = int(input("Número: "))
num2 = int(input("Número: "))

if ar == "+":
    soma = num1 + num2
    print(soma)
elif ar == "-":
    subtracao = num1 - num2
    print(subtracao)
elif ar == "*":
    multi = num1 * num2
    print(multi)
elif ar == "/":
    div = num1 / num2
    print(div)
else:
    print("ERRO")