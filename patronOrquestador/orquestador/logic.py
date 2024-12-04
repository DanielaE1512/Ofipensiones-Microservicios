import requests
from django.http import JsonResponse


def getEstudiantesMora(id):
    url = f"http://<IP_SERVICIO_B>:PUERTO_ESTUDIANTE/endpoint/{id}/" #TODO
    response = requests.get(url)
    return response

def calcularMora(lista):
    url = "http://<IP_SERVICIO_B>:PUERTO_FINANCIERO/endpoint/" #TODO
    response = requests.post(url, lista)
    return response

def requerimiento(codigo_curso):
    lista = getEstudiantesMora(codigo_curso)
    calculo = calcularMora(lista)
    return JsonResponse(calculo.json(), safe=False) #TODO