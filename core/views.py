from django.shortcuts import render
from numpy import block
from django.contrib.auth.models import User
from .models import Usuario
from django.core.validators import validate_email
from django.contrib import messages

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

    if not first_name or not email or not last_name or not password \
            or not password1:
        messages.error(request, 'Preencha todos os Campos!')
        return render(request, 'core/cadastar_usuario.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email Inválido!')
        return render(request, 'core/cadastar_usuario.html')   

    if len(password) < 6:
        messages.error(request, 'Senha precisa ter pelo menos 6 Caracteres!')
        return render(request, 'core/cadastar_usuario.html')

    if password != password1:
        messages.error(request, 'Senhas não Conferem!')
        return render(request, 'core/cadastar_usuario.html')

    if Usuario.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe!')
        return render(request, 'core/cadastar_usuario.html')

    messages.success(request, 'Usuário Registrado com Sucesso!')     

    novoUsuario = Usuario.objects.create_superuser(username=first_name, last_name=last_name, email=email, password=password)
    novoUsuario.save()
    return render(request, 'core/cadastar_usuario.html')     

def teste(request):
    return render(request, 'core/teste.html')    
