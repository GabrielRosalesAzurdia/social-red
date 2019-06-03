from django.urls import path
from django.conf.urls import url 
from .views import Ver_Perfiles ,seguir,mostrar_seguidores
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^ver_perfil/(?P<perfil_id_mostrar>\d+)/$', login_required(Ver_Perfiles), name='observar_perfil'), 
    url(r'^seguir/(?P<perfil_id_seguir>\d+)/$',login_required(seguir),name="seguir_usuario"),
    url(r'^mostar_lista_seguidores/(?P<id_perfil_seguidores>\d+)/$',login_required(mostrar_seguidores),name="mostrar_seguidores"),
]