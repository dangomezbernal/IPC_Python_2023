import sys, argparse
from subprocess import Popen, PIPE
parser = argparse.ArgumentParser(description ="""Exemple popen""")
parser.add_argument("consulta",type=str,help="consulta sql")
args=parser.parse_args()


#---------------------
cmd = "psql -qtA -F',' -h localhost -U postgres training"
pipeData = Popen(cmd, shell=True, bufsize=0, universal_newlines=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)

pipeData.stdin.write(args.consulta+"\n\q\n")

for line in pipeData.stdout:
    print(line, end="")

    
exit(0)