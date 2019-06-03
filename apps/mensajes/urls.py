from django.urls import path
from . import views
from django.conf.urls import url 
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('nuevo/',login_required(views.post_new), name='post_new'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(views.PostDelete.as_view()), name='eliminar_publicacion'),
    url(r'^like/(?P<id_publicacion>\d+)/$', login_required(views.like), name='like_publicacion'),     
]
