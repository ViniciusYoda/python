"""
#Comando de saidas de dados

nome = "Vinícius" #str
idade = 17 #int
peso = 67.5647 #float
maior_idade = False
#metodo por vingula
print("Sou o",nome,"tenho",idade,"anos e peso",peso,"kilos")
#metodo mais usado por ser usado no JS tbm
print(f"Sou o {nome}  tenho {idade} ano e peso {peso} kilos")
#metodo funçao format
print("Sou o {} tenho {} anos e peso {} kilos".format(nome, idade, peso ))
#como arredondar as casas decimais do peso
print(f"Sou o {nome} tenho {idade} ano e peso {peso:.2f} kilos")
print("Sou o {} tenho {} anos e peso {:.2f} kilos".format(nome, idade, peso))#:.2f
#variação do fromat
#print("Estou pesando {2:.2f} sou o {0} tenho {1} anos e peso (2:.2f} kilos ".format(nome, idade, peso))
print("Sou o {n} tenho {i} anos e peso {p:.2f} kilos".format(n=nome, i=idade, p=peso))


#casting

#com str

cobaia = "5";

print("cobaia = ", cobaia,", é do tipo =", type(cobaia))
resposta = cobaia + cobaia
print("Respsota = ",resposta)


#com int

cobaia = "5";
print("coabaia =", cobaia, ", é do tipo =", type(cobaia) )
resposta = int(cobaia) + int(cobaia) #transformou "5" + "5" em 5 +5
print("Resposta = ",resposta )

#com float
cobaia = "5.789";
print("cobaia = ", cobaia, ", é do tipo =", type(cobaia))
resposta = float(cobaia) + float(cobaia)
print("Resposta = ",resposta)
"""
"""
cobaia = "Vinicius"
resposta = 5 * cobaia
print(resposta)

# operadores aritmeticos

+ soma
- subtração
* multiplicação
/ divisão
% resto da divisão
// divisão inteira
** exponenciação

qunatia -130
nota de 50 = c50
nota de 20 = c20
nota de 10 = c10

c50 = quantia // 50 = 2
quantia = quantia % 50 = 30
c20 = quantia // 20 =1
quantia = quantia % 20
c10 = quantia // 10 = 1
quantia = quantia % 10 = 0

valor1 = 30
valor2 = 7
resposta = valor1 // valor2
print(resposta)

valor1 = 3
valor2 = 7
resposta = 5 + 6 ** 2 * 2

#função input

#variavel foi como srt
valor1 = input("Digite o 1 valor1:")
valor2 = input("Digite 0 2 valor2:")
resposta = valor1 + valor2
print(resposta)

#variavel como int

valor1 = input("digite o 1 numero:")
valor1 = int(valor1)
valor2 = int(input("digite o 2 numero"))
resposta = valor1 + valor2
print(resposta)

valor1 = int(input("Digite o primeito valor:"))
valor2 = int(input("Digite o segundo valor:"))
valor3 = int(input("Digite o terceiro valor:"))
resposta = valor1 * valor2 + valor3
print(resposta)

valor1 = int(input("Primeiro valor:"))
valor2 = int(input("Segundo valor:"))
resposta = valor1 * valor2
print(resposta)
"""
