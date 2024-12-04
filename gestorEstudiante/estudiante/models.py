import datetime

class Estudiante():
    id = str()
    codigo = str()
    nombre = str()
    cursos = list()

    def __str__(self):
        return self.nombre

    @staticmethod
    def from_mongo(dto):
        estudiante = Estudiante()
        estudiante.id = str(dto['_id'])
        estudiante.codigo = dto['codigo']
        estudiante.cursos = dto['cursos']
        return estudiante

class Curso():
    id = str()
    codigo_curso = str()
    mora = float()

    def __str__(self):
        return self.codigo_curso

    @staticmethod
    def from_mongo(dto):
        curso = Curso()
        curso.id = str(dto['_id'])
        curso.codigo_curso = dto['codigo_curso']
        curso.mora = dto['mora']
        return curso

