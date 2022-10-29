from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'curso.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema')
        break
    else:
        print('Erro, digite uma opção inválida')
    sleep(2)