import Moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {Moeda.moeda(p)} é {Moeda.metade(p, True)}')
print(f'O dobro de {Moeda.moeda(p)} é {Moeda.dobro(p, True)}')
print(f'Aumentando 10% temos {Moeda.aumentar(p, 10, True)}')
print(f'Diminuido em 80% temos {Moeda.diminuir(p, 80, True)}')