from html.parser import HTMLParser

#Criando uma classe que herda da HTMLParser para poder exibir mensagens personalizadas
class meuParser(HTMLParser):
    #Substituindo o método que verifica se foi encontrada uma tag de abertura
    def handle_starttag(self, tag, attrs):
        print("Tag de abertura encontrada!")
        if attrs.__len__() > 0:
            for a in attrs:
                print("  Valores encontrados: ", a[0], " = ", a[1])

    #Substituindo o método que manipula a tag de fechamento
    def handle_endtag(self, tag):
        print("Tag de fechamento encontrada!")

    #Substituindo o método que identifica um comentário
    def handle_comment(self, data):
        print("Comentário encontrado!")

    #Substituindo o método que identifica se valores foram encontrados
    def handle_data(self, data):
        print("Valores encontrados!")
        if data.isspace():
            print("O valor encontrado é um espaço")
        else:
            print("O valor encontrado é: ", data)

#Criando uma função que instancia um objeto do tipo meuParser
def meuObjeto():
    meuParser1 = meuParser()
    arquivo = open("C:\\Users\\Amorim\\OneDrive\\Python\\PythonLinkedinLearning\\ArquivosCurso\\exemplohtml.html", "r")
    dados = arquivo.read()
    #Metodo feed vai executar os métodos que foram substituidos
    meuParser1.feed(dados)

meuObjeto()

    
