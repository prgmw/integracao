#https://assinaturas.superlogica.com/hc/pt-br/articles/360008275514-Integra%C3%A7%C3%B5es-via-API

from flask import Flask
app = Flask(__name__)

import pyodbc
import requests

#Conecao com o banco
cursor = configDatabase()

def getCLientToken():
    uri = "https://api.superlogica.net/v2/financeiro/clientes/token"
    requests.post

#Configura banco
def configDatabase():
    server = 'tcp:myserver.database.windows.net' 
    database = 'mydb' 
    username = 'myusername' 
    password = 'mypassword' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    return cnxn.cursor()

# Exemplo para obter os clientes
def getClients():
    uri = 'https://api.superlogica.net/v2/financeiro/clientes'
    header = {
        "content-type" : "application/json",
        "app_token" : "<TOKEN>",
        "access_token" : "<TOKEN>"
        }
    requests.get(uri, headers=header)


if __name__ == "__main__":
    #app.run(host='0.0.0.0')    