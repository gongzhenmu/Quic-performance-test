import os
import subprocess

command = 'python3 checkConnection.py '

target_dir = os.sys.argv[1]
files = [ f.path for f in os.scandir(target_dir)]
for file in files:
    finalCommand = command + file
    subprocess.run(finalCommand, shell=True)