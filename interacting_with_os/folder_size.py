import os
from hurry.filesize import size
from operator import itemgetter, attrgetter

# traverse root directory, and list directories as dirs and files as files
folder_size_dic = dict()

for root, dirs, files in os.walk("/"):
    folder_size=0
    for file in files:
        file_name = os.path.join(root, file)
        if os.path.exists(file_name):
            folder_size += os.path.getsize(file_name)
    folder_size_dic[root] = folder_size


sorted_value_keys = sorted(folder_size_dic.items(), key=itemgetter(1), reverse=True)


for i in range(0,5):
    print sorted_value_keys[i][0], size(sorted_value_keys[i][1])



