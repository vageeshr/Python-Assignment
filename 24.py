with open("StudentFile.txt") as fileobj:
    for line in fileobj:  
       for ch in line:
           print (ch)
