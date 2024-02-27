# python-challenge
## This Python script analyzes financial and election data for a fictional company. It combines functionalities for both PyBank and PyPoll.

## Features
* PyBank Analysis: Analyzes financial records to calculate total months, total profits/losses, average change, greatest increase in profits, and greatest decrease in losses.
* PyPoll Analysis: Analyzes election data to calculate total votes, each candidate's total votes and percentage of votes, and determine the winner.

# PyPoll Election Analysis
## Overview
PyPoll Election Analysis is a Python script designed to analyze the results of an election. It reads in a CSV file containing voter data and calculates various election metrics, including total votes cast, each candidate's total votes, percentage of votes received by each candidate, and the winner of the election. The analysis results are printed to the terminal and exported to a text file.

## Requirements
Python 3.x
CSV file containing election data with columns: "Voter ID" and "Candidate"

## Usage
1. Place the CSV file containing election data in the specified folder.
2. Update the data_folder and analysis_folder variables in the script to point to the correct file paths for input and output.
3. Run the Python script (main.py).

## File Structure
* PyPoll/main.py : Python script for election analysis.
* PyPoll/Resources : Folder containing the CSV file with election data.
* Analysis/: Folder where the analysis results will be exported as a text file.
* election_analysis.txt: Text file containing the exported analysis results.

## Output
The script will print the election analysis results to the terminal in the following format:

<img width="288" alt="image" src="https://github.com/divya-jindal/python-challenge/assets/10901784/efc78307-a137-4e66-af36-deb3c938424e">

Additionally, the analysis results will be exported to a text file named election_analysis.txt in the "Analysis" folder.

# PyBank Financial Analysis
## Overview
PyBank Financial Analysis is a Python script designed to analyze the financial records company. It reads in a CSV file containing financial data and calculates various financial metrics, including total months, net total profit/loss, average change in profit/loss, greatest increase in profits, and greatest decrease in profits. The analysis results are printed to the terminal and exported to a text file.

## Requirements
* Python 3.x
* CSV file containing financial data with columns: "Date" and "Profit/Losses"

## Usage
1. Place the CSV file containing financial data in the specified folder.
2. Update the data_folder and analysis_folder variables in the script to point to the correct file paths for input and output.
3. Run the Python script (main.py) in the PyBank folder

## File Structure
* PyBank/main.py : Python script for financial analysis.
* PyBank/Resources : Folder containing the CSV file with financial data.
* PyBank/Analysis : Folder where the analysis results will be exported as a text file.
* financial_analysis.txt: Text file containing the exported analysis results.

## Output
The script will print the financial analysis results to the terminal in the following format:*

<img width="341" alt="image" src="https://github.com/divya-jindal/python-challenge/assets/10901784/dc369f3c-d89e-4128-a00d-abbc198f8518">

Additionally, the analysis results will be exported to a text file named financial_analysis.txt in the "Analysis" folder.
