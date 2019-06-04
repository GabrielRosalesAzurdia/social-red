from django.shortcuts import render, redirect
from apps.perfiles.models import Perfil
from django.urls import reverse_lazy 
import ast
from apps.mensajes.models import Publicacion
from django.contrib.auth.models import User

# Create your views here.

def Ver_Perfiles(request,perfil_id_mostrar):
    U = User.objects.filter(username = request.user)
    u = U[0]
    A = Perfil.objects.filter(id = perfil_id_mostrar)
    a = A[0]

    if a.nombre == u.first_name:
        return redirect('mostrar_perfil')
    else:

        Publicas = Publicacion.objects.filter(autor = a.nombre)
        Publicas_content = []
        for i in range(len(Publicas)):
            Publicas_content.append( { 'titulo':Publicas[i].titulo, 'cont': Publicas[i].contenido,'ide': Publicas[i].id } )
        a.publicaciones = Publicas_content
        return render(request,'ver_otro_perfil.html',{'usuario':a})

def seguir(request,perfil_id_seguir):
    A = Perfil.objects.filter(id = perfil_id_seguir)
    O = User.objects.filter(username = request.user)
    o = O[0]
    a = A[0]
    lista_seguidores = ast.literal_eval(a.seguitores_nombres)

    if o.first_name in a.seguitores_nombres:
        lista_seguidores.remove(o.first_name)
        a.seguitores_nombres = lista_seguidores
        a.seguidores = int(a.seguidores) - 1
        a.save()
        return render(request,'seguir_a_usuario.html',{'seguimiento':False})
    else:
        lista_seguidores.append(o.first_name)
        a.seguitores_nombres = lista_seguidores
        a.seguidores = int(a.seguidores) + 1
        a.save()
        return render(request,'seguir_a_usuario.html',{'seguimiento':True,})

def mostrar_seguidores(request,id_perfil_seguidores):
    A = Perfil.objects.filter(id = id_perfil_seguidores)
    a = A[0]
    lista_seguidores = ast.literal_eval(a.seguitores_nombres)
    O = Perfil.objects.all()
    return render(request,'mostrar_seguidores.html',{'lista':lista_seguidores,'Usuarios':O})