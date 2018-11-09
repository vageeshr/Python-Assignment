import csv
import sys
def main():
    login()
    
def login():
    username="formtutor"
    password="teacherpass"
    print("Enter username : ")
    answer1=input()
    print("Enter password : ")
    answer2=input()
    if answer1==username and answer2==password:
        print("Welcome - Access Granted")
        menu()
    else:
        print("Access Denied")

def menu():
    print("************MAIN MENU**************")
    #time.sleep(1)
    print()

    choice = input("""
                      A: Enter Student details
                      B: View Student details
                      Q: Quit/Log Out

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        enterstudentdetails()
    elif choice == "B" or choice =="b":
        viewstudentdetails()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A,B, or Q.")
        print("Please try again")
        menu()

def enterstudentdetails():
    #user is prompted to input all the required fields
    print("RegNo")
    RegNo=input()
    print("StudentName")
    StudentName=input()
    print("Branch")
    Branch=input()
    with open('StudentFile.txt','a') as studentfile:
        studentfileWriter=csv.writer(studentfile)
        studentfileWriter.writerow([RegNo, StudentName, Branch])
        print("Record has been written to file")
        studentfile.close()
        menu()

def viewstudentdetails():
#Open the file for reading
    f=open("studentfile.txt","r",encoding="utf8")
    #Create a list called "displaylist" into which all the files lines are read in to....
    displaylist=f.read()
    #print the list (that now has the file details in it)
    print(displaylist)
    f.close()
    menu()

main()