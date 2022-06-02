soma = 0
salarios = []
valor = int(input("Quantos salarios você quer digitar? "))
salario = valor
for _ in range(valor):
    salario = float(input("Qual seu salario: "))
    soma += salario
    salarios.append(salario)
media = soma / valor
for salario in salarios:
    if salario < media:
        print(f"Abaixo da media R${salario:.2f}")