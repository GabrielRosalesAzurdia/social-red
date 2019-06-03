from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import MyCreateView
from apps.mensajes.models import Publicacion
from apps.perfiles.models import Perfil
from django.conf import settings

class SignUp(generic.CreateView):
    form_class = MyCreateView
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def inicio(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        posts = Publicacion.objects.all()
        perfil = Perfil.objects.all()
        return render(request,"homepage.html",{'posts':posts,'perfiles':perfil})

def inicio2(request):
    posts = Publicacion.objects.all()
    perfil = Perfil.objects.all()
    return render(request,"homepage.html",{'posts':posts,'perfiles':perfil})