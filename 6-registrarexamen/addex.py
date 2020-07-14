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
s.send(bytes('00010getsvaddex','utf-8'))
recibido = s.recv(4096)
print(recibido)

while True:
    datos = s.recv(4096)
    if datos.decode('utf-8').find('addex'):
        #decodificar el mensaje
        datos = datos[10:]
        target = datos.decode()
        print(target)
        data = target.split()
        #realizar la operacion de buscar en la bd
        #indicador que cumple
        r1=[]
        r2 = []



        #paso 1, buscar si el paciente tiene consulta. 
        consulta1 = f"SELECT  consultas.id FROM consultas WHERE consultas.rut_paciente = '{data[0]}'"
        respuesta1 = consultar(consulta)
        if len(respuesta )!= 0:
            for i in respuesta1:
                r1.append(i)

        #paso 2 buscar si se tiene asociado un diagnostico
        consulta2 = f"select diagnosticos.id from diagnosticos, consultas where consultas.id = diagnosticos.consultas_id and consultas.rut_paciente = '{data[0]}';"
        respuesta2 = consultar(consulta2)
        if len(respuesta2 )!= 0:
            for i in respuesta2:
                r2.append(i)

        consulta3 = f"select examenes.id from examenes,diagnosticos,consultas where  consultas.id= diagnosticos.consultas_id and examenes.diagnosticos_id = diagnosticos.id and consultas.rut_paciente = '{data[0]}';"


        

            
        
            
        #si ta
        else:
            answer = 'conpa' + "no_hay_hora _del"


        

        #crear mensaje de respuesta
        print("envia3")
    else:
        pass
    



# realizar la operacion de creacion de consulta a la base de datos

s.close()