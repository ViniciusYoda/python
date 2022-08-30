casa = float(input("Qual é o valor da casa? R$"))
salario = float(input("Qual é o seu salário? R$"))
anos = int(input("Quantos anos de financiamento? "))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print("Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}".format(casa, anos, prestacao))
if prestacao <= minimo:
    print("Empréstimo pode ser concedido")
else:
    print("Empréstimo negado")