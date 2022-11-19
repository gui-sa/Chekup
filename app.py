import mysql.connector
from decouple import config
import pandas as pd

#Getting data from environment (.env)
HOST = config('HOST')
UID = config('UID')
PASS = config('PASS')



read = pd.read_excel(r"Dados2021 vmar22 Envio.xlsx",sheet_name='Vendas')
cliID = read['ID Cliente'].drop_duplicates()

class ExcelToDatabaseVmar:
    def __init__(self,HOST:str,UID:str,PASS:str,database='checkup',pathToSheet= r"Dados2021 vmar22 Envio.xlsx") -> None:
        ''' Recebe arquivo do formato "Dados2021 vmar22 Envio.xlsx"
            Cria um objeto ExcelToDatabaseVmar
        '''
        self.HOST = HOST
        self.UID = UID
        self.PASS = PASS
        self.database = database
        self.pathToSheet = pathToSheet

    def cliente(self)-> None:
        ''' Envia somente os clientes para o banco de dados.\n
            Por Default o nome eh 'teste'... aceita uma lista de nomes contendo o mesmo comprimento que os id.
        '''
        try:
            cnn = mysql.connector.connect(host=self.HOST, user=self.UID, passwd=self.PASS, database=self.database)

        except:
            print("Database has failed to connect")
            exit()
        read = pd.read_excel(self.pathToSheet,sheet_name='Vendas')
        cliID = read['ID Cliente'].drop_duplicates()
        db = cnn.cursor()
        for ID in cliID:
            SQL_ = f"INSERT INTO CLIENTE(id,nome) VALUES ({ID},'teste')"
            db.execute(SQL_)
        cnn.commit() 
        db.close()
        cnn.close()

    def pedido(self):
        ''' Envia somente os pedidos para o banco de dados.\n
        '''
        try:
            cnn = mysql.connector.connect(host=self.HOST, user=self.UID, passwd=self.PASS, database=self.database)

        except:
            print("Database has failed to connect")
            exit()
        read = pd.read_excel(self.pathToSheet,sheet_name='Vendas')
        
        codigos = read['Pedido']
        datas = read['Data']
        cliID = read['ID Cliente']
        db = cnn.cursor()
        for i in range(len(cliID)):
            SQL_ = f"INSERT INTO PEDIDO(codigo,datat,id_cliente) VALUES ('{codigos[i]}','{datas[i]}',{cliID[i]})"
            db.execute(SQL_)
        cnn.commit() 
        db.close()
        cnn.close()

    def transfer(self):
        ''' Transfere todos os dados da planilha para o banco de dados
        '''
        self.cliente()        
        self.pedido()        

excel1 = ExcelToDatabaseVmar(HOST,UID,PASS)
#excel1.cliente() 
#excel1.pedido()
excel1.transfer()