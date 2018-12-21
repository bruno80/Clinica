from django.shortcuts import render
from .models import Cliente
from .models import Medico

def home(request):
    return render(request, 'home.html', {})

def list_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/list.html', {'clientes':clientes})

def list_medico(request):
    medicos = Medico.objects.all()
    return render(request, 'medico/list.html', {'medicos':medicos})

def cliente_show(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    return render(request, 'cliente/show.html', {'cliente':cliente})

def cliente_create(request):
    return render(request, 'cliente/form.html')

def medico_show(request, medico_id):
    medico = Medico.objects.get(pk=medico_id)
    return render(request, 'medico/show.html', {'medico':medico})

