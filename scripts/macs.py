import MySQLdb
import getpass
import csv

user = 'sklein' # your username
passwd = getpass.getpass('Password: ') # your password
host = 'localhost' # your host
db = 'rhodes' # database where your table is stored
table = 'computers' # table you want to save

con = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
cursor = con.cursor()

query = "select equipment.Type, people.Name, equipment.Name, equipment.Model_ID, equipment.Serial_Num, equipment.price, equipment.ID from equipment join people on equipment.Owner_ID = people.ID where equipment.Name = 'Macbook';"
cursor.execute(query)

with open('export.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(('Type', 'User', 'Brand', 'Model', 'Serial Number', 'Cost', 'Equipment ID'))
    for row in cursor.fetchall():
        #print(row)
        writer.writerow(row)
