import csv

with open('csv/test.csv', 'r')as f:
  csv_reader = csv.reader(f)
  for lines in csv_reader:
        print(lines)