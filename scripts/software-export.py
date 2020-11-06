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

query = "select people.id, people.Name, software.Name, software.Type, software.License, software.price, software.status, software.annual, software.purchased_date from software join people on software.Owner_ID = people.ID;"
cursor.execute(query)

with open('export.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(('Person ID', 'User', 'Software', 'Type', 'License', 'Cost', 'Status', 'Annual Cost', 'Date Purchased'))
    for row in cursor.fetchall():
        #print(row)
        writer.writerow(row)
