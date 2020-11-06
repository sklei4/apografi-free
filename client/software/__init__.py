import mysql.connector
import time
import datetime
import getpass
import os

from __main__ import *

__author__ = "Sam Klein"
__software__ = "Rhodes Equipment Manager"
__version__ = "r0-mac-a.03-eq.py"
__project__ = "https://gitlab.com/sklein/rhodes"

def prompt():
	__status__ = 1
	while (__status__ == 1):
		os.system('cls' if os.name == 'nt' else 'clear')
		pointer = input(" 1. Add software license \n 2. Update license \n 3. Show tables \n 4. O365 User \n 5. Dropbox User \n --- \n Select: ")
		if pointer == "1":
			os.system('cls' if os.name == 'nt' else 'clear')
			print("ADDING SOFTWARE")
			prompt_add_general_equipment()
		elif pointer == "2":
			os.system('cls' if os.name == 'nt' else 'clear')
			print("UDPATING LICENSE")
			#prompt_update_equipment_general()
		elif pointer == "3":
			os.system('cls' if os.name == 'nt' else 'clear')
			print("SHOWING TABLES")
			#prompt_show_any_table()
		elif pointer == "4":
			prompt_common_o365()
		elif pointer == "5":
			prompt_dropbox()
		else:
			prompt()


def add_equipment(sf_id, sf_name, sf_type, sf_license, sf_owner_id, sf_price, sf_status, sf_annual, sf_purchased):
	add="insert into software values (" + str(sf_id) + ", '" + sf_name + "', '" + sf_type + "', '" + sf_license + "', '" + sf_owner_id + "', '" + sf_price + "', '" + sf_status + "', '" + sf_annual + "','" + sf_purchased + "');"
	ex_co(add)

def add_person(pers_name, pers_loc, pers_email, pers_phone):
	result=count_people()
	add="insert into people values (" + str(result) + ", '" + pers_name + "', '" + pers_loc + "', '" + pers_email + "', '" + pers_phone + "');"
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
		print("Adding person ID " + eq_na + " as owner.")
		return eq_na

def clean_count(myresult):
	for row in myresult:
		output=''.join(str(x) for x in row)
	return int(output)

def count_equipment():
	mycursor.execute('select count(ID) from software;')
	return clean_count(mycursor.fetchall())

def count_people():
	mycursor.execute('select count(ID) from people;')
	return clean_count(mycursor.fetchall())

def ex_co(query):
	mycursor.execute(query)
	mydb.commit()

def value_input(question): #need a way to process null
	fn = input(question)
	if fn == "None":
		fn = None
	if fn == "":
		fn = None
	return fn

def prompt_add_general_equipment():
	print('Was this software purchased today?')
	choice = input()
	if (choice == "no"):
		print("Date: (Example, 2008-07-23)")
		eq_pu = input()
		eq_pu = str(eq_pu)+ " 00:00:01"
	else:
		eq_pu = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	print('Please record values for the following prompts.')
	eq_ty=input('Type: ')
	eq_na=input('Name: ')
	eq_sn=input('License string: ')
	eq_ow=str(check_owner())
	eq_pr=input('Price: ')
	eq_st=input('Active or Disabled?')
	ans=input('Is the price an amount charged annually?')
	if (ans == "yes"):
		eq_ti = "1"
	else:
		eq_ti = "0"
	eq_id=count_equipment()
	eq_id=str(eq_id) #prevents increment by accident
	add_equipment(eq_id, eq_na, eq_ty, eq_sn, eq_ow, eq_pr, eq_st, eq_ti, eq_pu)
	print('Success.')

def prompt_add_person_from_equipment():
	print('Please record values for the following prompts.')
	ps_nm=input('Name: ')
	ps_lc=input('Address: ')
	ps_em=input('Email: ')
	ps_ph=input('Phone: ')
	add_person(ps_nm, ps_lc, ps_em, ps_ph)
	print('Success.')
	print('Continue entering values for software.')

def prompt_common_o365():
	eq_id=count_equipment()
	eq_id=str(eq_id) #prevents increment by accident
	eq_ow=str(check_owner())
	add_equipment(eq_id, "Office 365 Business Preimum", "O365", " ", eq_ow, "150", "Active" )

def prompt_dropbox():
        eq_id=count_equipment()
        eq_id=str(eq_id) #prevents increment by accident
        eq_ow=str(check_owner())
        add_equipment(eq_id, "Business Dropbox User License", "Data Storage", " ", eq_ow, "170", "Active", "1", "2018-08-13" )

def prompt_show_any_table():
	pointer = input(" 1. Full equipment list \n 2. Full people list. \n"
	+ " 3. Full cable list \n 4. Full computer list with owners. \n 5. " 
	+ "Equipment in inventory. \n 6. Computers in inventory. \n 7. " 
	+ "Cables in inventory. \n 8. Equipment besides Computers or Cables"
	+ " in inventory. \n --- \n Select: ")
	if pointer == "1":
		print_full_equipment()
	elif pointer == "2":
		print_full_people()
	elif pointer == "3":
		print_full_computer_users()
	elif pointer == "4":
		print_all_computers_inv()
	elif pointer == "5":
		print_all_equipment_inv()
	elif pointer == "6":
		print_all_cables_inv()
	elif pointer == "7":
		print_all_cables_inv()
	elif pointer == "8":
		print_equipment_besides_co_ca_inv()
	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("*-*-*-*-*-*-*-*-*-*-*-* \n|Something went wrong!| \n*-*-*-*-*-*-*-*-*-*-*-*")
		prompt_show_any_table()

def prompt_update_cable_general():
	show_cables_by_id()
	prompt_update_cable()

def return_data_by_row0():
	data = mycursor.fetchall()
	for row in data:
		return(row[0])

def show_data_by_raw():
	data = mycursor.fetchall()
	return(data)

def show_data_by_row0():
	data = mycursor.fetchall()
	for row in data:
		print(row[0])

def show_data_by_row0_row1():
	data = mycursor.fetchall()
	for row in data:
		print(row[0], ': ', row[1])

def show_data_by_row0_row1_row2():
	data = mycursor.fetchall()
	for row in data:
		print(row[0], row[1], ': ', row[2])

def show_data_by_row0_row2():
	data = mycursor.fetchall()
	for row in data:
		print(row[0], ':  ', row[2])

def show_data_by_row0_row1_row3():
	data = mycursor.fetchall()
	for row in data:
		print(row[0], row[1], row[3])

def show_data_by_row0_row1_row4():
	data = mycursor.fetchall()
	for row in data:
		print(row[0], row[1], row[4])


def show_equipment_by_id():
	mycursor.execute('select * from equipment;')
	show_data_by_row0_row1_row4()

def show_equipment_by_raw():
	mycursor.execute('select * from equipment;')
	print(show_data_by_raw())

def show_people_by_raw():
	mycursor.execute('select * from people;')
	print(show_data_by_raw())

def show_people_by_row():
	mycursor.execute('select * from people;')
	show_data_by_row0_row1()

prompt()

