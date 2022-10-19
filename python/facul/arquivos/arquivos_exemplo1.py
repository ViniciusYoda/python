#Criando e abrindo um arquiv
#arquivo = open("arquivo.txt", 'r') #read
arquivo = open('arquivo.txt', 'w') #write
# arquivo = open('arquivo.txt', 'a') #append

#escrevendo no arquvo.txt
arquivo.write("Olá, Mundo! \n")
arquivo.write("FIAP \n")

arquivo.write('Olá, Mundo FIAP!!!')

#método writelines()
# -> recebe um onjeto iterável (lista, tupla, dicionário...)
# insere várias linhas no arquivo

#criando uma lsita com as disciplinas
disciplinas = list()
disciplinas.append('Python \n')
disciplinas.append('Java \n')
disciplinas.append('IA Chatbot \n')
disciplinas.append('Banco de Dados \n')

#escrevendo várias linhas no arquivo
arquivo.writelines(disciplinas)

 
#fechando o arquivo
arquivo.close

#lendo de um arquivo
arquivo = open('arquivo.txt', 'r')
print(f'readline(3) {arquivo.readline(3)}')

print(f'readlines() - {arquivo.readlines()}')
print(f'read - {arquivo.read()}')
arquivo.close