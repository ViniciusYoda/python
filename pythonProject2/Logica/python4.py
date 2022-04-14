num1 = int(input('Escreva um número: ', ))
num2 = int(input('Escreva mais um número: ', ))
if num1 == 0:
    print(int(input('Escreva os números novamente: ',)))
elif num2 == 0:
    print(int(input('Escreva os números novamente: ', )))
else:
    res = (num1 + num2)/2
    print('o resultado é: ', res)