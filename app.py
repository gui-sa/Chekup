import mysql.connector
from decouple import config
import pandas as pd

#Getting data from environment (.env)
HOST = config('HOST')
UID = config('UID')
PASS = config('PASS')



read = pd.read_excel(r"Dados2021 vmar22 Envio.xlsx",sheet_name='Vendas')
cliID = read['ID Cliente'].drop_duplicates()

class ExcelToDatabase:
    def __init__(self,HOST:str,UID:str,PASS:str,database='checkup',pathToSheetVmar= r"Dados2021 vmar22 Envio.xlsx",pathToSheetProds= r"DadosProdutos.xlsx") -> None:
        ''' Recebendo arquivos do formato "Dados2021 vmar22 Envio.xlsx" e "DadosProdutos.xlsx"
            Extrai os dados e povoa o banco de dados MySQL. A tabela precisa estar limpa
            Cria um objeto ExcelToDatabaseVmar
        '''
        self.HOST = HOST
        self.UID = UID
        self.PASS = PASS
        self.database = database
        self.pathToSheetVmar = pathToSheetVmar
        self.pathToSheetProds = pathToSheetProds

    def cliente(self)-> None:
        ''' Envia somente os clientes para o banco de dados.\n
            Por Default o nome eh 'teste'... aceita uma lista de nomes contendo o mesmo comprimento que os id.
        '''
        try:
            cnn = mysql.connector.connect(host=self.HOST, user=self.UID, passwd=self.PASS, database=self.database)

        except:
            print("Database has failed to connect")
            exit()
        read = pd.read_excel(self.pathToSheetVmar,sheet_name='Vendas')
        cliID = read['ID Cliente'].drop_duplicates()
        db = cnn.cursor()
        for ID in cliID:
            SQL_ = f"INSERT INTO CLIENTE(id,nome) VALUES ({ID},'teste')"
            db.execute(SQL_)
        cnn.commit() 
        db.close()
        cnn.close()
        print("Datas for CLIENTE has been transfered")

    def grupo(self):
        ''' Envia somente os grupos para o banco de dados.\n
        '''
        try:
            cnn = mysql.connector.connect(host=self.HOST, user=self.UID, passwd=self.PASS, database=self.database)

        except:
            print("Database has failed to connect")
            exit()
        read = pd.read_excel(self.pathToSheetProds,sheet_name='TbProduto')
        
        imposto = read['Imposto']
        grupos = read['Grupo'].drop_duplicates()
        db = cnn.cursor()
        for i in grupos.index:
            SQL_ = f"INSERT INTO GRUPO(nome,imposto) VALUES ('{grupos[i]}',{imposto[i]})"
            db.execute(SQL_)
        cnn.commit() 
        db.close()
        cnn.close()
        print("Datas for GRUPO has been transfered")

    def produto(self):
        ''' Envia somente os pedidos para o banco de dados.\n
        '''
        try:
            cnn = mysql.connector.connect(host=self.HOST, user=self.UID, passwd=self.PASS, database=self.database)

        except:
            print("Database has failed to connect")
            exit()
        read = pd.read_excel(self.pathToSheetVmar,sheet_name='Vendas')
        read2 = pd.read_excel(self.pathToSheetProds,sheet_name='TbProduto')
        
        prodID = read2['ID Produto']
        grupo = read2['Grupo']
        preco = read['ID Cliente']
        db = cnn.cursor()
        for i in range(len(cliID)):
            SQL_ = f"INSERT INTO PEDIDO(codigo,datat,id_cliente) VALUES ('{codigos[i]}','{datas[i]}',{cliID[i]})"
            db.execute(SQL_)
        cnn.commit() 
        db.close()
        cnn.close()
        print("Datas for PEDIDOS has been transfered")

    def meta(self):
        pass

    def pedido(self):
        ''' Envia somente os pedidos para o banco de dados.\n
        '''
        try:
            cnn = mysql.connector.connect(host=self.HOST, user=self.UID, passwd=self.PASS, database=self.database)

        except:
            print("Database has failed to connect")
            exit()
        read = pd.read_excel(self.pathToSheetVmar,sheet_name='Vendas')
        
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
        print("Datas for PEDIDOS has been transfered")


    def transfer(self):
        ''' Transfere todos os dados da planilha para o banco de dados
        '''
        self.cliente()
        self.grupo()
        self.produto()        
        self.meta()        
        self.pedido()        

excel1 = ExcelToDatabase(HOST,UID,PASS)
#excel1.cliente() 
#excel1.grupo()
excel1.produto()
