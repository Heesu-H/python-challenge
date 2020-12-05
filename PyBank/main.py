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
    greatest_profit = 867884
    i = 0
    changes_dates = 0
  



    
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
            #value (j)  for each loop
            sum_changes += j
        average_change = round(sum_changes/int(len(changes)),2)

        # finding greatest profit
        for value in changes:
            if greatest_profit < int(value):
                greatest_profit = int(value)
                if int(value) == last_value:
                    break
        for value in changes:
            if int(value) == greatest_profit:
                changes_index = changes.index(value) 
                print(changes_index)
        for row in csv_reader:
            
            
            

          

    print(f"row count       {row_count}")
    print(f"net total       {net_total}")
    print(f"Average Change  {average_change}") 
    print(f"changes         {len(changes)}")
    print(f"greatest profit {greatest_profit}")
    print(f"last value      {last_value}")
    


PyBank(os.path.join("Resources","budget_data.csv"))
