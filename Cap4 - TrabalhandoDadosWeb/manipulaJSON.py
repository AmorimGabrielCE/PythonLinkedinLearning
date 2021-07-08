import urllib.request
import json

def ManipulaJSON():
    endereco = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webURL = urllib.request.urlopen(endereco)
    if webURL.getcode() == 200:
        #Salvando os dados da página
        dados = webURL.read()
        oJSON = json.loads(dados)

        #Contando quantos terremotos ocorreram de acordo com os dados
        contagem = oJSON["metadata"]["count"]
        print("Contagem: " + str(contagem))

        #Mostrando os locais onde ocorreram os terremotos
        #for local in oJSON["features"]:
        #   print(local["properties"]["place"])

        #Mostrando os locais onde ocorreram os terremotos
        for local in oJSON["features"]:
            if local["properties"]["place"] == "74 km WNW of Kalaoa, Hawaii" :
                print("Encontrado registro especial************")
            else:    
                print(local["properties"]["place"])    

ManipulaJSON()