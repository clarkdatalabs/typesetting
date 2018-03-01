from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.input, name='input'),
  url(r'^results/', views.results, name='results'),
  url(r'^override/', views.override, name='override'),
  # url(r'^casejson/', views.casejson, name='casejson'),
  url(r'^success_minchars/', views.success_minchars, name='success_minchars'),
]
