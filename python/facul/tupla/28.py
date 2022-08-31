intervalo = range(0) # atribui um intervalo vazio a variavel
print(intervalo)
intervalo = range(5, 10, 2) #atribui um intervalo [5..10[ e com passo 2.]]
print(intervalo)
lista = list(intervalo) #gera uma lista com os itens do intervalo.
print(lista)
tupla = tuple(intervalo) # gera uma tupla com os itens do intervalo;
print(tupla)
intervalo[-1] # acessa o último item do intervalo.
intervalo[0] = 77 # tentativa de alteração do intervalo.