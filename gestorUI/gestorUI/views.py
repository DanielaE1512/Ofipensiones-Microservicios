from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import requests
from django.contrib.auth.decorators import login_required

from gestorUI import settings
from gestorUI.auth0backend import getRole


def index(request):
    return render(request, 'index.html')

def lista_cursos(request):
    # Hacer la solicitud al microservicio gestorCursos para obtener los datos
    response = requests.get(f"{settings.PATH_Cursos}cursos/")
    
    if response.status_code == 200:
        cursos = response.json()  # Obtener la lista de cursos desde el microservicio
        return render(request, 'curso.html', {'cursos': cursos})
    else:
        return render(request, 'error.html', {'error': 'No se pudieron obtener los cursos.'})

@login_required    
def crear_curso(request):
    role = getRole(request)
    if role == "Administrador":
        if request.method == 'POST':
            # Obtener los datos del formulario
            codigo = request.POST.get('codigo')
            nombre = request.POST.get('nombre')

            # Hacer la solicitud al microservicio gestorCursos para crear el curso
            response = requests.post(f"{settings.PATH_Cursos}createcurso/", data={
                'codigo': codigo,
                'nombre': nombre
            })

            if response.status_code == 201:
                # Si el curso se crea con éxito, redirigir al listado de cursos
                return redirect('lista_cursos')
            else:
                # Si hubo un error, mostrar un mensaje
                return render(request, 'error.html', {'error': 'No se pudo crear el curso.'})

        return render(request, 'crear_curso.html')
    else:
        return HttpResponse("Unauthorized User")