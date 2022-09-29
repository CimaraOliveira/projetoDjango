from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from numpy import block
from django.contrib.auth.models import User
from .models import Usuario
from django.core.validators import validate_email

def home(request):
    return render(request, 'core/home.html')

def cadastar_usuario(request):
    if request.method != 'POST':
        return render(request, 'core/cadastar_usuario.html')   

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    password1 = request.POST['password1']

    novoUsuario = Usuario.objects.create_superuser(username=first_name, last_name=last_name, email=email, password=password)
    novoUsuario.save()
    return render(request, 'core/cadastar_usuario.html')     

def teste(request):
    return render(request, 'core/teste.html')    
