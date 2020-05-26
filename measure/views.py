from django.shortcuts import render, HttpResponse
import requests

#def home(request):
   # return render(request, "measure/home.html")
# Create your views here.

def measure(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': '°C', 'value': value}
            response = requests.post('http://backendandrew.azurewebsites.net/medicion/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://backendandrew.azurewebsites.net/medicion/')
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/measure.html", {'measures': measures})

def medicion(request):
    if 'valor' in request.GET:
        fecha = request.GET['fecha']
        origen = request.GET['origen']
        valor = request.GET['valor']
        codigos = request.GET['codigos']
        observacion = request.GET['observacion']

        # Verifica si el value no esta vacio
        if valor:
            # Crea el json para realizar la petición POST al Web Service
            args = {'fecha': fecha, 'origen': origen, 'valor': valor, 'codigos': codigos, 'observacion': observacion}
            print(args)
            response = requests.post('http://backendandrew.azurewebsites.net/medicion/', args)
            # Convierte la respuesta en JSON
            medicion_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://backendandrew.azurewebsites.net/medicion/')
    # Convierte la respuesta en JSON
    medicion = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/medicion.html", {'medicion': medicion})