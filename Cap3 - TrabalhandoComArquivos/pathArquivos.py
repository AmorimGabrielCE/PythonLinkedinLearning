from os import path
import time

def DadosArquivo():
    #Verifica se o arquivo existe
    arquivoExiste = path.exists("NovoArquivo.txt")
    #Verifica se o arquivo é um diretório
    ehDiretorio = path.isdir("NovoArquivo.txt")
    #Verifica qual o path do arquivo
    pathArquivo = path.realpath("NovoArquivo.txt")
    #Verifica o path relativo
    pathRelativo = path.relpath("NovoArquivo.txt")
    #Verifica a data de criação
    dataCriacao = time.ctime(path.getctime("NovoArquivo.txt"))
    #Verifica a data de modificação
    dataModificacao = time.ctime(path.getmtime("NovoArquivo.txt"))

    print(arquivoExiste)
    print(ehDiretorio)
    print(pathArquivo)
    print(pathRelativo)
    print(dataCriacao)
    print(dataModificacao)

DadosArquivo()

    