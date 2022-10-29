from logging import exception
from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print('Arquivo criado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace(';', '')
            print(f'{dado[0]:<30}{dado[1]:>30} anos')
    finally:
        a.close()

def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro')
    else:
        try:
            a.write(f'{nome}:{idade}\n')
        except:
            print('Mais um erro')
        else:
            print('Novo registro cadastrado')
            a.close()