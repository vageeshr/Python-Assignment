from flask import Flask, json, render_template, request
import sys
#sys.path.insert(0, 'models')
import random

import mysql.connector
global conn

conn = mysql.connector.connect(host="localhost", user="root",password = "root@123")


app = Flask(__name__)



#home page route by default GET
@app.route("/")
def main():
    def connection():
        if conn.is_connected():
            return True
        else:
            return False

    def create_table():

        conn_db=mysql.connector.connect(host="localhost",user="root",password = "root@123")
        if conn_db.is_connected():
            cursor=conn_db.cursor()
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS RTO")
                cursor.execute("CREATE TABLE IF NOT EXISTS RTO.rto_details(ID INT(10) PRIMARY KEY, RTOINCHARGE VARCHAR(255), Designation VARCHAR(255), PLACE varchar(255))")
                cursor.execute("CREATE TABLE IF NOT EXISTS RTO.user_details(USERID INT(10), USERNAME varchar(255), VEHICLETYPE varchar(255), VEHICLENO varchar(255), VEHICLECOLOR varchar(255))")

            finally:
                conn_db.close()


    
    create_table()


        #init db on home page visit
       
    return render_template('index.html')

    #Route to show new RTO registration form
@app.route('/RTO/register')
def newRTORegForm():
    return render_template('rto_form.html')


    #Route to show new User registration form
@app.route('/User/register')
def newUserRegForm():
    return render_template('user_form.html')


    #Route for new RTO registration
@app.route('/RTO/persist',methods=['POST'])
def newRTOReg():
    # read the posted values from the UI
    mycursor = conn.cursor()

    _RTOID = request.form['RTOID']
    _RTOINCHARGE = request.form['RTOINCHARGE']
    _Designation = request.form['Designation']
    _Location = request.form['Location']

    sql = "INSERT INTO RTO.rto_details (ID, RTOINCHARGE, Designation, PLACE) VALUES (%s, %s, %s, %s)"
    val = (_RTOID, _RTOINCHARGE, _Designation, _Location)
    #new_rto = RTO(_RTOID, _RTOINCHARGE, _Designation, _Location)
    mycursor.execute(sql, val)
    conn.commit()
    mycursor.close()
        #if new_rto.persist(conn):
    return json.dumps({'message':'RTO registration successful !'})
        #else:
        # return json.dumps({'message':'Failed. ID already taken!'})


    #Route for new RTO registration
@app.route('/User/persist',methods=['POST'])
def newUserReg():
# read the posted values from the UI
    mycursor = conn.cursor()
    _USERID = request.form['UserID']
    _UserName = request.form['UserName']
    _VehicleType = request.form['VehicleType']
    _VehicleColor = request.form['VehicleColor']
    _VEHICLENO = random.randint(1000, 9999) #4 digit random number


    sql = "INSERT INTO RTO.user_details (USERID, USERNAME, VEHICLETYPE, VEHICLENO, VEHICLECOLOR) VALUES (%s, %s, %s, %s, %s)"
    val = (_USERID, _UserName, _VehicleType, _VEHICLENO, _VehicleColor)
    mycursor.execute(sql, val)
    conn.commit()
    mycursor.close()

    
    # else:
            #return json.dumps({'message':'Failed. User ID already taken!'}



@app.route('/RTO/list')
def display():
    conn_db=mysql.connector.connect(host="localhost",db="RTO",user="root",password = "root@123")
    if conn_db.is_connected():
        cursor=conn_db.cursor()
        cursor.execute("SELECT * FROM RTO.rto_details")
        RTOs = cursor.fetchall();
        return render_template('rto_table.html', result = RTOs)
            
            
            
    conn_db.close()




@app.route('/User/list')
def listUsers():
# read the posted values from the UI
    conn_db=mysql.connector.connect(host="localhost",db="RTO",user="root",password = "root@123")
    if conn_db.is_connected():
        cursor=conn_db.cursor()
        cursor.execute("SELECT * FROM RTO.user_details")
        users = cursor.fetchall();
        return render_template('user_table.html', result = users)

        conn_db.close()

if __name__ == "__main__":
    app.debug = True
    app.run()

