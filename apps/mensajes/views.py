from django.shortcuts import render, redirect
from .models import Publicacion
from django.utils import timezone
from .forms import PostForm
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
import ast

# Create your views here.

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.fecha_publicacion = timezone.now()
            a = User.objects.filter(username = request.user)
            post.autor = a[0].first_name
            post.likes = '[]'
            post.Personas_likes = 0
            post.save()
            posts1 = Publicacion.objects.all()
            return redirect('antehomepage')
    else:
        form = PostForm()
    return render(request,'new_post.html',{'form':form})


class PostDelete(DeleteView):
    model = Publicacion
    template_name='delete_post.html'
    success_url = reverse_lazy('mostrar_perfil')

def like(request,id_publicacion):
    O = Publicacion.objects.filter(id = id_publicacion)
    o = O[0]
    x = User.objects.filter(username = request.user)
    lista_personas_likes = ast.literal_eval(o.likes)
    maybe = bool(x[0].first_name in lista_personas_likes)
    if maybe == True : 
        return render(request,'like.html',{'maybe':False})
    else:    
        o.Personas_likes = int(o.Personas_likes) + 1
        lista_personas_likes.append(x[0].first_name)
        o.likes = lista_personas_likes
        o.save()
        return render(request,'like.html',{'maybe':True})

    