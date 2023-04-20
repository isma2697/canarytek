from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

@login_required(login_url='iniciar_sesion/')
def iniciar_sesión(request):
    context = {
        'button_text': 'Iniciar Sesión'
    }
    return render(request, 'home.html', context)

def home(request):
    
    return render(request, 'home.html')

def inicio(request):
    
    return render(request, 'inicio.html')

def logout_view(request):
    logout(request)
    return redirect('/')

