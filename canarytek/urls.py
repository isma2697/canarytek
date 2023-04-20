"""
URL configuration for canarytek project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django_saml2_auth.views import signin
from myapp.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('inicio/', inicio, name='inicio'),

    path('home/', home, name='home'),
    path('iniciar_sesion/', iniciar_sesión, name='iniciar_sesión'),
   
    path('admin/', admin.site.urls),

    # path('saml2_auth/denied/', views.custom_denied, name='django_saml2_auth:denied'),
    path('saml2_auth/', include('django_saml2_auth.urls')),
    path('saml2_auth/login/', signin, name='saml2_auth_login'),
    path('logout/', logout_view, name='logout'),


]
