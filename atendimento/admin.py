from django.contrib import admin
from .models import Cliente
from .models import Medico

admin.site.register(Cliente)
admin.site.register(Medico)