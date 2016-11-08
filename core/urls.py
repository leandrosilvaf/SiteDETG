from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^docentes/$', views.lista_docentes, name='docentes'),
    #url(r'^docente/(?P<pk>[0-9]+)/$', views.docente_detail, name='docente'),
    url(r'^docente/(?P<slug>[\w_-]+)/$',  views.docente_detail, name='docente'),
    url(r'^disciplinas/$', views.lista_disciplinas, name='disciplinas'),    
]