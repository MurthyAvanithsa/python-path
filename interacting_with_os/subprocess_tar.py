
import subprocess

command = ["tar", "-czvf", "backup.tar.gz", "/Users/murthyavanithsa/Downloads/bkp_last_three_months/"]

print " ".join(command)

try:
    output = subprocess.check_output(command)
    print "Created tar"
except subprocess.CalledProcessError:
    print "Error while executing"