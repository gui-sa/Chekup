# Chekup
Checkup Challenge

To run that aplication, follow the steps:
- Python 3 ou superior pelo site oficial
- Clone a aplicação
- Entrar no diretorio e abrir o SHELL

Installing Venv (SHELL):
- python -m pip install --upgrade pip
- pip install virtualenv

Creating Virtual Environment for python:
- python3 -m venv CheckupChallenge
- source CheckupChallenge/bin/activate
- pip install -r requirements.txt

Setting up environment:
-Create a '.env' file and put your credentials:
    HOST=<serverIP|localhost>
    UID=<user>
    PASS=<password>

Setting up MySQL Server:
- Na pasta Query execute as querys de nome "Begin.sql"