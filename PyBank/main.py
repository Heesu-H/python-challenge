import os
import csv

def PyBank(csvfilepath):
    
    #calculating total months by finding last row of data
    #to exclude the header row 
    row_count = 0
    net_total = 0
    values = []
    changes = []
    difference = 0
    sum_changes = 0
    i=0
    csv_filepath = csvfilepath
    with open(csv_filepath,'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        next(csv_reader)
        for row in csv_reader:
            if row!="":
                row_count += 1    
                net_total += int(row[1])
                last_value = int(row[1])
                #put profit/losses list in separate list
                values.append(row[1])
        #loop through values of profit and losses        
        for value in values:
            #stop loop if we encounter the last value. without this there is
            #an error:list index out of range
            if int(value) == last_value:
                break
            else:
                difference = int(values[i+1]) - int(value) 
                #add differences to another list
                changes.append(difference)
                i+=1
        #for values in changes 
        for j in changes:
            # with sum_changes starting at 0, add 
            #value each loop
            sum_changes += j
        average_change = round(sum_changes/int(len(changes)),2)
        
            

    print(len(changes))
    print(row_count)
    print(net_total)
    print(average_change) 
        
PyBank(os.path.join("Resources","budget_data.csv"))
