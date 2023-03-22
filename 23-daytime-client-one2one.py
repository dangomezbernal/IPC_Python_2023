# construir un server en el puerto 50001 que sea un echo server
import sys, socket, argparse

parser= argparse.ArgumentParser(description="Port i server al que conectar")
parser.add_argument("-p","--port", type=int, dest="port", help="port al que conectar", metavar="port", default=50001)
parser.add_argument("-s","--server", type=str, dest="server", help="sserver al que conectar", metavar="server", default="localhost")
args=parser.parse_args()

# objeto que representa la idea de un socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_DGRAM es para UDP

# la s ya se convierte en una conexión
s.connect((args.server,args.port))

#lo que recibe (escucha)

#devuelve lo q ha recibido


data = s.recv(1024)
  
print('Recived', repr(data))

s.close

sys.exit(0)