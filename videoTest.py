import os
import subprocess


command = './videoTestOne.sh '

videoFiles = []

for file in os.listdir("/workdir/quic-data/www.example.org"):
    if file.endswith(".mp4"):
        videoFiles.append(file)

for i in videoFiles :
    finalCommand = command + i
    for i in range(0, 10):
        subprocess.run(finalCommand, shell=True)
        #print(finalCommand)


