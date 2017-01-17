import subprocess
import datetime
import os

BASE_DIR ="/Users/murthyavanithsa/Downloads"

archive_name = os.path.join(BASE_DIR, str(datetime.date.today())+".tar.gz")
destination_folder = os.path.join(BASE_DIR, "bkp_last_three_months")
process = subprocess.Popen(["tar", "-czvf", archive_name, destination_folder], stdout=subprocess.PIPE)
out, err = process.communicate()
print out
print process.returncode
