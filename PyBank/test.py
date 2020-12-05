import os
import csv


def import_csv():
    data = []
    with open(os.path.join("Resources","budget_data.csv"), "r") as scraped:
        reader = csv.reader(scraped, delimiter=',')
        row_index = 0
        for row in reader:
            if row:  # avoid blank lines
                row_index += 1
                columns = [str(row_index), row[0], row[1]]
                data.append(columns)
        
    output_path = os.path.join("analysis","new.csv")
    with open(os.path.join("analysis","new.csv"), 'w') as csvfilewrite:
        csvwriter = csv.writer(csvfilewrite,delimiter = ",")
        csvwriter.writerow(["total months","net total of profit/losses"])
        csvwriter.writerow([columns,"whatever"])

   #gives later row of that list
    last_row = data[-1]
    #prints first value in that list
    print(last_row[0])
    return data


import_csv()

##data = import_csv(os.path.join("Resources","budget_data.csv"))
#last_row = data[-1]