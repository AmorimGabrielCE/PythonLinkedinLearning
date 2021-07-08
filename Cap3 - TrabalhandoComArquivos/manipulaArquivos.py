import os
from os import path
import shutil

#Função para copiar arquivo
def copiaArquivo():
    if path.exists("NovoArquivo.txt"):
        pathAtual = path.realpath("NovoArquivo.txt")
        novoPath = pathAtual + ".bkp"
        shutil.copy(pathAtual, novoPath)

        #copia as permissões do arquivo
        shutil.copystat(pathAtual, novoPath)

copiaArquivo()

#Função para renomear arquivo
def renomearArquivo():
    if path.exists("NovoArquivo.txt"):
        os.rename("NovoArquivo.txt.bkp", "ArquivoAlterado.txt")

renomearArquivo()