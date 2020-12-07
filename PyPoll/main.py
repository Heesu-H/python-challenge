import os
import csv

def PyPoll(electiondata_filelocation):

    file_location = electiondata_filelocation

    list_candidates = []
    filtered = []
    
    k_total = 0
    c_total= 0   
    l_total = 0
    o_total = 0
    each_total = []
    percent = []
    most = 0
    
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
                k_total +=1
            if votes == filtered[1]:
                c_total+=1
            if votes == filtered[2]:
                l_total+=1
            if votes == filtered[3]:
                o_total+=1
        #solution to append multiple value at one time
        #found at https://stackoverflow.com/questions/20196159/how-to-append-multiple-values-to-a-list-in-python
        each_total.extend((k_total,c_total,l_total,o_total))
        

        #percentage of votes
        k_percent = round((k_total/total_votes)*100,3)
        c_percent = round((c_total/total_votes)*100,3)
        l_percent = round((l_total/total_votes)*100,3)
        o_percent = round((o_total/total_votes)*100,3)
        percent.extend((k_percent,c_percent,l_percent,o_percent))

        #solution to put two lists into dictionaries so we can 
        #find the name corresponding to the most amount of votes 
        #found at https://stackoverflow.com/questions/7271385/how-do-i-combine-two-lists-into-a-dictionary-in-python
        zip_nt = list(zip(filtered,each_total))
        #convert list to dictionary
        name_and_total = dict(zip_nt)

        

        #finding most votes
        for i in each_total:
            if most < i:
                most = i 
                index_most = each_total.index(most)
        #solution to find key from value
        #found at https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
        for name,vote in name_and_total.items():
            if vote == most:
                popular_vote = name


    print(f"Total votes: {total_votes}")
    print(f"Khan {k_total}      Correy {c_total}    Li {l_total}    O'Tooley {o_total}")  
    print(each_total)
    print(most)
    print(index_most)
    print(popular_vote)
    print(f"{popular_vote} won majority with a total of {most} votes.")
    print(filtered)

    output_file = os.path.join("analysis","Election_results.txt")

    with open(output_file,'w') as txtfile:
        csvwriter= csv.writer(txtfile,delimiter = ",")

        csvwriter.writerow(["Election Results"])
        csvwriter.writerow(["_____________________________"])
        csvwriter.writerow([f"Total votes: {total_votes}"])
        csvwriter.writerow(["_____________________________"])
        #uneven spacing to make txt columns to line up 
        csvwriter.writerow([f"{filtered[0]}         {percent[0]}%   {each_total[0]} votes"])
        csvwriter.writerow([f"{filtered[1]}       {percent[1]}%   {each_total[1]}  votes"])
        csvwriter.writerow([f"{filtered[2]}           {percent[2]}%   {each_total[2]}  votes"])
        csvwriter.writerow([f"{filtered[3]}     {percent[3]}%    {each_total[3]}  votes"])
        csvwriter.writerow(["_____________________________"])
        csvwriter.writerow([f"Winner: {popular_vote}"])
        csvwriter.writerow(["_____________________________"])



#additional solution to filtering out duplicates
#def list_to_dict(x):
  #return list( dict.fromkeys(x) )
    



PyPoll(os.path.join("Resources","election_data.csv"))