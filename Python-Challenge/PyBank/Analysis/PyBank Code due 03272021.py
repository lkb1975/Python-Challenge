#import files for pyBank
import csv

bank = "C:\\Users\\lkimb\\Python-Challenge\\PyBank\\Resources\\pyBankData.csv"

# Open the CSV
with open(bank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
# Remove the header
    header = next(csvreader)
    
# Need to calculate total number of months
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
print(len(months))
print(TotalRev)
print(AveDiff)
print(avgsum)
print(max_dt, max_diff)
print(min_dt,min_diff)

# Display the results
print("Financial Analysis")
print("-----------------")
print("Total Months:" + str(len(months)))
print("Total:" + "$" + str(TotalRev))
print("Average Change:" + "$" + str(avgsum))
print("Greatest Increase in Profit: " + str(max_dt) + " $" + str(max_diff))
print("Greatest Decrease in Profit: " + str(min_dt) + " $" + str(min_diff))


    
    

    




    


