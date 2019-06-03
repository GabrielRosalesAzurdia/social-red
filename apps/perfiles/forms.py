from django import forms
from .models import Perfil

class PerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = [
            'descripcion', 
            'cover',
        ]
        labels={
            'descripcion':'Descripcion',
            'cover':'Imagen de perfil',
        }
        widgets={
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
        }