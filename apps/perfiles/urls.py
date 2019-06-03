from django.urls import path
from django.conf.urls import url 
from .views import Perfil_mostrar, PerfilUpdate 
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(r'',login_required(Perfil_mostrar), name='mostrar_perfil'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(PerfilUpdate.as_view()), name='editar_perfil') 
]