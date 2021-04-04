#import files for PollData
import csv
import os

polls = os.path.join('..','Resources','PollData.csv')

# Open the CSV
with open(polls) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
# Remove the header
    header = next(csvreader)
    

# Create the list of variables
    total_votes = 0
    candidates_list = []
    per_votes_dict = {}
    tv_candidates_dict = {}
    winner_str = ""
    
# Total Number of votes cast
    for row in csvreader:
        total_votes = total_votes + 1
        
        
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            tv_candidates_dict[row[2]]  = 1
        else:
            tv_candidates_dict[row[2]]  += 1
print(tv_candidates_dict)

#percentage of votes per candidate
for i in tv_candidates_dict	:       
    per_votes_dict[i]= float(tv_candidates_dict[i]) * 100/float(total_votes)
print(per_votes_dict)

#winner of the election
max(per_votes_dict, key = per_votes_dict.get)

#print out the analysis 

print(f"Election Results")
print('-'*30)
print(f"Total Votes: : {total_votes}")
for key,value in per_votes_dict.items():
    print(f'{key},{value:.3f}%,({tv_candidates_dict[key]})')

print('-'*30)
print(f"Winner: {max(per_votes_dict, key = per_votes_dict.get)}")
print('-'*30)

f = open("myfile.txt", "w")
f.write(f"Election Results")
f.write('-'*30)
f.write(f"Total Votes: : {total_votes}")
for key,value in per_votes_dict.items():
    print(f'{key},{value:.3f}%,({tv_candidates_dict[key]})')

f.write('-'*30)
f.write(f"Winner: {max(per_votes_dict, key = per_votes_dict.get)}")
f.write('-'*30)
f.close()


    
