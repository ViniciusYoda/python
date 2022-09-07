import Moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é {Moeda.metade(p)}')
print(f'O dobro de R${p} é {Moeda.dobro(p)}')
print(f'Aumentando 10% temos R${Moeda.aumentar(p, 10)}')
print(f'Diminuido em 50% temos R${Moeda.diminuir(p, 50)}')