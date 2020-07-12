import socket
import time

def llenado(largo):
    aux = str(largo)
    while len(aux) < 5:
        aux = '0' + aux
    print(aux)
    return aux


ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.connect(("localhost", 5000))
ss.send('00005getsv'.encode())
print(" evento de conexion enviado")
recibido = ss.recv(4096)
print("recibiendo respuesta de conexion...")
print(recibido)


while True:
    opcion = input("""Que servicio desea
	1.- iniciar sesión funcionario 
	2.- registrar  consulta
	3.- solicitar  consulta por rut de paciente
	4.- registrar funcionario de salud
    5.- consulta de lista de espera
    6.- registrar orden de examen a paciente (pide rut)
    7.- solicitar orden de examen de paciente
    8.- registrar diagnostico de paciente
    9.- solicitar diagnostico de paciente

    0.- salir
	\n""")
    if(opcion == "1"):
        print("Ha seleccionado la opcion 'iniciar sesión de funcionario '")
        ss.send('00010getsvinmed'.encode())
        datos = input(
            " favor escribir su Nombre , rut sin puntos ni dv y especialidad separados por espacios: \n")
        temp = llenado(len(datos+'addpr'))
        mensaje = temp+'addpr'+datos
        ss.send(mensaje.encode())
        recibido = ss.recv(4096)
        # print(recibido)
        recibido = ss.recv(4096)
        # print("recibiendo:")
        print(recibido[12:])

    if(opcion == 2):
        print("Ha seleccionado 'registrar consulta'")
        # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1

        ss.send('00010getsvaddcon'.encode())
        datos = input(
            "Escribir nombre de paciente, rut, provision, fecha(dd/mm/aaa) y hora(hh:mm) separado por espacios: \n")
        temp = llenado(len(datos+'addcon'))
        mensaje = temp + 'delet' + datos
        ss.send(mensaje.encode())
        recibido = ss.recv(4096)
        #print('recibido', recibido)
        recibido = ss.recv(4096)
        #print('recibido', recibido)
        # print("recibiendo:")
        print(recibido[12:])

    if(opcion == 3):
        print("Ha seleccionado la opcion: 'solicitar consulta': \n")
        # se debe estar con sesión iniciada de entes, luego mover esto al if de op 1
        # la duda es con los eventos de conexion porque son "anidados"
        print("enviando evento de conexion ... \n")
        ss.send('00010getsvcon')

        datos = input("Escribir rut de paciente ( formato: 1111111-1): \n")

        # agregar condicion de verificacion (que este bien escrito)

        aux = llenado(len(datos+'con'))
        mensaje = aux + 'con' + datos
        s.send(mensaje)
        recibido = ss.recv(4096)
        print('recibido', recibido)
        recibido = ss.recv(4096)
        print('recibido: ', recibido)
        print("recibiendo:")
        print(recibido[12:])

    if(opcion == 4):
        print("Ha seleccionado 'registrar funcionario'")
        # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1

        ss.send('00010getupfun')
        datos = input(
            "Escribir nombre , rut, especialidad  separado por espacios: \n")
        temp = llenado(len(datos+'upfun'))
        mensaje = temp + 'upfun' + datos
        ss.send(mensaje)
        recibido = ss.recv(4096)
        #print('recibido', recibido)
        recibido = ss.recv(4096)
        #print('recibido', recibido)
        # print("recibiendo:")
        print(recibido[12:])

    if(opcion == 5):
        print("Ha seleccionado 'consultar paciente en lista de espera'")
        # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1

        ss.send('00010getsaddex')
        datos = input(
            "escribir hora, tipo de examen y rut del paciente separado por espacios (11111111): \n")
        temp = llenado(len(datos+'addex'))
        mensaje = temp + 'addex' + datos
        ss.send(mensaje)
        recibido = ss.recv(4096)
        #print('recibido', recibido)
        recibido = ss.recv(4096)
        #print('recibido', recibido)
        # print("recibiendo:")
        print(recibido[12:])

    if(opcion == 6):
        print("Ha seleccionado 'registrar orden de examen'")
        # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1

        ss.send('00010getsaddex')
        datos = input(
            "escribir hora, tipo de examen y rut del paciente separado por espacios (11111111): \n")
        temp = llenado(len(datos+'addex'))
        mensaje = temp + 'addex' + datos
        ss.send(mensaje)
        recibido = ss.recv(4096)
        #print('recibido', recibido)
        recibido = ss.recv(4096)
        #print('recibido', recibido)
        # print("recibiendo:")
        print(recibido[12:])

    if(opcion == 7):
        print("Ha seleccionado 'consultar orden de examen'")
        # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1

        ss.send('00010getsvex')
        datos = input("Escribir rut de paciente (11111111): \n")
        temp = llenado(len(datos+'con'))
        mensaje = temp + 'con' + datos
        ss.send(mensaje)
        recibido = ss.recv(4096)
        #print('recibido', recibido)
        recibido = ss.recv(4096)
        #print('recibido', recibido)
        # print("recibiendo:")
        print(recibido[12:])

    if(opcion == 8):
        print("Ha seleccionado 'registrar paciente '")
        # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1

        ss.send('00010getsaddig')
        datos = input("los datos de la tabla: \n")
        temp = llenado(len(datos+'adddig'))
        mensaje = temp + 'adddig' + datos
        ss.send(mensaje)
        recibido = ss.recv(4096)
        #print('recibido', recibido)
        recibido = ss.recv(4096)
        #print('recibido', recibido)
        # print("recibiendo:")
        print(recibido[12:])

    if(opcion == 9):
        print("Ha seleccionado 'consultar paciente en lista de espera'")
        # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1

        ss.send('00010getsvdig')
        datos = input("datos del diagnostico: \n")
        temp = llenado(len(datos+'dig'))
        mensaje = temp + 'dig' + datos
        ss.send(mensaje)
        recibido = ss.recv(4096)
        #print('recibido', recibido)
        recibido = ss.recv(4096)
        #print('recibido', recibido)
        # print("recibiendo:")
        print(recibido[12:])

    if(opcion == 0):
        ss.send('quit')
        time.sleep(5)
        break

print("ha cerrado terminal")
ss.close()
