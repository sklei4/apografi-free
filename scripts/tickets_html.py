import mysql.connector

cd='2019-04-15'

def query_mysql(query):
	cnx = mysql.connector.connect(user='sklein', password='n0t_aLL0wed',
								  host='localhost',
								  database='rhodes', use_unicode = True)
	cursor = cnx.cursor()
	cursor.execute(query)
	#get header and rows
	header = [i[0] for i in cursor.description]
	rows = [list(i) for i in cursor.fetchall()]
	#append header to rows
	rows.insert(0,header)
	cursor.close()
	cnx.close()
	return rows
 
#take list of lists as argument	
def nlist_to_html(list2d):
	#bold header
	htable=u'<table border="1" bordercolor=000000 cellspacing="0" cellpadding="1" style="table-layout:fixed;vertical-align:bottom;font-size:13px;font-family:verdana,sans,sans-serif;border-collapse:collapse;border:1px solid rgb(130,130,130)" >'
	list2d[0] = [u'<b>' + i + u'</b>' for i in list2d[0]] 
	for row in list2d:
		newrow = u'<tr>' 
		newrow += u'<td align="left" style="padding:1px 4px">'+str(row[0])+u'</td>'
		row.remove(row[0])
		newrow = newrow + ''.join([u'<td align="right" style="padding:1px 4px">' + str(x) + u'</td>' for x in row])  
		newrow += '</tr>' 
		htable+= newrow
	htable += '</table>'
	return htable



def sql_html(query):
	return nlist_to_html(query_mysql(query))

#usage example
print("<h2>Opened Tickets</h2>")
query = "select tickets.category as Category, tickets.title as Request, people.name as Person, tickets.created as Opened from tickets join people on tickets.requester = people.id where created > '"+ cd  +"';"
print(sql_html(query))
query = "select count(*) from tickets where created > '"+ cd  +"';"
print(sql_html(query))
print("<h2>System Administration</h2>")
query = "select count(*) from tickets where Category = 'System Administration' and created > '"+ cd  +"';"
print(sql_html(query))
print("<h2>Network</h2>")
query = "select count(*) from tickets where Category = 'Network' and created > '"+ cd  +"';"
print(sql_html(query))
print("<h2>Desktop</h2>")
query = "select count(*) from tickets where Category = 'Desktop' and created > '"+ cd  +"';"
print(sql_html(query))
print("<h2>Closed Tickets</h2>")
query = "select tickets.category as Category, tickets.title as Request, people.name as Person, tickets.created as Opened, tickets.modified as Modified from tickets join people on tickets.requester = people.id where modified and tickets.status = 4 > '"+ cd  +"';"
print(sql_html(query))
query = "select count(*) from tickets where modified > '"+ cd  +"';"
print(sql_html(query))
