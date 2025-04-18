import moeda

preco = float(input("Digite o preço: R$"))
taxa = float(input("Digite a taxa (%): "))

print(f"Aumentando {taxa}%, temos {moeda.aumentar(preco, taxa, True)}")
print(f"Diminuindo {taxa}%, temos {moeda.diminuir(preco, taxa)}")
print(f"O dobro de {preco} é {moeda.dobro(preco, True)}")
print(f"A metade de {preco} é {moeda.metade(preco)}")
moeda.resumo(preco, taxa, taxa)