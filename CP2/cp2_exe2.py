#dados armazenadis
user = 'Teste123'
pwd = 123

continuar = True

while continuar:
    cont = 1
    while cont <= 3:
        #dados digitados pelo usuario
        login = input('Login: ')
        senha = int(input('Senha: '))
        if login == user and senha == pwd:
            print('Login efetuado com sucesso')
            continuar = False
            break
        else:
            cont+=1
    if cont > 3:
        print('Número de tentativas excedido!')
        print('Redefina sua senha...')
        user = input('Login: ')
        pwd = int(input('Senha: '))