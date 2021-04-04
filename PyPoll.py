# The data we need to retreive:
     # 1. The total number of votes cast
     # 2. A complete list of candidates who received votes
     # 3. The total number of votes each candidate won
     # 4. The percentage of votes each candidate won
     # 5. The winner of the election based on popular vote

# Add Dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

#Create a filename variable to save to 
file_to_save = os.path.join("Analysis","election_analysis.txt")

# Initialize totalvote counter
total_votes = 0

#Intial the candidate options 
candidate_options = []

# Declare dictionary (empty)
candidate_votes = {}

# Winning Candidate
winner = ""
winner_count = 0
winner_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     
     # Read and print the header row.
     headers = next(file_reader)
     #print(headers)

     # Print each row in the CSV file.
     for row in file_reader:
        
        #Add to the totalvotes
        total_votes += 1

        #Print Candidate Name
        candidate_name = row[2]

        #Add Candidate Name to Candidate Options (if unique) & intialize their votes
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        # track candidate votes with the for loop
        candidate_votes[candidate_name] += 1 



#Print total votes, candidate options
print(total_votes)
print(candidate_options)
print(candidate_votes) 

# Determine Percentage of votes for each candidate
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning count and candidate by comparing votes to winning count
    if (votes > winner_count) and (vote_percentage > winner_percentage):
        winner_count = votes
        winner_percentage = vote_percentage
        winner = candidate_name

winner_summary = (
    f"-------------------------\n" 
    f"Winner: {winner}\n"
    f"Winning Vote Count: {winner_count:,}\n"
    f"Winning Percentage: {winner_percentage:.1f}%\n"
    f"-------------------------\n" )
print(winner_summary)

# Close the file.
election_data.close()

# Using open() function with the "w" mode we will write data to the file
output = open(file_to_save, "w")

# Write some data to the file.
output.write("Counties in the Election\n------------------\nArapahoe\nDenver\nJefferson")

# Close the file
output.close()
