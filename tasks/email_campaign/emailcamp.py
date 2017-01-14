import argparse
import os
import csv
import cgi
import emailtemplates
import settings
import requests


# default file
EMAIL_CSV_FILE = "email_data.csv"

REQUIRED_FIELDS = ["email", "first_name", "last_name"]




# Send email using request object
def send_email(to_address, body):

    request_result = requests.post(url=settings.MAILGUN_URL,
                                   auth=('api', settings.MAILGUN_API_KEY),
                                   data={"to": to_address,
                                         "from": "murthyavanithsa@gmail.com",
                                         "html": body,
                                         "subject": "Happy festivals"})

    return request_result


def create_email_string(first_name):
    return emailtemplates.SIMPLE_EMAIL_TEMPALTE.format(first_name)


def is_row_valid(row, emails_only_list):
    for field in REQUIRED_FIELDS:
        if not field in row:
            return False
        if len(row[field]) <= 0:
            return False
        if len(emails_only_list) > 0:
            if row["email"] not in emails_only_list:
                return False
        return True


# get the current working directory
pwd = os.path.dirname(os.path.realpath(__file__))

# check if a file exists
default_csv_file = os.path.join(pwd, EMAIL_CSV_FILE)


parser = argparse.ArgumentParser(description='A simple email campaign script')


parser.add_argument('-c',
                    default=default_csv_file,
                    help="csv file to parse",
                    dest="csv_file")

parser.add_argument('-n',
                    default=-1,
                    help="no of lines to read",
                    type=int,
                    dest="row_count")

parser.add_argument('-emails',
                    nargs='+',
                    type=str,
                    help="send email to only these emails",
                    dest="emails",
                    default=[])


results = parser.parse_args()

csv_file = results.csv_file


if not os.path.exists(csv_file):
    print "No file found:%s .. exiting" % csv_file
    exit()

# iterate through rows in CSV
with open(csv_file) as csv_file_obj:
    csv_reader = csv.DictReader(csv_file_obj)
    for row in csv_reader:
        if is_row_valid(row, results.emails):
            email_text = create_email_string(row['first_name'])
            res = send_email(to_address=row['email'], body=email_text)
            if res.status_code == 200:
                print "Email sent to {}, status:{}".format(row['email'], res.status_code)
            else:
                print "Error ! while sending email :{} status:{}".format(row['email'], res.status_code)
        else:
            print "found invalid row {}, please check the required fields {} " \
                  "and only_emails_list {}".format(row, REQUIRED_FIELDS, results.emails)



