import socket
import sys
# "" ejemplo de conexion al bus , es la conexion a socket""

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))

# default port for socket
port = 80



s.connect(("www.google.com", port))
#s.connect(("200.14.84.235", 5000)) co eso se conecta 
#s.send('Hello world'.encode())
print ("the socket has successfully connected on port: ", port )
recibido = s.recv(4096)
print(recibido)
