import random

dezmil = open('dezmil.txt', 'a')

for i in range(random.randint(0, 10000)):
    dezmil.append(i)

dezmil.close

cemmil = open('cemmil.txt', 'a')

for i in range(random.randint(0, 100000)):
    cemmil.append(i)

cemmil.close

quientomil = open('quientomil', 'a')

for i in range(random.randint(0, 500000)):
    quientomil.append(i)

quientomil.close

umilhao = open('umilhao', 'a')

for i in range(random.randint(0, 1000000)):
    umilhao.append(i)

umilhao.close

cincomilhao = open('cincomilhao', 'a')

for i in range(random.randint(0, 5000000)):
    cincomilhao.append(i)

cincomilhao.close


