from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('contato', views.ContatctView.as_view(), name='contato'),
    path('quemsomos', views.QuemSomosView.as_view(), name='quemsomos'),
]