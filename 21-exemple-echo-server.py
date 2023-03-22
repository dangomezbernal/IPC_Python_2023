# construir un server en el puerto 50001 que sea un echo server
import sys, socket
HOST = ''
PORT = 50001

# objeto que representa la idea de un socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_DGRAM es para UDP

#enlaza el host con el puerto
s.bind((HOST,PORT))

#el server esta escuchando. el 1 da igual, siempre se pone
s.listen(1)

#
conn, addr = s.accept()

#
print("Conn", type(conn), conn)
print("Connected by;", addr)

while True:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)
conn.close
sys.exit(0)

