from .models import *
import django_filters

class UserFilter(django_filters.FilterSet):
	class Meta:
		model = Profile
		exclude = [
		]
		fields = {'user__username' : ['icontains'],
				  'user__first_name' : ['icontains'],
				  'user__email' : ['icontains'],
			      'tipo' : ['icontains'],
		}

class CursoFilter(django_filters.FilterSet):
	class Meta:
		model = Curso
		exclude = ['horas_clase_magistral',
				   'horas_estudio_independiente',
				   'validable',
				   'habilitable',
				   'docente',
				   'creditos'
		]
		

class ProgramaFilter(django_filters.FilterSet):
	class Meta:
		model = Programa
		exclude = ['director',
					'numero_creditos_graduacion'
		]