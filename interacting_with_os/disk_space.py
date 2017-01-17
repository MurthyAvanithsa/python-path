import subprocess

command = ["/bin/df", "-h"]

process = subprocess.Popen(command, stdout=subprocess.PIPE)
out, err = process.communicate()

df_out_list = out.split("\n")
for line in df_out_list:
    print line.split()


