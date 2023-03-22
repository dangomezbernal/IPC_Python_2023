#
#
#

import sys, argparse
from subprocess import Popen, PIPE
parser = argparse.ArgumentParser(description ="""Exemple popen""")

parser.add_argument("-d","--database", type=str, dest="database", default="training", help="database a utilitzar")

parser.add_argument("-c","--numclie", type=str, dest="numclie", action="append", help="identificador de client")



args=parser.parse_args()

# print(args.database)
# print(args.numclie)
# exit(0)


#---------------------

cmd = "psql -qtA -F',' -h localhost -U postgres "+ args.database
pipeData = Popen(cmd, shell = True, bufsize=0, universal_newlines=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)


for clie in args.numclie:

    pipeData.stdin.write("select * from clientes where num_clie="+clie+";\n")
    print(pipeData.stdout.readline(), end="")
        
pipeData.stdin.write("\q\n")
sys.exit(0)