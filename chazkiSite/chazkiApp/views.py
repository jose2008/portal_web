from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.shortcuts import render



hashVehiculo = {}


def preProcesarData():
	'''aqui creamos una tabla hash de implementos de vehiculos(solo debe de hacerse una sola vez)'''
	global hashVehiculo 
	for i in listVehiculos:
		if listVehiculos[i].cargaMudanza == True: 
			hashVehiculo['mudanza'].append(listVehiculos[i])
		if listVehiculos[i].cargaMudanza == True: 
			hashVehiculo['bebe'].append(listVehiculos[i])
		if listVehiculos[i].cargaMudanza == True: 
			hashVehiculo['animal'].append(listVehiculos[i])




def insertarEnHash(vehiculo):
	''' cuando se registra un nuevo vehiculo, este debe ingresarse en una tabla hash(en python son diccionarios), para su facíl acceso'''
	if vehiculo.cargaMudanza == True: 
		hashVehiculo['mudanza'].append(vehiculo)
	if vehiculo.portaBebe == True: 
		hashVehiculo['bebe'].append(vehiculo)
	if vehiculo.portaAnimal == True: 
		hashVehiculo['animal'].append(vehiculo)






def obtenerVehiculos(params):
	''' función para obtener un conjunto de vehiculos que cumpla con los requerimientos(uso un ejemplo con 3 requerimientos)'''
	list_vehiculos_aptos = set()
	for i1 in hashVehiculo['mudanza']:
		list_vehiculos_aptos.push(i1)
	for i1 in hashVehiculo['bebe']:
		list_vehiculos_aptos.push(i1)
	for i1 in hashVehiculo['animal']:
		list_vehiculos_aptos.push(i1)

	return list_vehiculos_aptos




# Create your views here.

def index(request):
	''' solo esta función para renderizar la página de inicio'''
	return render_to_response('index.html')




def obtieneVehiculos(request):
	
	


	
	return HttpResponse(json.dumps(data))