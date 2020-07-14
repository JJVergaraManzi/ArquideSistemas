#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket  


def llenado(largo):
    aux = str(largo)
    while len(aux) < 5:
        aux = '0' + aux
    print(aux)
    return aux



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
s.connect(("localhost", 5000)) 
s.send(bytes('00020sinitregis','utf-8'))
recibido=s.recv(4096)
print(recibido)

while True:
    datos = s.recv(4096)
    print(datos)

s.close()