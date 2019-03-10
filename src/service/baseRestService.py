import requests
import json
from datetime import date

class BaseRestService:

    # Dados Acesso Superlogica
    APP_TOKEN = ""
    ACCESS_TOKEN = ""

    # Constantes
    API_URI = "https://api.superlogica.net/v2/"
    ITENS_PAGINA = 150
    QUANTIDADE_MESES = 1

    #Construtor
    def __init__(self):
        print('Instanciando o Base Rest Service')

    # Fornece a data de hoje
    def get_data(self):
        return date.today().strftime('%m/%d/%Y')

    # Fornece o header da requisicao
    def get_header(self):
        return {
            "content-type": "application/json",
            "app_token": self.APP_TOKEN,
            "access_token": self.ACCESS_TOKEN
        }

    # Método para requisicoes GET
    def obter_conteudo(self, uri):
        content = []
        response = requests.get(uri, headers=self.get_header())

        if response.status_code == 200:
            content = json.loads(response.content.decode('utf-8'))
        return content
  
