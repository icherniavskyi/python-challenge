#Import the dependencies
import csv
import os 

#Create new objects to hold variables for analysis
total_cast = 0
candidates = []
Stockham_count = 0
DeGette_count = 0
Doane_count = 0 

#Set path for file
csv_election = os.path.join("python-challenge", "PyPoll", "Resources", "election_data.csv")

#Open CSV file
with open (csv_election) as csvfile:
    
    csvreader = csv.reader(csvfile)

    #Skip the first raw
    election_header = next(csvreader)

    #Iterate through each row of the CSV
    for row in csvreader:

        #Increase the total votes by 1 for each row
        total_cast += 1

        #Check if candiate's name is not in a list
        if row[2] not in candidates:

            #if not, add to the list
            candidates.append(row[2])
        
        #if candidate name is Stockham, add one vote to their vote count
        if "Stockham" in row[2]:
            Stockham_count +=1
        
        #if candidate name is DeGette, add one vote to their vote count
        elif "DeGette" in row[2]:
            DeGette_count += 1

        #otherwise add one vote to Doane's vote count
        else:
            Doane_count +=1

#Calculate percentage for each candidate and format the values
Stockham_percent = format((Stockham_count/total_cast)*100, ".3f")
DeGette_percent = format((DeGette_count/total_cast)*100, ".3f")
Doane_percent = format((Doane_count/total_cast)*100, ".3f")

#Determine the winner based on most votes
if (Stockham_count > DeGette_count) and (Stockham_count > Doane_count):
    winner = candidates[0]
elif (DeGette_count > Stockham_count) and (DeGette_count > Doane_count):
    winner = candidates[1]
else:
    winner = candidates[2]

#Prepare the output message format
message = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_cast}\n"
    f"-------------------------\n"
    f"{candidates[0]}: {Stockham_percent}% ({Stockham_count})\n"
    f"{candidates[1]}: {DeGette_percent}% ({DeGette_count})\n"
    f"{candidates[2]}: {Doane_percent}% ({Doane_count})\n"
    f"-------------------------\n"
    f"Winner: {winner}\n" 
    f"-------------------------\n"
)

#Print message to the terminal
print(message)

#Create a path to save results
save_path = os.path.join("python-challenge", "PyPoll", "Analysis", "Final_Analysis.txt")

#Create a txt file and wrie ouput message in it
with open(save_path, 'w') as text_file:
    text_file.write(message)
