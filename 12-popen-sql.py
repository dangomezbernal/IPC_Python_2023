import sys, argparse
from subprocess import Popen, PIPE
parser = argparse.ArgumentParser(description ="""Exemple popen""")
parser.add_argument("sqlStatement",type=str,help="consulta sql")
args=parser.parse_args()


#---------------------
command = [ "psql", "-qtA", "-F','", "-h", "localhost", "-U", "postgres", "training", "-c",  args.sqlStatement]
pipeData = Popen(command, stdout=PIPE)

for line in pipeData.stdout:
    print(line.decode("utf-8"),end="")

    
exit(0)