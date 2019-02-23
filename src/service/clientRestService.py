import requests
import json
from .baseRestService import BaseRestService
from datetime import date

class ClientRestService(BaseRestService):

    #Construtor
    def __init__(self):
        super().__init__()
        print('Instanciando o Client Rest Service')

    # Método que obtem os clientes adimplentes
    def get_clientes_adimplentes(self, pagina, dataExecucao):
        return self.get_clientes_adimplentes_customizado(pagina, self.ITENS_PAGINA, dataExecucao)

    # Método que obtem os clientes adimplentes.
    def get_clientes_adimplentes_customizado(self, pagina, itensPagina, dataExecucao):
        uri = self.API_URI + 'financeiro/clientes/adimplentes?pagina=' + str(pagina) + ' & itensPorPagina=' + str(itensPagina) + ' & posicaoEm=' + str(dataExecucao)  
        return self.obter_conteudo(uri, pagina)

    # Método que obtem os clientes inadimplentes
    def get_clientes_inadimplentes(self, pagina, dataExecucao):
        return self.get_clientes_inadimplentes_customizado(pagina, self.ITENS_PAGINA, dataExecucao)

    # Método que obtem os clientes inadimplentes
    def get_clientes_inadimplentes_customizado(self, pagina, itensPagina, dataExecucao):
        uri = self.API_URI + 'financeiro/clientes/inadimplencia?pagina=' + str(pagina) + ' & itensPorPagina=' + str(itensPagina) + ' & posicaoEm=' + str(dataExecucao) 
        return self.obter_conteudo(uri, pagina)    

