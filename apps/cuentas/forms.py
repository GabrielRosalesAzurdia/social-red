from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyCreateView(UserCreationForm):
    class Meta:
        model = User

        fields = [
            'username',
            'first_name',
            'email',
        ]
        labels = {
            'username':'Nombre de usuario',
            'first_name': 'Nombre',
            'email': 'Correo electronico',
        }
    