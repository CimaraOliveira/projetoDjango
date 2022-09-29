from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('cadastar_usuario/', views.cadastar_usuario, name='cadastar_usuario'),

    path('teste', views.teste, name='teste'),
]