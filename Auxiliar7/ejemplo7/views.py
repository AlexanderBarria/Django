from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Formulario
from django.core.files.storage import FileSystemStorage
from .models import Cursos,Usuarios


def index(request):
	bienvenida={'titulo': 'Auxiliar 7','intro': 'Hoy veremos como usar formularios con bases de datos '}
	return render(request, 'ejemplo7/index.html', bienvenida)

def cursos(request):
	bienvenida={'titulo':'Cursos registrados', 'intro':"Nombre de los cursos rendidos almenos una vez ", 'cursos':Cursos.objects.values('nombre').distinct()}
	return render(request,'ejemplo7/cursos.html', bienvenida)

def users(request):
    info={'titulo':'Usuarios registrados en el sistema', 'intro':"Los siguientes usuarios están registrados en nuestra base de datos",
    'user':Usuarios.objects.all(),'user_beau':Usuarios.objects.exclude(puntaje_psu__gt=740)} # se escribe como atributo__condicion = valor_buscado # esto es del tipo where usuarios.puntaje_psu>740
    return render(request,'ejemplo7/users.html', info)

def adduser(request):
    form=Formulario()
    info={'titulo':'Agregar Usuarios', 'intro':"Registrese, Entreguenos todos sus datos aqui",'form':form} # se escribe como atributo__condicion = valor_buscado # esto es del tipo where usuarios.puntaje_psu>740
    return render(request,'ejemplo7/adduser.html', info)

def added(request):
	password = request.POST.get('password')
	password_valida = request.POST.get('password_valida')

	if password_valida == password:
		context = {'Titulo':'Formulario Correcto', 'comentario':'Gracias'}
		new_user=Usuarios(nombre=request.POST['nombre'],apellido=request.POST['apellido'],direccion=request.POST['direccion'], rut=request.POST['rut'], puntaje_psu=request.POST['puntaje_psu'], username=request.POST['username'], password=request.POST['password'], email=request.POST['email']);
		new_user.save();
		render_direccion = 'ejemplo7/added.html'
	if password_valida != password:
		context = {'Titulo':'El Formulario no se completo correctamente', 'comentario':'Favor volver a intentarlo'}
		render_direccion = 'ejemplo7/error.html'

	return render(request, render_direccion, context)
