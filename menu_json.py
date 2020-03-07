#!/usr/bin/python
from funciones import *

def mostrar_menu():
	print("1 - Listar información")
	print("2 - Contar información")
	print("3 - Buscar o filtrar información")
	print("4 - Buscar información relacionada")
	print("5 - Ejercicio libre")
	print("0 - Salir")


mostrar_menu()

menu = int(input("-> "))

while menu != 0:
	if menu == 1:
		# 1 - Listar información
		print("-------------------------------")
		for i in listar_informacion():
			print(i)
	elif menu == 2:
		# 2 - Contar información
		print("-------------------------------")
		for i in contar_informacion():
			print("Nombre: \t",i[0])
			print("Edad: \t\t", i[1])
			print("Total amigos: \t", i[2])
			print("................................")
	elif menu == 3:
		# 3 - Buscar o filtrar información
		color = str(input("Color: "))
		for i in buscar_filtrar_informacion(color):
			print("Nombre: ", i["nombre"] ,"\t Edad: ", i["edad"] ,"\t Genero: ", i["genero"])
			print("..................................................................")
	elif menu == 4:
		# 4 - Buscar información relacionada
		nombre_amigo = str(input("Nombre del amigo: "))
		for i in buscar_informacion_relacionada(nombre_amigo):
			print("Nombre: ", i["nombre"] ,"\t Telefono: ", i["telefono"])
			print("URL foto: ", i["url"])
			print("................................................................")
	elif menu == 5:
		# 5 - Ejercicio libre
		id = str(input("ID: "))
		diccionario = ejercicio_libre(id)
		print("Nombre: ", diccionario['nombre'])
		print("Email: ", diccionario["email"])
		print("Coordenadas: lat-> ", diccionario["coordenadas"][0] ," lon-> ", diccionario["coordenadas"][1])
		print("Tags:")
		for i in  diccionario["tags"]:
			print("----->", i)
	else:
		print("Orden no encontrada.")


	mostrar_menu()
	menu = int(input("-> "))

print("Adios :)")








