#data to retrive

# 1. the total number of votes cast
# 2. A complete list of candidates who received votes
# 3. percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. the winner of the election based on popular vote

# dependencies
import csv
import os

# Add our dependencies.

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

    # for row in file_reader:
        
        # print(row)

    # To do: read and analyze the data here.










# print(dir(csv))
# file_to_load = "C:\\Users\\bdodson\\Box\Personal\\School\\Data_Science_UCSD\\Election_Analysis\\Resources\\election_results.csv"
# file_to_load = os.path.join("Resources", "election_results.csv")
# print(file_to_load)

# election_data = open(file_to_load, 'r')

# print(election_data)

# election_data.close()

# with open(file_to_load) as election_data:
#     print (election_data)


# file_to_save = os.path.join("Analysis", "election_analysis.txt")
# # outfile = open(file_to_save, "w")

# # outfile.write("Hello World")

# # outfile.close()

# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Arapahoe\nDenver\nJefferson")
#     # txt_file.write("Denver, ")
#     # txt_file.write("Jefferson")

