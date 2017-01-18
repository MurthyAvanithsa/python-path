import subprocess

command = ["/bin/df", "-h"]
try:
    output = subprocess.check_output(command)
    print output
except subprocess.CalledProcessError:
    print "Error"
