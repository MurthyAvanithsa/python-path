import subprocess

#command = ["ps", "aux"]
command = ["/bin/df", "-h"]

result = subprocess.call(command)
if result is not 0:
    print "Error while executing"
else:
    print "Return Code", result
