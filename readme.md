# Requisitos:

```
Python 3
SQL Server Database
```

# Primeira Instalacão:

1 - sudo apt-get update

2 - sudo apt-get install python3-pip python3-dev

3 - sudo pip3 install virtualenv

4 - virtualenv venv

5 - source venv/bin/activate

6 - Instalar o driver do banco => ( https://docs.microsoft.com/pt-br/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017 )

7 - pip3 install pyodbc

8 - pip3 install requests

9 - Execute o(s) script(s) SQL contidos na pasta **SQL** no banco de dados.


# Iniciar Projeto:

1 - cd << Seu-Workspace >> /

2 - source venv/bin/activate

3 - cd src

3 - python job.py << parametros >>

## Parametros:
- Rodar para a data atual => python job.py
- Rodar para uma data especifica  => python job.py mm/dd/YYYY
- Rodar para um intervalo de datas (data inicial e data final)  => python job.py mm/dd/YYYY mm/dd/YYYY
