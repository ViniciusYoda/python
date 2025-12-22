from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'dados.txt'

if not arquivoExiste(arq):
    criar_arquivo(arq)

while True:
    # Exibe o menu e aguarda a opção do usuário
    resposta = menu(['Criar Arquivo', 'Adicionar Dados', 'Ver Dados', 'Sair'])
    
    # Verifica a opção escolhida pelo usuário
    if resposta == 1:
        criar_arquivo('dados.txt')
    elif resposta == 2:
        adicionar_dados('dados.txt')
    elif resposta == 3:
        ver_dados('dados.txt')
    elif resposta == 4:
        print('Saindo...')
        break
    else:
        print('\033[31mOpção inválida! Tente novamente.\033[m')
    sleep(2)