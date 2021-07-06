#Defininfo um Loop FOR
def loopFor():
    for x in range(5,10):
        print(x)

loopFor()

#Usando um LOOP FOR em uma coleção
def loopArray():
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
    for d in dias:
        print(d)

loopArray()    

#Usando enumerate para buscar valores e seus índices
def loopEnum():
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
    for i,  d in enumerate(dias):
        print(i, d)

loopEnum() 