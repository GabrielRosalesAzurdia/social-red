"""red_social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url 
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth.decorators import login_required
from apps.cuentas.views import inicio,inicio2
from django.conf import settings 
from django.urls import path, include 
from django.conf.urls.static import static 

urlpatterns = [
    path(r'',inicio),
    path(r'home2/',login_required(inicio2),name="antehomepage"),
    path('admin/',admin.site.urls),
    path(r'follows/',include('apps.follows.urls')),
    path(r'perfiles/',include('apps.perfiles.urls')),
    path(r'post/',include('apps.mensajes.urls')),
    path(r'cuentas/',include('apps.cuentas.urls')),
    path(r'accounts/',include('django.contrib.auth.urls')),
    path(r'accounts/login/',LoginView.as_view(template_name='registration/login.html'), name="login"),
    path(r'reset/password_reset/',PasswordResetView.as_view(template_name='registration/password_reset_form.html',email_template_name='registration/password_reset_email.html'),name="pasword_reset"),
    path(r'reset/password_reset_done/',PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name="password_reset_done"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name="password_reset_confirm"),
    path(r'reset/done',PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),name="password_reset_complete"),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
