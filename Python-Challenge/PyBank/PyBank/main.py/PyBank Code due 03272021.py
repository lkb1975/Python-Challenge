#import files for pyBank
import csv
import os

bank = os.path.join('..','Resources','PyBankData.csv')

# Open the CSV
with open(bank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
# Remove the header
    header = next(csvreader)
    
# Create a list of months
    months =[]
    TotalRev = 0
    Diff = 0
    Previous = 0
    AveDiff = []
    
    
    max_diff = 0
    max_dt = ""
    
    min_diff = 0
    min_dt=""
    
    for row in csvreader:
        months.append(row[0])
        TotalRev = TotalRev + int(row[1])
        Diff = int(row[1]) - Previous
        AveDiff.append(Diff)
        Previous = int(row[1])
        
        if Diff > max_diff:
            max_diff = Diff
            max_dt = row[0]
          
        if Diff < min_diff:
            min_diff = Diff
            min_dt = row[0]    
            
            
    avgsum = round(sum(AveDiff[1:])/len(AveDiff[1:]),2)     


# Display the results
print("Financial Analysis")
print("-----------------")
print("Total Months:" + str(len(months)))
print("Total:" + "$" + str(TotalRev))
print("Average Change:" + "$" + str(avgsum))
print("Greatest Increase in Profit: " + str(max_dt) + " $" + str(max_diff))
print("Greatest Decrease in Profit: " + str(min_dt) + " $" + str(min_diff))

# Create the txt file 
f = open("myfile.txt", "w")    
f.write("Financial Analysis")
f.write("-----------------")
f.write("Total Months:" + str(len(months)))
f.write("Total:" + "$" + str(TotalRev))
f.write("Average Change:" + "$" + str(avgsum))
f.write("Greatest Increase in Profit: " + str(max_dt) + " $" + str(max_diff))
f.write("Greatest Decrease in Profit: " + str(min_dt) + " $" + str(min_diff))
f.close()
    




    


