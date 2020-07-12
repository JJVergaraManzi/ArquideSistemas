import threading
import socket

host = 'localhost'
port = 5000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
nCuenta = ""
monto = ""
mensaje = ""

s.connect((host,port))

respuesta = s.recv(1000)

print("Resultado: ", respuesta)
s.close()