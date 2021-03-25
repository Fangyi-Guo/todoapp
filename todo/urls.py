from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^details/(?P<id>\w{0,50})/$', views.details),
    url(r'^add/(?P<id>\w{0,50})/$', views.add, name="add"),
    url(r'^delete/(?P<id>\w{0,50})/$', views.delete, name="delete"),
    url(r'^Note', views.Note, name ='Note'),
    url(r'^removeNote/(?P<id>\w{0,50})/$', views.removeNote, name="removeNote")
]