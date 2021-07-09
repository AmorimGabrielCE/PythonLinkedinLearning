import pymongo
from pymongo import MongoClient

def manipulaDadosMongoDB():
    #Conectando-se ao banco
    cliente = pymongo.MongoClient("mongodb://localhost:27017")
    db = cliente.conheca_python

    #Incluindo documentos no banco de dados
    for i in range(1,10):
        objDic = {'codigo' : i}
        db.conheca_mongodb.insert_one(objDic)

    #Atualizando o documento onde o código é igual a 2
    db.conheca_mongodb.update_one({'codigo' : 2}, {"$set" : {'atributoNovo' : 789}})
    #Excluindo documento com o código 1
    db.conheca_mongodb.delete_one({'codigo' : 1})

    resultadoConsulta = db.conheca_mongodb.find({})
    for doc in resultadoConsulta:
        print(doc)

manipulaDadosMongoDB()