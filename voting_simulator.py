# Code to simulate different voting systems given an input
# Counties are treated as individual voters, where the county's ranking is based on ranking the candidates by the number of delegates they get per county. 

import csv
import numpy

# First index corresponds with Buttigieg, second index corresponds with Sanders, third index corresponds with Warren, and fourth index corresponds with Biden
votes = [0] * 4

def vote_updater(index,total):
    if index == 0:
        votes[0] += total
    elif index == 1:
        votes[1] += total
    elif index == 2:
        votes[2] += total
    else:
        votes[3] += total

with open('CountyDataCleaned.csv', mode = 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)
    
    # Plurality with Runoff
    for row in rows:
        for i in range(0, len(row)): 
            row[i] = float(row[i]) 
        vote_updater(row.index(max(row)), sum(row))
        
    print("First we do Plurality with Runoff.")
    print("Resulting votes of running just Plurality. First index corresponds with Buttigieg, second index corresponds with Sanders, third index corresponds with Warren, and fourth index corresponds with Biden. These will always be our indices for the votes list.")
    print(votes)
    print("Buttigieg and Sanders (the two first indices) got the most votes. Now we do Plurality with runoff.")
    
    votes = [0] * 4
    
    print("Now we just consider the first two indices since they're the highest.")
    for row in rows:
        vote_updater(row.index(max(row[:2])), sum(row))
    
    print(votes)
    print("Looks like Sanders (the second index) got more votes than Buttigieg, so Sanders wins the Plurality with runoff.")
    print("Note that in the actual Caucus, Buttigieg beat Sanders by a slim margin. However, Sanders wins the Plurality with runoff because Sanders wins in the some of the most important counties (Polk, Linn, Scott, Black Hawk, Story, etc.) so he takes all of their delegates in Plurality with runoff, while in the normal election, those delegates are split between the candidates.")
    
    # STV
    votes = [0] * 4
    
    print()
    print("Now we do STV.")
    for row in rows:
        vote_updater(row.index(max(row)), sum(row))
    
    print("Resulting votes of first round of STV.")
    print(votes)
    print("Biden got the least votes, so we eliminate him and now only consider the first three indices since they're the highest.")
    
    votes = [0] * 4
    
    for row in rows:
        vote_updater(row.index(max(row[:3])), sum(row))
    
    print(votes)
    print("Warren got the least votes, so we eliminate her and now only consider the first two indices since they're the highest.")
    
    votes = [0] * 4
    
    for row in rows:
        vote_updater(row.index(max(row[:2])), sum(row))
    
    print(votes)
    
    print("Looks like Sanders (the second index) got more votes than Buttigieg, so Sanders wins the STV.")
    print("Note that the number of delegates that Sanders wins in both STV and Plurality with runoff are the same. This makes sense, because in every county that Biden won, Warren did not get the second most votes, so in STV, when we first eliminated Biden, all of his votes only transferred to Sanders and Buttigieg. Thus, after we eliminate Warren the STV situation is the same as the Plurality with runoff situation, since all of Warren and Biden's delegates get transferred to Sanders and Buttigieg the same way.")
    
    # Borda
    print()
    print("Now we do Borda.")
    votes = [0] * 4
    
    for row in rows:
        s = numpy.array(row)
        sort_index = numpy.argsort(s)
        # print(row)
        # print(sort_index)
        for i in sort_index:
            votes[sort_index[i]] += row[sort_index[i]] * i
        # print(votes)
    
    print(votes)
    print("Looks like Sanders (the second index) got the most delegates using the positional scoring of Borda, so Sanders wins the Borda.")
        