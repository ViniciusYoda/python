with open("teste.txt", "r") as arquivo:
    conteudo=arquivo.read()
print("Tipo de dado da variável",type(conteudo))
print("Conteúdo do arquivo:",conteudo)