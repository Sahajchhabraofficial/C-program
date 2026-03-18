import csv

with open('C-program/Data.csv', mode='r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    # Skip the header row if present
    # next(csv_reader, None)
    
    for row in csv_reader:
        print(row[0])
        print(type(row[0]))