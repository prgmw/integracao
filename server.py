#https://assinaturas.superlogica.com/hc/pt-br/articles/360008275514-Integra%C3%A7%C3%B5es-via-API

from flask import Flask
app = Flask(__name__)

import pyodbc
import requests

# Fornece uma conexao com o sqlserver
def getDatabaseConnection():
    #SELECT @@SERVERNAME
    server = 'paulo-G7-7588'
    database= 'TestDB'
    username = 'SA'
    password = 'P4ul0m3d3!' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    return cnxn.cursor()

# Exemplo de requisicao GET para obter os clientes
def getClients():
    uri = 'https://api.superlogica.net/v2/financeiro/clientes'
    header = {
        "content-type" : "application/json",
        "app_token" : "<TOKEN>",
        "access_token" : "<TOKEN>"
        }
    response = requests.get(uri, headers=header)

# Teste simples com database
def testeBanco():
    #Conexao sqlserver
    cursor = getDatabaseConnection()
    
    cursor.execute("SELECT * from Inventory;")
    row = cursor.fetchone() 
    while row: 
        print (row)
        row = cursor.fetchone()



if __name__ == "__main__":
    testeBanco()    