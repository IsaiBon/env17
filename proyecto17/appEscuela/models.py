from django.db import models

# Create your models here.

#DEFINIENDO LAS TABLAS DE LA BASE DE DATOS POSTGRESQL CON SUS CAMPOS
#EL CAMPO ID SE CREA AUTOMATICAMENTE
class Carreras(models.Model):
    Nombre_Carrera= models.CharField(max_length=100)

class Estudiantes(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    edad=models.PositiveIntegerField()
    #LLAVE FORANEA
    carrera_id=models.ForeignKey(Carreras, on_delete=models.CASCADE)

class Profesores(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    correo=models.CharField(max_length=100)
    
class Asignatura(models.Model):
    nombre_asignatura=models.CharField(max_length=100)
    id_profesor=models.ForeignKey(Profesores, on_delete=models.CASCADE)
    carrera_id=models.ForeignKey(Carreras, on_delete=models.CASCADE)

