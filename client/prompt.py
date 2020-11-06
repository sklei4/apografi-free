#!/usr/bin/env python3
## System
import mysql.connector
import getpass
import os
##
## Rhodes
#import rhodes-equipment
#import rhodes-tickets
#import rhodes-software
##

__author__ = "Sam Klein"
__software__ = "Client for Rhodes Database Manager CLI"
__version__ = "r0-mac-a.03-prompt.py"
__project__ = "https://gitlab.com/sklein/apografi-free"

def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	pointer = input(" 1. Equipment \n 2. Tickets \n 3. Software \n --- \n Select: ")
	if pointer == "1":
		os.system('cls' if os.name == 'nt' else 'clear')
		import equipment
	elif pointer == "2":
		os.system('cls' if os.name == 'nt' else 'clear')
		import tickets
	elif pointer == "3":
		os.system('cls' if os.name == 'nt' else 'clear')
		import software
	else:
		main()

if __name__ == "__main__":
	os.system('cls' if os.name == 'nt' else 'clear')
	print(" " + __software__ + " " + __version__)
	print(" " + __project__)
	print(" by " + __author__)
	#password=getpass.getpass(' Password: ')
	password="n0t_aLL0wed"
	mydb = mysql.connector.connect(
		host='localhost',
		user='sklein',
		passwd=password,
		database='rhodes'
		)
	mycursor = mydb.cursor()
	main()
