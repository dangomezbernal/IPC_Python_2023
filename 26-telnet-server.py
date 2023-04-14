# construir un server en el puerto 50001 que sea un echo server
import sys, socket, argparse, os, signal
from subprocess import Popen, PIPE
HOST = ''

parser= argparse.ArgumentParser(description="Port que utilitza el server")
parser.add_argument("-p", "--port", type=int, dest="port", help="port a utilitzar", metavar="port", default=50001)
parser.add_argument("-d", "--debug", action="store_true")
args=parser.parse_args()


# objeto que representa la idea de un socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_DGRAM es para UDP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#enlaza el host con el puerto (¿por que puerto escucha mi servicio? (Host no significa host, se refiere a las interficies del server (looback, enp05, etc.)))
s.bind((HOST,args.port))

#el server esta escuchando. el 1 da igual, siempre se pone
s.listen(1)


while True:
    conn, addr = s.accept()

    while True:
      command = conn.recv(1024)
      if args.debug:
         print("ese culo bota caca")
      if not command: break
      pipeData = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
   
      for line in pipeData.stdout:
         conn.send(bytes(str(line), 'utf-8'))

      for line in pipeData.stderr:
         conn.send(bytes(str(line), 'utf-8'))

      conn.send(bytes(chr(4), 'utf-8'))
    conn.close()
      

# conn.sendall es para asegurarse de que envia el flujo de info