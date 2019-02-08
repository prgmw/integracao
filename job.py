#https://assinaturas.superlogica.com/hc/pt-br/articles/360008275514-Integra%C3%A7%C3%B5es-via-API

import re

import clientRestService
import clientDao

class job:

    # Construtor
    def __init__(self):
        print('Iniciando o Job')

    # Realiza o processamento dos clientes
    def processar(self):
        print ('Iniciando o processamento dos clientes...')

        dao = clientDao.clienteDao()
        dao.limpar_tabelas()
        
        self._processa_clientes_adimplentes()
        self._processa_clientes_inadimplentes()

    # Processa os clientes adimplentes
    def _processa_clientes_adimplentes(self):
        clientesAdimplentes = []
        print('Obtendo os adimplentes...')

        dao = clientDao.clienteDao()
        service = clientRestService.ClientRestService()

        condicao = True
        pagina = 0

        # Enquanto retornar 50 clientes
        while (condicao):
            print('Requisitando...')

            pagina += 1
            aux = service.get_clientes_adimplentes(pagina)
            clientesAdimplentes += aux
            condicao = (len(aux) == 50)

            print('Na pagina ' + str(pagina) + ' obteve ' + str(len(aux)) + ' clientes adimplentes')

        print('Existem ' + str(len(clientesAdimplentes)) + ' adimplentes para inserir')

        for cliente in clientesAdimplentes:
            dao.incluir_cliente_adimplente(cliente)

    # Processa os clientes inadimplentes
    def _processa_clientes_inadimplentes(self):
        clientes_inadimplentes = []
        print('Obtendo os inadimplentes...')

        dao = clientDao.clienteDao()
        service = clientRestService.ClientRestService()

        condicao = True
        pagina = 0

        # Enquanto retornar 50 clientes
        while (condicao):
            print('Requisitando...')

            pagina += 1
            aux = service.get_clientes_inadimplentes(pagina)
            clientes_inadimplentes += aux
            condicao = (len(aux) == 50)

            print('Na pagina ' + str(pagina) + ' obteve ' + str(len(aux)) + ' clientes inadimplentes')

        print('Existem ' + str(len(clientes_inadimplentes)) + ' inadimplentes para inserir')

        for cliente in clientes_inadimplentes:
            dao.incluir_cliente_inadimplente(cliente)
            
            for recebimento in cliente['recebimento']:
                dao.incluir_cliente_recebimentos(recebimento, cliente['id_sacado_sac'])    
            
if __name__ == "__main__":
    job = job()
    job.processar()
