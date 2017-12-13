from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.input, name='input'),
  url(r'^results/', views.results, name='results'),
  url(r'^override/', views.override, name='override'),
]
