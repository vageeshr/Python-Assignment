import mysql.connector
import sys
import datetime
import random
global conn,cursor;

conn = mysql.connector.connect(host="localhost",user="root")

def connection():
    
    if conn.is_connected():
        return True
    else:
        return False

def create_database():
    if connection():
        mycursor = conn.cursor()
        try:
            mycursor.execute("CREATE DATABASE RTO")
            print("\n Successfully database created \n" )
        except:
            print("Warning: Database already exists \n")
    else:
        print("\nCould not connect to mysql server \n")

def create_table():
	conn_db=mysql.connector.connect(host="localhost",db="RTO",user="root")
	if conn_db.is_connected():
		cursor=conn_db.cursor()
		try:
			cursor.execute("CREATE TABLE rto_details(ID INT(10) PRIMARY KEY, RTOINCHARGE VARCHAR(255), Designation VARCHAR(255), PLACE varchar(255))")
			cursor.execute("CREATE TABLE user_details(USERID INT(10),USERNAME varchar(255),VEHICLETYPE varchar(255),VEHICLENO varchar(255),VEHICLECOLOR varchar(255)")

			print("Successfully created table")
		except:
			print("Warning:already created")
	else:
		print("fail connection")
		conn_db.close()


def insert_values():
	db_conn=mysql.connector.connect(host="localhost",db="RTO",user="root")
	if db_conn.is_connected():
		mycursor= db_conn.cursor()

		query = "INSERT INTO reg_no(ID,RTOINCHARGE,Designation,PLACE) VALUES (%s,%s,%s,%s) "
		ID = input("\n Enter id\n")
		RTOINCHARGE = input("\n Enter name of rtoincharge\n")
		Designation = input("\n Enter designation\n")
		PLACE=input("\n enter the place ")
		value=(ID,RTOINCHARGE,Designation,PLACE)

		query = "INSERT INTO reg_no(ID,RTOINCHARGE,Designation,PLACE) VALUES (%s,%s,%s,%s) "
		USERID = input("\n Enter user id\n")
		USERNAME = input("\n Enter USER name \n")
		VEHICLETYPE = input("\n Enter vehicle type\n")
		VEHICLENO=input("\n Enter VEHICLE NO ")
		VEHICLECOLOR=input("\n Enter vechicle color")
		value=(USERID,VEHICLETYPE,VEHICLENO,VEHICLECOLOR)


		mycursor.execute(query,value)
		db_conn.commit()
		print("sucessfully inserted")

		

	db_conn.close()

def display():
	conn_db=mysql.connector.connect(host="localhost",db="RTO",user="root")
	if conn_db.is_connected():
		cursor=conn_db.cursor()
		try:
			cursor.execute("SELECT * FROM rto_details")
			rows = cursor.fetchall();
			for row in rows:
   				print(row);
			
			cursor.execute("SELECT * FROM user_details")
			rows = cursor.fetchall();
			for row in rows:
   				print(row);
		except:
			print("Warning:already created")
	else:
		print("fail connection")
		conn_db.close()

def main():
	connection();
	while True:
		print("\nEnter your choice::\n")
		print( "Create database - 1:" )
		print( "Create table (rto_details & user_details) - 2:")
	
		print("Insert values (rto_details & user_details) - 3:")
		print("Display table values (reg_no) - 4:")
		print("Quit- q:\n")

		choice = input("Enter the option:\t")
		
		
		if choice == '1':
			create_database()
		if choice == '2':
			create_table()
		if choice == '3':
			insert_values()
		if choice == '4':
			display()
		
		if choice == 'q':
			sys.exit()
		


if __name__ == "__main__":
	main();
	
