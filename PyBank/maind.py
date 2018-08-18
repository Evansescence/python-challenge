import os
import csv
budget_data.csv = os.path.join('..','Downloads', 'Resources')

with open(csvpath, newline='')as csvfile:

    csvreader =csv.reader(csvfile, delimiter=',')

print (csvreader)
csv_header = next(csvreader)
print(f"This is the header: {csv_header}")