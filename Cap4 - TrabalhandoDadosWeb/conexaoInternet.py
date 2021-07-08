import urllib.request

#Função que se conecta a internet
def ConectaInternet():
    objUrl = urllib.request.urlopen("http://www.google.com")

    #O método getcode retorna o código http que retorna se a conexão fez sucesso ou não
    if objUrl.getcode() == 200:
        dados = objUrl.read()
        print(dados)

ConectaInternet()
