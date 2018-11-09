import csv

def main():

    # 'a+' opens a file for both reading and writing and creates file if not exists
    with open('students.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        students = list()
        branches = list()
        for row in csv_reader:
            students.append(row['RegNo'])
            branches.append(row['branch'])

        
        #set can be used to remove duplicates from a list and as set has only unique elements.
        #Hence we convert the branches and students list to a set
        students = set(students)
        branches = set(branches)

        avg = len(students) / len(branches)

        print("\nAverage number of students in a branch is {0:.2f}\t".format(avg) +"\n")




if __name__=="__main__":
main()