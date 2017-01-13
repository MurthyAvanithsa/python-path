#!/usr/bin/env python

import argparse

# define argument parser
parser = argparse.ArgumentParser(description='A simple email campaign script')

# Add arguments
parser.add_argument('-c',
                    default="email_data.csv",
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
                    dest="emails")


arguments = parser.parse_args()

print "csv file:", arguments.csv_file, "type:", type(arguments.csv_file)

print "row count:", arguments.row_count, "type:", type(arguments.row_count)

print "emails", arguments.emails, "type:", type(arguments.emails)



