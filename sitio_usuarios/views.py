import pandas as pd
from django.shortcuts import render, redirect
from .models import Usuario

def index(request):
    return render(request, 'index.html')

def home(request):
    return HttpResponse("Bienvenido a la API de Usuarios. Visita /api/ para acceder a la API.")

def cargar_usuarios_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        df = pd.read_csv(csv_file)
        for index, row in df.iterrows():
            Usuario.objects.create(
                nombre=row['nombre'],
                apellido_paterno=row['apellido_paterno'],
                apellido_materno=row['apellido_materno'],
                edad=row['edad'],
                nombre_cuenta=row['nombre_cuenta'],
                contraseña=row['contraseña'],
            )
        return redirect('success')

    return render(request, 'cargar_usuarios.html')

def success(request):
    return render(request, 'success.html')
