from datetime import *

def deltaTempo():

    delta = timedelta(days=86, hours=8532, minutes=7645)
    print(delta)

    hoje = datetime.now()
    print("Data no futuro: ", hoje + delta)
    print("Data no passado: ", hoje - delta)

deltaTempo()

