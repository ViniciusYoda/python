import utilidadescev
import utilidadescev.moeda

preco = float(input("Digite o preço: R$"))
taxa = float(input("Digite a taxa (%): "))

print(f"Aumentando {taxa}%, temos {utilidadescev.moeda.aumentar(preco, taxa, True)}")
print(f"Diminuindo {taxa}%, temos {utilidadescev.moeda.diminuir(preco, taxa)}")
print(f"O dobro de {preco} é {utilidadescev.moeda.dobro(preco, True)}")
print(f"A metade de {preco} é {utilidadescev.moeda.metade(preco)}")
utilidadescev.moeda.resumo(preco, taxa, taxa)