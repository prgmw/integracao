#https://assinaturas.superlogica.com/hc/pt-br/articles/360008275514-Integra%C3%A7%C3%B5es-via-API

import sys
import re
from datetime import date
import threading

from service.clientRestService import ClientRestService
from dao.clientDao import ClienteDao

class job:

    # Construtor
    def __init__(self):
        print('Iniciando o Job')

    # Realiza o processamento dos clientes
    def processar(self, dataExecucao):
        print ('Iniciando o processamento para período ' + dataExecucao) 

        dao = ClienteDao()
        dao.limpar_tabelas(dataExecucao)

        chamadas = [self._processa_clientes_adimplentes, self._processa_clientes_inadimplentes]

        threads = []
        for metodo in chamadas:
            t = threading.Thread(target=metodo, args=(dataExecucao,))
            threads.append(t)
            t.start()
            print ('Iniciando uma Thread...')

    # Processa os clientes adimplentes
    def _processa_clientes_adimplentes(self, dataExecucao):
        clientesAdimplentes = []
        print('Obtendo os adimplentes...')

        # criando um objeto ClienteDao
        dao = ClienteDao()
        # criando um objeto ClienteRestService
        service = ClientRestService()

        condicao = True
        pagina = 0

        # Enquanto retornar 150 clientes
        while (condicao):
            print('Requisitando...')

            pagina += 1
            aux = service.get_clientes_adimplentes(pagina, dataExecucao)
            clientesAdimplentes += aux
            condicao = (len(aux) == 150)

            print('Na pagina ' + str(pagina) + ' obteve ' + str(len(aux)) + ' clientes adimplentes')

        print('Existem ' + str(len(clientesAdimplentes)) + ' adimplentes para inserir')

        for cliente in clientesAdimplentes:
            dao.incluir_cliente_adimplente(cliente, dataExecucao)

    # Processa os clientes inadimplentes
    def _processa_clientes_inadimplentes(self, dataExecucao):
        clientes_inadimplentes = []
        print('Obtendo os inadimplentes...')

        # criando um objeto ClienteDao
        dao = ClienteDao()
        # criando um objeto ClienteRestService
        service = ClientRestService()

        condicao = True
        pagina = 0

        # Enquanto retornar 150 clientes
        while (condicao):
            print('Requisitando...')

            pagina += 1
            aux = service.get_clientes_inadimplentes(pagina, dataExecucao)
            clientes_inadimplentes += aux
            condicao = (len(aux) == 150)

            print('Na pagina ' + str(pagina) + ' obteve ' + str(len(aux)) + ' clientes inadimplentes')

        print('Existem ' + str(len(clientes_inadimplentes)) + ' inadimplentes para inserir')

        for cliente in clientes_inadimplentes:
            dao.incluir_cliente_inadimplente(cliente, dataExecucao)

            for recebimento in cliente['recebimento']:
                dao.incluir_recebimentos_pendentes(recebimento, cliente['id_sacado_sac'], dataExecucao)    

                for encargo in recebimento['encargos']:
                    dao.incluir_encargos_recebimentos(encargo, recebimento['id_recebimento_recb'], dataExecucao)

#Inicio
if __name__ == "__main__":
    #Obtém data passada por parâmetro
    parametros = sys.argv

    #Se não foi passada a data por parâmetro, então usa a data atual
    dataExecucao = parametros[1] if len(parametros) == 2 else date.today().strftime('%m/%d/%Y')

    job = job()

    job.processar(dataExecucao)
