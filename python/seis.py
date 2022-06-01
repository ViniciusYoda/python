nome = input("Qual o nome do funcionario? ")
codigo = int(input("Qual o código da peça? "))
preco = float(input("Qual o preço do produto? "))
quantidade = int(input("Qual a quantidade vendida? "))
res = quantidade * preco
cota = res + (5/100)
print(f"O funcionario {nome} vendeu o {codigo} que custa {preco:.2f}, vendeu {quantidade} com isso ele recebeu {cota} de cota")