import moeda

preco = 100
print(f"O dobro de {preco} é {moeda.dobro(preco)}")
print(f"A metade de {preco} é {moeda.metade(preco)}")
print(f"Aumentando 10%, temos {moeda.aumentar(preco, 10)}")
print(f"Reduzindo 10%, temos {moeda.diminuir(preco, 10)}")