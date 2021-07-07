#Declarando uma variável
f = 0
#Imprimindo a variável
print(f)


#Declarando a mesma variável novamente
f = "abc"
print(f)

#Gerando um erro, usando variáveis de tipos diferentes
print("Isto é uma string" + str(123))

#Variável Global x variável local
def AlgumaFuncao():
    global f
    f = "def"
    print(f)

AlgumaFuncao()
print(f)

