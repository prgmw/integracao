#https://assinaturas.superlogica.com/hc/pt-br/articles/360008275514-Integra%C3%A7%C3%B5es-via-API

import re
import pyodbc
from datetime import date

class clienteDao:

    # Dados Acesso ao banco
    server = 'localhost'
    database = ''
    username = 'SA'
    password = ''

    # Construtor
    def __init__(self):
        print('Iniciando o Cliente Dao')

    # Fornece uma conexao com o sqlserver
    def _get_conexao_banco(self):
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        return cnxn.cursor()

    # Auxiliar para remover caracteres invalidos
    def _remove_caracteres_especiais(self, termo):
        return re.sub('\W+',' ', termo)

    # Auxiliar para obter data        
    def _get_data(self, data):
        return data if data else None

    # Inclui ios clientes adimplentes
    def incluir_cliente_adimplente(self, cliente):
        # Conexao sqlserver
        cursor = self._get_conexao_banco()
        
        nomeCliente = self._remove_caracteres_especiais(cliente['st_nome_sac'])
        dataHoje = date.today().strftime('%m/%d/%Y')
        dataCadastro = self._get_data(cliente['dt_cadastro_sac'])
        dataCongelamento = self._get_data(cliente['dt_congelamento_sac'])
        dataDesativacao = self._get_data(cliente['dt_desativacao_sac'])

        print('Inserindo Cliente Adimplente >> ' + nomeCliente)

        sql = "INSERT INTO SL_CLIENTES_ADIMPLENTES (cliente_id, nome, dia_vencimento, dt_cadastro, dt_congelamento, dt_desativacao, dt_processamento) values ( ? , ?, ?, ?, ?, ?, ?)"

        cursor.execute(sql, 
            cliente['id_sacado_sac'], 
            nomeCliente, 
            cliente['st_diavencimento_sac'], 
            dataCadastro, 
            dataCongelamento, 
            dataDesativacao, 
            dataHoje)
        
        cursor.commit()

    # Inclui os clientes inadimplentes
    def incluir_cliente_inadimplente(self, cliente):
        # Conexao sqlserver
        cursor = self._get_conexao_banco()
        
        nomeCliente = self._remove_caracteres_especiais(cliente['st_nome_sac'])
        dataHoje = date.today().strftime('%m/%d/%Y')
        dataCadastro = self._get_data(cliente['dt_cadastro_sac'])
        dataCongelamento = self._get_data(cliente['dt_congelamento_sac'])
        dataDesativacao = self._get_data(cliente['dt_desativacao_sac'])

        print('Inserindo Cliente Inadimplente >> ' + nomeCliente)

        sql = "INSERT INTO SL_CLIENTES_INADIMPLENTES (cliente_id, nome, dia_vencimento, dt_cadastro, dt_congelamento, dt_desativacao, dt_processamento) values ( ? , ?, ?, ?, ?, ?, ?)"

        cursor.execute(sql, 
            cliente['id_sacado_sac'], 
            nomeCliente, 
            cliente['st_diavencimento_sac'], 
            dataCadastro, 
            dataCongelamento, 
            dataDesativacao, 
            dataHoje)
        
        cursor.commit()

    # Inclui os recebimentos
    def incluir_cliente_recebimentos(self, recebimento, cliente_id):
        # Conexao sqlserver
        cursor = self._get_conexao_banco()
        
        dataHoje = date.today().strftime('%m/%d/%Y')
        dataGeracao = self._get_data(recebimento['dt_geracao_recb'])
        dataVencimento = self._get_data(recebimento['dt_vencimento_recb'])

        print('Inserindo Recebimentos do cliente >> ' + cliente_id)

        sql = "INSERT INTO SL_CLIENTES_RECEBIMENTOS (cliente_id, recebimento_id, dt_geracao, dt_vencimento, valor, dt_processamento) values (?,?,?,?,?,?)"

        cursor.execute(sql, 
            cliente_id, 
            recebimento['id_recebimento_recb'], 
            dataGeracao, 
            dataVencimento, 
            recebimento['vl_emitido_recb'], 
            dataHoje)
        
        cursor.commit()

    # Limpa as tabelas
    def limpar_tabelas(self):
        # Conexao sqlserver
        cursor = self._get_conexao_banco()

        sql_clientes_adimplentes = 'DELETE FROM SL_CLIENTES_ADIMPLENTES'
        sql_clientes_inadimplentes = 'DELETE FROM SL_CLIENTES_INADIMPLENTES'
        sql_recebimentos = 'DELETE FROM SL_CLIENTES_RECEBIMENTOS'

        cursor.execute(sql_clientes_adimplentes)
        cursor.execute(sql_clientes_inadimplentes)
        cursor.execute(sql_recebimentos)

        cursor.commit()    
