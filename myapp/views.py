from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'button_text': 'Iniciar Sesión'
    }
    return render(request, 'home.html', context)

def custom_denied(request):
    # # Crea un objeto HttpResponse y guarda la información en el contexto
    # http_response = HttpResponse(f"Usuario denegado: {request.user}")
    # context = {'user': request.user, 'http_response': http_response}

    # # Renderiza la plantilla HTML con el contexto
    # return render(request, 'denied.html', context)
   
   
    # # Imprime información del usuario en la consola:
    # print("Usuario denegado:", request.user)

    # # Devuelve una respuesta HTTP con información del usuario:
    # return HttpResponse(f"Usuario denegado: {request.user}")
     # Crea un objeto HttpResponse y guarda la información en el contexto
    http_response = HttpResponse(f"Usuario denegado: {request.user}")
    context = {'user': request.user, 'http_response': http_response}

    print("Usuario denegado:", request.user, "context:", context)

    return HttpResponse(f"Usuario denegado: {request.user} context: {context} , request: {request}")

