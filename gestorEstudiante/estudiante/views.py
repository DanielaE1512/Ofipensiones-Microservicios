from django.shortcuts import render
import estudiante.logic as estudiante_logic
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

@api_view(["POST"])
def crearEstudiante(request):
    if request.method == "POST":
        try:
            data = JSONParser().parse(request)
            estudiante = estudiante_logic.createEstudiante(data)
            response = {
                "objectId": str(estudiante.id),
                "message": f"Estudiante {estudiante.nombre} creado en la base de datos"
            }
            return JsonResponse(response, safe=False)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)
        
@api_view(["GET"])
def obtenerEstudiantesMora(request, codigo_curso):
    if request.method == "GET":
        try:
            lista = estudiante_logic.getEstudiantesMora(codigo_curso)
            return JsonResponse(lista, safe=False)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
        


@api_view([ "DELETE"])
def deleteAllEstudiantes(request):
    if request.method == "DELETE":
        estudiante_logic.deleteAll()
        respo = {
            "Mensaje ": "Se borraron todos los estudiantes"
        }
        return JsonResponse(respo, safe=False)