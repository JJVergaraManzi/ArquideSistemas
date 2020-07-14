import socket  

from conect import *






s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.connect(("localhost",5000)) 
s.send(bytes('00010sinitconli','utf8'))
print("enviado \n")
recibido = s.recv(4096)
print(recibido)

# realizar la operacion de creacion de consulta a la base de datos

while True:
    datos = s.recv(4096)
    print(datos)
    if datos.decode('utf-8').find('conli'):
        #decodificar el mensaje
        datos = datos[10:]
        target = datos.decode()
        print(target)
        data = target.split()
        hr = []
        ids = []
        hrex = []





        consulta = f"SELECT  consultas.hora, consultas.id FROM consultas WHERE consultas.hora = '{data[0]}'"
        respuesta = consultar(consulta)

        for h,i in respuesta:
            hr.append(h)
            ids.append(i)

        
        consulta2 =  f"select examenes.hora from examenes,diagnosticos,consultas where examenes.diagnosticos_id = diagnosticos.id and diagnosticos.consultas_id = consultas.id and consultas.rut_paciente = '{data[0]}';";
        


        
        respuesta2 = 'conli'


        respuesta='conli'+str(respuesta)
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
    #elif datos == 'quit':
    #    print ("adios")
    #    s.shutdown()
    #    for sock in s:
    #        sock.close() 
    #    break

s.close()