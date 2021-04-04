# Add Dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

#Create a filename variable to save to 
file_to_save = os.path.join("Analysis","election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     
     # Read and print the header row.
     headers = next(file_reader)
     print(headers)
     # The data we need to retreive:
     # 1. The total number of votes cast
     # 2. A complete list of candidates who received votes
     # 3. The total number of votes each candidate won
     # 4. The percentage of votes each candidate won
     # 5. The winner of the election based on popular vote
     # Close the file.
election_data.close()
# Using open() function with the "w" mode we will write data to the file
output = open(file_to_save, "w")
# Write some data to the file.
output.write("Counties in the Election\n------------------\nArapahoe\nDenver\nJefferson")
# Close the file
output.close()
