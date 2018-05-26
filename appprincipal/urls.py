from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.conf.urls import include
from material.frontend import urls as frontend_urls

urlpatterns = [
	url(r'', include(frontend_urls)),
	path('login', views.autenticar, name='Autentication'),
	path('', views.inicio, name='inicio'),
	path('logout', auth_views.logout, {'next_page': '/'}, name='logout'),	
	path('usuarios', views.gestionarusuarios, name= 'gestionarusuarios'),
	path('usuarios/', views.gestionarusuarios, name= 'gestionarusuarios'),
	path('usuarios/new', views.agregarusuario, name='agregarusuario'),
	path('usuarios/consultar/<pk>', views.detalleUsuario, name='crudUsuario'),
	path('usuarios/editar/<pk>', views.modificarUsuario, name='crudUsuario'),
	path('usuarios/eliminar/<pk>', views.eliminarUsuario),
	path('programas/', views.gestionarprogramas, name='gestionarprogramas'),
	path('programas/new', views.agregarprograma, name='agregarprograma'),
	path('programas/editar/<codigo>', views.editarPrograma, name='editarprograma'),
	path('programas/eliminar/<codigo>', views.eliminarPrograma, name='eliminarprograma'),
	path('programas/ver/<codigo>', views.verPrograma, name='verprograma'),
	path('cursos', views.gestionarCursos, name='gestionarcursos'),
	path('cursos/', views.gestionarCursos, name='gestionarcursos'),
	path('cursos/new', views.agregarCurso, name='agregarCurso'),
	path('cursos/consultar/<codigo>', views.consultarCurso),
	path('cursos/editar/<codigo>', views.modificarCurso),
	path('cursos/eliminar/<codigo>', views.eliminarCurso),
	path('cursos/competencias/<codigo>', views.gestionarCompetencias),
	path('cursos/<codigo>/competencias/new', views.agregarCompetencia),
	path('cursos/<codigo_curso>/competencia/consultar/<codigo_competencia>', views.consultarCompetencia),
	path('cursos/<codigo_curso>/competencia/editar/<codigo_competencia>', views.modificarCompetencia),
	path('cursos/<codigo_curso>/competencia/eliminar/<codigo_competencia>', views.eliminarCompetencia),
	path('resultados/gestionar/<codigo_competencia>', views.gestionarResultados),
	path('resultados/new/<codigo_competencia>', views.agregarResultado),
	path('resultados/consultar/<codigo_resultado>', views.consultarResultado),
	path('resultados/editar/<codigo_resultado>', views.modificarResultado),
	path('resultados/eliminar/<codigo_resultado>', views.eliminarResultado),
	path('indicadores/gestionar/<codigo_resultado>', views.gestionarIndicadores),
	path('indicadores/new/<codigo_resultado>', views.agregarIndicador),
	path('indicadores/editar/<codigo_indicador>', views.modificarIndicador),	
	path('indicadores/eliminar/<codigo_indicador>', views.eliminarIndicador),
	path('actividadesF/gestionar/<codigo_resultado>', views.gestionarActividadesF),
	path('actividadesF/new/<codigo_resultado>', views.agregarActividadesF),
]