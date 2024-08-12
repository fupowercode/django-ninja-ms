from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import redirect  # Asegúrate de importar redirect
from sitio_usuarios.views import index
from .api import api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', lambda request: redirect('/api/docs')),
    path('api/', api.urls),
    path('', index, name='index'),
]
