# Chekup
Checkup Challenge
- Mission in a sheet of "Dados2021 vmar22 Envio.xlsx"
- Some data in the workbook "Dados2021 vmar22 Envio.xlsx"
- Some data in "DadosProdutos.xlsx"

To run that aplication, follow the steps:
- Python 3 ou superior pelo site oficial
- Clone a aplicação
- Enter at the cloned directory and open SHELL

Installing Venv (SHELL):
- python -m pip install --upgrade pip
- pip install virtualenv

Creating Virtual Environment for python:
- python3 -m venv CheckupChallenge
- source CheckupChallenge/bin/activate
- pip install -r requirements.txt

Setting up environment:
-Create a '.env' file and put your credentials:
    - HOST=<serverIP|localhost>
    - UID=<user>
    - PASS=<password>

Setting up MySQL Server:
- In the folder begin.sql execute in mysql server "Begin.sql"

More information:
- Relational Model pĺanning at RelationalSchema.txt
- Entity and Relationships diagram at EntityDiagramCheckup.jpg