qtde_num = int(input('Qtde: '))
cont = 1
soma = 0 
while cont <= qtde_num:
    num = int(input('Número: '))
    soma += num
    cont+=1
print(f'Soma: {soma}')