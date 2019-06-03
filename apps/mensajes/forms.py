from django import forms
from .models import Publicacion

class PostForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = [ 
            'titulo',
            'contenido',
        ]
        labels={
            'titulo':'Titulo del Post',
            'contenido':'Contenido del Post',
        }
        widgets={
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'contenido':forms.Textarea(attrs={'class':'form-control'}),
        }