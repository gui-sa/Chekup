import mysql.connector
from decouple import config

HOST = config('HOST')
UID = config('UID')
PASS = config('PASS')

try:
    db = mysql.connector.connect(host=HOST, user=UID, passwd=PASS, database="checkup")

except:
    print("Database has failed to connect")
    exit()

print("mySQL Server has been connected")

dbCursor = db.cursor()

dbCursor.execute("drop table teste")
dbCursor.execute("show tables")

