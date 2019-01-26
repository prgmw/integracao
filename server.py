#https://assinaturas.superlogica.com/hc/pt-br/articles/360008275514-Integra%C3%A7%C3%B5es-via-API

from flask import Flask
app = Flask(__name__)

import pyodbc
import requests

# Fornece uma conexao com o sqlserver
def getDatabaseConnection():
    #SELECT @@SERVERNAME
    server = 'localhost'
    database= 'TestDB'
    username = 'SA'
    password = 'P4ul0m3d3!' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    return cnxn.cursor()

# Teste como obter dados do banco
def testeBuscaBanco():
    #Conexao sqlserver
    cursor = getDatabaseConnection()
    cursor.execute("SELECT * from Inventory;")
    row = cursor.fetchone() 
    while row: 
        print (row)
        row = cursor.fetchone()

def testeInclusaoBanco(name='Teste', quantity='100'):
    # Conexao sqlserver
    cursor = getDatabaseConnection()
    cursor.execute("INSERT INTO Inventory (name, quantity) values ('" + name + "', " + quantity + ");")
    cursor.commit()

# Fornece o header da requisicao
def getHeader():
    return {
        "content-type": "application/json",
        "app_token": "<TOKEN>",
        "access_token": "<TOKEN>"
    }

# Obtem os clientes inadimplentes por id
def getDefaultingClients(ids):
    uri = 'https://api.superlogica.net/v2/financeiro/clientes/inadimplencia?clientes= ' + ids + '1'
    response = requests.get(uri, headers=getHeader())

    if(response.status_code == 200)
        print(response.json)


# Obtem os ids dos clientes superlogica
def getClientsId():
    # Teste como obter dados do banco
    cursor = getDatabaseConnection()
    cursor.execute("SELECT ID from pessoa;")
    row = cursor.fetchone()
    ids = []
    while row:
        print(row)
        ids.push(row)
    return ids

if __name__ == "__main__":
    #testeBuscaBanco()
    testeInclusaoBanco()