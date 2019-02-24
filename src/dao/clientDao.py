#https://assinaturas.superlogica.com/hc/pt-br/articles/360008275514-Integra%C3%A7%C3%B5es-via-API

import re
import pyodbc
from .baseDao import BaseDao

from datetime import date

class ClienteDao(BaseDao):

    # Construtor
    def __init__(self):
        super().__init__()
        print('Iniciando o Cliente Dao')

    # Inclui ios clientes adimplentes
    def incluir_cliente_adimplente(self, cliente, dataExecucao):
        # Conexao sqlserver
        cursor = self.get_conexao_banco()
        
        nomeCliente = self.remove_caracteres_especiais(cliente['st_nome_sac'])
        dataCadastro = self.get_data(cliente['dt_cadastro_sac'])
        dataCongelamento = self.get_data(cliente['dt_congelamento_sac'])
        dataDesativacao = self.get_data(cliente['dt_desativacao_sac'])

        print('Inserindo Cliente Adimplente >> ' + nomeCliente)

        sql = (
            "INSERT INTO SL_CLI_ADIMPLENTES ( "
                " cliente_id, " 
                " nome, "
                " dia_vencimento, "
                " dt_cadastro, "
                " dt_congelamento, "
                " dt_desativacao, "
                " dt_processamento) "
            " values ( ? , ?, ?, ?, ?, ?, ?)")

        cursor.execute(sql, 
            cliente['id_sacado_sac'], 
            nomeCliente, 
            cliente['st_diavencimento_sac'], 
            dataCadastro, 
            dataCongelamento, 
            dataDesativacao, 
            dataExecucao)
        
        cursor.commit()

    # Inclui os clientes inadimplentes
    def incluir_cliente_inadimplente(self, cliente, dataExecucao):
        # Conexao sqlserver
        cursor = self.get_conexao_banco()
        
        nomeCliente = self.remove_caracteres_especiais(cliente['st_nome_sac'])
        dataCadastro = self.get_data(cliente['dt_cadastro_sac'])
        dataCongelamento = self.get_data(cliente['dt_congelamento_sac'])
        dataDesativacao = self.get_data(cliente['dt_desativacao_sac'])

        print('Inserindo Cliente Inadimplente >> ' + nomeCliente)

        sql = (
            "INSERT INTO SL_CLI_INADIMPLENTES ( "
                " cliente_id, "
                " nome, " 
                " dia_vencimento, " 
                " dt_cadastro, " 
                " dt_congelamento, " 
                " dt_desativacao, " 
                " dt_processamento) "
            " values ( ? , ?, ?, ?, ?, ?, ?)")

        cursor.execute(sql, 
            cliente['id_sacado_sac'], 
            nomeCliente, 
            cliente['st_diavencimento_sac'], 
            dataCadastro, 
            dataCongelamento, 
            dataDesativacao, 
            dataExecucao)
        
        cursor.commit()

    # Inclui os encargos dos recebimentos
    def incluir_encargos_recebimentos(self, encargo, recebimento_id, dataExecucao):
        # Conexao sqlserver
        cursor = self.get_conexao_banco()
        
        print('Inserindo Encargos dos Recebimentos >> ' + recebimento_id)

        sql = (
            "INSERT INTO SL_CLI_RECEBIMENTOS_ENCARGOS ("
                " recebimento_id, " 
                " valor_corrigido, "
                " dias_atraso, "
                " dt_processamento) "
            " values (?,?,?,?)")

        cursor.execute(sql, 
            recebimento_id,
            encargo['valorcorrigido'],
            encargo['diasatraso'],
            dataExecucao)
        
        cursor.commit()

    # Inclui os recebimentos
    def incluir_recebimentos_pendentes(self, recebimento, cliente_id, dataExecucao):
        # Conexao sqlserver
        cursor = self.get_conexao_banco()

        dataGeracao = self.get_data(recebimento['dt_geracao_recb'])
        dataVencimento = self.get_data(recebimento['dt_vencimento_recb'])

        print('Inserindo Recebimentos do cliente >> ' + cliente_id)

        sql =  (
            "INSERT INTO SL_CLI_INADIMPLENTES_RECEBIMENTOS ("
                " cliente_id, "
                " recebimento_id, "
                " dt_geracao, " 
                " dt_vencimento, "
                " valor, "
                " dt_processamento) "
            " values (?,?,?,?,?,?)")

        cursor.execute(sql,
                        cliente_id,
                        recebimento['id_recebimento_recb'],
                        dataGeracao,
                        dataVencimento,
                        recebimento['vl_emitido_recb'],
                        dataExecucao)

        cursor.commit()


    # Limpa as tabelas
    def limpar_tabelas(self, dataExecucao):

        sql_clientes_adimplentes = 'DELETE FROM SL_CLI_ADIMPLENTES WHERE dt_processamento = ?'
        sql_clientes_inadimplentes = 'DELETE FROM SL_CLI_INADIMPLENTES WHERE dt_processamento = ?'
        sql_recebimentos = 'DELETE FROM SL_CLI_INADIMPLENTES_RECEBIMENTOS WHERE dt_processamento = ?'
        sql_recebimentos_encargos = 'DELETE FROM SL_CLI_RECEBIMENTOS_ENCARGOS WHERE dt_processamento = ?'

        self.limpar_tabela(sql_clientes_adimplentes, dataExecucao)
        self.limpar_tabela(sql_clientes_inadimplentes, dataExecucao)
        self.limpar_tabela(sql_recebimentos, dataExecucao)
        self.limpar_tabela(sql_recebimentos_encargos, dataExecucao)
