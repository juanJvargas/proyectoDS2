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
	tipo = models.TextField(max_length=500, blank=True, choices=T_OPTION)

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if(created):
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()

class Programa(models.Model):
	codigo = models.CharField(max_length=10, primary_key=True)
	nombre_programa = models.CharField(max_length=50)
	escuela = models.CharField(max_length=40)
	numero_semestres =  models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
	numero_creditos_graduacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(200)])
	director = models.ForeignKey(User, on_delete=models.CASCADE, default=False)

	def __str__(self): 
		return self.nombre_programa

	class Meta:
		ordering = ('codigo',)

class Curso(models.Model):
	codigo=models.CharField(max_length=10, primary_key=True)
	nombre=models.CharField(max_length=40)
	creditos=models.IntegerField()
	horas_clase_magistral=models.IntegerField()
	horas_estudio_independiente=models.IntegerField()
	T_OPTION = (
        ('Asignatura basica', 'Asignatura basica'),
        ('Asignatura profesional', 'Asignatura profesional'),
        ('Asignatura electiva complementaria', 'Asignatura electiva complementaria'),
        ('Asignatura electiva profesional', 'Asignatura electiva profesional'),
    )
	tipo_curso=models.CharField(max_length=50, choices=T_OPTION)
	V_OPTION = (
        ('si', 'Si'),
        ('no', 'No'),
    )
	validable=models.CharField(max_length=2, choices=V_OPTION) #Solo se acepta si o no
	habilitable=models.CharField(max_length=2, choices=V_OPTION) #Solo se acepta si o no
	programa=models.ForeignKey(Programa, on_delete=models.CASCADE)
	semestre=models.IntegerField()
	docente=models.ForeignKey(User, on_delete=models.CASCADE, default=False)

	def __str__(self): 
		return self.nombre

	class Meta:
		ordering = ('codigo',)


class Competencia(models.Model):
	nombre = models.CharField(max_length=40,)
	descripcion = models.TextField(max_length=500, blank=True)
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE, default=False)

class Resultado(models.Model):
	T_OPTION1 = (
        ('distingue', 'Distingue'),
        ('analiza', 'Analiza'),
        
    )
	verbo=models.CharField(max_length=50, choices=T_OPTION1)
	contenido=models.TextField(max_length=50, blank=True)
	contexto=models.TextField(max_length=50, blank=True)
	proposito=models.TextField(max_length=50, blank=True)
	competencia= models.ForeignKey(Competencia, on_delete=models.CASCADE, default=False)

class Indicador(models.Model):
	T_OPTION1 = (
        ('distingue', 'Distingue'),
        ('analiza', 'Analiza'),
        
    )
	habilidad=models.CharField(max_length=50, choices=T_OPTION1)
	contenido=models.TextField(max_length=50, blank=True)
	contexto=models.TextField(max_length=50, blank=True)
	resultado= models.ForeignKey(Resultado, on_delete=models.CASCADE, default=False)

class ActividadF(models.Model):
	nombre = models.CharField(max_length=40,)
	descripcion = models.TextField(max_length=500, blank=True)
	resultado= models.ForeignKey(Resultado, on_delete=models.CASCADE, default=False)
