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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.connect(("localhost",5000)) 
s.send(bytes('00010sinitsupfu','utf8'))
print("enviado \n")
recibido = s.recv(4096)
print(recibido)


# realizar la operacion de creacion de consulta a la base de datos

while True:
    datos = s.recv(4096)
    print(datos)
    if datos[5:10] == 'supfu':
        datos = datos[10:]
        datos = datos.split()
        print(datos)
       # respuesta='supfu'+add_producto(int(datos[0]), datos[1], int(datos[2]))  
        #print(respuesta)
        #temp=llenado(len(respuesta))  
        #print('tmp: ', temp)
        #print('tmp + respuesta:',temp+respuesta)
        #s.send(bytes(temp+respuesta,'utf-8'))
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