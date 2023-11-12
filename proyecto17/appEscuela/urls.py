from django.urls import path
from . import views
#LAS DIRECCIONES DE LA APLICACIONES, LLAMAN A LAS VISTAS EN VIEWS.PY
#Primero se incluye la vista1 que tiene el archivo escuela-admin.html 
#para acceder a los otros archivos se especifica lo que se va agregar a la URL , ej:carreras/'
urlpatterns = [
    path('',views.vista1, name='vista1'),
    path('carreras/',views.lis_carre, name='lis_carre'),
    path('estudiantes/',views.lis_estu, name='lis_estu'),
    path('asignaturas/',views.lis_asig, name='lis_asig'),
    path('profesores/',views.lis_profes, name='lis_profes'),

]