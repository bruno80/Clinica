from django.shortcuts import render
from .models import Cliente
from .models import Medico

def home(request):
    return render(request, 'home.html', {})

def list_cliente(request):
    clientes = Cliente.objects.all
    return render(request, 'cliente/cliente.html', {'clientes':clientes})

def list_medico(request):
    medicos = Medico.objects.all
    return render(request, 'medico/medico.html', {'medicos':medicos})