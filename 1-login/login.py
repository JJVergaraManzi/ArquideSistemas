#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket  
import os
import sys

# Do the import
from conect import *
#query de la consulta de un paciente mediante rut 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
s.connect(("localhost", 5000)) 
s.send(bytes('00010sinitlogin','utf-8'))
recibido=s.recv(4096)
print(recibido)

while True:
    datos = s.recv(4096)
    if datos.decode('utf-8').find('login'):
        #decodificar el mensaje
        datos = datos[10:]
        target = datos.decode()
        print(target)
        data = target.split()


        consulta = f"SELECT  funcionarios.rut, funcionarios.especialidad FROM funcionarios WHERE funcionarios.rut = '{data[0]}' AND funcionarios.especialidad = '{data[1]}'"
        respuesta = consultar(consulta)
        respuesta='login'+str(respuesta)
        print(respuesta)
        temp=llenado(len(respuesta))  
        print('tmp: ', temp)
        print('tmp + respuesta:',temp+respuesta)
        s.send(bytes(temp+respuesta,'utf-8'))

        

        #realizar la operacion de buscar en la bd
        
        

        #crear mensaje de respuesta
        print("envia3")
    else:
        pass
    
s.close()

