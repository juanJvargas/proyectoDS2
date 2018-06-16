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
		filter_overrides = {
             models.CharField: {
                 'filter_class': django_filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
             models.BooleanField: {
                 'filter_class': django_filters.BooleanFilter,
                 'extra': lambda f: {
                     'widget': forms.CheckboxInput,
                 },
             },
         }		

class ProgramaFilter(django_filters.FilterSet):
	class Meta:
		model = Programa
		exclude = ['director',
					'numero_creditos_graduacion'
		]
		filter_overrides = {
             models.CharField: {
                 'filter_class': django_filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
             models.BooleanField: {
                 'filter_class': django_filters.BooleanFilter,
                 'extra': lambda f: {
                     'widget': forms.CheckboxInput,
                 },
             },
         }