#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nomeUser = str(input('Qual é o seu nome de usuáruo: '))
senha = str(input('Digite a senha: '))

while(nomeUser == senha):
    print('A senha não pode ser igual ao nome de usuário')
    nomeUser = str(input('Qual é o seu nome de usuáruo: '))
    senha = str(input('Digite a senha: '))
else:
    print('cadastro realizado com sucesso')
