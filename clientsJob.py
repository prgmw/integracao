#https://assinaturas.superlogica.com/hc/pt-br/articles/360008275514-Integra%C3%A7%C3%B5es-via-API

from flask import Flask

app = Flask(__name__)

import pyodbc
import requests
import json
from datetime import date


# Dados Acesso Suoerlogica
APP_TOKEN = ""
ACCESS_TOKEN = ""

# Dados Acesso ao banco
server = 'localhost'
database = 'TestDB'
username = 'SA'
password = ''

# Constantes
API_URI = "https://api.superlogica.net/v2/"


# Fornece uma conexao com o sqlserver
def getConexaoBanco():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    return cnxn.cursor()

# Fornece o header da requisicao
def getHeader():
    return {
        "content-type": "application/json",
        "app_token": APP_TOKEN,
        "access_token": ACCESS_TOKEN
    }

# Metodo que realiza o processamento dos clientes
def processarClientes():
    clientesAdimplentes = getClientesAdimplentes()

    for cliente in clientesAdimplentes:
        incluirClienteAdimplente(cliente)

    clientesInadimplentes = getClientesInadimplentes()

     for cliente in clientesInadimplentes:
        incluirClienteInadimplente(cliente)


# Metodo que obtem os clientes adimplentes
def getClientesAdimplentes():
    uri = API_URI + 'financeiro/clientes/adimplentes'
    return obterConteudo(uri)

# Metodo que obtem os clientes inadimplentes
def getClientesInadimplentes():
    uri = API_URI + 'financeiro/clientes/inadimplencia'
    return obterConteudo(uri)

# Metodo para requisicoes GET
def obterConteudo(uri):
    content = []
    response = requests.get(uri, headers=getHeader())

    if response.status_code == 200:
        content = json.loads(response.content)
    return content


# Metodo que Inclui ios clientes adimplentes
def incluirClienteAdimplente(cliente):
    # Conexao sqlserver
    cursor = getConexaoBanco()

    today = date.today().strftime('%m/%d/%Y')
    sql = "INSERT INTO SL_CLIENTES_ADIMPLENTES (id, nome, dia_vencimento, dt_cadastro, dt_congelamento, dt_desativacao, dt_processamento) values ( " + cliente['id_sacado_sac'] + ", '" + cliente['st_nome_sac'] + "', " + cliente['st_diavencimento_sac'] + ", '" + cliente['dt_cadastro_sac'] + "', '" + cliente['dt_congelamento_sac'] + "', '" + cliente['dt_desativacao_sac'] + "', '"  + today +  "' )"

    cursor.execute(sql)
    cursor.commit()


# Metodo que Inclui ios clientes inadimplentes
def incluirClienteInadimplente(cliente):
    # Conexao sqlserver
    cursor = getConexaoBanco()

    today = date.today().strftime('%m/%d/%Y')
 #   sql = "INSERT INTO SL_CLIENTES_ADIMPLENTES (id, nome, dia_vencimento, dt_cadastro, dt_congelamento, dt_desativacao, dt_processamento) values ( " + cliente['id_sacado_sac'] + ", '" + cliente['st_nome_sac'] + "', " + cliente['st_diavencimento_sac'] + ", '" + cliente['dt_cadastro_sac'] + "', '" + cliente['dt_congelamento_sac'] + "', '" + cliente['dt_desativacao_sac'] + "', '"  + today +  "' )"

 #   cursor.execute(sql)
  #  cursor.commit()


# Metodo que obtem os ids dos clientes da superlogica
def getClientes():
    # Teste como obter dados do banco
    cursor = getConexaoBanco()
    cursor.execute("SELECT ID from pessoa;")
    row = cursor.fetchone()
    ids = []
    while row:
        print(row)
        ids.push(row)
    return ids

if __name__ == "__main__":
    processarClientes()
    #TODO: Processar os clientes indadimplentes