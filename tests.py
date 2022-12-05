import os
import subprocess
from subprocess import Popen, PIPE

# change to src
wd = "./depot_tools/src"
password = "qwer1234"

r1 = subprocess.run(["mkdir", "-p", "$HOME/.pki/nssdb"], 
                stderr=subprocess.PIPE, text=True, 
                cwd = wd)
print(r1.stderr)

# r2 = subprocess.run(["certutil", "-d", "$HOME/.pki/nssdb", "-N"], 
#                 stderr=subprocess.PIPE, text=True,
#                 cwd = wd)
# print(r2.stderr)
p = Popen(["certutil", "-d", "$HOME/.pki/nssdb", "-N"], 
            stdin=PIPE, stderr=PIPE, stdout=PIPE, text=True, cwd=wd)
p.stdin.write(password + "\n")
p.stdin.flush()
print(p.stdout.read())
print('exit code:', p.wait())

# prompt1 = p.communicate(password + '\n')
# print(prompt1[0])
# prompt2 = p.communicate(password + '\n')
# print(prompt2[0])

# r3 = subprocess.run(["certutil", "-d", "sql:$HOME/.pki/nssdb", 
#                 "-A", "-t", "C,,", "-n", "quic_cert",
#                 "-i", "net/tools/quic/certs/out/2048-sha256-root.pem"], 
#                 stderr=subprocess.PIPE, text=True,
#                 cwd = wd)
# print(r3.stderr)
p = Popen(["certutil", "-d", "sql:$HOME/.pki/nssdb", 
                "-A", "-t", "C,,", "-n", "quic_cert",
                "-i", "net/tools/quic/certs/out/2048-sha256-root.pem"], 
            stdin=PIPE, stderr=PIPE, stdout=PIPE, text=True, cwd=wd)
p.stdin.write(password + "\n")
p.stdin.flush()
print(p.stdout.read())
print('exit code:', p.wait())


# certutil -d $HOME/.pki/nssdb -N

# certutil -d sql:$HOME/.pki/nssdb -A -t "C,," -n quic_cert \
# -i net/tools/quic/certs/out/2048-sha256-root.pem

# subprocess.run(["ls", "-la"])

# ./out/Debug/quic_client --host=10.0.0.1 --port=6121 --allow_unknown_root_cert https://www.example.org/
