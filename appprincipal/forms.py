
#aqui se almacenan los formularios, creados a partir de los modelos

from django import forms
from .models import *
from django.contrib.auth.models import User


class ProgramaForm(forms.ModelForm):
	class Meta:
		model = Programa
		fields = '__all__'

class PreRequisitoForm(forms.ModelForm):
	class Meta:
		model = PreRequisito
		fields = '__all__'

class ActividadFForm(forms.ModelForm):
	class Meta:
		model = ActividadF
		fields = '__all__'


class IndicadorForm(forms.ModelForm):
	class Meta:
		model = Indicador
		fields = '__all__'   

class ResultadoForm(forms.ModelForm):
	class Meta:
		model = Resultado
		fields = '__all__'

class CompetenciaForm(forms.ModelForm):
	class Meta:
		model = Competencia
		fields = '__all__'

class CursoForm(forms.ModelForm):
	class Meta:
		model = Curso
		fields = '__all__'

	def clean(self):
		try:
			magistral = self.cleaned_data['horas_clase_magistral']
			independiente = self.cleaned_data['horas_estudio_independiente']
			cred = self.cleaned_data['creditos']
			print(magistral)
			print(independiente)
			print(cred)
			if(magistral + independiente != cred*3):
				raise forms.ValidationError("Verifique los creditos y las horas de trabajo individual y magistral. Recuerde que la ecuacion que representa la relacion es: Horas clase magistral + Horas de trabajo independiente = Numero de creditos * 3")
		except Exception as e:
			raise forms.ValidationError("Verifique los creditos y las horas de trabajo individual y magistral. Recuerde que la ecuacion que representa la relacion es: Horas clase magistral + Horas de trabajo independiente = Numero de creditos * 3")

class UserForm(forms.ModelForm):
	class Meta:
		password=forms.PasswordInput()
		model = User
		fields = ('first_name', 'username', 'password', 'email',)

class TipoForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('tipo',)

class ActividadEvaForm(forms.ModelForm):
	class Meta:
		model = ActividadEvaluacion
		fields = '__all__'