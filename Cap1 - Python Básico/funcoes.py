#Defininfo função básica
def func1():
    print("Eu sou uma função")

func1()

#Função que recebe argumentos
def func2(arg1, arg2):
    print(arg1 + " " + arg2)

func2("Gabriel", "Amorim")

#Função que retorna valor
def cubo(x):
    return x*x*x
    
print(cubo(3))
    