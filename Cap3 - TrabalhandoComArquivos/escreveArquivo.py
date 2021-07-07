def EscreveArquivo():
    #w indica que o arquivo será escrito, e o + cria o arquivo se ele não existir
    arquivo = open("NovoArquivo.txt", "w+")

    arquivo.write("Linha gerada com a funcao 'EscreveArquivo' \r\n")

    arquivo.close()

#EscreveArquivo()

def AlteraArquivo():
    #w indica append para escrever nas próximas linhas do arquivo, e o + cria o arquivo se ele não existir
    arquivo = open("NovoArquivo.txt", "a+")

    arquivo.write("Linha gerada com a funcao 'AlteraArquivo' \r\n")

    arquivo.close()

AlteraArquivo()