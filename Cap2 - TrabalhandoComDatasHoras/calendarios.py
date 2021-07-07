import calendar

#Criando um calendário no formato texto
def CalendarioTexto():
    #Calendário começando pelo Domingo
    calendarioTexto = calendar.TextCalendar(calendar.SUNDAY)
    txtCalendario =  calendarioTexto.formatmonth(2021, 2)
    print(txtCalendario)

#CalendarioTexto()

#Criando um calendário no formato HTML
def CalendarioHTML():
    #Calendário começando pelo Domingo
    calendarioHTML = calendar.HTMLCalendar(calendar.SUNDAY)
    htmlCalendario =  calendarioHTML.formatmonth(2021, 2)
    print(htmlCalendario)

CalendarioHTML()