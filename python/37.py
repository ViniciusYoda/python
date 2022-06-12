def perguntar():
    resposta = input("O que deseja realizar?
" +
                  "<I> - Para Inserir um usuário
" +
                  "<P> - Para Pesquisar um usuário
" +
                  "<E> - Para Excluir um usuário
" +
                  "<L> - Para Listar um usuário: ").upper()
    return resposta

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                          input("Digite a última data de acesso: "),
                                          input("Qual a última estação acessada: ").upper()]
