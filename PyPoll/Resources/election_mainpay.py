
"""PyPoll Homework Solution."""

# Import required packages

import csv
import os

file_to_load = os.path.join("election_data.csv")

total_votes = 0
all_candidates = []
votes = {}
candidate = ""
popular_count = 0
with open(file_to_load) as election_data:
   reader = csv.reader(election_data)
   header = next(reader)
   for row in reader:
       
       total_votes = total_votes + 1
       candidate_name = row[2]
       if candidate_name not in all_candidates:
           all_candidates.append(candidate_name)
           votes[candidate_name] = 0
       votes[candidate_name] = votes[candidate_name] + 1

   election_results = (
       f"\n\nElection Results\n"
       f"-------------------------\n"
       f"Total Votes: {total_votes}\n"
       f"-------------------------\n")
   print(election_results, end="")
   for candidate_1 in votes:
       votes_1 = votes.get(candidate_1)
       vote_percentage = float(votes_1) / float(total_votes) * 100
       if (votes_1 > popular_count):
           popular_count = votes_1
           candidate = candidate_1
       voter_output = f"{candidate_1}: {vote_percentage:.3f}% ({votes_1})\n"
       print(voter_output, end="")
      
   popular_candidate_summary = (
       f"-------------------------\n"
       f"Winner: {candidate}\n"
       f"-------------------------\n")
   print(popular_candidate_summary)

   #set path to write changes to csv
output_file = os.path.join("Poll_Analysis.csv")
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("---------------------\n")
    file.write("Total Votes: %d\n" % total_votes)
    file.write("------------------------\n")
    file.write("%s\n" % voter_output)
    file.write("------------------------\n")
    file.write(f"Winner: {candidate}\n")
    file.write("------------------------\n")  