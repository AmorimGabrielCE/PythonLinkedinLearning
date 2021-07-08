import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipExtFile, ZipFile


#Diferentes modos de criar arquivos compactados
def CriaZipModo1():
    shutil.make_archive("ArquivoCompactado", "zip", "C:\\Users\\Amorim\\OneDrive\\Python\\PythonLinkedinLearning\\Cap3 - TrabalhandoComArquivos" )

#CriaZipModo1()

def CriaZipModo2():
    with ZipFile("ArquivoZipModo2.zip", "w") as novoZip:
        novoZip.write("NovoArquivo.txt.bkp")
        novoZip.write("NovoArquivo.txt")
        novoZip.write("ArquivoCompactado.zip")

#CriaZipModo2()

#Função para deletar arquivos
def DeletaArquivo():
    os.remove("NovoArquivo.txt")

DeletaArquivo()    