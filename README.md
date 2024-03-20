# PyBank

A Python script to analyze the financial records of the company. The script calculates the total number of months, the net total profits or losses, the average change in profits or losses, and the month with greatest increase/decrease and its $ value. As a last step the script creats .txt file with the message containing all the abovementioned data, as well as prints the message to the terminal.

## Dependencies

  - **Python 3**
  - **CSV module**
  - **OS module**

## Setup
Before running the script specify input and output data file paths. The paths are saved to csv_budget and save_path variables.

## Usage

In order to run the skript:

  1) Open script: main.py
  2) Ensure the specified input data path is correct and data is saved in the appropriate location.
  3) Run the script.
  4) Check the message in the terminal.
  5) Access the summary message in the user-selected folder.

## Expected Data Format

~~~
Date,Profit/Losses
Jan-10,1088983
...
~~~

## Results

Generates a Final_Analysis.txt file with **total months**, **total profit/losses**, **average change**, and the **month and $ value of the greatest increase/decrease in profits**. 

_____________________________________________________________________________________________________________________________________________________________________

# PyPoll

A Python script to analyze the votes collected during an election in a small rural town. The script generates a complete list of candidates who received votes. Additionally, it calculates the total number of votes cast and percentage and total number of votes each candidate won. The script then determines a winner of the election based on the popular vote. As a last step the script creats .txt file with the message containing all the abovementioned data, as well as prints the message to the terminal.

## Dependencies

  - **Python 3**
  - **CSV module**
  - **OS module**

## Setup
Before running the script specify input and output data file paths. The paths are saved to csv_election and save_path variables. 

## Usage

  1) Open script: main.py
  2) Ensure the specified input data path is correct and data is saved in the appropriate location.
  3) Run the script.
  4) Check the message in the terminal.
  5) Access the summary message in the user-selected folder.

## Expected Data Format

~~~
Ballot ID,County,Candidate
1323913,Jefferson,Charles Casper Stockham
...
~~~

## Results

Generates a Final_Analysis.txt file with **total votes count**, **percentage and total number of votes** each candidate won, and **the winner** of the election.
