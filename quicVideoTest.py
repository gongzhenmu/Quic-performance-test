import os
import subprocess

calculateAverage = int(os.sys.argv[1])
command = './quicVideoTestOne.sh '

videoFiles = []

for file in os.listdir("/workdir/quic-data/www.example.org"):
    if file.endswith(".mp4"):
        videoFiles.append(file)

for i in videoFiles :
    finalCommand = command + i
    for i in range(0, 5):
        subprocess.run(finalCommand, shell=True)
        #print(finalCommand)
    if calculateAverage == 2:
        subprocess.run("python3 averageTime.py Videotimestamp.log >> quicVideoResult.log", shell=True)
# Calculate average time 
if calculateAverage == 1:
    subprocess.run("python3 averageTime.py Videotimestamp.log > quicVideoResult.log", shell=True)