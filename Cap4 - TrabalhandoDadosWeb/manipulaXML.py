import xml.dom.minidom

def manipulaXML():
    #Criando objeto com os dados do arquivo XML
    doc = xml.dom.minidom.parse("C:\\Users\\Amorim\\OneDrive\\Python\\PythonLinkedinLearning\\ArquivosCurso\\exemploXML.xml")

    print("Nome da primeira tag: ", str(doc.firstChild.tagName))
    #Este comando retorna um array com todas ocorrências da tag
    primeiroNome = doc.getElementsByTagName("firstname")
    print("O primeiro nome é: ", primeiroNome[0].firstChild.nodeValue)

    for skill in doc.getElementsByTagName("skill"):
        print("Skill encontrado: ", skill.getAttribute("name"))

manipulaXML()