import mysql.connector
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
		pointer = input(" 1. Add Equipment \n 2. Update cable stock. \n 3. Show Tables \n --- \n Select: ")
		if pointer == "1":
			os.system('cls' if os.name == 'nt' else 'clear')
			print("ADDING EQUIPMENT")
			prompt_add_general_equipment()
		elif pointer == "2":
			os.system('cls' if os.name == 'nt' else 'clear')
			print("UDPATING CABLES")
			prompt_update_cable_general()
		elif pointer == "3":
			os.system('cls' if os.name == 'nt' else 'clear')
			print("SHOWING TABLES")
			prompt_show_any_table()
		elif pointer == "4":
			exit()
		else:
			prompt()

def add_cable(cabl_id, cabl_upc, cabl_ca, cabl_cb, cabl_ln, cabl_in_stock, cabl_taken):
	add="insert into cables values (" + str(cabl_id) + ", '" + cabl_upc + "', '" + cabl_ca + "', '" + cabl_cb + "', '" + cabl_ln + "', '" + cabl_in_stock + "', '" + cabl_taken + "');"
	ex_co(add)

def add_computer(comp_id, comp_memory_installed, comp_process_type, comp_os, comp_os_version, comp_vc):
	add="insert into computers (Operating_System, OS_Version, Memory_Installed_Amount, Processor_Type, Video_Controller, ID)" + ' values ("' + comp_os + '", "' + comp_os_version + '", "' + comp_memory_installed + '", "' + comp_process_type + '", "' + comp_vc + '", "' + comp_id + '");'
	ex_co(add)

def add_equipment(eq_id, equip_name, equip_type, equip_model_id, equip_serial_number, equip_owner_id, equip_price):
	add="insert into equipment values (" + str(eq_id) + ", '" + equip_name + "', '" + equip_type + "', '" + equip_model_id + "', '" + equip_serial_number + "', '" + equip_owner_id + "', '" + equip_price + "');"
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

def count_cable_stock(cable_id):
	mycursor.execute('select In_Stock from cables where ID = ' + cable_id + ';')
	return clean_count(mycursor.fetchall())

def count_equipment():
	mycursor.execute('select count(ID) from equipment;')
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

def prompt_add_cable_from_equipment(eq_id):
	cb_id = eq_id
	print('Please record values for the following prompts.')
	print('Type NULL if not available.')
	cbupc = input('UPC: ')
	cb_ca = input('Connector A: ')
	cb_cb = input('Connector B: ')
	cb_lg = input('Length: ')
	cb_is = input('Number of cables in stock: ')
	cb_tk = "0"
	add_cable(cb_id, cbupc, cb_ca, cb_cb, cb_lg, cb_is, cb_tk)
	print('Success.')

def prompt_add_computer_from_equipment(eq_id):
	cp_id = eq_id
	print('Please record values for the following prompts.')
	print('Type NULL if not available.')
	cp_mi = input('Memory installed: ')
	cp_pt = input('Processor type: ')
	cp_os = input('Operating system, do not include version: ')
	cp_ov = input('Operating system version: ')
	cp_vc = input('Video controller: ')
	add_computer(cp_id, cp_mi, cp_pt, cp_os, cp_ov, cp_vc)
	print('Success.')

def prompt_add_general_equipment():
	print('Please record values for the following prompts.')
	eq_ty=input('Type: ')
	eq_na=input('Name: ')
	eq_mo=input('Model: ')
	eq_sn=input('Serial Number: ')
	eq_ow=str(check_owner())
	eq_pr=input('Price: ')
	eq_id=count_equipment()
	eq_id=str(eq_id) #prevents increment by accident
	add_equipment(eq_id, eq_na, eq_ty, eq_mo, eq_sn, eq_ow, eq_pr)
	print('Success.')
	if (eq_ty == "Computer"):
		prompt_add_computer_from_equipment(eq_id)
	if (eq_ty == "Cable"):
		prompt_add_cable_from_equipment(eq_id)

def prompt_add_person_from_equipment():
	print('Please record values for the following prompts.')
	ps_nm=input('Name: ')
	ps_lc=input('Address: ')
	ps_em=input('Email: ')
	ps_ph=input('Phone: ')
	add_person(ps_nm, ps_lc, ps_em, ps_ph)
	print('Success.')
	print('Continue entering values for equipment.')

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

def prompt_update_cable():
	cable_id = input("Cable ID: ")
	action = input("Take or Stock?")
	if action == "take":
		update_cable_increment_taken(cable_id)
	elif action == "stock":
		update_cable_increment_stock(cable_id)
	else:
		print("Nothing.")

def prompt_update_cable_general():
	show_cables_by_id()
	prompt_update_cable()

def return_data_by_row0():
	data = mycursor.fetchall()
	for row in data:
		return(row[0])

def show_cables_by_id():
	mycursor.execute('select cables.ID, equipment.Name, cables.In_Stock from cables join equipment on cables.ID = equipment.ID;')
	show_data_by_row0_row1_row2()

def show_cables_by_raw():
	mycursor.execute('select equipment.Name, cables.In_Stock from cables join equipment on cables.ID = equipment.ID;')
	print(show_data_by_raw())

def show_cable_instock(cable_id):
	mycursor.execute('select In_Stock from cables where ID = "' + cable_id + '";')
	show_data_by_row0()

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

def update_cable_increment_stock(cable_id):
	mycursor.execute('select In_Stock from cables where ID = "' + cable_id + '";')
	current_stock = return_data_by_row0()
	current_stock = current_stock # error correctin
	number_increase = input('How many to add? ')
	rm_to_stock = int(current_stock) + int(number_increase)
	update_stock = 'update cables set In_Stock = ' + str(rm_to_stock) + ' where ID = ' + cable_id +  ';'
	ex_co(update_stock)

def update_cable_increment_taken(cable_id):
	mycursor.execute('select In_Stock from cables where ID = "' + cable_id + '";')
	current_stock = return_data_by_row0()
	current_stock = current_stock # error correctin
	mycursor.execute('select Taken from cables where ID = "' + cable_id + '";')
	current_taken = return_data_by_row0()
	current_taken = current_taken # error correcting
	number_increase = input('How many to take?')
	rm_to_stock = int(current_stock) - int(number_increase)
	in_to_taken = int(current_taken) + int(number_increase)
	update_stock = 'update cables set In_Stock = ' + str(rm_to_stock) + ' where ID = ' + cable_id +  ';'
	update_taken = 'update cables set Taken = ' + str(in_to_taken) + ' where ID = ' + cable_id + ';'
	ex_co(update_stock)
	ex_co(update_taken)

def update_cable_count(cable_id):
	print("test")

prompt()
