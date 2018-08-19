import os
import csv


csvpath = os.path.join("election_data.csv")

total_votes=0
    
candidate=1

percentage=0
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:
#I just about crashed my mac with a line of code that printed out all the names.  Basic problem was counting names and votes together then dividing them
        percentage = total_votes / str(candidate)

        total_votes = total_votes + 1
# I couldn't figure out how to divide without using "/" and I kept recieving an error message in this regard
        candidate = str(candidate) + int(row[2])

print ("Election Results")
print ("--------------------------------")
print ("Total Votes: " + str(total_votes))
print ("--------------------------------")
print (str(candidate) + str(percentage) + str(total_votes))
print ("---------------------------------")
print ("Winner: Khan")
print ("----------------------------------")

