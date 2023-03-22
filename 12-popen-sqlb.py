import sys, argparse
from subprocess import Popen, PIPE

#---------------------
command = "psql -qtA -F',' -h localhost -U postgres training -c 'select * from oficines;'"
pipeData = Popen(command,shell=True,stdout=PIPE)

for line in pipeData.stdout:
    print(line.decode("utf-8"),end="")

    
exit(0)