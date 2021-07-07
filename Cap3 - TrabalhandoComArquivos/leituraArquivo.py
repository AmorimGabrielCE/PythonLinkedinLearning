def leituraArquivo():
    #r indica que eu irei ler o arquivo
    arquivo = open("NovoArquivo.txt", "r")
    if arquivo.mode == "r":
        conteudo = arquivo.read()
        print(conteudo)

    arquivo.close()

#leituraArquivo()


#Lendo um arquivo grande linha por linha
def leituraArquivoGrande():
    #r indica que eu irei ler o arquivo
    arquivo = open("NovoArquivo.txt", "r")
    if arquivo.mode == "r":
        conteudoTotal = arquivo.readlines()

        for conteudo in conteudoTotal:
            print(conteudo)

    arquivo.close()

leituraArquivoGrande()


