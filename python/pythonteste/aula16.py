lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim','Batata Frita')
# Tuplas são imutáveis
#lanche[1] = 'Refrigetante'
print(lanche)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print(len(lanche))

for cont in range(0, len(lanche)):
    print(f'Eu comi {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print(len(lanche))

print(sorted(lanche))

a = (2,5,4)
b = (5,8,1,2)
print(a,b)
c = a + b
print(c)
print(c.count(5))
print(c.index(8))

pessoa = ('Vinicius', 18, 'M', 69.1)
print(pessoa)
del(pessoa)
print(pessoa)