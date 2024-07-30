"""
URL configuration for Clases_Coder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cursos/create-comun/', views.cursos_create_comun_form, name="cursos_create_comun"),
    path('cursos/create-api/', views.cursos_create_api_form, name="cursos_create_api"),
    path('cursos/read/', views.cursos_read_api_form, name="cursos_read"),
    path('estudiantes/create-comun/', views.estudiantes_create_comun_form, name="estudiantes_create_comun"),
    path('estudiantes/create-api/', views.estudiantes_create_api_form, name="estudiantes_create_api"),
    path('profesores/create-comun/', views.profesores_create_comun_form, name="profesores_create_comun"),
    path('profesores/create-api/', views.profesores_create_api_form, name="profesores_create_api"),
    path('entregables/create-comun/', views.entregables_create_comun_form, name="entregables_create_comun"),
    path('entregables/create-api/', views.entregables_create_api_form, name="entregables_create_api"),
]