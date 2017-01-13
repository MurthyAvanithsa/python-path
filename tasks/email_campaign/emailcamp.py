import argparse
import os
import csv


def create_email_string(first_name):
    return '''
    <b>%s</b>
    <p>Hi there, have a great festival.</p>
    <b>Thank you.</b>
    ''' %(first_name)

# default file
EMAIL_CSV_FILE = "email_data.csv"

# get the courrent working directory
pwd = os.path.dirname(os.path.realpath(__file__))

# check if a file exists
default_csv_file = os.path.join(pwd, EMAIL_CSV_FILE)


parser = argparse.ArgumentParser(description='A simple email campaign script')

parser.add_argument('-c', action="store_true",
                    default=default_csv_file,
                    dest="csv_file",
                    help="CSV file as an input, if skipped will take default CSV in the current working dir")

results = parser.parse_args()

csv_file = results.csv_file

if not os.path.exists(csv_file):
    print "No file found:%s .. exiting" % csv_file
    exit()

with open(csv_file) as csv_file_obj:
    csv_reader = csv.DictReader(csv_file_obj)
    for row in csv_reader:
        if "email" in row:
            email_text = create_email_string(row['first_name'])
            print email_text
            # send_email(email,email_text)
