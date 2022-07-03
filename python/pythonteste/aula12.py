nome = str(input('Qual é seu nome? '))
if nome == 'Bruno':
    print("Seu nome é brunito")
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print("Seu nome é popular")
elif nome in 'Ana Cláudua Jéssica Juliana':
    print('Nome feminino')
else:
    print("Seu nome está correto")
print('Tenha um bom dia {}'.format
(nome))