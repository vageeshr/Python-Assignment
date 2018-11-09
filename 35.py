
import mysql.connector
import sys 
import datetime
global conn,cursor;

conn = mysql.connector.connect(host="localhost", user="root",password="root")

def connection():
    
    if conn.is_connected():
        return True
    else:
        return False

def create_database(db_name):
    if connection():
        mycursor = conn.cursor()
        try:
            mycursor.execute("CREATE DATABASE " + db_name)
            print("\n Success: Database ",db_name," created \n")
        except Exception as e:
            print(e)
            print( "\n Warning: Database ",db_name," already exists \n")
    else:
        print( "\n Error: Could not connect to mysql server \n")


def create_table(table_name, db_name):
    conn_db = mysql.connector.connect(host="localhost", db=db_name, user="root",password="root")
    if conn_db.is_connected():
        mycursor = conn_db.cursor()
        try:
            mycursor.execute("CREATE TABLE "+table_name+"(id INT(10) PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), dob DATE)")
            print("\n Success: Table ",table_name," created\n")
        except Exception as e:
            print(e)
            print( "\n Warning: Table ",table_name," already exists \n")
    else:
        print( "\n Error: Could not connect to mysql server \n")

    conn_db.close()


def insert_values(table_name, db_name):
    conn_db = mysql.connector.connect(host="localhost", db=db_name, user="root",password="root")
    if conn_db.is_connected():
        mycursor = conn_db.cursor()

        sql = "INSERT INTO "+table_name+" (id, fname, lname, dob) VALUES (%s, %s, %s, %s)"

        id = input("\nEnter id\n")
        fname = input("\nEnter fname\n")
        lname = input("\nEnter lname\n")
        dob = input("\nEnter dob ( yyyy-mm-dd )\n")

        if not valid_date(dob):
            print( "\n Error: Incorrect 'dob' format, should be YYYY-MM-DD \n")
            sys.exit()


        val = (id, fname, lname, dob)
        try:
            mycursor.execute(sql, val)
            conn_db.commit()
            print("\n Success: Insertion Successful \n")

        except Exception as e:
            print(e)
            print( "\n Error: Could not insert the values \n")
    else:
        print( "\n Error: Could not connect to mysql server \n")
    conn_db.close()



def alter_table(table_name, db_name):
    conn_db = mysql.connector.connect(host="localhost", db=db_name, user="root",password="root")
    if conn_db.is_connected():
        mycursor = conn_db.cursor()

        col = input("\nEnter column name\n")
        sql = "ALTER TABLE "+table_name+" add %s VARCHAR(255)" % (col)

        try:
            mycursor.execute(sql)
            conn_db.commit()
            print("\n Success: column added to table Successful \n")

        except Exception as e:
            print(e)
            print( "\n WARNING: column already exists in table \n")
    else:
        print( "\n Error: Could not connect to mysql server \n")
    conn_db.close()


def truncate_table(table_name, db_name):
    conn_db = mysql.connector.connect(host="localhost", db=db_name, user="root",password="root")
    if conn_db.is_connected():
        mycursor = conn_db.cursor()

        sql = "DROP TABLE "+ table_name
        try:
            mycursor.execute(sql)
            conn_db.commit()
            print("\n Success: table dropeed Successfully \n")

        except Exception as e:
            print(e)
            print( "\n WARNING: could not drop table \n")
    else:
        print( "\n Error: Could not connect to mysql server \n")
    conn_db.close()


def display_values(table_name, db_name):
    conn_db = mysql.connector.connect(host="localhost", db=db_name, user="root",password="root")
    if conn_db.is_connected():
        mycursor = conn_db.cursor()

        try:
            mycursor.execute("SELECT * FROM "+table_name)
            myresult = mycursor.fetchall()
            for x in myresult:
              print(x)

        except Exception as e:
            print(e)
            print( "\n WARNING: could not print table \n")
    else:
        print( "\n Error: Could not connect to mysql server \n")
    conn_db.close()

def valid_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True;
    except ValueError:
        return False

def main():
    while True:


        print("\nEnter your choice::\n")
        print("Create database - 1:\t")
        print("Create table - 2:\t")
        print("Insert values - 3:\t")
        print("Display table values - 4:\t")
        print("Alter table (add column) - 5:\t")
        print("Trucate table - 6:")
        print("Quit- q:\n")

        choice = input("Enter the option:\t")


        if choice == '1':
            db_name = input("Enter new db name:\t")
            create_database(db_name)

        if choice == '2':
            db_name = input("Enter db name:\t")
            table_name = input("Enter table name in " + db_name + ":\t")
            create_table(table_name, db_name)

        if choice == '3':
            db_name = input("Enter db name:\t")
            table_name = input("Enter table name in " + db_name + ":\t")
            insert_values(table_name, db_name)

        if choice == '4':
            db_name = input("Enter db name:\t")
            table_name = input("Enter table name in " + db_name + ":\t")
            display_values(table_name, db_name)   

        if choice == '5':
            db_name = input("Enter db name:\t")
            table_name = input("Enter table name in " + db_name + ":\t")
            alter_table(table_name, db_name)

        if choice == '6':
            db_name = input("Enter db name:\t")
            table_name = input("Enter table name in " + db_name + ":\t")
            truncate_table(table_name, db_name)
        if choice == 'q':
            sys.exit()
        



if __name__ == "__main__":
main();