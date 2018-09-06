import os
import csv

poll_csv_path = os.path.join("..","Resources","election_data.csv")
results_txt_path = os.path.join("..","Output","poll_result.txt")

votecount = 0                                     # total votes tallied
election = {}                                       #election is a dictionary with candidate and vote count
with open (poll_csv_path, "r",newline = "") as pollfile:
    pollreader = csv.reader(pollfile,delimiter = ",")
    header = next(pollreader)
    for row in pollreader:                          #tally the votes
        votecount +=1              
        if row[2] in election:                    # if the candidate is already listed add 1 to his/her total
            election[row[2]] += 1
        else:                                       # first vote for a candidate add to election with 1 vote
            election[row[2]] = 1

if votecount >0:                                #find the winner
    candidate = list(election.keys() )
    tally = list( election.values()  )
    winner = candidate[tally.index(max(tally))  ] 

    result=[]                                               #prepare results in a list
    result.append("         Election Results")
    result.append("----------------------------")
    result.append(f"         Total Votes: {votecount}")
    result.append("----------------------------")
    for candidate in election.keys():
        result.append("  {0:>13} : {1:>0.3f}% ({2:>8}) ".format(candidate,100*election[candidate]/votecount,election[candidate]))
    result.append("----------------------------")
    result.append("         Winner: {0} ".format(winner))
    result.append("----------------------------")

    for line in result:                         #print results to terminal
        print (line)

    with open (results_txt_path, "w") as resultfile:        #send results to a file
       for line in result:
            resultfile.write(line + "\n" )