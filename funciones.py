import json
with open("USUARIOS.json") as fichero:
	datos=json.load(fichero)

# Listar información: Lista los nombres de los usuarios con su correos electrónico.

def listar_informacion():
	lista_usuario=[]
	for i in datos:
		lista_usuario.append("Nombre: "+ i["name"]+ "\t Email: "+ i["email"])
	return lista_usuario


# Contar información: Lista los usuarios con el nombre, la edad y el numero de amigos.

def contar_informacion():
	lista=[]
	for i in datos:
		lista_usuario=[]
		lista_usuario.append(i["name"])
		lista_usuario.append(i["age"])
		lista_usuario.append(len(i["friends"]))
		lista.append(lista_usuario)
	return lista


# Buscar o filtrar información: Pide por teclado un color y lista los usuarios con el
#                               ese color con su nombre, edad y genero.

def buscar_filtrar_informacion(color):
	lista=[]
	for i in datos:
		if i["eyeColor"] == color:
			contenedor={}
			contenedor["nombre"] = i["name"]
			contenedor["edad"] = i["age"]
			contenedor["genero"] = i["gender"]
			lista.append(contenedor)
	return lista



# Buscar información relacionada: Pide un nombre de amigo y busca los usuarios que
#                                 tienen ese amigo, mostrando el nombre, telefono y
#                                 la url de la imagen.

def buscar_informacion_relacionada(nombre_amigo):
	lista=[]
	for i in datos:
		for amigos in i["friends"]:
			if amigos["name"] == nombre_amigo:
				contenedor={}
				contenedor["nombre"] = i["name"]
				contenedor["telefono"] = i["phone"]
				contenedor["url"] = i["picture"]
				lista.append(contenedor)
	return lista


# Ejercicio libre: Pide un id de usuario y muestra el nombre, las coordenadas, email
#                  y los tags de dicho usuario.

def ejercicio_libre(id):
	diccionario={}
	for i in datos:
		if id == i["_id"]:
			diccionario["nombre"] = i["name"]
			cordenadas = [i["latitude"], i["longitude"]]
			diccionario["coordenadas"] = cordenadas
			diccionario["email"] = i["email"]
			diccionario["tags"] = i["tags"]

	return diccionario
