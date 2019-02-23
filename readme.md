# Requisitos:

```
Python 3
```

# Primeira Instalacão:

1 - sudo apt-get update

2 - sudo apt-get install python3-pip python3-dev nginx

3 - sudo pip3 install virtualenv

## Linux:

5 - virtualenv venv

6 - source venv/bin/activate

7 - sudo apt-get install unixodbc-dev

8 - sudo apt-get install python-pip

9 - pip install pyodbc

10 - sudo pip install requests


# Iniciar Projeto:

1 - cd <Seu-Workspace>/

2 - source venv/bin/activate

3 - cd src

3 - python job.py << parametros >>

## Parametros:
- Rodar para a data atual => python job.py
- Rodar para uma data especifica  => python job.py mm/dd/YYYY
- Rodar para um intervalo de datas (data inicial e data final)  => python job.py mm/dd/YYYY mm/dd/YYYY
