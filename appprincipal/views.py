from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django import forms
from .models import *


from django.contrib import messages		
from django.contrib.auth import update_session_auth_hash		
from django.contrib.auth.forms import PasswordChangeForm		
from django.contrib.auth.forms import AdminPasswordChangeForm		
from django.shortcuts import render, redirect		
from .filters import UserFilter

class Factory:
	def crearFormulario(self, tipo, request=None):
		if(tipo == 'user'):
			if(request != None):
				return UserForm(request.POST)
			else:
				return UserForm()
		elif(tipo == 'tipo'):
			if(request != None):
				return TipoForm(request.POST)
			else:
				return TipoForm()
		elif(tipo == 'programa'):
			if(request != None):
				return ProgramaForm(request.POST)
			else:
				return ProgramaForm()
		elif(tipo == 'curso'):
			if(request != None):
				return CursoForm(request.POST)
			else:
				return CursoForm()
		elif(tipo == 'competencia'):
			if(request != None):
				return CompetenciaForm(request.POST)
			else:
				return CompetenciaForm()
		elif(tipo == 'resultado'):
			if(request != None):
				return ResultadoForm(request.POST)
			else:
				return ResultadoForm()
		elif(tipo == 'indicador'):
			if(request != None):
				return IndicadorForm(request.POST)
			else:
				return IndicadorForm()
		elif(tipo == 'actividadF'):
			if(request != None):
				return ActividadFForm(request.POST)
			else:
				return ActividadFForm()
		elif(tipo == 'preRequisito'):
			if(request != None):
				return PreRequisitoForm(request.POST)
			else:
				return PreRequisitoForm()

	
# Create your views here.
def autenticar(request):
	template = loader.get_template('login.html')
	if(request.user.is_authenticated):
		return redirect('/')
	if(request.method == 'POST'):
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		user = authenticate(username=username, password=password)#Agregar login con correo
		if(user != None):
			login(request, user)
			return redirect('/')
		else:
			context = {
				'datosIncorrectos' : True
			}
			return HttpResponse(template.render(context, request))
	context = {
		'datosIncorrectos' : False
  }
	return HttpResponse(template.render(context, request))

def inicio(request):
	if(request.user.is_authenticated):
		usuario = request.user
		form = UserForm(instance=usuario)
		formT = TipoForm(instance=usuario.profile)
		formPass = PasswordChangeForm(request.user)
		exitoPass = False
		if(request.method == 'POST'):
			formPass = PasswordChangeForm(request.user, request.POST)
			if formPass.is_valid():
				user = formPass.save()
				update_session_auth_hash(request, user)  # Important!
				exitoPass = True
				formPass = PasswordChangeForm(request.user)
		template = loader.get_template('verPerfil.html')
		context = {
			'texto' : "Información de mi perfil eee:",
			'form' : form,
			'tipo' : formT,
			'formPass' : formPass,
			'exitoPass' : exitoPass
		}
		return render(request, 'verPerfil.html', context)
		#return HttpResponse(template.render(context, request))
	else:
		return redirect('/login')

#------------------Crud usuarios--------------
def agregarusuario(request):
	factory = Factory()
	if(request.user.is_authenticated):
		if(request.user.profile.tipo == 'admin'):
			if(request.method == 'POST'):
				form = factory.crearFormulario('user', request)
				formT = factory.crearFormulario('tipo', request)
				username = request.POST.get('username', None)
				name = request.POST.get('first_name', None)
				password = request.POST.get('password', None)
				email = request.POST.get('email', None)
				tipo = request.POST.get('tipo', None)
				if form.is_valid():
					user = User.objects.create_user(username=username, password=password, email=email, first_name=name)
					user.profile.tipo = tipo
					user.save()
					return HttpResponseRedirect('/usuarios')
			else:
				form = factory.crearFormulario('user')
				formT = factory.crearFormulario('tipo')
			template = loader.get_template('agregarUsuario2.html')
			context = {
				'form' : form,
				'tipo' : formT, 
			}
			form.fields['password'] = forms.CharField(widget=forms.PasswordInput)
			return HttpResponse(template.render(context, request))
		else:
			return redirect('/')
	else:
		return redirect('/')

def gestionarusuarios(request):
	if(request.user.is_authenticated):
		if(request.user.profile.tipo == 'admin'):
			perfiles  = Profile.objects.all()
			user_filter = UserFilter(request.GET, queryset=perfiles)
			template = loader.get_template('usuarios.html')
			context = {
				'user_filter' : user_filter
			}
			return HttpResponse(template.render(context, request))
		else:
			return redirect('/')
	else:
		return redirect('/')
	
	
def detalleUsuario(request, pk):
	if(request.user.is_authenticated):
		if(request.user.profile.tipo == 'admin'):
			usuario = get_object_or_404(User, pk=pk)
			form = UserForm(instance=usuario)
			formT = TipoForm(instance=usuario.profile)
			template = loader.get_template('verPerfil.html')
			context = {
				'texto' : "Perfil del usuario:",
				'form' : form,
				'tipo' : formT
			}
			return HttpResponse(template.render(context, request))
		else:
			return redirect('/')
	else:
		return redirect('/')

def modificarUsuario(request, pk):
	if(request.user.is_authenticated):
		if(request.user.profile.tipo == 'admin'):
			usuario = get_object_or_404(User, pk=pk)
			exitoCambio = False
			exitoPass = False
			formPass = AdminPasswordChangeForm(usuario)
			form = UserForm(instance=usuario)
			form.fields['password'].widget = forms.HiddenInput()
			formT = TipoForm(instance=usuario.profile)
			template = loader.get_template('modificarUsuario.html')
			if(request.method == 'POST'):
				if (request.POST['_submit'] == "DATOS"):
					form = UserForm(request.POST, instance=usuario)
					form.fields['password'].widget = forms.HiddenInput()
					formT = TipoForm(request.POST, instance=usuario)
					username = request.POST.get('username', None)
					name = request.POST.get('first_name', None)
					email = request.POST.get('email', None)
					tipo = request.POST.get('tipo', None)
					if form.is_valid() and formT.is_valid():
						if(username != ""):
							usuario.username = username
						if(tipo != ""):
							usuario.profile.tipo = tipo
						if(name != ""):
							usuario.last_name = name
						if(email != ""):
							usuario.email = email
						usuario.save()
						exitoCambio = True	
				if (request.POST['_submit'] == "PASS"):
					#return redirect('/loca') # sin permisos
					formPass = AdminPasswordChangeForm(usuario, request.POST)
					if formPass.is_valid():
						exitoPass = True
						user = formPass.save()
						#update_session_auth_hash(request, user)  # Important!
						formPass = AdminPasswordChangeForm(user)	
			context = { #Diccionario que se le pasa al HTML
				'form': form,
				'tipo' : formT,
				'formPass' : formPass,
				'exitoCambio' : exitoCambio,
				'exitoPass' : exitoPass
			}
			return HttpResponse(template.render(context, request))
		else:
			return redirect('/')
	else:
		return redirect('/')


#-------------Crud programas------------------
def agregarprograma(request):
	factory = Factory()
	if(request.user.is_authenticated):
		if(request.user.profile.tipo == 'decano'):
			template = loader.get_template('agregarPrograma.html')
			profileQuery = Profile.objects.filter(tipo="director")
			qs = User.objects.filter(profile__in=profileQuery).order_by('id')
			form = factory.crearFormulario('programa', request)
			form.fields['director'].queryset=qs;
			if request.method == 'POST':
				if form.is_valid():
					programa = form.save()
					programa.save()
					return HttpResponseRedirect('/programas')
			else:
				form = factory.crearFormulario('programa')
				form.fields['director'].queryset=qs;
			context = {
				'form' : form
			}
			return HttpResponse(template.render(context, request))
		else:
			return redirect('/') # sin permisos
	else:
		return redirect('/login')

def gestionarprogramas(request):

	if(request.user.is_authenticated):
		if(request.user.profile.tipo == 'decano'):
			programas = Programa.objects.order_by('codigo')
			template = loader.get_template('programas.html')
			context = { #Diccionario que se le pasa al HTML
				'programas': programas,
				'puedoeliminar' : request.user.profile.tipo == 'decano',
			}
			return HttpResponse(template.render(context, request))
		elif(request.user.profile.tipo == 'director'):
			programas = Programa.objects.filter(director_id=request.user.id)
			if (programas.count() == 0):
				template = loader.get_template('error.html') #---------Buscame-------------
				context = { #Diccionario que se le pasa al HTML
					'error': "No tiene programa academico asignado",
				}
				return HttpResponse(template.render(context, request))
			template = loader.get_template('programas.html') #Modificar template para gestion del director
			context = { #Diccionario que se le pasa al HTML
				'programas': programas
			}
			return HttpResponse(template.render(context, request))
		else:
			return redirect('/') # sin permisos
	else:
		return redirect('/login')

def editarPrograma(request, codigo): #Falta revisar html
	if(request.user.is_authenticated):
		programa = Programa.objects.get(codigo=codigo)
		if((request.user.profile.tipo == 'decano') or (request.user.id == programa.director_id)):
			profileQuery = Profile.objects.filter(tipo="director")
			qs = User.objects.filter(profile__in=profileQuery).order_by('id')
			if request.method == 'POST':
				#Actualiza
				#programa = Programa.objects.get(codigo=codigo)
				form = ProgramaForm(request.POST, instance=programa)
				form.fields['director'].queryset=qs;
				form.fields['codigo'].widget = forms.HiddenInput()
				if form.is_valid():
					form.save()
					return HttpResponseRedirect('/programas')
				else:
					form.fields['codigo'].widget = forms.HiddenInput()
					form.fields['director'].queryset=qs;
					template = loader.get_template('editarPrograma.html')
					context = {
					'form' : form,
					'pr' : programa
					}
					return HttpResponse(template.render(context, request))
			else:
				#programa =  Programa.objects.get(codigo=codigo)
				form = ProgramaForm(instance=programa)
				form.fields['codigo'].widget = forms.HiddenInput()
				form.fields['director'].queryset=qs;
				template = loader.get_template('editarPrograma.html')
				context = { #Diccionario que se le pasa al HTML
				'form': form,
				'pr' : programa
				}
				return HttpResponse(template.render(context, request))
		else:
			return redirect('/') # sin permisos
	else:
		return redirect('/login')

def eliminarPrograma(request, codigo):
	if(request.user.is_authenticated):
		programa = Programa.objects.get(codigo=codigo)
		if(request.user.profile.tipo == 'decano'):
			if request.method == 'POST':
				respuesta = request.POST.get('opcion', None)
				if(respuesta=="si"):
					#programa = Programa.objects.get(codigo=codigo);
					programa.delete()
				return redirect('/programas')
			else:
				#Mostrar en eliminar/<pk>
				#programa =  Programa.objects.get(codigo=codigo)
				template = loader.get_template('confirmar.html')
				texto = "¿Seguro que desea borrar " + programa.nombre_programa + "?"
				context = { #Diccionario que se le pasa al HTML
				'texto' : texto
				}
				return HttpResponse(template.render(context, request))
		else:
			return redirect('/') # sin permisos
	else:
		return redirect('/login')

def verPrograma(request,codigo):
	if(request.user.is_authenticated):
		programa = Programa.objects.get(codigo=codigo)
		if(request.user.profile.tipo == 'decano' or request.user.id == programa.director_id):
			#Tabla a HTML
			#programa = Programa.objects.get(codigo=codigo)
			form = ProgramaForm(instance=programa)
			form.fields['director'].widget = forms.HiddenInput()
			template = loader.get_template('verprogramas.html')
			context = { #Diccionario que se le pasa al HTML
				'form' : form,
				'puedoeliminar' : request.user.profile.tipo == 'decano',
				'programa' : programa,
			}
			return HttpResponse(template.render(context, request))
		else:
			return redirect('/') #sin permisos
	else:
		return redirect('/login')

def eliminarUsuario(request, pk):
	if(request.user.is_authenticated):
		if(request.user.profile.tipo == 'admin'):
			user = User.objects.get(pk=pk)
			if(request.method == 'POST'):
				opcion = request.POST.get('opcion', None)
				if(opcion == 'si'):
					user.delete()
				return redirect('/usuarios')
			else:
				template = loader.get_template('confirmar.html')
				texto = "¿Seguro que desea borrar " +  user.first_name + " ?:"
				context = { #Diccionario que se le pasa al HTML
				'texto' : texto
				}
				return HttpResponse(template.render(context, request))
		else:
			return redirect('/')
	else:
		return redirect('/')


#-------------------Crud cursos---------------------


def gestionarCursos(request):
	if(request.user.is_authenticated):
		if(request.user.profile.tipo == 'director'):
			try:
				programa = Programa.objects.get(director_id=request.user.id)
			except Programa.DoesNotExist:
				template = loader.get_template('error.html') #---------Buscame-------------
				context = { #Diccionario que se le pasa al HTML
					'error': "No tiene programa academico asignado",
				}
				return HttpResponse(template.render(context, request))
			cursos = Curso.objects.filter(programa_id=programa.codigo)
			template = loader.get_template('cursos.html')
			
			context = {
				'cursos' : cursos,
				'puedoeliminar' : request.user.profile.tipo == 'director'
			}
			return HttpResponse(template.render(context, request))
		elif(request.user.profile.tipo == 'profesor'):
			cursos = Curso.objects.filter(docente_id=request.user.pk)
			template = loader.get_template('cursos.html') #Modificar template para gestion del director
			context = { #Diccionario que se le pasa al HTML
				'cursos': cursos,
				'puedoeliminar' : request.user.profile.tipo == 'director'
			}
			return HttpResponse(template.render(context, request))
		else:
			return redirect('/')
	else:
		return redirect('/')

def agregarCurso(request):
	factory = Factory()
	if(request.user.is_authenticated):
		if(request.user.profile.tipo == 'director'):
			try:
				programa = Programa.objects.get(director_id=request.user.id)
			except Programa.DoesNotExist:
				template = loader.get_template('error.html') #---------Buscame-------------
				context = { #Diccionario que se le pasa al HTML
					'error': "No tiene programa academico asignado",
				}
				return HttpResponse(template.render(context, request))
			if(request.method == 'POST'):
				#agregar un curso a su prpgrama academico
				form = factory.crearFormulario('curso', request)
				profileQuery = Profile.objects.filter(tipo="profesor")
				qs = User.objects.filter(profile__in=profileQuery).order_by('id')
				form.fields['docente'].queryset=qs;
				form.fields['programa'].initial = programa #programa del director
				form.fields['programa'].widget = forms.HiddenInput()
				if form.is_valid():
					curso = form.save()
					curso.save()
					return HttpResponseRedirect('/cursos')
			else:
				form = factory.crearFormulario('curso')
				profileQuery = Profile.objects.filter(tipo="profesor")
				qs = User.objects.filter(profile__in=profileQuery).order_by('id')
				form.fields['docente'].queryset=qs;
				form.fields['programa'].initial = programa #programa del director
				form.fields['programa'].widget = forms.HiddenInput()
			template = loader.get_template('agregarCurso.html')
			context = {
				'form' : form,
				'programa' : programa
			}
			return HttpResponse(template.render(context, request))
		else:
			return redirect('/')
	else:
		return redirect('/')

def modificarCurso(request, codigo):
	if(request.user.is_authenticated):
		curso = Curso.objects.get(codigo=codigo)
		programa = Programa.objects.get(codigo=curso.programa_id)
		if((request.user.profile.tipo == 'director' and request.user.id == programa.director_id) or request.user.id == curso.docente_id):
			if(request.method == 'POST'):
				#curso = Curso.objects.get(codigo=codigo)
				form = CursoForm(data = request.POST or None , instance=curso)
				profileQuery = Profile.objects.filter(tipo="profesor")
				qs = User.objects.filter(profile__in=profileQuery).order_by('id')
				form.fields['docente'].queryset=qs;
				form.fields['codigo'].widget = forms.HiddenInput()
				form.fields['programa'].initial = programa #programa del director
				form.fields['programa'].widget = forms.HiddenInput()
				if form.is_valid():
					form.save()
					return HttpResponseRedirect('/cursos')
				else:
					template = loader.get_template('modificarCurso.html')
					context = {
						'form' : form,
						'pr' : programa
					}
					return HttpResponse(template.render(context, request))
			
			form = CursoForm(instance = curso)
			profileQuery = Profile.objects.filter(tipo="profesor")
			qs = User.objects.filter(profile__in=profileQuery).order_by('id')
			form.fields['docente'].queryset=qs;
			form.fields['codigo'].widget = forms.HiddenInput()
			form.fields['programa'].initial = programa #programa del director
			form.fields['programa'].widget = forms.HiddenInput()
			template = loader.get_template('modificarCurso.html')
	
			context = {
				'form' : form
			}
			return HttpResponse(template.render(context, request))
		else:
			return redirect('/')
	else:
		return redirect('/')

def eliminarCurso(request, codigo):
	if(request.user.is_authenticated):
		curso = Curso.objects.get(codigo=codigo)
		programa = Programa.objects.get(codigo=curso.programa_id)
		if(request.user.profile.tipo == 'director' and request.user.id == programa.director_id):
			if(request.method == 'POST'):
				opcion = request.POST.get('opcion', None)
				if(opcion == 'si'):
					curso = Curso.objects.get(codigo=codigo)
					curso.delete()
				return redirect('/cursos')
			else:
				template = loader.get_template('confirmar.html')
				texto = "¿Seguro que desea borrar " + curso.nombre + " ?:"
				context = { #Diccionario que se le pasa al HTML
				'texto' : texto
				}
				return HttpResponse(template.render(context, request))
		else:
			return redirect('/')
	else:
		return redirect('/')



def consultarCurso(request, codigo):
	if(request.user.is_authenticated):
		curso = Curso.objects.get(codigo=codigo)
		programa = Programa.objects.get(codigo=curso.programa_id)
		form = CursoForm(instance = curso)
		if((request.user.profile.tipo == 'director' and request.user.id == programa.director_id) or request.user.id == curso.docente_id):
			template = loader.get_template('verCursos.html')
			context = { #Diccionario que se le pasa al HTML
				'form' : form,
				'curso' : curso,
			}
			return HttpResponse(template.render(context, request))
		else:
			return redirect('/')
	else:
		return redirect('/')


#-----------------Crud de Competencias-----------------------

def gestionarCompetencias(request, codigo):
	if(request.user.is_authenticated):
		try:
			curso = Curso.objects.get(codigo=codigo)
		except Curso.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El curso no Existe",
			}
			return HttpResponse(template.render(context, request))
		if((request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id) or request.user.profile.tipo == 'director' or request.user.profile.tipo == 'decano'):
				competencias = Competencia.objects.filter(curso=codigo)
				template = loader.get_template('competencias.html')
				
				context = {
					'curso' : curso,
					'competencias' : competencias,
					'puedogestionar' : request.user.profile.tipo == 'profesor'
				}
				return HttpResponse(template.render(context, request))
		else:
			return redirect('/')
	else:
		return redirect('/')

def agregarCompetencia(request, codigo):
	factory = Factory()
	if(request.user.is_authenticated):
		try:
			curso = Curso.objects.get(codigo=codigo)
		except Curso.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El curso no Existe",
			}
			return HttpResponse(template.render(context, request))
		if(request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id):
			if(request.method == 'POST'):
				#agregar una competencia a su curso
				form = factory.crearFormulario('competencia', request)
				form.fields['curso'].initial = curso.codigo #programa del director
				form.fields['curso'].widget = forms.HiddenInput()
				if form.is_valid():
					competencia = form.save()
					competencia.save()
					return HttpResponseRedirect('/cursos')
			else:
				form = factory.crearFormulario('competencia')
				form.fields['curso'].initial = curso.codigo
				form.fields['curso'].widget = forms.HiddenInput()
			template = loader.get_template('agregarCompetencia.html')
			context = {
				'form' : form,
				'curso' : curso
			}
			return HttpResponse(template.render(context, request))
			
		else:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "No esta asignado a este curso",
			}
			return HttpResponse(template.render(context, request))
	else:
		return redirect('/')

def consultarCompetencia(request,codigo_curso,codigo_competencia):
	if(request.user.is_authenticated):
		try:
			curso = Curso.objects.get(codigo=codigo_curso)
			competencia = Competencia.objects.get(id=codigo_competencia)
		except curso.DoesNotExist as e:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El curso no Existe",
			}
			return HttpResponse(template.render(context, request))
		form = CompetenciaForm(instance = competencia)
		if((request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id) or request.user.profile.tipo == 'decano' or request.user.profile.tipo == 'director'):
			template = loader.get_template('verCompetencias.html')
			context = {
				'form': form,
				'competencia': competencia,
			}
			return HttpResponse(template.render(context, request))
		else:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "No esta asignado a este curso",
			}
			return HttpResponse(template.render(context, request))
	else:
		return redirect('/')


def modificarCompetencia(request, codigo_curso, codigo_competencia):
	if(request.user.is_authenticated):
		try:
			curso = Curso.objects.get(codigo=codigo_curso)
			competencia = Competencia.objects.get(id=codigo_competencia)
		except curso.DoesNotExist as e:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El curso no Existe",
			}
			return HttpResponse(template.render(context, request))
		if(request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id):
			if(request.method == 'POST'):
				form = CompetenciaForm(data = request.POST or None , instance=competencia)
				form.fields['curso'].initial = competencia.curso #programa del director
				form.fields['curso'].widget = forms.HiddenInput()
				if form.is_valid():
					form.save()
					return HttpResponseRedirect('/cursos')
				else:
					template = loader.get_template('modificarCompetencia.html')
					context = {
						'form' : form,
						'competencia' : competencia
					}
					return HttpResponse(template.render(context, request))
			else:
				form = CompetenciaForm(instance = competencia)
				form.fields['curso'].initial = competencia.curso #programa del director
				form.fields['curso'].widget = forms.HiddenInput()
				template = loader.get_template('modificarCompetencia.html')
				context = {
					'form' : form,
					'competencia' : competencia
				}
			return HttpResponse(template.render(context, request))
		else:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "No esta asignado a este curso",
			}
			return HttpResponse(template.render(context, request))
	else:
		return redirect('/')

def eliminarCompetencia(request, codigo_curso, codigo_competencia):
	if(request.user.is_authenticated):
		try:
			curso = Curso.objects.get(codigo=codigo_curso)
			competencia = Competencia.objects.get(id=codigo_competencia)
		except curso.DoesNotExist as e:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El curso no Existe",
			}
			return HttpResponse(template.render(context, request))
		if(request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id):
			if(request.method == 'POST'):
				opcion = request.POST.get('opcion', None)
				if(opcion == 'si'):
					competencia.delete()
				return redirect('/cursos')
			else:
				template = loader.get_template('confirmar.html')
				texto = "¿Seguro que desea borrar " + competencia.nombre + " ?:"
				context = { #Diccionario que se le pasa al HTML
				'texto' : texto
				}
				return HttpResponse(template.render(context, request))
		else:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "No esta asignado a este curso",
			}
			return HttpResponse(template.render(context, request))
	else:
		return redirect('/')

#-----------------CRUD de resultados de aprendizaje ----------------------------}

def gestionarResultados(request, codigo_competencia):
	if(request.user.is_authenticated):
		try:
			competencia= Competencia.objects.get(id=codigo_competencia)
			curso = Curso.objects.get(codigo=competencia.curso_id)
		except Competencia.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "La competencia no Existe",
			}
			return HttpResponse(template.render(context, request))
		if((request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id) or request.user.profile.tipo == 'director' or request.user.profile.tipo == 'decano'):
				resultados = Resultado.objects.filter(competencia=codigo_competencia)
				template = loader.get_template('resultados.html')
				context = {
					'competencia' : competencia,
					'resultados' : resultados,
					'puedogestionar' : request.user.profile.tipo == 'profesor'
				}
				return HttpResponse(template.render(context, request))
		else:
			return redirect('/')
	else:
		return redirect('/')

def agregarResultado(request, codigo_competencia):
	factory = Factory()
	if(request.user.is_authenticated):
		try:
			competencia= Competencia.objects.get(id=codigo_competencia)
			curso = Curso.objects.get(codigo=competencia.curso_id)
		except Competencia.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "La competencia no Existe",
			}
			return HttpResponse(template.render(context, request))
		if(request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id):
			if(request.method == 'POST'):
				#agregar una competencia a su curso
				form = factory.crearFormulario('resultado', request)
				form.fields['competencia'].initial = competencia.id #programa del director
				form.fields['competencia'].widget = forms.HiddenInput()
				if form.is_valid():
					resultado = form.save()
					resultado.save()
					return HttpResponseRedirect('/cursos')
			else:
				form = factory.crearFormulario('resultado')
				form.fields['competencia'].initial = competencia.id
				form.fields['competencia'].widget = forms.HiddenInput()
			template = loader.get_template('agregarResultado.html')
			context = {
				'form' : form,
				'competencia' : competencia
			}
			return HttpResponse(template.render(context, request))
			
		else:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "No esta asignado a esta competencia",
			}
			return HttpResponse(template.render(context, request))
	else:
		return redirect('/')

def consultarResultado(request, codigo_resultado):
	if(request.user.is_authenticated):
		try:
			resultado = Resultado.objects.get(id = codigo_resultado)
			competencia= Competencia.objects.get(id=resultado.competencia_id)
			curso = Curso.objects.get(codigo=competencia.curso_id)
		except resultado.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El Resultado de Aprendizaje no Existe",
			}
			return HttpResponse(template.render(context, request))
		form = ResultadoForm(instance = resultado)
		if((request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id) or request.user.profile.tipo == 'decano' or request.user.profile.tipo == 'director'):
			template = loader.get_template('verResultado.html')
			form.fields['competencia'].initial = competencia.id
			form.fields['competencia'].widget = forms.HiddenInput()
			context = {
				'form': form,
				'resultado': resultado,
			}
			return HttpResponse(template.render(context, request))
		else:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "No esta asignado a este curso",
			}
			return HttpResponse(template.render(context, request))
	else:
		return redirect('/')

def modificarResultado(request, codigo_resultado):
	if(request.user.is_authenticated):
		try:
			resultado = Resultado.objects.get(id = codigo_resultado)
			competencia= Competencia.objects.get(id=resultado.competencia_id)
			curso = Curso.objects.get(codigo=competencia.curso_id)
		except resultado.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El Resultado de Aprendizaje no Existe",
			}
			return HttpResponse(template.render(context, request))
		if(request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id):
			if(request.method == 'POST'):
				form = ResultadoForm(data = request.POST or None , instance=resultado)
				form.fields['competencia'].initial = resultado.competencia_id #programa del director
				form.fields['competencia'].widget = forms.HiddenInput()
				if form.is_valid():
					form.save()
					return HttpResponseRedirect('/cursos')
				else:
					template = loader.get_template('modificarResultado.html')
					context = {
						'form' : form,
						'resultado' : resultado
					}
					return HttpResponse(template.render(context, request))
			else:
				form = ResultadoForm(instance = resultado)
				form.fields['competencia'].initial = resultado.competencia_id #programa del director
				form.fields['competencia'].widget = forms.HiddenInput()
				template = loader.get_template('modificarResultado.html')
				context = {
					'form' : form,
					'competencia' : competencia
				}
			return HttpResponse(template.render(context, request))
		else:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "No esta asignado a este curso",
			}
			return HttpResponse(template.render(context, request))
	else:
		return redirect('/')

def eliminarResultado(request, codigo_resultado):
	if(request.user.is_authenticated):
		try:
			resultado = Resultado.objects.get(id = codigo_resultado)
			competencia= Competencia.objects.get(id=resultado.competencia_id)
			curso = Curso.objects.get(codigo=competencia.curso_id)
		except resultado.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El Resultado de Aprendizaje no Existe",
			}
			return HttpResponse(template.render(context, request))
		if(request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id):
			if(request.method == 'POST'):
				opcion = request.POST.get('opcion', None)
				if(opcion == 'si'):
					resultado.delete()
				return redirect('/cursos')
			else:
				template = loader.get_template('confirmar.html')
				texto = "¿Seguro que desea borrar El resultado de aprendizaje ?:"
				context = { #Diccionario que se le pasa al HTML
				'texto' : texto
				}
				return HttpResponse(template.render(context, request))
		else:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "No esta asignado a este curso",
			}
			return HttpResponse(template.render(context, request))
	else:
		return redirect('/')

#-----------------CRUD Indicadores de Logros-----------------------------------

def gestionarIndicadores(request, codigo_resultado):
	if(request.user.is_authenticated):
		try:
			resultado= Resultado.objects.get(id= codigo_resultado)
			competencia= Competencia.objects.get(id=resultado.competencia_id)
			curso = Curso.objects.get(codigo=competencia.curso_id)
		except Competencia.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El Resultado Academico no Existe",
			}
			return HttpResponse(template.render(context, request))
		if((request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id) or request.user.profile.tipo == 'director' or request.user.profile.tipo == 'decano'):
				indicadores = Indicador.objects.filter(resultado=codigo_resultado)
				template = loader.get_template('indicadores.html')
				context = {
					'indicadores' : indicadores,
					'resultado' : resultado,
					'puedogestionar' : request.user.profile.tipo == 'profesor'
				}
				return HttpResponse(template.render(context, request))
		else:
			return redirect('/')
	else:
		return redirect('/')

def agregarIndicador(request, codigo_resultado):
	factory = Factory()
	if(request.user.is_authenticated):
		try:
			resultado= Resultado.objects.get(id= codigo_resultado)
			competencia= Competencia.objects.get(id=resultado.competencia_id)
			curso = Curso.objects.get(codigo=competencia.curso_id)
		except Competencia.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El Resultado Academico no Existe",
			}
			return HttpResponse(template.render(context, request))
		if(request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id):
			if(request.method == 'POST'):
				#agregar una competencia a su curso
				form = factory.crearFormulario('indicador', request)
				form.fields['resultado'].initial = resultado.id #programa del director
				form.fields['resultado'].widget = forms.HiddenInput()
				if form.is_valid():
					indicador = form.save()
					indicador.save()
					return HttpResponseRedirect('/cursos')
			else:
				form = factory.crearFormulario('indicador')
				form.fields['resultado'].initial = resultado.id
				form.fields['resultado'].widget = forms.HiddenInput()
			template = loader.get_template('agregarIndicador.html')
			context = {
				'form' : form,
				'resultado' : resultado
			}
			return HttpResponse(template.render(context, request))
			
		else:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "No esta asignado a este indicador",
			}
			return HttpResponse(template.render(context, request))
	else:
		return redirect('/')

def consultarIndicador(request, codigo_indicador):
	if(request.user.is_authenticated):
		try:
			indicador = Indicador.objects.get(id = codigo_indicador)
			resultado = Resultado.objects.get(id = indicador.resultado_id)
			competencia= Competencia.objects.get(id=resultado.competencia_id)
			curso = Curso.objects.get(codigo=competencia.curso_id)
		except resultado.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El Indicador de Aprendizaje no Existe",
			}
			return HttpResponse(template.render(context, request))
		form = IndicadorForm(instance = indicador)
		if((request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id) or request.user.profile.tipo == 'decano' or request.user.profile.tipo == 'director'):
			template = loader.get_template('verIndicador.html')
			form.fields['resultado'].initial = indicador.resultado_id 
			form.fields['resultado'].widget = forms.HiddenInput()
			context = {
				'form': form,
				'indicador': indicador,
			}
			return HttpResponse(template.render(context, request))
		else:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "No esta asignado a este curso",
			}
			return HttpResponse(template.render(context, request))
	else:
		return redirect('/')


def modificarIndicador(request, codigo_indicador):#acomodar despues
	if(request.user.is_authenticated):
		try:
			indicador = Indicador.objects.get(id = codigo_indicador)
			resultado = Resultado.objects.get(id = indicador.resultado_id)
			competencia= Competencia.objects.get(id=resultado.competencia_id)
			curso = Curso.objects.get(codigo=competencia.curso_id)
		except resultado.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El Indicador de Aprendizaje no Existe",
			}
			return HttpResponse(template.render(context, request))
		if(request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id):
			if(request.method == 'POST'):
				form = IndicadorForm(data = request.POST or None , instance=indicador)
				form.fields['resultado'].initial = indicador.resultado_id 
				form.fields['resultado'].widget = forms.HiddenInput()
				if form.is_valid():
					form.save()
					return HttpResponseRedirect('/cursos')
				else:
					template = loader.get_template('modificarIndicador.html')
					context = {
						'form' : form,
						'indicador' : indicador
					}
					return HttpResponse(template.render(context, request))
			else:
				form = IndicadorForm(instance = indicador)
				form.fields['resultado'].initial = indicador.resultado_id 
				form.fields['resultado'].widget = forms.HiddenInput()
				template = loader.get_template('modificarIndicador.html')
				context = {
					'form' : form,
					'indicador' : indicador
				}
			return HttpResponse(template.render(context, request))
		else:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "No esta asignado a este curso",
			}
			return HttpResponse(template.render(context, request))
	else:
		return redirect('/')


def eliminarIndicador(request, codigo_indicador):
	if(request.user.is_authenticated):
		try:
			indicador = Indicador.objects.get(id = codigo_indicador)
			resultado = Resultado.objects.get(id = indicador.resultado_id)
			competencia= Competencia.objects.get(id=resultado.competencia_id)
			curso = Curso.objects.get(codigo=competencia.curso_id)
		except resultado.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El Indicador de Aprendizaje no Existe",
			}
			return HttpResponse(template.render(context, request))
		if(request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id):
			if(request.method == 'POST'):
				opcion = request.POST.get('opcion', None)
				if(opcion == 'si'):
					indicador.delete()
				return redirect('/cursos')
			else:
				template = loader.get_template('confirmar.html')
				texto = "¿Seguro que desea borrar El Indicador de Logro ?:"
				context = { #Diccionario que se le pasa al HTML
				'texto' : texto
				}
				return HttpResponse(template.render(context, request))
		else:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "No esta asignado a este curso",
			}
			return HttpResponse(template.render(context, request))
	else:
		return redirect('/')

#-----------------CRUD Actividades de Formacion------------------------

def gestionarActividadesF(request, codigo_resultado):
	if(request.user.is_authenticated):
		try:
			resultado= Resultado.objects.get(id= codigo_resultado)
			competencia= Competencia.objects.get(id=resultado.competencia_id)
			curso = Curso.objects.get(codigo=competencia.curso_id)
		except Competencia.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El Resultado Academico no Existe",
			}
			return HttpResponse(template.render(context, request))
		if((request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id) or request.user.profile.tipo == 'director' or request.user.profile.tipo == 'decano'):
				actividades = ActividadF.objects.filter(resultado=codigo_resultado)
				template = loader.get_template('actividadesF.html')
				context = {
					'actividades' : actividades,
					'resultado' : resultado,
					'puedogestionar' : request.user.profile.tipo == 'profesor'
				}
				return HttpResponse(template.render(context, request))
		else:
			return redirect('/')
	else:
		return redirect('/')

def agregarActividadesF(request, codigo_resultado):
	factory = Factory()
	if(request.user.is_authenticated):
		try:
			resultado= Resultado.objects.get(id= codigo_resultado)
			competencia= Competencia.objects.get(id=resultado.competencia_id)
			curso = Curso.objects.get(codigo=competencia.curso_id)
		except Competencia.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El Resultado Academico no Existe",
			}
			return HttpResponse(template.render(context, request))
		if(request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id):
			if(request.method == 'POST'):
				#agregar una competencia a su curso
				form = factory.crearFormulario('actividadF', request)
				form.fields['resultado'].initial = resultado.id #programa del director
				form.fields['resultado'].widget = forms.HiddenInput()
				if form.is_valid():
					actividadF = form.save()
					actividadF.save()
					return HttpResponseRedirect('/cursos')
			else:
				form = factory.crearFormulario('actividadF')
				form.fields['resultado'].initial = resultado.id
				form.fields['resultado'].widget = forms.HiddenInput()
			template = loader.get_template('agregarActividadF.html')
			context = {
				'form' : form,
				'resultado' : resultado
			}
			return HttpResponse(template.render(context, request))
			
		else:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "No esta asignado a este indicador",
			}
			return HttpResponse(template.render(context, request))
	else:
		return redirect('/')

def consultarActividadF(request, codigo_actividad):
	if(request.user.is_authenticated):
		try:
			actividad = ActividadF.objects.get(id = codigo_actividad)
			resultado = Resultado.objects.get(id = actividad.resultado_id)
			competencia= Competencia.objects.get(id=resultado.competencia_id)
			curso = Curso.objects.get(codigo=competencia.curso_id)
		except actividad.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El Indicador de Aprendizaje no Existe",
			}
			return HttpResponse(template.render(context, request))
		form = ActividadFForm(instance = actividad)
		if((request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id) or request.user.profile.tipo == 'decano' or request.user.profile.tipo == 'director'):
			template = loader.get_template('verActividad.html')
			form.fields['resultado'].initial = actividad.resultado_id 
			form.fields['resultado'].widget = forms.HiddenInput()
			context = {
				'form': form,
				'actividad': actividad,
			}
			return HttpResponse(template.render(context, request))
		else:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "No esta asignado a este curso",
			}
			return HttpResponse(template.render(context, request))
	else:
		return redirect('/')

def modificarActividadF(request, codigo_actividad):#acomodar despues
	if(request.user.is_authenticated):
		try:
			actividad = ActividadF.objects.get(id = codigo_actividad)
			resultado = Resultado.objects.get(id = actividad.resultado_id)
			competencia= Competencia.objects.get(id=resultado.competencia_id)
			curso = Curso.objects.get(codigo=competencia.curso_id)
		except actividad.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El Indicador de Aprendizaje no Existe",
			}
			return ActividadFForm(template.render(context, request))
		if(request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id):
			if(request.method == 'POST'):
				form = IndicadorForm(data = request.POST or None , instance=actividad)
				form.fields['resultado'].initial = actividad.resultado_id 
				form.fields['resultado'].widget = forms.HiddenInput()
				if form.is_valid():
					form.save()
					return HttpResponseRedirect('/cursos')
				else:
					template = loader.get_template('modificarIndicador.html')
					context = {
						'form' : form,
						'actividad' : actividad
					}
					return HttpResponse(template.render(context, request))
			else:
				form = ActividadFForm(instance = actividad)
				form.fields['resultado'].initial = actividad.resultado_id 
				form.fields['resultado'].widget = forms.HiddenInput()
				template = loader.get_template('modificarIndicador.html')
				context = {
					'form' : form,
					'actividad' : actividad
				}
			return HttpResponse(template.render(context, request))
		else:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "No esta asignado a este curso",
			}
			return HttpResponse(template.render(context, request))
	else:
		return redirect('/')

def eliminarActividadF(request, codigo_actividad):
	if(request.user.is_authenticated):
		try:
			actividad = ActividadF.objects.get(id = codigo_actividad)
			resultado = Resultado.objects.get(id = actividad.resultado_id)
			competencia= Competencia.objects.get(id=resultado.competencia_id)
			curso = Curso.objects.get(codigo=competencia.curso_id)
		except actividad.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El Indicador de Aprendizaje no Existe",
			}
			return HttpResponse(template.render(context, request))
		if(request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id):
			if(request.method == 'POST'):
				opcion = request.POST.get('opcion', None)
				if(opcion == 'si'):
					actividad.delete()
				return redirect('/cursos')
			else:
				template = loader.get_template('confirmar.html')
				texto = "¿Seguro que desea borrar La Actividad de Formacion ?:"
				context = { #Diccionario que se le pasa al HTML
				'texto' : texto
				}
				return HttpResponse(template.render(context, request))
		else:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "No esta asignado a este curso",
			}
			return HttpResponse(template.render(context, request))
	else:
		return redirect('/')



#----------------------CRUD Prerequisitos--------------------------------#

def gestionarPreRequisitos(request, codigo_curso):
	if(request.user.is_authenticated):
		try:
			curso = Curso.objects.get(codigo=codigo_curso)
		except Curso.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El curso no Existe",
			}
			return HttpResponse(template.render(context, request))
		if((request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id) or request.user.profile.tipo == 'director' or request.user.profile.tipo == 'decano'):
				try:
					prerequisitos = curso.prerequisitos_set.all()
				except Exception as e:
					raise

				template = loader.get_template('preRequisitos.html')
				context = {
					'curso' : curso,
					'prerequisitos' : prerequisitos,
					'puedogestionar' : request.user.profile.tipo == 'profesor'
				}
				return HttpResponse(template.render(context, request))
		else:
			return redirect('/')
	else:
		return redirect('/')

def agregarPreRequisitos(request, codigo_curso):
	factory = Factory()
	if(request.user.is_authenticated):
		try:
			curso = Curso.objects.get(codigo=codigo_curso)
		except Curso.DoesNotExist:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "El curso no Existe",
			}
			return HttpResponse(template.render(context, request))
		if(request.user.profile.tipo == 'profesor' and request.user.id == curso.docente_id):
			if(request.method == 'POST'):
				#agregar una competencia a su curso
				form = factory.crearFormulario('preRequisito', request)
				form.fields['curso'].initial = curso.codigo #programa del director
				form.fields['curso'].widget = forms.HiddenInput()
				if form.is_valid():
					preRequisito = form.save()
					preRequisito.save()
					return HttpResponseRedirect('/cursos')
			else:
				form = factory.crearFormulario('preRequisito')
				form.fields['curso'].initial = curso.codigo
				form.fields['curso'].widget = forms.HiddenInput()
			template = loader.get_template('agregarPreRequisito.html')
			context = {
				'form' : form,
				'curso' : curso
			}
			return HttpResponse(template.render(context, request))
			
		else:
			template = loader.get_template('error.html') #---------Buscame-------------
			context = { #Diccionario que se le pasa al HTML
				'error': "No esta asignado a este curso",
			}
			return HttpResponse(template.render(context, request))
	else:
		return redirect('/')
