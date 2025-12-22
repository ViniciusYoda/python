import urllib.error
import urllib.request

try:
    response = urllib.request.urlopen("http://www.pudim.com.br", timeout=5)
except urllib.error.URLError:
    print("Não foi possível acessar o site Pudim.")
else:
    print('Acesso ao site Pudim realizado com sucesso!')
    print(response.read())