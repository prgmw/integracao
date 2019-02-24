#https://assinaturas.superlogica.com/hc/pt-br/articles/360008275514-Integra%C3%A7%C3%B5es-via-API

import sys
import re

from datetime import date, timedelta, datetime
import threading

from service.clientRestService import ClientRestService
from service.metricasRestService import MetricasRestService
from dao.clientDao import ClienteDao
from dao.metricasDao import MetricasDao

class job:

    # Define o número de jobs iniciais sendo:
    # Número de threads iniciais x número de chamadas por endpoint (cada endpoint tem uma thread)
    # Aumentar com cautela para evitar sobrecarga e travamentos no banco e servidor
    threadLimiter = threading.BoundedSemaphore(2)

    # Construtor
    def __init__(self):
        print('Iniciando o Job')

    # Realiza o processamento dos clientes
    def processar(self, data_exec):
        print ('Iniciando o processamento para período ' + data_exec) 

        metricasDao = MetricasDao()
        metricasDao.limpar_tabelas(data_exec)

        clientesDao = ClienteDao()
        clientesDao.limpar_tabelas(data_exec)

        chamadas = [self._processar_metricas, self._processa_clientes_adimplentes, self._processa_clientes_inadimplentes]

        threads = []
        for metodo in chamadas:
            t = threading.Thread(target=metodo, args=(data_exec,))
            threads.append(t)
            t.start()

    def _processar_metricas(self, data_exec):
        metricas = ''
        print('Obtendo as métricas...')

        #criando um objeto MetricasDao
        dao = MetricasDao()
        dao.limpar_tabelas(data_exec)

        # criando um objeto MetricasRestServices
        service = MetricasRestService()
        # Obtendo sa métrica na superlógica
        metricas = service.get_metricas(data_exec)

        for metrica in metricas:
            #Salvando no banco de dados
            dao.incluir_metrica(metrica, data_exec)


    # Processa os clientes adimplentes
    def _processa_clientes_adimplentes(self, data_exec):
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
            aux = service.get_clientes_adimplentes(pagina, data_exec)
            clientesAdimplentes += aux
            condicao = (len(aux) == 150)

            print('Na pagina ' + str(pagina) + ' obteve ' + str(len(aux)) + ' clientes adimplentes')

        print('Existem ' + str(len(clientesAdimplentes)) + ' adimplentes para inserir')

        for cliente in clientesAdimplentes:
            dao.incluir_cliente_adimplente(cliente, data_exec)

    # Processa os clientes inadimplentes
    def _processa_clientes_inadimplentes(self, data_exec):
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
            aux = service.get_clientes_inadimplentes(pagina, data_exec)
            clientes_inadimplentes += aux
            condicao = (len(aux) == 150)

            print('Na pagina ' + str(pagina) + ' obteve ' + str(len(aux)) + ' clientes inadimplentes')

        print('Existem ' + str(len(clientes_inadimplentes)) + ' inadimplentes para inserir')

        for cliente in clientes_inadimplentes:
            dao.incluir_cliente_inadimplente(cliente, data_exec)

            for recebimento in cliente['recebimento']:
                dao.incluir_recebimentos_pendentes(recebimento, cliente['id_sacado_sac'], data_exec)    

                for encargo in recebimento['encargos']:
                    dao.incluir_encargos_recebimentos(encargo, recebimento['id_recebimento_recb'], data_exec)

    # Semaforo para controlar o numero de threads ativas por periodo
    def _run(self, data_exec):
        self.threadLimiter.acquire()
        try:
            print('>>>> Thread ' + str(data_exec) + ' Iniciada')
            self.processar(str(data_exec))
        finally:
            print('>>>> Thread Liberada')
            self.threadLimiter.release()                    

    # Cria as threads
    def _create_threads(self, periodo):
        for data_exec in periodo:
            t = threading.Thread(target=self._run, args=(data_exec,))
            t.start()

#Inicio
if __name__ == "__main__":
    periodo = []

    DATE_PATTERN = '%m/%d/%Y'

    #Obtém data passada por parâmetro
    parametros = sys.argv

    #Se passou apenas uma data
    if (len(parametros) == 2):
        periodo.append(datetime.strptime(str(parametros[1]), DATE_PATTERN))
    
    #Se passou um periodo
    elif (len(parametros) == 3):
        data_inicial = datetime.strptime(str(parametros[1]), DATE_PATTERN)
        data_final   = datetime.strptime(str(parametros[2]), DATE_PATTERN)

        # Popula o array com o range de datas
        periodo = [ data_inicial + timedelta(n) for n in range(int ((data_final - data_inicial).days))]

    else:
        periodo.append(date.today().strftime(DATE_PATTERN))

    #Inicia o processo
    job()._create_threads(periodo)
