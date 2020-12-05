import os
import csv

def PyBank(csvfilepath):
    
    #calculating total months by finding last row of data
    #to exclude the header row 
    row_count = 0
    net_total = 0

    csv_filepath = csvfilepath
    with open(csv_filepath,'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        cvsheader = next(csv_reader)
        for row in csv_reader:
            if row != "":
                row_count += 1    
                net_total += int(row[1])
        print(row_count)
        print(net_total)

PyBank(os.path.join("Resources","budget_data.csv"))

