# construir un server en el puerto 50001 que sea un echo server
import sys, socket
HOST = ''
PORT = 50001

# objeto que representa la idea de un socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_DGRAM es para UDP

# la s ya se convierte en una conexión
s.connect((HOST,PORT))

#info que envia
s.send(b'Hello, world')

#lo que recibe (escucha)
data = s.recv(1024)

#cierra la conexión
s.close()

#devuelve lo q ha recibido
print('Recived', repr(data))
sys.exit(0)