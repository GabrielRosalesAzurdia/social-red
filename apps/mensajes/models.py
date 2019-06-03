from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Publicacion(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()
    autor = models.CharField(max_length=20)
    likes = models.TextField(default='[]')
    Personas_likes = models.IntegerField(default=0)

    def __str__(self):
        return "%s"%(self.titulo)