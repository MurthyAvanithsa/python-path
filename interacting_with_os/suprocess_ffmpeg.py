import subprocess

commands = ["/usr/local/bin/ffmpeg", "-i", "/Users/murthyavanithsa/Downloads/video.webm", "/Users/murthyavanithsa/Downloads/video2.mp4"]
output = subprocess.check_output(commands)
print output