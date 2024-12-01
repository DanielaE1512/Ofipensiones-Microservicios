from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from cursos.models import Curso


from gestorUI.gestorUI.auth0backend import getRole

def crear_curso(request):
                    if request.method == "POST":
                        codigo = request.POST.get('codigo')
                        nombre = request.POST.get('nombre')

                        # Crear y guardar el curso en la base de datos
                        curso = Curso(codigo=codigo, nombre=nombre)
                        curso.save()

                        # Retorna un mensaje de éxito o un estado 201 (creado)
                        return JsonResponse({"message": "Curso creado exitosamente"}, status=201)

                    return JsonResponse({"error": "Método no permitido"}, status=405)
            
    
def lista_cursos(request):
    cursos = Curso.objects.all()  # Obtener todos los cursos de la base de datos
    cursos_list = [{"id": curso.id, "codigo": curso.codigo, "nombre": curso.nombre} for curso in cursos]
    return JsonResponse(cursos_list, safe=False) 
