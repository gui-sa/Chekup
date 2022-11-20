# Chekup
CheckUp Medicina e Diagnósticos. TI Challenge:
- Mission in a sheet of "Dados2021 vmar22 Envio.xlsx"
- Some data in the workbook "Dados2021 vmar22 Envio.xlsx"
- Some data in "DadosProdutos.xlsx"

To run that aplication, follow the steps:
- Python 3 ou superior -> oficial web site 
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
- Create a '.env' file and put your credentials:
    - HOST=<serverIP|localhost>
    - UID=<user>
    - PASS=<password>

Setting up MySQL Server:
- In the folder begin.sql execute in mysql server "Begin.sql"

Pushing data from excells file to mysql database:
- Put the excell files into the same directory as the app.py
- Using the SHELL that are using Virtual Environment:
  -  python3 app.py

Opening mysql database(it is recommended to use a workbench), run in Query folder:
- query1.sql : answering the task 1;
- query2.sql : answering the task 2;
- query3.sql : answering the task 3;
- query4.sql : answering the task 4;

More information:
- Relational Model pĺanning at RelationalSchema.txt
- Entity and Relationships diagram at EntityDiagramCheckup.jpg
- query4.csv is a saved answer of task4.
- Checkup Challenge.pdf is the answer document for the challenge.