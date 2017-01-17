import os

# traverse root directory, and list directories as dirs and files as files
files_dic = dict()


def get_extension_size(file_with_path):
    extension = os.path.splitext(file_with_path)[1]
    size = os.path.getsize(file_with_path)
    return extension, size

for root, dirs, files in os.walk("/Users/murthyavanithsa/"):
    for file in files:
        file_name = os.path.join(root, file)
        if os.path.exists(file_name):
            extension, size = get_extension_size(file_name)
            if extension in files_dic:
                files_dic[extension] += 1
            else:
                files_dic[extension] = 1
print files_dic

