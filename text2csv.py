import csv

# Open the text file
with open('text_file.txt', 'r') as text_file:
  # Read the lines of the file
  lines = text_file.readlines()

# Open the CSV file
with open('text_file.csv', 'w', newline='') as csv_file:
  # Create a CSV writer
  writer = csv.writer(csv_file, delimiter='|')

  # Iterate over the lines and write them to the CSV file
  for line in lines:
    writer.writerow(line.split())
