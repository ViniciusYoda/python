import math
valor = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(valor))
cosseno = math.cos(math.radians(valor))
tangente = math.tan(math.radians(valor))
print("O ângulo de {:.2f} tem o SENO de {:.2f}".format(valor, seno))
print("O ângulo de {:.2f} tem o COSSENO de {:.2f}".format(valor, cosseno))
print("O ângulo de {:.2f} tem a TANGENTE de {:.2f}".format(valor, tangente))