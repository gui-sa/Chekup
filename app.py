import mysql.connector
from decouple import config

#Getting data from environment (.env)
HOST = config('HOST')
UID = config('UID')
PASS = config('PASS')

class database:
    def __init__(self,HOST:str,UID:str,PASS:str,DATABASE="checkup") -> object:
        ''' Handles Datbase Server Connection\n
            Receives HOST IP or localhost\n
            Receives UID, user name with right credential\n
            Receives PASS, its users password\n
            Receives DATABASE, inside it, which database is the target\n
            Returns database object\n
        '''
        self.HOST = HOST
        self.UID = UID
        self.PASS = PASS
        self.DATABASE = DATABASE
            

    def connect(self)->object:
        ''' Try connection with the SQL SERVER\n
            If sucess returns a cursor for execution handling\n
            If fail returns -1 integer\n
        '''
        try:
            db = mysql.connector.connect(host=HOST, user=UID, passwd=PASS, database="checkup")

        except:
            print("Database has failed to connect")
            return -1

        print("MySQL Server has been connected")

        return db.cursor()


db = database(HOST,UID,PASS).connect()