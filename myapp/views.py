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

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from djangosaml2 import views

@require_POST
@csrf_exempt
def saml2_acs(request):
    # Procesar la respuesta SAML2
    response = views.assertion_consumer_service(request)

    # Obtener el valor de "group" de la respuesta SAML2
    group = response.attribute_statement[0].attribute[0].attribute_value[0].text

    # Mostrar el valor de "group" en la consola
    print(group)

    # Crear o autenticar el usuario según corresponda
    user = authenticate(request=request, saml_response=response)
    if user is not None:
        login(request, user)

    return HttpResponseRedirect('/')
