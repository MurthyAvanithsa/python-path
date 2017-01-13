import argparse

parser = argparse.ArgumentParser(description='A simple email campaign script')

parser.add_argument('-c', action="store_true",
                    default="email.csv",
                    dest="csv_file",
                    help="CSV file as an input, if skipped will take default CSV in the current working dir")

results = parser.parse_args()

print results