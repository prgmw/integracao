import requests
import json

class ClientRestService:

    # Dados Acesso Superlogica
    APP_TOKEN = ""
    ACCESS_TOKEN = ""

    # Constantes
    API_URI = "https://api.superlogica.net/v2/"

    #Construtor
    def __init__(self):
        print('Instanciando o Rest Service')

    # Fornece o header da requisicao
    def _get_header(self):
        return {
            "content-type": "application/json",
            "app_token": self.APP_TOKEN,
            "access_token": self.ACCESS_TOKEN
        }
        
    # Metodo que obtem os clientes adimplentes
    def get_clientes_adimplentes(self, pagina):
        uri = self.API_URI + 'financeiro/clientes/adimplentes?pagina=' + str(pagina)
        return self._obter_conteudo(uri, pagina)

    # Metodo que obtem os clientes inadimplentes
    def get_clientes_inadimplentes(self, pagina):
        uri = self.API_URI + 'financeiro/clientes/inadimplencia?pagina=' + str(pagina) 
        return self._obter_conteudo(uri, pagina)

    # Metodo para requisicoes GET
    def _obter_conteudo(self, uri, pagina):
        content = []
        response = requests.get(uri, headers=self._get_header())

        if response.status_code == 200:
            content = json.loads(response.content)
        return content
