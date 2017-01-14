import csv

with open("user_data.csv") as csv_file:
    csv_dic_reader = csv.DictReader(csv_file)
    for row in csv_dic_reader:
        print type(row), row

# dic reader, helps you in reading every row as a dictionary
with open("user_data.csv") as csv_file:
    csv_dic_reader = csv.DictReader(csv_file)
    for row in csv_dic_reader:
        print type(row), row

