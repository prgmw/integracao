#https://assinaturas.superlogica.com/hc/pt-br/articles/360008275514-Integra%C3%A7%C3%B5es-via-API

import re
import pyodbc
from datetime import date

class BaseDao:

    # Dados Acesso ao banco
    server = ''
    database = ''
    username = ''
    password = ''

    # Construtor
    def __init__(self):
        print('Iniciando o Dao')

    # Fornece uma conexao com o sqlserver
    def get_conexao_banco(self):
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        return cnxn.cursor()

    # Auxiliar para remover caracteres invalidos
    def remove_caracteres_especiais(self, termo):
        return re.sub('\W+',' ', termo)

    # Auxiliar para obter data        
    def get_data(self, data):
        return data if data else None

    # Limpa tabela
    def limpar_tabela(self, query, dataExecucao):
        # Conexao sqlserver
        cursor = self.get_conexao_banco()
        cursor.execute(query, dataExecucao)
      
        cursor.commit()    
