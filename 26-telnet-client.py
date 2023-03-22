# construir un server en el puerto 50001 que sea un echo server
import sys, socket, argparse


parser= argparse.ArgumentParser(description="Port i server al que conectar")
parser.add_argument("-p","--port", type=int, dest="port", help="port al que conectar", metavar="port", default=50001)
parser.add_argument("server", type=str, help="server al que conectar", metavar="server", default="localhost")
args=parser.parse_args()

# objeto que representa la idea de un socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_DGRAM es para UDP

# la s ya se convierte en una conexión
s.connect((args.server,args.port))

while True:
    ordre = input()
    if ordre == "exit":
        break
    s.send(bytes(ordre, 'utf-8'))

    while True:
        data = s.recv(1024)
        if data[-1:] == bytes(chr(4), 'utf-8'):
            print(str(data[:-1]))
            break
        print(str(data))


s.close()
sys.exit(0)