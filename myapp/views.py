from django.shortcuts import render
from django.http import HttpResponse
from django_saml2_auth.views import denied






def custom_denied(request, exception=None):
    message = "Acceso denegado."
    if exception:
        message += f" Razón: {str(exception)}"
    return HttpResponse(message, status=403)



