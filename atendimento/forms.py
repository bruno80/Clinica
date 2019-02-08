from django.forms import ModelForm, TextInput
from .models import Cliente
from .models import Medico

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class':'form-control'}),
            'sexo': TextInput(attrs={'class':'form-control'}),
            'data_nascimento': TextInput(attrs={'class':'form-control'})  
        }

class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class':'form-control'}),
            'sexo': TextInput(attrs={'class':'form-control'}),
            'data_nascimento': TextInput(attrs={'class':'form-control'}),
            'cpf': TextInput(attrs={'class':'form-control'})
        }