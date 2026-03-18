import csv
Email="sahajchhabra24@gmail.com"
with open("C-program/Data.csv",mode='r',newline='') as datafile:
        username=csv.reader(datafile,delimiter=',')
        for name in username:
            if Email==name[0]:
                print(name[0])
                print("Yes: ")
                break
        else:
            print("No: ",name[0])