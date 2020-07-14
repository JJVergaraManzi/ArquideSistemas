import socket  
import os
import sys

from conect import *

conexion()
cerrar()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.connect(("localhost",5000)) 
s.send(bytes('00010sinitadddi','utf8'))
print("enviado \n")
recibido = s.recv(4096)
print(recibido)



# realizar la operacion de creacion de consulta a la base de datos

while True:
    datos = s.recv(4096)
    print(datos)
    if datos.decode('utf-8').find('adddi'):
        datos = datos[10:]
        datos = datos.split()
        print(datos)
        print("envia3")
    else:
        pass
    #elif datos == 'quit':
    #    print ("adios")
    #    s.shutdown()
    #    for sock in s:
    #        sock.close() 
    #    break

s.close()