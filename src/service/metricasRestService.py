import requests
import json
from .baseRestService import BaseRestService
from datetime import date

class MetricasRestService(BaseRestService):

    #Construtor
    def __init__(self):
        super().__init__()
        print('Instanciando o Metricas Rest Service')

    # Método que obtem as métricas
    def get_metricas(self, dataExecucao):
        return self.get_metricas_customizado(self.QUANTIDADE_MESES, dataExecucao)

    # Método que obtem as métricas
    def get_metricas_customizado(self, quantidadeMeses, dataExecucao):
        uri = self.API_URI + 'financeiro/metricas?quantidadeMeses=' + str(quantidadeMeses) + ' & dtFim=' + str(dataExecucao)  
        return self.obter_conteudo(uri)
