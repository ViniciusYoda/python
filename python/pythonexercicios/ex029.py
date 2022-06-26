velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade <= 80:
    print("Dirija com segurança!")
else:
    print("MULTADO! Você passou da velocidade permitda! Você foi multado em R${:.2f}".format((velocidade-80) * 7.00 ))