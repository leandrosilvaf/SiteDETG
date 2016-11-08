from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.noticias, name='noticias'),
    #url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<slug>[\w_-]+)/$', views.post_detail, name='post_detail'),
] 