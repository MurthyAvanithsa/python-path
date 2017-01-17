import os
import datetime
from hurry.filesize import size

PATH_TO_WALK = "/Users/murthyavanithsa/Downloads"

for root, dirs, files in os.walk(PATH_TO_WALK):
    folder_size = 0
    for file_obj in files:
        abs_file_name = os.path.join(root,file_obj)
        folder_size += os.path.getsize(abs_file_name)
    print root, size(folder_size)




