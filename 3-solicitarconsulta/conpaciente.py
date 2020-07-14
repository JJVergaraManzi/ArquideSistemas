import socket  
import os
import sys
scriptpath = "/home/nico/Escritorio/trabajoarqui/ArquideSistemas/"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
# Do the import
from conect import *




#query de la consulta de un paciente mediante rut 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.connect(("localhost",5000)) 
s.send(bytes('00010sinitconpa', 'utf-8'))
recibido = s.recv(4096)
print(recibido)

while True:
    datos = s.recv(4096)
    if datos.decode('utf-8').find('conpa'):
        #decodificar el mensaje
        datos = datos[10:]
        target = datos.decode()
        print(target)

        #realizar la operacion de buscar en la bd

        consulta = f"SELECT  consultas.rut_paciente FROM consultas WHERE consultas.rut_paciente = '{data[0]}'"
        respuesta = consultar(consulta)
        respuesta='conpa'+str(respuesta)
        print(respuesta)
        temp=llenado(len(respuesta))  
        print('tmp: ', temp)
        print('tmp + respuesta:',temp+respuesta)
        s.send(bytes(temp+respuesta,'utf-8'))
        
        

        #crear mensaje de respuesta
        print("envia3")
    else:
        pass
    



# realizar la operacion de creacion de consulta a la base de datos

s.close()