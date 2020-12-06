import os
import csv

def PyPoll(electiondata_filelocation):

    file_location = electiondata_filelocation

    list_candidates = []
    candidates_filtered = []
    total_votes = 0


    # open file in read mode
    with open(file_location,'r') as election_data_file:
        
        csvreader = csv.reader(election_data_file, delimiter = ",")  
        #header row  
        next(csvreader)
        #counting total number of votes and appending name of candidates to a list
        for row in csvreader:
            if row:
                total_votes +=1
                list_candidates.append(row[2])
        
        for candidate in list_candidates:
            if candidate not in candidates_filtered:
                candidates_filtered.append(candidate)
        #or can conver list to dict and back to list. found at https://www.w3schools.com/python/python_howto_remove_duplicates.asp
        #candidates = list_to_dict(list_candidates)
    #print(candidates)
    print(candidates_filtered)


#additional solution to filtering out duplicates
#def list_to_dict(x):
  #return list( dict.fromkeys(x) )
    







PyPoll(os.path.join("Resources","election_data.csv"))