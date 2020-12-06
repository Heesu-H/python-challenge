import os
import csv

def PyPoll(electiondata_filelocation):

    file_location = electiondata_filelocation

    list_candidates = []
    filtered = []
    k_votes = []
    k_total = 0
    c_votes = []
    c_total= 0
    l_votes = []
    l_total = 0
    o_votes = []
    o_total = 0
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
            if candidate not in filtered:
                filtered.append(candidate)
        #or can conver list to dict and back to list. found at https://www.w3schools.com/python/python_howto_remove_duplicates.asp
        #candidates = list_to_dict(list_candidates)
    #print(candidates)

        #counting total number of votes for each candidate
        for votes in list_candidates:
            if votes == filtered[0]:
                k_votes.append(votes)
                k_total +=1
            if votes == filtered[1]:
                c_votes.append(votes)
                c_total+=1
            if votes == filtered[2]:
                l_votes.append(votes) 
                l_total+=1
            if votes == filtered[3]:
                o_total+=1
                o_votes.append(votes)

    print(k_total,c_total,l_total,o_total)

    print(filtered)



#additional solution to filtering out duplicates
#def list_to_dict(x):
  #return list( dict.fromkeys(x) )
    







PyPoll(os.path.join("Resources","election_data.csv"))