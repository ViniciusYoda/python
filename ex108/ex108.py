import moeda

preco = 100

print(f"O preço aumentado em 10% é: {moeda.aumentar(preco, 10)}")
print(f"O preço diminuído em 15% é: {moeda.diminuir(preco, 15)}")
print(f"O dobro do preço é: {moeda.dobro(preco)}")
print(f"A metade do preço é: {moeda.metade(preco)}")