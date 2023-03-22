# construir un server en el puerto 50001 que sea un echo server
import sys, socket
from subprocess import Popen, PIPE
HOST = ''
PORT = 50001

# objeto que representa la idea de un socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_DGRAM es para UDP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#enlaza el host con el puerto
s.bind((HOST,PORT))

#el server esta escuchando. el 1 da igual, siempre se pone
s.listen(1)

#
conn, addr = s.accept()

#
print("Connected by;", addr)

command = [ "date" ]
pipeData = Popen(command, stdout=PIPE)

for line in pipeData.stdout:
    conn.send(line)
   

conn.close
sys.exit(0)

