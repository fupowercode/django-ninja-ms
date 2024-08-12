from django.urls import path
from .views import cargar_usuarios_csv, success

urlpatterns = [
    path('cargar/', cargar_usuarios_csv, name='cargar_usuarios'),
    path('success/', success, name='success'),
    path('', home, name='home'),
]
