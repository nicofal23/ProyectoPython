from django.shortcuts import render, redirect
from .models import Curso, Estudiante, Profesor, Entregable
from .forms import CursoFormulario, BuscaCursoForm, EstudianteFormulario, ProfesorFormulario, EntregableFormulario
from django.contrib import messages

def inicio(request):
    return render(request, "AppCoder/index.html")

def cursos_create_comun_form(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            camada = request.POST.get('camada')
            if nombre and camada:
                curso = Curso(nombre=nombre, camada=camada)
                curso.save()
                messages.success(request, 'Curso cargado con éxito.')
            else:
                messages.error(request, 'Faltan datos en el formulario.')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
        return redirect('cursos_create_comun')
    # Pasar los mensajes al contexto sin json_script
    return render(request, "AppCoder/create_form_comun.html", {
        'messages': messages.get_messages(request)
    })

from django.shortcuts import render, redirect
from .models import Curso, Estudiante, Profesor, Entregable
from .forms import CursoFormulario, BuscaCursoForm, EstudianteFormulario, ProfesorFormulario, EntregableFormulario
from django.contrib import messages

def cursos_create_comun_form(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            camada = request.POST.get('camada')
            if nombre and camada:
                curso = Curso(nombre=nombre, camada=camada)
                curso.save()
                messages.success(request, 'Curso cargado con éxito.')
            else:
                messages.error(request, 'Faltan datos en el formulario.')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
        return redirect('cursos_create_comun')
    return render(request, "AppCoder/create_form_comun.html", {
        'messages': messages.get_messages(request)
    })

def cursos_create_api_form(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            messages.success(request, 'Curso creado con éxito mediante API.')
            return redirect('Inicio')
    else:
        miFormulario = CursoFormulario()
    return render(request, "AppCoder/create_api_form.html", {"miFormulario": miFormulario})

def estudiantes_create_comun_form(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            edad = request.POST.get('edad')
            email = request.POST.get('email')
            if nombre and apellido and edad and email:
                estudiante = Estudiante(nombre=nombre, apellido=apellido, edad=edad, email=email)
                estudiante.save()
                messages.success(request, 'Estudiante creado con éxito.')
            else:
                messages.error(request, 'Faltan datos en el formulario.')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
        return redirect('estudiantes_create_comun')
    return render(request, "AppCoder/estudiante_create_form.html", {
        'messages': messages.get_messages(request)
    })

def estudiantes_create_api_form(request):
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], edad=informacion["edad"], email=informacion["email"])
            estudiante.save()
            messages.success(request, 'Estudiante creado con éxito mediante API.')
            return redirect('Inicio')
    else:
        miFormulario = EstudianteFormulario()
    return render(request, "AppCoder/create_api_form.html", {"miFormulario": miFormulario})

def cursos_read_api_form(request):
    if request.method == 'POST':
        miFormulario = BuscaCursoForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])
            return render(request, "AppCoder/show_courses.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()
    return render(request, "AppCoder/read_api_form.html", {"miFormulario": miFormulario})

def profesores_create_comun_form(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            especialidad = request.POST.get('especialidad')
            if nombre and apellido and especialidad:
                profesor = Profesor(nombre=nombre, apellido=apellido, especialidad=especialidad)
                profesor.save()
                messages.success(request, 'Profesor creado con éxito.')
            else:
                messages.error(request, 'Faltan datos en el formulario.')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
        return redirect('profesores_create_comun')
    return render(request, "AppCoder/profesor_create_form.html", {
        'messages': messages.get_messages(request)
    })

def profesores_create_api_form(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], especialidad=informacion["especialidad"])
            profesor.save()
            messages.success(request, 'Profesor creado con éxito mediante API.')
            return redirect('Inicio')
    else:
        miFormulario = ProfesorFormulario()
    return render(request, "AppCoder/create_api_form.html", {"miFormulario": miFormulario})

def entregables_create_comun_form(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            fecha_entrega = request.POST.get('fecha_entrega')
            entregado = request.POST.get('entregado', False) == 'on'
            if nombre and fecha_entrega:
                entregable = Entregable(nombre=nombre, fecha_entrega=fecha_entrega, entregado=entregado)
                entregable.save()
                messages.success(request, 'Entregable creado con éxito.')
            else:
                messages.error(request, 'Faltan datos en el formulario.')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
        return redirect('entregables_create_comun')
    return render(request, "AppCoder/entregales_comun.html", {
        'messages': messages.get_messages(request)
    })

def entregables_create_api_form(request):
    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            entregable = Entregable(nombre=informacion["nombre"], fecha_entrega=informacion["fecha_entrega"], entregado=informacion["entregado"])
            entregable.save()
            messages.success(request, 'Entregable creado con éxito mediante API.')
            return redirect('Inicio')
    else:
        miFormulario = EntregableFormulario()
    return render(request, "AppCoder/create_api_form.html", {"miFormulario": miFormulario})
