import os
import csv

# Path to the folder containing the budget data CSV file
data_folder = "/Users/divya/python-challenge/PyBank/Resources"
# Path to folder where output needs to be generated
analysis_folder = "/Users/divya/python-challenge/PyBank/Analysis"
budget_data_csv = os.path.join(data_folder, "budget_data.csv")

# Function to calculate financial analysis
def calculate_financial_analysis(csv_path):
    total_months = 0
    net_total = 0
    changes = []
    dates = []
    
    # Read the CSV file
    try:
        with open(csv_path, newline="") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")
            
            # Skip the header row
            next(csvreader)
            
            # Loop through rows in the CSV file
            for row in csvreader:
                # Increment total months
                total_months += 1
                # Add the profit/loss to net total
                net_total += int(row[1])
                # Add profit/loss and date to lists
                changes.append(int(row[1]))
                dates.append(row[0])
    except FileNotFoundError:
        print(f"Error: File '{csv_path}' not found.")
        return None

    # Calculate changes in profit/loss
    change_values = [changes[i + 1] - changes[i] for i in range(len(changes) - 1)]
    # Calculate average change
    average_change = sum(change_values) / len(change_values)
    # Find the greatest increase and decrease in profits
    greatest_increase = max(change_values)
    greatest_decrease = min(change_values)
    
    # Find the corresponding dates for greatest increase and decrease
    increase_date = dates[change_values.index(greatest_increase) + 1]
    decrease_date = dates[change_values.index(greatest_decrease) + 1]
    
    # Prepare the financial analysis as a dictionary
    financial_analysis = {
        "Total Months": total_months,
        "Total": net_total,
        "Average Change": round(average_change, 2),
        "Greatest Increase in Profits": {"Date": increase_date, "Amount": greatest_increase},
        "Greatest Decrease in Profits": {"Date": decrease_date, "Amount": greatest_decrease}
    }
    
    return financial_analysis

# Function to print analysis to the terminal and export results to a text file
def print_and_export_analysis(analysis):
    if analysis is None:
        return

    # Print analysis to the terminal
    print("\nFinancial Analysis")
    print("______________________________________")
    print()
    for key, value in analysis.items():
        if isinstance(value, dict):
            print(f"{key}: {value['Date']} (${value['Amount']})")
        else:
            print(f"{key}: ${value}")
    print()

    # Export results to a text file
    output_file_path = os.path.join(analysis_folder, "financial_analysis.txt")
    with open(output_file_path, "w") as txtfile:
        txtfile.write("\nFinancial Analysis\n")
        txtfile.write("______________________________________\n\n")
        for key, value in analysis.items():
            if isinstance(value, dict):
                txtfile.write(f"{key}: {value['Date']} (${value['Amount']})\n")
            else:
                txtfile.write(f"{key}: ${value}\n")
    print(f"Results exported to: {output_file_path}")

# Main function
def main():
    # Calculate financial analysis
    analysis = calculate_financial_analysis(budget_data_csv)
    # Print analysis to the terminal and export to text file
    print_and_export_analysis(analysis)

# Execute the main function
if __name__ == "__main__":
    main()
