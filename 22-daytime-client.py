# construir un server en el puerto 50001 que sea un echo server
import sys, socket
HOST = ''
PORT = 50001

# objeto que representa la idea de un socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_DGRAM es para UDP

# la s ya se convierte en una conexión
s.connect((HOST,PORT))

#lo que recibe (escucha)

#devuelve lo q ha recibido

while True:
    data = s.recv(1024)
    if not data: break
    print('Recived', repr(data))
s.close

sys.exit(0)

