import mysql.connector
import time
import datetime
import getpass
import os

from __main__ import *

__author__ = "Sam Klein"
__software__ = "Rhodes Ticket Manager"
__version__ = "r0-mac-a.01-tck.py"
__project__ = "https://gitlab.com/sklein/rhodes"

def prompt():
	os.system('cls' if os.name == 'nt' else 'clear')
	pointer = input(" 1. Create Ticket \n 2. Active Tickets \n 3. Export Tickets \n 4. Show Completed Tickets \n --- \n Select: ")
	if pointer == "1":
		os.system('cls' if os.name == 'nt' else 'clear')
		print("CREATING TICKET")
		prompt_add_general_ticket()
	elif pointer == "2":
		os.system('cls' if os.name == 'nt' else 'clear')
		print("PREVIEWING ACTIVE TICKETS")
		prompt_update_general_ticket()
	elif pointer == "3":
		os.system('cls' if os.name == 'nt' else 'clear')
		print("EXPORTING TICKETS")
		#export_general_ticket()
	elif pointer == "005":
		os.system('cls' if os.name == 'nt' else 'clear')
		print("DEBUGGING: FIXING TICKET ISSUES")
		fix_all_tickets_request()
	else:
		main()

def add_ticket(tkt_id, tkt_cd, tkt_du, tkt_ca, tkt_tl, tkt_rs, tkt_rq, tkt_ev, tkt_st):
	add="insert into tickets values ('" + str(tkt_id) + "', '" + tkt_cd + "', '" + tkt_du + "', '" + tkt_cd + "', '" + tkt_ca + "', '" + tkt_tl + "', '" + tkt_rq + "', '" + tkt_rs + "', '" + tkt_ev + "', '" + tkt_st +"');"
	ex_co(add)

def check_owner():
	pointer = input("See list of people in database?")
	if pointer == "yes":
		show_people_by_row()
	print("If the person is new, type new.")
	eq_na=input("")
	if eq_na == "new":
		prompt_add_person_from_equipment()
		return str(count_people() - 1)
	else:
		print("Adding person ID " + eq_na + ".")
		return eq_na

def clean_count(myresult):
	for row in myresult:
		output=''.join(str(x) for x in row)
	return int(output)

def count_comments():
	mycursor.execute('select count(ID) from comments;')
	return clean_count(mycursor.fetchall())

def count_tickets():
	mycursor.execute('select count(ID) from tickets;')
	return clean_count(mycursor.fetchall())

def fix_all_tickets_request():
	mycursor.execute("select * from tickets")
	search_and_fix_request()

def fix_ticket_request(ticket_id, ticket_req, ticket_res):
	alter_request="update tickets set tickets.Requester = " + str(ticket_res) + " where tickets.ID = " + str(ticket_id) +  ";"
	ex_co(alter_request)
	print(alter_request)
	alter_respond="update tickets set tickets.Responder = " + str(ticket_req) + " where tickets.ID = " + str(ticket_id) + ";"
	ex_co(alter_respond)
	print(alter_respond)

def ex_co(query):
	print(query)
	mycursor.execute(query)
	mydb.commit()

def export_general_ticket():
	print("test")

def prompt_add_general_ticket():
	print('Is this a ticket made today?')
	choice = input()
	if (choice == "no"):
		print("Date: (Example, 2008-07-23)")
		tk_cd = input()
		tk_cd = str(tk_cd)+ " 00:00:01"
		print("Due date:")
		tk_du = input()
		tk_du = str(tk_du) + " 00:00:01"
	else:
		tk_cd = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
		tk_du = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	tk_id = count_tickets()
	print('Please record values for the following prompts.')
	tk_ca = input('Category: ')
	tk_tl = input('Title: ')
	print('Who made the request?')
	tk_rs = str(check_owner())
	print('Who is responding?')
	tk_rq = str(check_owner())
	print('Elevation:')
	print('0 = Low')
	print('1 = Medium')
	print('2 = High')
	print('3 = Immediate')
	tk_el = str(int(input()))
	print('Status:')
	print('0 = New')
	print('1 = In Progress')
	print('2 = Follow Up')
	print('3 = On Hold')
	print('4 = Complete')
	tk_st = str(int(input()))
	add_ticket(tk_id, tk_cd, tk_du, tk_ca, tk_tl, tk_rs, tk_rq, tk_el, tk_st)

def prompt_update_general_ticket():
	print('NEW: ')
	show_new_tickets_by_id()
	print('IN PROGRESS: ')
	show_inprogress_tickets_by_id()
	print('FOLLOW UP: ')
	show_followup_tickets_by_id()
	print('ON HOLD: ')
	show_hold_tickets_by_id()
	tkt_id = input('Select ID from active tickets.')
	option = input(' 1. Add Comment \n 2. Modify Ticket \n --- \n Select:')
	if (option == "1"):
		update_ticket_comment(tkt_id)
	elif (option == "2"):
		print('Status:')
		print('0 = New')
		print('1 = In Progress')
		print('2 = Follow Up')
		print('3 = On Hold')
		print('4 = Complete')
		tkt_st = str(int(input()))
		update_ticket_status(tkt_id, tkt_st)
	else:
		prompt_update_general_ticket()

def search_and_fix_request():
	data = mycursor.fetchall()
	for row in data:
		fix_ticket_request(row[0], row[6], row[5])

def show_data_by_row0_row1():
	data = mycursor.fetchall()
	for row in data:
		print(row[0], '- ', row[1])

def show_data_by_row0_row1_row2():
	data = mycursor.fetchall()
	for row in data:
		print(row[0], row[1], '- ', row[2])

def show_data_by_row0_row1_row2_row3():
	data = mycursor.fetchall()
	for row in data:
		print(row[0], '\t', row[1], 'requested by', row[2], 'on', row[3])

def show_people_by_row():
	mycursor.execute('select * from people;')
	show_data_by_row0_row1()

def show_complete_tickets_by_id():
	mycursor.execute("select tickets.id, tickets.title, people.name, tickets.created from tickets join people on tickets.requester = people.id where status = '4';")
	show_data_by_row0_row1_row2_row3()

def show_followup_tickets_by_id():
	mycursor.execute("select tickets.id, tickets.title, people.name, tickets.created from tickets join people on tickets.requester = people.id where status = '2';")
	show_data_by_row0_row1_row2_row3()

def show_hold_tickets_by_id():
	mycursor.execute("select tickets.id, tickets.title, people.name, tickets.created from tickets join people on tickets.requester = people.id where status = '3';")
	show_data_by_row0_row1_row2_row3()

def show_inprogress_tickets_by_id():
	mycursor.execute("select tickets.id, tickets.title, people.name, tickets.created from tickets join people on tickets.requester = people.id where status = '1';")
	show_data_by_row0_row1_row2_row3()

def show_new_tickets_by_id():
	mycursor.execute("select tickets.id, tickets.title, people.name, tickets.created from tickets join people on tickets.requester = people.id where status = '0';")
	show_data_by_row0_row1_row2_row3()

def update_ticket_comment(tk_id):
	com_id = count_comments()
	show_people_by_row()
	com_au = input()
	print('Comment: ')
	com_co = input()
	add="insert into comments values ('" + str(com_id) + "', '" + str(tk_id) + "', '" + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "', '" + com_au + "', '" + com_co +"');"
	ex_co(add)
	print('Update status?')
	option = input()
	if (option == "yes"):
		print('Status:')
		print('0 = New')
		print('1 = In Progress')
		print('2 = Follow Up')
		print('3 = On Hold')
		print('4 = Complete')
		tk_st = str(int(input()))
		update_ticket_status(tk_id, tk_st)

def update_ticket_status(tk_id, tk_st):
	tct=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	add="update tickets set tickets.status = "+ tk_st + "  where tickets.id = "+ tk_id + ";"
	ex_co(add)
	add="update tickets set tickets.modified = '" + tct +"' where tickets.id = " + tk_id+ ";"
	ex_co(add)
	prompt_update_general_ticket()

prompt()
