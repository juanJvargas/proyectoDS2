from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator 


class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	T_OPTION = (
        ('admin', 'Administrador'),
        ('decano', 'Decano'),
        ('director', 'Director'),
        ('profesor', 'Profesor'),
    )
	tipo = models.TextField(max_length=500, blank=False, choices=T_OPTION)

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if(created):
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()

class Programa(models.Model):
	codigo = models.CharField(max_length=10, primary_key=True, blank=False)
	nombre_programa = models.CharField(max_length=50, blank=False)
	escuela = models.CharField(max_length=40, blank=False)
	numero_semestres =  models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], blank=False)
	numero_creditos_graduacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(200)], blank=False)
	director = models.ForeignKey(User, on_delete=models.CASCADE, default=False, blank=False, unique=True)

	def __str__(self): 
		return self.nombre_programa

	class Meta:
		ordering = ('codigo',)

class Curso(models.Model):
	codigo=models.CharField(max_length=10, primary_key=True, blank=False)
	nombre=models.CharField(max_length=40, blank=False)
	creditos=models.IntegerField(blank=False)
	horas_clase_magistral=models.IntegerField(blank=False)
	horas_estudio_independiente=models.IntegerField(blank=False)
	T_OPTION = (
        ('Asignatura basica', 'Asignatura basica'),
        ('Asignatura profesional', 'Asignatura profesional'),
        ('Asignatura electiva complementaria', 'Asignatura electiva complementaria'),
        ('Asignatura electiva profesional', 'Asignatura electiva profesional'),
    )
	tipo_curso=models.CharField(max_length=50, choices=T_OPTION, blank=False)
	V_OPTION = (
        ('si', 'Si'),
        ('no', 'No'),
    )
	validable=models.CharField(max_length=2, choices=V_OPTION, blank=False) #Solo se acepta si o no
	habilitable=models.CharField(max_length=2, choices=V_OPTION, blank=False) #Solo se acepta si o no
	programa=models.ForeignKey(Programa, on_delete=models.CASCADE, blank=False)
	semestre=models.IntegerField()
	docente=models.ForeignKey(User, on_delete=models.CASCADE, default=False, blank=False)

	def __str__(self): 
		return self.nombre

	class Meta:
		ordering = ('codigo',)


class Competencia(models.Model):
	nombre = models.CharField(max_length=40, blank=False)
	descripcion = models.TextField(max_length=500, blank=False)
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE, default=False, blank=False)

class Resultado(models.Model):
	
	verbo=models.CharField(max_length=50, blank=False)
	contenido=models.TextField(max_length=50, blank=False)
	contexto=models.TextField(max_length=50, blank=False)
	proposito=models.TextField(max_length=50, blank=False)
	competencia= models.ForeignKey(Competencia, on_delete=models.CASCADE, default=False, blank=False)

class Indicador(models.Model):
	
	habilidad=models.CharField(max_length=50,blank=False)
	contenido=models.TextField(max_length=50, blank=False)
	contexto=models.TextField(max_length=50, blank=False)
	resultado= models.ForeignKey(Resultado, on_delete=models.CASCADE, default=False, blank=False)

class ActividadF(models.Model):
	nombre = models.CharField(max_length=40, blank=False)
	descripcion = models.TextField(max_length=500, blank=False)
	resultado= models.ForeignKey(Resultado, on_delete=models.CASCADE, default=False, blank=False)

class PreRequisito(models.Model):
	cursoP = models.ForeignKey(Curso, on_delete=models.CASCADE, default=False, primary_key=True, unique=True)
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE, default=False, related_name= 'curs')

	class META:
		unique_together = (('cursoP', 'curso'),)

class ActividadEvaluacion(models.Model):
	nombre = models.CharField(max_length=40, blank=False)
	descripcion = models.TextField(max_length=500, blank=False)
	indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE, default=False, blank=False)