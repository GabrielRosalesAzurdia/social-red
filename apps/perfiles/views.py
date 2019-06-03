from django.shortcuts import render
from django.views.generic import ListView , UpdateView
from django.urls import reverse_lazy 
from .forms import PerfilForm
from .models import Perfil
from django.contrib.auth.models import User
from apps.mensajes.models import Publicacion
import ast
# posts/views.py

def Perfil_mostrar(request):
    U = User.objects.filter(username = request.user)
    b = []

    maybe = bool(Perfil.objects.filter(nombre = U[0].first_name))

    if maybe :
        Publicas = Publicacion.objects.filter(autor = U[0].first_name)
        Publicas_content = []
        for i in range(len(Publicas)):
            Publicas_content.append( { 'titulo':Publicas[i].titulo, 'cont': Publicas[i].contenido, 'ide': Publicas[i].id} )

        A = Perfil.objects.filter(nombre = U[0].first_name)
        a = A[0]
        a.publicaciones = Publicas_content
        return render(request,'perfil.html',{'usuario':a})
    else:
        Publicas = Publicacion.objects.filter(autor = U[0].first_name)
        Publicas_content = []
        for i in range(len(Publicas)):
            Publicas_content.append( { 'titulo':Publicas[i].titulo, 'cont': Publicas[i].contenido, 'ide': Publicas[i].id} )
                
        a = Perfil(nombre = U[0].first_name,descripcion='Aqui colocaras tu descripcion :D',publicaciones=Publicas_content,seguidores=0,cover='',seguitores_nombres='[]')
        a.save()

        return render(request,'perfil.html',{'usuario':a})

class PerfilUpdate(UpdateView): 
    model = Perfil
    form_class = PerfilForm
    template_name = 'editar_perfil.html'
    success_url = reverse_lazy('mostrar_perfil')