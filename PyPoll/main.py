import csv
import sys

# Define input and output file paths
input_file = "/Users/divya/python-challenge/PyPoll/Resources/election_data.csv"
output_file = "/Users/divya/python-challenge/PyPoll/Analysis/election_results.txt"

try:
    # Read the CSV file
    with open(input_file, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip header
        next(csvreader)

        # Initialize variables
        total_votes = 0
        candidates = {}
        winner = ""

        # Count total votes and tally votes for each candidate
        for row in csvreader:
            total_votes += 1
            candidate_name = row[2]
            if candidate_name not in candidates:
                candidates[candidate_name] = 1
            else:
                candidates[candidate_name] += 1

    # Find the winner
    max_votes = 0
    for candidate, votes in candidates.items():
        if votes > max_votes:
            max_votes = votes
            winner = candidate

    # Calculate percentage of votes for each candidate
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        candidates[candidate] = {"votes": votes, "percentage": percentage}

    # Print results to terminal
    print()
    print("Election Results")
    print("______________________________")
    print(f"\nTotal Votes: {total_votes}")
    print("______________________________\n")
    for candidate, data in candidates.items():
        print(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})")
    print("______________________________\n")
    print(f"Winner: {winner}")
    print("______________________________")

    # Write results to a text file
    with open(output_file, "w") as txtfile:
        txtfile.write("\nElection Results\n")
        txtfile.write("______________________________\n")
        txtfile.write(f"\nTotal Votes: {total_votes}\n")
        txtfile.write("______________________________\n\n")
        for candidate, data in candidates.items():
            txtfile.write(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})\n")
        txtfile.write("______________________________\n\n")
        txtfile.write(f"Winner: {winner}\n")
        txtfile.write("______________________________\n")

except FileNotFoundError:
    print("Error: Input file not found. Please provide the correct file path.")
    sys.exit(1)
except Exception as e:
    print("An error occurred:", e)
    sys.exit(1)
