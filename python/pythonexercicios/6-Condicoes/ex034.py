salario = float(input('Digite o seu salário: R$'))
if salario > 1250.00:
    aumento = salario + (salario*(10/100))
    print("Seu novo salário é de R${:.2f}".format(aumento))
else:
    aumento = salario + (salario*(15/100))
    print("Seu novo salário é de R${:.2f}".format(aumento))