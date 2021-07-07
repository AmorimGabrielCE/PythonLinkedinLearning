from datetime import datetime

#Datas e horas podem ser formatados usando um conjunto de strings predefinidas
def FormataDataHora():
    

# %y/%Y - Ano, %a%A - Dia da semana, %b%B - Mês. %d - Dia do mês
    hoje = datetime.now()

    print (hoje.strftime("O ano é: %y"))

#%c - Data e hora da localidade. %x - data da localidade, %X - hora da localidade
    print (hoje.strftime("Data e hora local: %c"))

# %I%H - 12/24 horas, %M - minutos, %S - segundos, %p - AM/PM
    print (hoje.strftime("A hora atual é: %I:%M:%S %p"))

FormataDataHora()