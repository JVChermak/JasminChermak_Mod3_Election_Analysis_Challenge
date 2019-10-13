# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The total number of votes each candidate won
# 4. The percentage of votes each candidate won
# 5. The winner of the election based on popular vote
# Add our dependencies
import csv
import os
# Assign a variable for the file to load from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to a direct or indirect path to a file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Initialize lists for Candidate Options and County Options.
candidate_options = []
county_options = []
# Create empty dictionaries for candidates and votes, county and votes.
candidate_votes = {}
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Largest County and count tracker
largest_county = ""
county_count = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and perform analysis
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read the header row in the CSV file.
    headers = next(file_reader)
    # Print each row in the csv file
    for row in file_reader:
        # Add to the total vote count.
        total_votes +=1
        # Print the candidate name from each row.
        candidate_name = row[2]
        # Print the county name from each row.
        county_name = row[1]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name from each row.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        # If the county does not match any existing counties...
        if county_name not in county_options:
            # Add the county name from each row.
            county_options.append(county_name)
            # Begin tracking that county's vote count.
            county_votes[county_name] = 0
        county_votes[county_name] += 1
# Using the with statement open a text file to save the results.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"Election Results\n"
        f"-----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each county.
    for county in county_votes:
        # Retriece vote count for each county.
        co_votes = county_votes[county]
        # Calculate percentage for each county.
        co_vote_percentage = float(co_votes) / float(total_votes) * 100
        # Store the county name, vote count, and percentage of votes.
        county_results = (f"{county}: {co_vote_percentage:.1f}% ({co_votes:,})\n")
        # Print county results to terminal
        print(county_results)
        # Save the county results to text file.
        txt_file.write(county_results)

        # Determine largest county turnout.
        if (co_votes > county_count):
            county_count = co_votes
            # Set the largest county equal to county name.
            largest_county = county
    largest_county_summary = (
        f"\n-------------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------------\n")
    print(largest_county_summary)
    # Save largest county name to text file.
    txt_file.write(largest_county_summary)

    # Determine the percentage of votes for each candidate by looping through counts.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Store the candidate name, vote count, and percentage of votes.
        candidate_results = (f'{candidate}: {vote_percentage:.1f}% ({votes:,})\n')
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate.
        # Determine if the voters are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning candidate equal to the candidate's name.
            winning_candidate = candidate
    winning_candidate_summary = (
        f"-------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)