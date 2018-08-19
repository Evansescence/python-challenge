# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("budget_data.csv")

total_months = 0
total_revenue = 0


# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Loop through looking for the month
    for row in csvreader:	
   	 	
   	 	total_months = total_months + 1
   	 	
   	 	total_revenue = total_revenue + int(row[1])
            
average_change = (int(row[1])) / total_months
# I could not figure out how to determine the greatest increase or decrease below.
greatest_increase = ((int(row[1])-average_change))
greatest_decrease= ((int(row[1])+average_change))
print("Total Months: " + str(total_months))
print("Total: $" + str(total_revenue))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(greatest_increase))
print("Greatest Decrease in Profits: " + str(greatest_decrease))
