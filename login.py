#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket  


def llenado(largo):
    aux = str(largo)
    while len(aux) < 5:
        aux = '0' + aux
    print(aux)
    return aux



#query de la consulta de un paciente mediante rut 

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sc.connect(("localhost",5000)) 
sc.send('00010sinitlogin')
print("enviado \n")
recibido = sc.recv(4096)
print(recibido)



# realizar la operacion de creacion de consulta a la base de datos

s.close()