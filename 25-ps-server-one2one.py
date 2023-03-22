# construir un server en el puerto 50001 que sea un echo server
import sys, socket, argparse, os, signal
from subprocess import Popen, PIPE
HOST = ''

##signals
llista_peers=[]
count=0
##########

parser= argparse.ArgumentParser(description="Port que utilitza el server")
parser.add_argument("-p","--port", type=int, dest="port", help="port a utilitzar", metavar="port", default=50001)
args=parser.parse_args()

#===========================================================================


def mysigusr1(signum, frame):
     print("Aquests son el dispositius que s'han conectat:",llista_peers)
     sys.exit(0)

def mysigusr2(signum, frame):
    print("En total s'han establert",count,"connexions.")
    sys.exit(0)

def mysigterm(signum, frame):
     print("Aquests son el dispositius que s'han conectat:",llista_peers)
     print("En total s'han establert",count,"connexions.")
     sys.exit(0)
    


pid=os.fork()
if pid !=0:
  print("Engegat server:", pid)
  sys.exit(0)


# assignar un handler al senyal
signal.signal(signal.SIGUSR1,mysigusr1) # 10
signal.signal(signal.SIGUSR2,mysigusr2) # 12
signal.signal(signal.SIGTERM,mysigterm) # 15

#===========================================================================


# objeto que representa la idea de un socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_DGRAM es para UDP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#enlaza el host con el puerto (¿por que puerto escucha mi servicio? (Host no significa host, se refiere a las interficies del server (looback, enp05, etc.)))
s.bind((HOST,args.port))

#el server esta escuchando. el 1 da igual, siempre se pone
s.listen(1)


while True:

    conn, addr = s.accept()
    
    llista_peers.append(addr)
    count+=1

    f = open("logs/hola.txt","w")
    
    while True:
      data = conn.recv(1024)
      if not data: break  
      f.write(data)
      f.write("\n")

    f.close()
    conn.close()
