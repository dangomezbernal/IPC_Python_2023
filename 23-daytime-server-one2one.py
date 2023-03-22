# construir un server en el puerto 50001 que sea un echo server
import sys, socket, argparse
from subprocess import Popen, PIPE
HOST = ''

parser= argparse.ArgumentParser(description="Port que utilitza el server")
parser.add_argument("-p","--port", type=int, dest="port", help="port a utilitzar", metavar="port", default=50001)
args=parser.parse_args()

# objeto que representa la idea de un socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_DGRAM es para UDP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#enlaza el host con el puerto
s.bind((HOST,args.port))

#el server esta escuchando. el 1 da igual, siempre se pone
s.listen(1)

#
conn, addr = s.accept()

#

while True:
    conn, addr = s.accept()
    print("Connected by;", addr)

    command = [ "date" ]
    pipeData = Popen(command, stdout=PIPE)

    for line in pipeData.stdout:
        conn.send(line)
    
    conn.close()
