nome = [4, 1, 2]
nome.append(3) #adiciona um item ao fima da lista
print(nome)
nome.sort() #ordena a lista no lugar, trocando os valores em seus indices. 
print(nome)
nome.extend("oi") #adiciona itens de uma estrutura iteravel 
print(nome)
nome.insert(0, 0) #É muito parecido com o append. Ele insere um item em uma lista, mas o item inserido vai para a posiçãi indicada
print(nome)
nome.remove('i') #é usado para remover uma lista de valores do primeiro jogo
print(nome)
nome.pop() #retorna um elemento da lista e no mesmo instante, remove-o.
print(nome)
print(nome.index(4)) # retorna o index de determinado elemento.
sobrenome = nome.copy() #copia algo da lista
print(sobrenome)
sobrenome.clear() #apaga todos os elementos no dicionario
print(sobrenome)
A = ["a", "b", "c", "d", "e", "f"]

print(A.count("z"))  #retorna a quantidade de vezes que um mesmo elemento está contido numa lista.
print(A.count("a"))

