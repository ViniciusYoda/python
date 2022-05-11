print('(+) Adição')
print('(-) Multiplicação')
print('(*) Subtração')
print('(/) Divisão')
print('(=) Resultado')

n = int(input('Número: '))
op = input('| + | - | * | / | = |')
result = n
maior = n 
menor = n 

while op != '=':
    n = int(input('Número: '))

    #Maior e menor
    if n > maior:
        maior = n
    if n < menor:
        menor = n 

    #Encontra o resultado as operações escolhidas pelo usuário
    if op == "+":
        result += n 
    elif op == '-' :
        result -= n
    elif op == '*':
        result *= n   
    elif op == '/':
        result /= n

    op = input('| + | - | * | / | = |')
print(f'Maior: {maior}')  
print(f'Menor: {menor}')
print(f'Resultado: ' {result})