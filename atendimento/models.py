from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=80)
    sexo = models.CharField(max_length=1)
    data_nascimento = models.DateField()

class Medico(models.Model):
    nome = models.CharField(max_length=80)
    sexo = models.CharField(max_length=1)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
