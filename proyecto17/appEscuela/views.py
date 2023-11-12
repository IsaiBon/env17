from django.shortcuts import render
from .models import Carreras
from .models import Profesores
from .models import Asignatura
from .models import Estudiantes

#FUNCIONES DE CADA VISTA PARA DEVOLVER LOS VALORES DE CADA TABLAS EN LA BASE DE DATOS
#Y REQUERIR EL ARCHIVO HTML CORRESPONDIENTE

def vista1(request):
    return render(request,"escuela-admin.html")
def lis_estu(request):
    estudiantes= Estudiantes.objects.all()
    return render(request,'estudiantes.html',{'estudiantes':estudiantes})

def lis_asig(request):
    asignaturas= Asignatura.objects.all()
    return render(request,'asignaturas.html',{'asignaturas':asignaturas})

def lis_profes(request):
    profesores= Profesores.objects.all()
    return render(request,'profesores.html',{'profesores':profesores})

def lis_carre(request):
    carreras= Carreras.objects.all()
    return render(request,'carreras.html',{'carreras':carreras})
# Create your views here.
