from django.http import HttpResponse
from django.shortcuts import render
from numpy import block

def home(request):
    #return HttpResponse("hello word")
    return render(request, 'core/home.html')

def teste(request):
    return render(request, 'core/teste.html')    

"""{% block body %}
{% endblocl %}"""