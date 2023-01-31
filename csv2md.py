import csv
import os
import sys

def convert_csv_to_md(filename):
    # Open the input file and read its contents
    with open(filename, 'r') as input_file:
        reader = csv.reader(input_file)
        headers = next(reader)
        table = []
        for row in reader:
            table.append(row)

    # Build the markdown table
    output = '| ' + ' | '.join(headers) + ' |\n'
    output += '| ' + ' | '.join(['---' for _ in headers]) + ' |\n'

    for row in table:
        output += '| ' + ' | '.join(row) + ' |\n'

    # Create the output file name by changing the extension from .csv to .md
    output_filename = os.path.splitext(filename)[0] + ".md"

    # Write the table to the output file
    with open(output_filename, 'w') as output_file:
        output_file.write(output)

    # Confirm completion
    print(f"Converted {filename} to {output_filename}")

# Check if a file name argument is provided
if len(sys.argv) == 2:
    # Process the single file specified in the argument
    filename = sys.argv[1]
    convert_csv_to_md(filename)
else:
    # Check if the current working directory contains any .csv files
    if not any(filename.endswith(".csv") for filename in os.listdir(os.getcwd())):
        print("No .csv files found in the current working directory")
        sys.exit()

    # Loop through each file in the current working directory
    for filename in os.listdir(os.getcwd()):
        # Only process .csv files
        if filename.endswith(".csv"):
            convert_csv_to_md(filename)

    print("All .csv files have been processed.")
