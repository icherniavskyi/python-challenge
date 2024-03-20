#Import the dependencies
import csv
import os 

#Create new objects to hold variables for analysis and comperison
total_month = 0
net_total = 0
month_change = []
profit_change_l = []
previous_change = 0
gr_incr = ["", 0]
gr_decr = ["", 0]

#Set path for file
csv_budget = os.path.join("python-challenge", "PyBank", "Resources", "budget_data.csv")

#Open CSV file
with open (csv_budget) as csvfile:
    
    csvreader = csv.reader(csvfile)

    #Skip the first raw
    budget_header = next(csvreader)

    #Iterate through each row of the CSV
    for row in csvreader:
        
       #Increase the value of total month by 1 for each row
       total_month += 1
       
       #Add the Profit/Loss of the month to the net total
       net_total += int(row[1])

       #Calculate the monthly change
       change = int(row[1]) - previous_change

       #Assign new value of the previous change for next iteration
       previous_change = int(row[1])

       #Add monthly change value to the dedicated list  
       profit_change_l.append(change)

       #Add the currently calculated monthn to the dedicated list  
       month_change.append(row[0])
    
       #Compare current change to greatest decrease value, if current is less
       if change < gr_decr[1]:
           #Update greatest decrease value with current change
           gr_decr[0] = row[0]
           #Update the month in which it occured
           gr_decr[1] = change

       #Compare current change to greatest increase value, if current is larger
       if change > gr_incr[1]:
           #Update greatest increase value with current change
           gr_incr[0] = row[0]
           #Update the month in which it occured
           gr_incr[1] = change

#Delete the firs month and profit change value in the lists as irrelevant for average
profit_change_l.pop(0)
month_change.pop(0)

#Calculate and forma the value of average of average change
average = format(sum(profit_change_l)/len(profit_change_l), ".2f")

#Prepare the output message format
message = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_month}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average}\n"
    f"Greatest Increase in Profits: {gr_incr[0]} (${gr_incr[1]})\n"
    f"Greatest Decrease in Profits: {gr_decr[0]} (${gr_decr[1]})\n"
)

#Print message to the terminal
print(message)

#Create a path to save results
save_path = os.path.join("python-challenge", "PyBank", "Analysis", "Final_Analysis.txt")

#Create a txt file and wrie ouput message in it
with open(save_path, 'w') as text_file:
    text_file.write(message)
