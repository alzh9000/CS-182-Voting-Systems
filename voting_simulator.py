# Code to simulate different voting systems given an input
# Counties are treated as individual voters, where the county's ranking is based on ranking the candidates by the number of delegates they get per county. 

import csv

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
    for row in rows:
        for i in range(0, len(row)): 
            row[i] = float(row[i]) 
        vote_updater(row.index(max(row)), sum(row))
    
    print(votes)
    
    
    
        

# Take in a 2-D list of rankings (a list of rankings, which are also formatted as a list)
def STV(rankings):
    ranking_totals = [ sum(x) for x in zip(*rankings) ]
    