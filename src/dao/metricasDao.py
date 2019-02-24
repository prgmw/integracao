
import re
import pyodbc
from .baseDao import BaseDao

from datetime import date

class MetricasDao(BaseDao):

    # Construtor
    def __init__(self):
        super().__init__()
        print('Iniciando o Métricas Dao')

    # Inclui as métrica
    def incluir_metrica(self, metrica, dataExecucao):
        # Conexao sqlserver
        cursor = self.get_conexao_banco()
        
        dataReal = self.get_data(metrica['datareal'])

        print('Inserindo Métricas do data >> ' + dataExecucao)

        sql = (
            "INSERT INTO SL_METRICAS ( " 
            " dt_real, "
            " conquistadas, "
            " desativadas, "
            " liquido, " 
            " clientes_conquistados, "
            " clientes_reativados, "
            " clientes_desativados, "
            " assinaturas_conquistadas, "
            " migracao_conquistadas, "
            " migracao_assinaturas_conquistadas, "
            " assinaturas_desativadas, "
            " migracao_desativadas, "
            " migracao_assinaturas_desativadas, "
            " assinaturas_contraidas, "
            " assinaturas_expandidas, "
            " conquistadas_liquido, "
            " desativadas_liquido, "
            " clientes, "
            " assinaturas, "
            " ticket, "
            " churn_mrr, "
            " grow_mrr, "
            " churn, "
            " grow, "
            " mrr, "
            " ltv, "
            " lt, "
            " churn_corrigido, "
            " churn_corrigido_valor, "
            " arr, "
            " boleto, "
            " cartao_credito, "
            " debito_auto, "
            " net_mrr, "
            " net_mrr_percentual, "
            " dt_processamento ) "
            " values ( ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ?, ?, ?, ?, ?, ?, ? , ?, ?, ?, ?, ?, ?, ? , ?, ?, ?, ?, ?, ?)")

        cursor.execute(sql, 
            dataReal, 
            metrica['conquistadas'], 
            metrica['desativadas'], 
            metrica['liquido'], 
            metrica['clientes conquistados'], 
            metrica['clientes reativados'],
            metrica['clientes desativados'], 
            metrica['assinaturas_conquistadas'], 
            metrica['migracao_conquistadas'], 
            metrica['migracao_assinaturas_conquistadas'],
            metrica['assinaturas_desativadas'], 
            metrica['migracao_desativadas'], 
            metrica['migracao_assinaturas_desativadas'], 
            metrica['assinaturas_contraidas'],
            metrica['assinaturas_expandidas'], 
            metrica['conquistadas_liquido'], 
            metrica['desativadas_liquido'], 
            metrica['clientes'],
            metrica['assinaturas'], 
            metrica['ticket'],
            metrica['churn mrr'],
            metrica['grow mrr'],
            metrica['churn'],
            metrica['grow'],
            metrica['mrr'],
            metrica['ltv'],
            metrica['lt'],
            metrica['churn_corrigido'],
            metrica['churn_corrigido_valor'],
            metrica['arr'],
            metrica['boleto'],
            metrica['cartao de credito'],
            metrica['debito automatico'],
            metrica['net_mrr'],
            metrica['net_mrr_percentual'],
            dataExecucao)
        
        cursor.commit()


    # Limpa as tabelas
    def limpar_tabelas(self, dataExecucao):
        sql_metricas = 'DELETE FROM SL_METRICAS WHERE dt_processamento = ?'    
        self.limpar_tabela(sql_metricas, dataExecucao)
