
import csv

def main():

    # 'a+' opens a file for both reading and writing and creates file if not exists
    with open('students.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        students = dict()

        for row in csv_reader:
            students[row['RegNo']] = row['name']

        print("\nDone\n")
        print(students)


if __name__=="__main__":
main()