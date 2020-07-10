import socket 
import time 
import sys

sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockets.connect(("200.14.84.235", 5000))
sockets.send('00005getsv')
#print("enviado")
recibido = sockets.recv(4096)
#print("recibiendo")
#print(recibido)

#doctor  ya registrado y que este en la BD
while True:
	#print('\n')
	opcion = input("""Que servicio desea
	1.- solicitar diagnostico de consulta
	2.- registrar diagnostico de consulta
	3.- login para los funcionarios de salud
	4.- registrar paciente lista de espera
    5.- registrar funcionario de salud
    \n""")
	if(opcion=="1"):
		print("Ha seleccionado 'Agregar producto'")
		#print("entramos al while, enviamos getsv")
		#mensaje='00010getsv'
		#sv = raw_input("> ")
		s.send('00010getsvaddpr')
		datos = input("Escribir Id, Nombre y Stock separados por espacios: \n")
		temp=llenado(len(datos+'addpr'))
		mensaje=temp+'addpr'+datos
		s.send(mensaje)
		recibido=s.recv(4096)
		#print(recibido)
		recibido= s.recv(4096)
		#print("recibiendo:")
		print(recibido[12:])

	if opcion == '2':
		print("Ha seleccionado 'Eliminar producto por id'")
		#print("entramos al while, enviamos getsv")
		#mensaje='00010getsv'
		#sv = raw_input("> ")
		s.send('00010getsvdelet')
		datos=input("Escribir id producto y cantidad: \n")
		temp=llenado(len(datos+'delet'))
		mensaje=temp+'delet'+datos
		s.send(mensaje)
		recibido=s.recv(4096)
		#print('recibido', recibido)
		recibido = s.recv(4096)
		#print('recibido', recibido)
		#print("recibiendo:")
		print(recibido[12:])

	if opcion == '3':
		print("Ha seleccionado 'Consulta stock de productos'")
		s.send('00010getsvStock')
		datos = input('Ingrese el nombre del producto a buscar:\n')
		temp = llenado(len(datos+'Stock'))
		mensaje=temp+'Stock'+datos
		s.send(mensaje)
		recibido = s.recv(4096)
		#print(recibido)
		recibido=s.recv(4096)
		#print(recibido)
		if recibido[12:]=='ss':
			print('El producto no esta ingresado en la bodega\n')
		else:
			cant = int(recibido[12:])
			print('La cantidad del producto '+datos+' es: '+str(cant))
		#for i in range(0, cant):
		#	recibido = s.recv(4096)
		#	print(recibido[10:])

	if opcion == '4':
		#print('entramos al if 4')
		s.send('00010getsvConpr')
		datos = input('Ingrese el nombre del producto a buscar: \n')
		temp = llenado(len(datos+'Conpr'))
		mensaje=temp+'Conpr'+datos
		s.send(mensaje)
		recibido = s.recv(4096)
		#print('primer recibido\n')
		#print(recibido)
		recibido=s.recv(4096)
		#print('segundo recibido\n')
		#print(recibido)
		#print(recibido[12:14])
		if recibido[12:14]=='ss':
			print('El producto no esta ingresado en la bodega\n')
		else:
			datos=recibido[13:]
			datos = datos.split()
			#print(datos)
			cant_pr=len(datos)/3
			resultado=[]
			test=True
			i=0
			y=0
			while test:
				resultado.append(datos[0+i]+'   '+datos[i+1]+'    '+datos[i+2])
				i=i+3
				y=y+1
				if(y==cant_pr):
					test=False
			print('Id   Nombre   Stock')
			for i in range(0,len(resultado)):
				print(resultado[i])
			print('\n')

		#for i in range(0, cant):
		#	recibido = s.recv(4096)
		#	print(recibido[10:])
	elif opcion == 'quit':
		s.send('quit')
		time.sleep(5)
		break

print("adios")

s.close()
