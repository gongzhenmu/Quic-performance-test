import os
import subprocess

iterations = int(os.sys.argv[1]) if len(os.sys.argv) > 1 else 5
calculateAverage = int(os.sys.argv[2]) if len(os.sys.argv) > 2 else 0
command = './quicWebTestOne.sh '

videoFiles = []
target_dir = "/workdir/quic-data"
subfolders = [ f.path for f in os.scandir(target_dir) if f.is_dir() ]

for i in subfolders:
    folderName = i.split("/")[-1]
    finalCommand = command + folderName
    for i in range(iterations):
        subprocess.run(finalCommand, shell=True)
        #print(finalCommand)
    if calculateAverage == 2:
        subprocess.run("python3 averageTime.py Webtimestamp.log >> quicWebResult.log", shell=True)
# Calculate average time 
if calculateAverage == 1:
    subprocess.run("python3 averageTimeRaw.py Webtimestamp.log > quicWebResult.log", shell=True)
