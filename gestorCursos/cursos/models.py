from django.db import models

class Curso(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)  # Campo para el nombre del curso
    
    
    # Este método devuelve una representación en cadena de un objeto estudiante
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
