import os
import datetime
from dateutil.relativedelta import *
from stat import *
import shutil

DIR_PATH = "/Users/murthyavanithsa/Downloads"
BKP_DIR = "bkp_last_three_months"

files = os.listdir(DIR_PATH)

if not os.path.exists(os.path.join(DIR_PATH, BKP_DIR)):
    # create a folder
    os.mkdir(os.path.join(DIR_PATH, BKP_DIR))
for file in files:
    stats = os.stat(os.path.join(DIR_PATH,file))
    modified_date = datetime.datetime.fromtimestamp(stats.st_mtime)
    today = datetime.datetime.today()
    # the date in past for 3 months
    three_months_past = today + relativedelta(months=-3)
    if modified_date <= three_months_past:
        file_mode = os.stat(os.path.join(DIR_PATH,file)).st_mode
        if not S_ISDIR(file_mode):
            shutil.copy2(os.path.join(DIR_PATH, file), os.path.join(DIR_PATH, BKP_DIR))
