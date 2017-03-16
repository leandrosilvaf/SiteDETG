from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^docentes/$', views.lista_docentes, name='docentes'),
    #url(r'^docente/(?P<pk>[0-9]+)/$', views.docente_detail, name='docente'),
    url(r'^docente/(?P<slug>[\w_-]+)/$', views.docente_detail, name='docente'),
    url(r'^disciplinas/$', views.lista_disciplinas, name='disciplinas'),
    url(r'^laboratorios/$', views.lista_laboratorios, name='laboratorios'),
    url(r'^laboratorio/(?P<slug>[\w_-]+)/$', views.laboratorio_detail, name='laboratorio'),
    url(r'^especializacoes/$', views.lista_especializacoes, name='especializacoes'),
    url(r'^especializacao/(?P<slug>[\w_-]+)/$', views.especializacao_detail, name='especializacao'),
    url(r'^administrativo/$', views.lista_administrativo, name='administrativo'),

]