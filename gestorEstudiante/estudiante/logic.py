from estudiante.models import Estudiante, Curso
from pymongo import MongoClient
from bson.objectid import ObjectId
from django.conf import settings


def verifyEstudianteData(data):
    if 'nombre' not in data:
        raise ValueError('nombre is required')

    if 'codigo' not in data:
        raise ValueError('codigo is required')
    
    estudiante = Estudiante()
    estudiante.codigo = data['codigo']
    estudiante.nombre = data['nombre']
    estudiante.cursos = data['cursos']
    

    return estudiante

def createEstudiante(data):

    # Verify estudiante data
    estudiante = verifyEstudianteData(data)

    
    # Create place in MongoDB
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    estudiantes_collection = db['estudiantes']
    estudiante.id = estudiantes_collection.insert(
        {
            'codigo': estudiante.codigo,
            'nombre': estudiante.nombre,
            'cursos': estudiante.cursos
        }
    )
    addCursos
    client.close()
    return estudiante


def verifyCursoData(data):
    if 'codigo_curso' not in data:
        raise ValueError('codigo_curso is required')
    if 'mora' not in data or not isinstance(data['mora'], (int, float)):
        raise ValueError('mora is required and must be number')

    curso = Curso()
    curso.codigo_curso = data['codigo_curso']
    curso.mora = data['mora']


    return curso


def getEstudiantesMora(codigo_curso):
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    estudiantes_collection = db['estudiantes']
    
    # Consulta a la base de datos
    resultados = estudiantes_collection.aggregate([
        {
            "$match": {
                "cursos": {
                    "$elemMatch": {
                        "id_curso": codigo_curso,
                        "valor_mora": {"$gt": 0}  # Filtrar cursos con mora mayor a 0
                    }
                }
            }
        },
        {
            "$project": {
                "codigo_estudiante": 1,
                "nombre": 1,
                "valor_mora": {
                    "$arrayElemAt": [
                        "$cursos.valor_mora",
                        {"$indexOfArray": ["$cursos.id_curso", codigo_curso]}
                    ]
                }
            }
        },
        {
            "$group": {
                "_id": None,  # Agrupación general para calcular el total
                "estudiantes": {
                    "$push": {
                        "codigo_estudiante": "$codigo_estudiante",
                        "nombre": "$nombre",
                        "valor_mora": "$valor_mora"
                    }
                },
                "total_valor_mora": {"$sum": "$valor_mora"}  # Sumar las moras
            }
        }
    ])

    # Convertir resultados a una lista
    resultados_lista = list(resultados)
    return resultados_lista


def deleteAll():
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    estudiantes_collection = db['estudiantes']
    estudiantes_collection.delete_many({})
    return

