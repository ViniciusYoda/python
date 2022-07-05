n1 = float(input("Primeiro nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2
if media < 5.0:
    print("A média de {} e {} é {}. O aluno está reprovado".format(n1, n2, media))
elif 7 > media >= 5.0:
    print("A média de {} e {} é {}. O aluno está de recperação".format(n1, n2, media))
else:
    print("A média de {} e {} é {}. O aluno está aprovado".format(n1, n2, media))